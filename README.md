# Ev Fiyat Tahmini

Bu proje, evin yaşam alanına (metrekare) göre fiyat tahmini yapan basit bir makine öğrenmesi uygulamasıdır. King County, USA'deki ev satış verilerini kullanarak eğitilmiş bir lineer regresyon modeli kullanmaktadır.

## Özellikler

- Yaşam alanına göre ev fiyat tahmini (metrekare cinsinden giriş)
- Otomatik metrekare - feet kare dönüşümü
- Kullanıcı dostu arayüz
- Giriş değeri doğrulama ve sınırlama
- Veri ölçeklendirme

## Gereksinimler

- Python 3.x
- NumPy
- Pandas
- Scikit-learn
- Matplotlib

## Kurulum

1. Repoyu klonlayın:

```bash
git clone https://github.com/muhammedozbeek/house-price-prediction.git
cd house-price-prediction
```

2. Gerekli kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```

## Kullanım

1. Modeli eğitmek için:

```bash
python train.py
```

2. Fiyat tahmini yapmak için:

```bash
python views/main.py
```

Program size yaşam alanını metrekare cinsinden soracak ve geçerli aralıkta bir değer girmeniz durumunda tahmini ev fiyatını dolar cinsinden gösterecektir.

## Veri Seti

King County, USA'deki ev satış verilerini içermektedir. Bu projede sadece yaşam alanı (sqft_living) özelliği kullanılmaktadır. Program otomatik olarak feet kare - metrekare dönüşümü yapmaktadır.

## Proje Yapısı

```
house-price-prediction/
│
├── data/
│   ├── data_processor.py   # Veri işleme ve dönüşüm sınıfı
│   └── house_data.csv      # Ev fiyatları veri seti
│
├── models/
│   └── linear_model.py     # Model sınıfı
│
├── views/
│   └── main.py            # Kullanıcı arayüzü
│
├── train.py              # Model eğitim script'i
├── requirements.txt      # Bağımlılıklar
└── README.md            # Bu dosya
```

## Katkıda Bulunma

1. Bu repoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.
