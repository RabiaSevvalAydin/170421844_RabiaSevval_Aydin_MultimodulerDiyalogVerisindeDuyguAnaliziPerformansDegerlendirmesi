# Bitirme Tezi - Multimodular Duygu Analizi
Sude ve Rabia'nın Ultra Güzel Minnoş Bitirme Tezi Projesi

## 📂 Proje Yapısı

```Projenin repo yapısı:
bitirme-tezi/
│── data/                  # Veri kümesi
│   ├── raw/               # Ham veri seti (orijinal hali)
│   ├── processed/         # Ön işlenmiş ve dönüştürülmüş veriler
│   ├── features/          # Özellik çıkarılmış veriler
│── src/                   # Kaynak kodlar (ana Python scriptleri)
│   ├── preprocessing.py   # Veri temizleme ve ön işleme
│   ├── feature_extraction.py  # Özellik çıkarımı (MFCC, spectrogram vb.)
|   ├── model.py           # İlk model denemesi
│── notebooks/             # Jupyter Notebook'lar (Keşifsel analiz vb.)
│   ├── rabia_workspace    # Local çalışma alanı, git takip etmeyecek 
│   ├── sude_workspace     # Local çalışma alanı, git takip etmeyecek
│── docs/                  # Proje dökümantasyonu
│   ├── README.md          # Proje açıklamaları
│── environment.yml        # Conda ortamının paket bilgileri
│── .gitignore             # Gereksiz dosyaları git takibinden çıkarmak için