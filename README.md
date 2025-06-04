# Modüler Python Uygulaması

Bu proje, modüler programlama ve okunabilir kod yazma alışkanlıklarını geliştirmek için oluşturulmuştur.

## 🔧 Özellikler
- Python ile yazılmıştır.
- Dört temel işlem (toplama, çıkarma, çarpma, bölme) modüler yapıda tasarlanmıştır.
- Her işlem ayrı bir dosyada tanımlanmış ve `main.py` üzerinden çağrılmıştır.

## 📁 Proje Yapısı
```
moduler-python/
├── main.py
├── hesaplama/
│   ├── toplama.py
│   ├── cikarma.py
│   ├── carpma.py
│   └── bolme.py
└── README.md
```

## 🚀 Nasıl Çalıştırılır?
```bash
python main.py
```

## 🧠 Amaç
- Modüler programlamayı öğrenmek
- Fonksiyonları ayrı dosyalarda tanımlamak
- Kod okunabilirliğini artırmak

## VEML3328 Sensörü
VEML3328 sensöründen RGB verilerini okuyup SQL Server’a kaydetmek için `veml3328_sql.py` dosyasını çalıştırabilirsiniz. Dosya içinde sensörün I2C adresi ve SQL Server bağlantı bilgilerini güncellemeyi unutmayın.
```bash
python veml3328_sql.py
```
