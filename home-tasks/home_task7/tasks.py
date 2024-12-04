# Завдання 1
# Ймовірність того, що серед обраних 6 деталей 2 виявляться нестандартними, визначається за формулою гіпергеометричного розподілу:
# P(X=2) = [C(5,2) * C(45,4)] / C(50,6)
# Де C(n, k) = n! / (k!(n-k)!) - число комбінацій.


# Завдання 2
# Використовуємо формулу біноміального розподілу:
# P(X >= 5) = P(X=5) + P(X=6) + P(X=7)
# P(X=k) = C(7, k) * (0.8^k) * (0.2^(7-k))
# C(n, k) - число комбінацій.

from math import comb

p_hit = 0.8
n_shots = 7
probability = sum(comb(n_shots, k) * (p_hit ** k) * ((1 - p_hit) ** (n_shots - k)) for k in range(5, 8))
print(f"Ймовірність того, що буде не менше за 5 влучань: {probability:.4f}")


# Завдання 3
# Знаходимо всі можливі комбінації результатів кидання 3 кубиків і порівнюємо кількість випадків, коли сума = 11 або 12.

from itertools import product

outcomes = list(product(range(1, 7), repeat=3))
sum_11 = sum(1 for outcome in outcomes if sum(outcome) == 11)
sum_12 = sum(1 for outcome in outcomes if sum(outcome) == 12)
print(f"Ймовірність суми 11: {sum_11 / len(outcomes):.4f}")
print(f"Ймовірність суми 12: {sum_12 / len(outcomes):.4f}")


# Завдання 4
# Для визначення події виходу з ладу всієї схеми через Ai виражаємо A як об'єднання подій A1, ..., A6, залежно від топології схеми.
# Наприклад, якщо схема послідовна: A = A1 \cap A2 \cap ... \cap A6.
# Якщо паралельна: A = A1 \cup A2 \cup ... \cup A6.


# Завдання 5
# Ймовірність того, що точка потрапить у кільце, дорівнює відношенню площі кільця до площі великого кола:
# P = (pi * 10^2 - pi * 5^2) / (pi * 10^2)
# Спрощуємо: P = (100 - 25) / 100 = 75 / 100 = 0.75

ring_probability = (10**2 - 5**2) / 10**2
print(f"Ймовірність потрапляння у кільце: {ring_probability:.2f}")


# Завдання 6
# Використовуємо теорему Баєса для знаходження ймовірності того, що залишена куля біла:
# P(B2|W1) = P(W1|B2) * P(B2) / P(W1)
# P(W1) = P(W1|B1) * P(B1) + P(W1|B2) * P(B2)

P_B1 = 0.5
P_B2 = 0.5
P_W1_given_B1 = 1
P_W1_given_B2 = 0.5
P_W1 = P_W1_given_B1 * P_B1 + P_W1_given_B2 * P_B2
P_B2_given_W1 = P_W1_given_B2 * P_B2 / P_W1
print(f"Ймовірність того, що залишилася біла куля: {P_B2_given_W1:.2f}")


# Завдання 7 (а)
# Визначаємо аналітично середню ціну через t=3 одиниці часу.
# Середнє значення: M(X) = 0 + 3 * (2 * 0.5 - 1 * 0.5) = 3 * 0.5 = 1.


# Завдання 7 (б)
# Симулюємо процес випадкового блукання і знаходимо середню ціну для різних кількостей симуляцій.

import numpy as np
import matplotlib.pyplot as plt

def simulate_price(t, n_simulations):
    steps = np.random.choice([2, -1], size=(n_simulations, t))
    prices = steps.sum(axis=1)
    return prices

n_simulations_list = [10, 100, 1000, 10000]
t = 3

for n_simulations in n_simulations_list:
    prices = simulate_price(t, n_simulations)
    mean_price = np.mean(prices)
    print(f"Середнє значення ціни для {n_simulations} симуляцій: {mean_price:.2f}")
    plt.hist(prices, bins=20, alpha=0.5, label=f"{n_simulations} симуляцій")

plt.title("Гістограма цін для різної кількості симуляцій")
plt.xlabel("Ціна")
plt.ylabel("Частота")
plt.legend()
plt.show()


####

import numpy as np
import matplotlib.pyplot as plt


# Функція для розрахунку ціни акції через t кроків
def stock_price_at_time(t):
    # Ініціалізація початкової ціни
    price = 0
    for _ in range(t):
        step = np.random.choice([2, -1])  # Кроки: +2 або -1
        price += step
    return price


# Функція для симуляції n разів і збереження результатів
def simulate_n_times(n, t):
    np.random.seed(42)  # Фіксація генератора випадкових чисел
    results = [stock_price_at_time(t) for _ in range(n)]
    return results


# Візуалізація результатів для різних кількостей симуляцій
for n in [10, 100, 1000, 10000]:
    prices = simulate_n_times(n, 3)
    mean_price = np.mean(prices)

    # Виведення середнього значення
    print(f"Середнє значення ціни для {n} симуляцій: {mean_price:.2f}")

    # Побудова гістограми
    plt.figure(figsize=(8, 4))
    plt.hist(prices, bins=20, color='blue', alpha=0.7, edgecolor='black')
    plt.title(f"Гістограма цін (n={n})")
    plt.xlabel("Ціна")
    plt.ylabel("Частота")
    plt.grid(alpha=0.3)
    plt.show()
