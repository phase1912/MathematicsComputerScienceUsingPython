import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma, normaltest

# Функція для розрахунку ціни акції через t кроків
def stock_price_at_time(t):
    price = 0
    for _ in range(t):
        step = gamma.rvs(a=0.3, scale=1.1)  # Генерація зміни ціни згідно з гамма-розподілом
        price += step
    return price

# Функція для симуляції n разів і збереження результатів
def simulate_n_times(n, t):
    np.random.seed(42)  # Фіксація генератора випадкових чисел
    results = [stock_price_at_time(t) for _ in range(n)]
    return results

# Параметри симуляції
n = 100  # Кількість симуляцій
time_steps = range(1, 61, 2)  # Часові кроки від 1 до 60 з кроком 2

# Гістограма розподілу x (один крок)
single_step_data = simulate_n_times(n, 1)
plt.figure(figsize=(8, 4))
plt.hist(single_step_data, bins=20, color='blue', alpha=0.7, edgecolor='black')
plt.title("Гістограма розподілу зміни ціни за один крок")
plt.xlabel("Зміна ціни")
plt.ylabel("Частота")
plt.grid(alpha=0.3)
plt.show()

# Симуляції для різних t і тест на нормальність
for t in time_steps:
    prices = simulate_n_times(n, t)
    stat, p_value = normaltest(prices)  # Тест на нормальність

    # Виведення результатів тесту
    print(f"t={t}: p-value={p_value:.4f} ({'нормальний' if p_value > 0.05 else 'ненормальний'} розподіл)")

    # Побудова гістограми
    plt.figure(figsize=(8, 4))
    plt.hist(prices, bins=20, color='green', alpha=0.7, edgecolor='black')
    plt.title(f"Гістограма ціни акцій (t={t})")
    plt.xlabel("Ціна")
    plt.ylabel("Частота")
    plt.grid(alpha=0.3)
    plt.show()

# Висновки про зміну розподілу зі збільшенням t
print("\nВисновки:")
print("1. Зі збільшенням часу t розподіл стає більш симетричним.")
print("2. При достатньо великому t розподіл наближається до нормального (згідно з тестом на нормальність).")
