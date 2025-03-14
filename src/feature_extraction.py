# Ses, metin ve görüntü için ayrı özellik çıkarımı işlemleri için
# Her biri için ayrı script yazılabilir, uzun olursa

# RoBERTa ile meitn verisinden öznitelik çıkarımı

import pandas as pd
from transformers import RobertaTokenizer, RobertaModel
import torch
from collections import defaultdict

# MELD veri setini yükle ve ilgili sütunları al
meld_dev = pd.read_csv("../../data/raw/dev_sent_emo.csv")

meld_texts = meld_dev["Utterance"].tolist()
meld_labels = meld_dev["Emotion"].tolist()
meld_speaker = meld_dev["Speaker"].tolist()
meld_conversation = meld_dev["Dialogue_ID"].tolist()

# Tokenizer'ı yükle ve bütün metinleri tokenize et
tokenizer = RobertaTokenizer.from_pretrained("roberta-large")

tokens = tokenizer(
    meld_texts, 
    padding="max_length",  # Maksimum uzunluğa göre pad ekler
    truncation=True,       # Uzun metinleri keser
    max_length=128,        # Maksimum uzunluk
    return_tensors="pt"    # PyTorch tensörü olarak döndürür
)

# RoBERTa modelini yükle ve model ile embedding çıkart
model = RobertaModel.from_pretrained("roberta-large")

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
