from scipy.optimize import linprog
import matplotlib.pyplot as plt
import numpy as np

# Вартість послуг (в тисячах $): сайти, інтернет-магазини, інтеграція з ERP
profit = [2, 9, 6]

# Час, який витрачають дизайнери, розробники, тестувальники (в годинах)
designers_time = [12, 6, 2]
developers_time = [12, 24, 18]
testers_time = [12, 18, 12]

# Доступний фонд праці для кожної групи (в годинах)
max_designers_hours = 2 * 160  # 2 дизайнери, кожен по 160 годин
max_developers_hours = 192    # 2 розробники, спільний фонд 192 години
max_testers_hours = 180       # 1 тестувальник, працює понаднормово

# Система обмежень: час роботи спеціалістів не перевищує доступного фонду праці
lhs_ineq = [
    designers_time,  # обмеження для дизайнерів
    developers_time, # обмеження для розробників
    testers_time     # обмеження для тестувальників
]

rhs_ineq = [
    max_designers_hours,
    max_developers_hours,
    max_testers_hours
]

# Змінні мають бути невід'ємними
bounds = [(0, None), (0, None), (0, None)]

# Використовуємо метод лінійного програмування для максимізації прибутку (мінімізуємо -profit)
result = linprog(c=[-p for p in profit], A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bounds, method="highs")

# Отримуємо оптимальний розподіл
optimal_services = result.x  # Кількість послуг кожного виду
total_profit = -result.fun   # Сумарний прибуток

print("Оптимальний розподіл послуг:")
print(f"Сайти: {optimal_services[0]:.2f}")
print(f"Інтернет-магазини: {optimal_services[1]:.2f}")
print(f"Інтеграція з ERP: {optimal_services[2]:.2f}")
print(f"Сумарний місячний дохід: {total_profit:.2f} тисяч $")

# Побудова графіка для двох змінних (сайти та інтернет-магазини)
x1 = np.linspace(0, 30, 300)  # Кількість сайтів

# Обмеження для дизайнерів, розробників і тестувальників (залежно від x1)
x2_designers = (max_designers_hours - 12 * x1) / 6
x2_developers = (max_developers_hours - 12 * x1) / 24
x2_testers = (max_testers_hours - 12 * x1) / 18

# Область допустимих рішень
plt.figure(figsize=(10, 6))
plt.plot(x1, x2_designers, label="Обмеження дизайнерів")
plt.plot(x1, x2_developers, label="Обмеження розробників")
plt.plot(x1, x2_testers, label="Обмеження тестувальників")

# Додаткові умови
plt.fill_between(x1, 0, np.minimum(np.minimum(x2_designers, x2_developers), x2_testers), color="grey", alpha=0.3, label="Допустима область")

# Графік
plt.xlabel("Кількість сайтів (x1)")
plt.ylabel("Кількість інтернет-магазинів (x2)")
plt.title("Область допустимих рішень")
plt.axhline(0, color="black",linewidth=0.5)
plt.axvline(0, color="black",linewidth=0.5)
plt.legend()
plt.grid()
plt.show()
