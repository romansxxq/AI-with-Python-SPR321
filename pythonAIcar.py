import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

df = pd.read_csv("assets/cars_realistic_with_brand.csv")
print(df.head())  

# X = df[['engine_volume', 'mileage', 'horsepower', 'year']]  
X = df[['brand','model','year','engine_volume','mileage','horsepower','price']]  
y = df['price']

print("Cars: ", X)
print("Target:", y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

your_car = pd.DataFrame([{
    'brand': 'Toyota',
    'model': 'Camry',
    'year': 2015,
    'engine_volume': 2.5,
    'mileage': 30000,
    'horsepower': 200,
    'price': 25000
    # 'engine_volume': 2.0,       
    # 'mileage': 50000,           
    # 'horsepower': 150,          
    # 'year': 2015                
}])

predicted_price = model.predict(your_car)
print(f"Прогнозована ціна автомобіля: {predicted_price[0]:,.2f} $")

y_pred = model.predict(X_test)

mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
print(f"MAPE (середня відносна помилка): {mape:.2f}%")

r2 = r2_score(y_test, y_pred)
print(f"R²: {r2:.2f}")

plt.figure(figsize=(8, 6))
sns.regplot(x=y_test, y=y_pred, scatter_kws={'s': 50, 'color': 'blue'}, line_kws={'color': 'red'})
plt.xlabel("Справжня ціна")
plt.ylabel("Прогнозована ціна")
plt.title("Справжня vs Прогнозована ціна автомобіля")
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_test - y_pred, color='blue', s=50, edgecolor='black')
plt.hlines(y=0, xmin=y_test.min(), xmax=y_test.max(), color='red', lw=2)
plt.xlabel("Справжня ціна")
plt.ylabel("Помилка прогнозу")
plt.title("Помилка прогнозу vs Справжня ціна")
plt.show()
