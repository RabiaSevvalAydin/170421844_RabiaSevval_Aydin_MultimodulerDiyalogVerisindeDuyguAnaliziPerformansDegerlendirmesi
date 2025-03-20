# Bitirme Tezi - Multimodular Duygu Analizi
Sude ve Rabia'nın Ultra Güzel Minnoş Bitirme Tezi Projesi

## 📂 Proje Repo Yapısı
```
bitirme-tezi/
│── data/                  # Veri kümesi
│   ├── features/          # Özellik çıkarılmış veriler
│   ├── models/ 
│       ├── roberta_models/
│   ├── processed/         # Ön işlenmiş ve dönüştürülmüş veriler
│   ├── raw/               # Ham veri seti (orijinal hali)
│── docs/                  # Proje dökümantasyonu
│   ├── README.md          # Proje açıklamaları
│── notebooks/             # Jupyter Notebook'lar (Keşifsel analiz vb.)
│   ├── local_workspace    # Local çalışma alanı, git takip etmeyecek
│── src/                   # Kaynak kodlar (ana Python scriptleri)
│   ├── DialogueRNN/
│   ├── RoBERTa/
│       ├── roberta-large/
│           ├── NOTE.txt
│       ├── commonsense_model.py
│       ├── dataloader.py
│       ├── encoder.json
│       ├── model.py
│       ├── multiprocessing_bpe_encoder.py
│       ├── roberta_feature_extract_meld.py
│       ├── roberta_init_meld.py
│       ├── roberta_preprocess_meld.sh
│       ├── roberta_train_meld.sh
│       ├── train_meld.py
│── .gitignore             # Gereksiz dosyaları git takibinden çıkarmak için
│── environment.yml        # Conda ortamının paket bilgileri
```
- Yeni dosyalar eklendikçe güncelle, dosya sayısı çok olursa klasörler isimlerini güncellersiniz
  
### 📌 Commit Mesaj Formatı  
```
<kategori>: <kısa açıklama>

<isteğe bağlı detaylı açıklama>

--------------------
Commit kategorileri:
feat:	Yeni bir özellik eklendiğinde kullanılır
fix:	Hata düzeltmesi yapıldığında kullanılır
docs:	README, dökümantasyon veya yorum satırları güncellendiğinde kullanılır
refactor:	Kod yapısında değişiklik yapıldığında (davranış değişikliği olmadan) kullanılır
test:	Test dosyaları eklendiğinde veya güncellendiğinde kullanılır
chore:	Linter düzenlemeleri, bağımlılık güncellemeleri gibi küçük işlemler için kullanılır
```

📌 Branch Yapısı
```
main → Stabil ve güncel sürüm burada tutulur.
dev → Aktif geliştirme bu branch üzerinde yapılır.
feature/<özellik-adı> → Yeni bir özellik geliştirildiğinde oluşturulur.
Örnek: feature/ses-verisi-ön-isleme
fix/<hata-adı> → Hata düzeltmeleri için kullanılır.
Örnek: fix/veri-yolu-hatasi
```
- Yeni branch'ler dev üzerinden oluşturulur, tamamlandıktan sonra dev'e merge edilir.
- Değişiklikler dev üzerinde test edildikten sonra her şey stabil ise main branch'e merge edilir.
- Büyük değişiklikler veya hatalar için issue açılmalıdır.
