import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.linear_model import HousePriceModel
from data.data_processor import DataProcessor

def get_input(prompt, input_type=int):
    while True:
        try:
            value = input_type(input(prompt))
            if value < 0:
                print("Lütfen pozitif bir değer girin.")
                continue
            return value
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")

def main():
    try:
        # Modeli yükle
        model = HousePriceModel()
        try:
            model.load_model()
        except FileNotFoundError:
            print("Model dosyası bulunamadı. Lütfen önce modeli eğitin.")
            return
        
        # Veri işleyiciyi başlat
        data_processor = DataProcessor()
        
        # Limitleri yükle
        data_processor.load_limits()
        
        print("\n=== Ev Fiyat Tahmini ===")
        print(f"Not: Yaşam alanı {data_processor.min_sqft:.0f} ile {data_processor.max_sqft:.0f} metrekare arasında olmalıdır.")
        print("Örnek değerler:")
        print("100 metrekare = 1076 feet kare")
        print("150 metrekare = 1615 feet kare")
        print("200 metrekare = 2153 feet kare\n")
        
        # Kullanıcıdan giriş al
        yasam_alani = get_input("Evin yaşam alanı kaç metrekare? ")
        
        # Girişi dönüştür
        input_data = np.array([[yasam_alani]])
        transformed_input = data_processor.transform_input(input_data)
        
        if transformed_input is None:
            return
            
        # Tahmin yap
        tahmin = model.predict(transformed_input)
        
        print(f"\nTahmini fiyat: ${tahmin[0]:,.2f}")
        
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
