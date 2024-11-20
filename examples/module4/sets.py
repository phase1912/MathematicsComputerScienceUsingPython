num_set = {1, 2, 3, 4, 5, 6}
print(num_set)

###########

string_set = {"Nicholas", "Michelle", "John", "Mercy"}
print(string_set)

###########

num_set = set([1, 2, 3, 4, 5, 6])
print(num_set)

#############

months = set(["Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])
# Чи належить елемент "May" множині months
print("May" in months)

#############

# Об'єднання  множин з елементами рядками
months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
months_b = set(["July", "Aug", "Sep", "Oct", "Nov", "Dec"])


all_months = months_a.union(months_b)
print(all_months)

###############

# Об'єднання  множин з елементами числами
x = {1, 2, 3}
y = {4, 3, 6}
z = {7, 4, 9}


print(x | y | z)

#############Приклад коду, що реалізує виведення результату перетину множин:

x = {1, 2, 3}
y = {4, 3, 6}


print(x & y) # Результат: 3

##########А таким чином можна отримати результат різниці множин a і b:

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
diff_set = set_a.difference(set_b)
print(diff_set)

###############Симетрична різниця між множинами



set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a ^ set_b)