import pandas as pd
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class DataProcessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.feature_names = ['sqft_living']
        
    def load_data(self, filename):
        """Veri setini yükler"""
        try:
            self.data = pd.read_csv(filename)
            # Minimum ve maksimum değerleri kaydet (metrekare cinsinden)
            self.min_sqft = self.data['sqft_living'].min() * 0.092903  # feet kare'yi metrekareye çevir
            self.max_sqft = self.data['sqft_living'].max() * 0.092903
            return self.data
        except Exception as e:
            print(f"Veri yükleme hatası: {e}")
            return None
    
    def preprocess_data(self):
        """Veriyi ön işler"""
        try:
            X = self.data[self.feature_names]  # Sadece yaşam alanını kullan
            y = self.data['price']  # Hedef değişken fiyat
            
            # Verileri ölçeklendir
            X_scaled = self.scaler.fit_transform(X)
            
            # Scaler'ı kaydet
            self.save_scaler()
            
            # Min-max değerleri kaydet
            self.save_limits()
            
            # Eğitim ve test verilerini ayır
            X_train, X_test, y_train, y_test = train_test_split(
                X_scaled, y, test_size=0.2, random_state=42
            )
            
            return X_train, X_test, y_train, y_test
        except Exception as e:
            print(f"Veri ön işleme hatası: {e}")
            return None, None, None, None
    
    def transform_input(self, input_data_m2):
        """Kullanıcı girişini dönüştürür (metrekare girişi)"""
        try:
            # Scaler'ı ve limitleri yükle
            self.load_scaler()
            self.load_limits()
            
            # Metrekareyi feet kareye çevir
            input_data_sqft = input_data_m2 / 0.092903
            
            # Girişi DataFrame'e çevir
            input_df = pd.DataFrame(input_data_sqft, columns=self.feature_names)
            
            # Değer kontrolü (metrekare cinsinden)
            if input_data_m2[0][0] < self.min_sqft:
                print(f"Uyarı: Girilen değer minimum değerden ({self.min_sqft:.0f} metrekare) küçük!")
                return None
            if input_data_m2[0][0] > self.max_sqft:
                print(f"Uyarı: Girilen değer maksimum değerden ({self.max_sqft:.0f} metrekare) büyük!")
                return None
                
            return self.scaler.transform(input_df)
        except Exception as e:
            print(f"Giriş dönüştürme hatası: {e}")
            return None
            
    def save_scaler(self, filename="models/scaler.pkl"):
        """StandardScaler'ı kaydeder"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self.scaler, f)
        except Exception as e:
            print(f"Scaler kaydetme hatası: {e}")
            
    def load_scaler(self, filename="models/scaler.pkl"):
        """StandardScaler'ı yükler"""
        try:
            with open(filename, "rb") as f:
                self.scaler = pickle.load(f)
        except Exception as e:
            print(f"Scaler yükleme hatası: {e}")
            
    def save_limits(self, filename="models/limits.pkl"):
        """Min-max değerlerini kaydeder"""
        try:
            limits = {
                'min_sqft': self.min_sqft,
                'max_sqft': self.max_sqft
            }
            with open(filename, "wb") as f:
                pickle.dump(limits, f)
        except Exception as e:
            print(f"Limitleri kaydetme hatası: {e}")
            
    def load_limits(self, filename="models/limits.pkl"):
        """Min-max değerlerini yükler"""
        try:
            with open(filename, "rb") as f:
                limits = pickle.load(f)
                self.min_sqft = limits['min_sqft']
                self.max_sqft = limits['max_sqft']
        except Exception as e:
            print(f"Limitleri yükleme hatası: {e}") 