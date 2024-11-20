﻿# Присвоєння значень
X = True # Присвоїмо логічне значення "Істина"
print(X)
Y = False # Присвоїмо логічне значення "Хибність"
print(Y)
print(type(X)) #Виведемо тип логічної змінної

#############

# Програмування таблиці істинності
X_arr=[False,True,False,True]
Y_arr=[False,False,True,True]
print("#  | X |  Y  | X∧Y | X∨Y |")
for i in range(len(X_arr)):
  print(f"{i+1}|{X_arr[i]}|{Y_arr[i]}|{X_arr[i] and Y_arr[i]}|{X_arr[i] or Y_arr[i]}|")