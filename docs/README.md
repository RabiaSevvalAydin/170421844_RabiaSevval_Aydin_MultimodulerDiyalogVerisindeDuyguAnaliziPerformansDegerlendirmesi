# Bitirme Tezi - Multimodular Duygu Analizi
Sude ve Rabia'nın Ultra Güzel Minnoş Bitirme Tezi Projesi

## 📂 Proje Repo Yapısı
```
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
