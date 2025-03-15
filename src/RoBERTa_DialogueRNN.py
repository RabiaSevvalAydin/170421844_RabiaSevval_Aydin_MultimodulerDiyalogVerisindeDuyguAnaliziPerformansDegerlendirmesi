import torch
import numpy as np
import pandas as pd
from transformers import RobertaTokenizer, RobertaModel
import torch.nn as nn
import torch.optim as optim
from collections import defaultdict

# MELD veri setini yükle
meld_dev = pd.read_csv("../data/raw/dev_sent_emo.csv")

# İlgili sütunları al
meld_texts = meld_dev["Utterance"].tolist()  # Kullandım
meld_labels = meld_dev["Emotion"]  # Kullandım
meld_speaker = meld_dev["Speaker"].tolist()
meld_conversation = meld_dev["Dialogue_ID"].tolist()

# Tokenizer'ı yükle
tokenizer = RobertaTokenizer.from_pretrained("roberta-large")

# Bütün metinleri tokenize et
tokens = tokenizer(
    meld_texts, 
    padding="max_length",  # Maksimum uzunluğa göre pad ekler
    truncation=True,       # Uzun metinleri keser
    max_length=128,        # Maksimum uzunluk
    return_tensors="pt"    # PyTorch tensörü olarak döndürür
)

# RoBERTa modelini yükle
model = RobertaModel.from_pretrained("roberta-large")

# Model ile embedding çıkartma
with torch.no_grad():
    outputs = model(**tokens)

# Son gizli katman çıktısı (CLS token embedding'i kullan)
roberta_features = outputs.last_hidden_state[:, 0, :]  # (batch_size, hidden_dim)

# Diyalogları gruplama
dialogues = defaultdict(list)
for text, speaker, conv_id, feature, label in zip(meld_texts, meld_speaker, meld_conversation, roberta_features, meld_labels):
    dialogues[conv_id].append((feature, speaker, label))

# Sıralı diyalog listesi oluştur
sorted_dialogues = [dialogues[key] for key in sorted(dialogues.keys())]

# Duygu etiketleri için one-hot encoding dönüşümü
def one_hot_encode(label, num_classes=7):
    one_hot = np.zeros(num_classes)
    one_hot[label] = 1
    return one_hot

# Sözlük yapısı kullanarak duygu etiketlerinin rakam temsilini oluşturma
emotion_dict = {
    "neutral": 0,
    "joy": 1,
    "sadness": 2,
    "anger": 3,
    "fear": 4,
    "disgust": 5,
    "surprise": 6
}

# Etiket sütununu önce sayısal daha sonra one-hot encode formatına getirme
meld_labels = meld_labels.map(emotion_dict)
meld_labels = meld_labels.apply(lambda x: one_hot_encode(x))  # One-hot encoding

# Model
class DialogueRNN(nn.Module):
    def __init__(self, input_dim=1024, hidden_dim=128, num_classes=7):
        super(DialogueRNN, self).__init__()
        
        self.rnn = nn.GRU(input_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, num_classes)
        
    def forward(self, x):
        rnn_out, _ = self.rnn(x)
        output = self.fc(rnn_out)
        return output

# Modeli oluştur
dialoguernn = DialogueRNN()

# Cihazı belirle
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
dialoguernn.to(device)

# Kayıp fonksiyonu ve optimizasyon
criterion = nn.BCEWithLogitsLoss()  # One-hot encoding için uygun
optimizer = optim.Adam(dialoguernn.parameters(), lr=0.001)

# Eğitim döngüsü
num_epochs = 5
for epoch in range(num_epochs):
    total_loss = 0
    
    for conversation in sorted_dialogues:
        features, speakers, labels = zip(*conversation)
        features = torch.stack(features).to(device)
        
        # One-hot encoding'li etiketleri tensor'a dönüştür
        labels = torch.tensor(np.stack([one_hot_encode(emotion_dict[label]) for label in labels]), dtype=torch.float).to(device)
        
        # Modeli çalıştır
        outputs = dialoguernn(features)
        
        # Kayıp fonksiyonunu hesapla
        loss = criterion(outputs, labels)  # Artık boyut hatası vermez
        
        # Geri yayılım
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
    
    print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}")
