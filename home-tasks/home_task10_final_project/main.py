import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import gdown

# Завантаження даних із Google Drive
url = 'https://drive.google.com/uc?id=1UBBRY_uFUoJwQsBbYUMcfOXZZxETt_LR'
output = 'rent_data.csv'
gdown.download(url, output, quiet=False)

# Читання CSV файлу
data = pd.read_csv(output)

#### part1

# Підрахунок кількості рядків до обробки
initial_row_count = data.shape[0]

# Загальна кількість пропущених значень до обробки
total_missing_before = data.isnull().sum().sum()
print(f"Загальна кількість пропущених значень до обробки: {total_missing_before}")

# Обробка пропущених значень
for column in data.columns:
    if data[column].isnull().any():
        if data[column].dtype == 'object':
            data[column].fillna(data[column].mode()[0], inplace=True)
        else:
            data[column].fillna(data[column].mean(), inplace=True)

# Загальна кількість пропущених значень після обробки
total_missing_after = data.isnull().sum().sum()
print(f"Загальна кількість пропущених значень після обробки: {total_missing_after}")

# Підрахунок кількості видалених рядків (якщо використовувалось видалення)
rows_removed = initial_row_count - data.shape[0]
print(f"Кількість видалених рядків: {rows_removed}")

# Перегляд перших рядків даних
print(data.head())

# Інформація про дані
print(data.info())

# Перевірка пропущених значень
print(data.isnull().sum())

# Заповнення пропущених значень (середнє для числових, мода для категорійних)
for column in data.columns:
    if data[column].dtype == 'object':
        data[column] = data[column].fillna(data[column].mode()[0])
    else:
        data[column] = data[column].fillna(data[column].mean())

# Перетворення даних для кореляційної матриці (залишаються лише числові стовпці)
numeric_data = data.select_dtypes(include=['int64', 'float64'])

# Кореляційна матриця
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_data.corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Кореляційна матриця')
plt.show()

# Масштабування числових змінних
numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
scaler = StandardScaler()
data[numerical_features] = scaler.fit_transform(data[numerical_features])

# Видалення або перетворення нечислових змінних
non_numeric_columns = data.select_dtypes(exclude=['int64', 'float64']).columns
print(f"Нечислові колонки: {non_numeric_columns}")

# Якщо є дати або текстові змінні, їх потрібно обробити або видалити
# Наприклад, видалення колонки з датами
data = data.drop(columns=non_numeric_columns)

############## part 2

# Розділення даних на ознаки (X) і цільову змінну (y)
X = data.drop('Rent', axis=1)
y = data['Rent']

# Розділення на тренувальну і тестову вибірки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Модель 1: Лінійна регресія
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred_lr = lin_reg.predict(X_test)

# Модель 2: Випадковий ліс
rf_reg = RandomForestRegressor(random_state=42)
rf_reg.fit(X_train, y_train)
y_pred_rf = rf_reg.predict(X_test)

# Метрики для обох моделей
def evaluate_model(y_true, y_pred, model_name):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    print(f"{model_name} - MAE: {mae:.2f}, RMSE: {rmse:.2f}")

# Оцінка моделей
evaluate_model(y_test, y_pred_lr, "Лінійна регресія")
evaluate_model(y_test, y_pred_rf, "Випадковий ліс")

########### part 3

# Порівняння справжніх і передбачених значень
plt.figure(figsize=(10, 5))
plt.scatter(y_test, y_pred_lr, alpha=0.7, label='Лінійна регресія')
plt.scatter(y_test, y_pred_rf, alpha=0.7, label='Випадковий ліс', color='orange')
plt.plot([y.min(), y.max()], [y.min(), y.max()], '--k', color='red')
plt.xlabel('Справжні значення')
plt.ylabel('Передбачені значення')
plt.legend()
plt.title('Справжні vs Передбачені значення')
plt.show()

# Графік залишків для лінійної регресії
residuals_lr = y_test - y_pred_lr
plt.figure(figsize=(10, 5))
sns.histplot(residuals_lr, kde=True)
plt.title('Графік залишків (Лінійна регресія)')
plt.show()

# Висновки
print("Висновки:")
print("1. Випадковий ліс демонструє меншу помилку, ніж лінійна регресія.")
print("2. Помилки найбільші для високих значень оренди.")