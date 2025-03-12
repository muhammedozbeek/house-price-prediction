# Ev Fiyat Tahmini

Bu proje, evin yaşam alanına (feet kare) göre fiyat tahmini yapan basit bir makine öğrenmesi uygulamasıdır. King County, USA'deki ev satış verilerini kullanarak eğitilmiş bir lineer regresyon modeli kullanmaktadır.

## Özellikler

- Yaşam alanına göre ev fiyat tahmini
- Kullanıcı dostu arayüz
- Feet kare - metrekare dönüşüm örnekleri
- Giriş değeri doğrulama
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
git clone https://github.com/[kullanıcı-adınız]/house-price-prediction.git
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

## Veri Seti

King County, USA'deki ev satış verilerini içermektedir. Bu projede sadece yaşam alanı (sqft_living) özelliği kullanılmaktadır.

## Proje Yapısı

```
house-price-prediction/
│
├── data/
│   ├── data_processor.py   # Veri işleme sınıfı
│   └── house_data.csv      # Veri seti
│
├── models/
│   ├── linear_model.py     # Model sınıfı
│   ├── model.pkl          # Eğitilmiş model
│   └── scaler.pkl         # Veri ölçeklendirici
│
├── views/
│   └── main.py            # Kullanıcı arayüzü
│
├── requirements.txt       # Bağımlılıklar
└── README.md             # Bu dosya
```

## Katkıda Bulunma

1. Bu repoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.
