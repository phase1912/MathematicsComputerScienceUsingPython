import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, pearsonr

# Завантаження даних із Google Sheets
url = 'https://docs.google.com/spreadsheets/d/18WCpPS96Tb3cB0FCsIA92PEhcmBkp08sjYhS9DsQfJE/edit#gid=954244094'
url = url[:url.find('/edit')] + '/export?format=csv'
df = pd.read_csv(url)

# Функція для аналізу колонки
def analyze_column(col_name):
    col = df[col_name]
    mean = col.mean()
    variance = col.var()
    std_dev = col.std()

    # Перевірка на нормальність
    stat, p_value = shapiro(col)
    normality = p_value > 0.05  # Якщо p > 0.05, розподіл нормальний

    # Кореляція з Product_Sold
    corr, _ = pearsonr(col, df["Product_Sold"])

    # Побудова гістограми
    plt.figure(figsize=(8, 4))
    sns.histplot(col, kde=True, bins=10, color='skyblue', edgecolor='black')
    plt.title(f"Гістограма {col_name}")
    plt.xlabel(col_name)
    plt.ylabel("Частота")
    plt.show()

    # Повернення результатів
    return {
        "mean": mean,
        "variance": variance,
        "std_dev": std_dev,
        "normality_p_value": p_value,
        "is_normal": normality,
        "correlation_with_Product_Sold": corr,
    }

# Аналіз усіх колонок
results = {}
for col in df.columns:
    if col != "Product_Sold":
        print(f"=== Аналіз для {col} ===")
        results[col] = analyze_column(col)
        print(results[col])

# Виведення результатів
print("\nРезультати аналізу:")
for key, value in results.items():
    print(f"{key}: {value}")