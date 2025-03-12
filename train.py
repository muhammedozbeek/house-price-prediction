from data.data_processor import DataProcessor
from models.linear_model import HousePriceModel
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

def train_model():
    try:
        # Veri işleyiciyi başlat
        data_processor = DataProcessor()
        
        # Veriyi yükle
        data = data_processor.load_data('data/house_data.csv')
        if data is None:
            return False
            
        # Veriyi ön işle
        X_train, X_test, y_train, y_test = data_processor.preprocess_data()
        if X_train is None:
            return False
            
        # Modeli oluştur ve eğit
        model = HousePriceModel()
        model.train(X_train, y_train)
        
        # Model performansını değerlendir
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print(f"Model Performansı:")
        print(f"MSE: {mse:.2f}")
        print(f"R2 Score: {r2:.2f}")
        
        # Modeli kaydet
        model.save_model()
        print("Model başarıyla eğitildi ve kaydedildi.")
        return True
        
    except Exception as e:
        print(f"Model eğitimi sırasında hata oluştu: {e}")
        return False

if __name__ == "__main__":
    train_model() 