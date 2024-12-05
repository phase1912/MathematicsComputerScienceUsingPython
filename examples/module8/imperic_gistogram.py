import numpy as np
import matplotlib.pyplot as plt
import random

#Під'єднуємось до гугл диску
from google.colab import drive
drive.mount('/content/drive')

file_path = '/content/drive/MyDrive/ds/mat_stat.csv'


# Створи об'єкт, який міститиме в собі наш датасет
value_data = pd.read_csv(file_path, sep = ';')


value_data.describe()
# value_data.head()
print(value_data.Q106)
print(len(value_data.Q106))

N=len(value_data.Q106) # розмір вибірки
X = value_data.Q106


# формується 2 масиви: n - кількість елементів, що попали в інтервал, x - масив меж інтервалів
print(np.histogram(X, bins=13))
n,x=np.histogram(X, bins=13)


# масив початків інтервалів (прибрали останнє, найбільше значення)
xmin=x[:-1]


# ширина інтервалу (різниця двох послідовних стовпчиків).
dx=x[1]-x[0]


# емпірична приведена частота: частка від кількості елементів в інтервалі та загальної кількості елементів.
y=n/N


# масив центрів інтервалів
xmid=xmin+dx/2
# виводимо емпіричну гістограму приведених частот
plt.bar(xmid, y, width=dx, color='y')


# Виводимо підписи на осях
plt.xlabel('x')
plt.ylabel('Частота (ймовірність)')


# Малюємо сітку та гістограму.
plt.grid()
plt.show()

#############

import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import stats


N=len(value_data.Q106) # розмір вибірки
X = value_data.Q106


# формується 2 масиви: n - кількість елементів, що попали в інтервал, x - масив меж інтервалів
print(np.histogram(X, bins=13))
n,x=np.histogram(X, bins=13)


mean,std = stats.norm.fit(X)


# масив початків інтервалів (прибрали останнє, найбільше значення)
xmin=x[:-1]


# ширина інтервалу (різниця двох послідовних стовпчиків).
dx=x[1]-x[0]


# емпірична приведена частота: частка від кількості елементів в інтервалі та загальної кількості елементів.
y=n/N


# масив центрів інтервалів
xmid=xmin+dx/2
# виводимо емпіричну гістограму приведених частот
plt.bar(xmid, y, width=dx, color='y')


X1=np.linspace(-2,10,1000)
dist2 = stats.norm(loc=mean, scale=std)
plt.plot(X1, dist2.pdf(X1),'k-')



# Виводимо підписи на осях
plt.xlabel('x')
plt.ylabel('Частота (ймовірність)')


# Малюємо сітку та гістограму.
plt.grid()
plt.show()

###

.normaltest(X) # тест на нормальний розподіл (k2 - сума квадратів коефіцієнтів асиметрії і ексцесу)
print (f"Перевірка на відповідність нормальному розподілу: {k2},pvalue = {pvalue}<0.05") # наприклад, якщо pvalue < 0.05, то це не нормальний розподіл


# масив початків інтервалів (прибрали останнє, найбільше значення)
xmin=x[:-1]
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import stats


N=len(value_data.Q106) # розмір вибірки
X = value_data.Q106


# формується 2 масиви: n - кількість елементів, що попали в інтервал, x - масив меж інтервалів
print(np.histogram(X, bins=13))
n,x=np.histogram(X, bins=13)


mean,std = stats.norm.fit(X)



k2,pvalue = stats
# ширина інтервалу (різниця двох послідовних стовпчиків).
dx=x[1]-x[0]


# емпірична приведена частота: частка від кількості елементів в інтервалі та загальної кількості елементів.
y=n/N


# масив центрів інтервалів
xmid=xmin+dx/2
# виводимо емпіричну гістограму приведених частот
plt.bar(xmid, y, width=dx, color='y')


X1=np.linspace(-2,10,1000)
dist2 = stats.norm(loc=mean, scale=std)
plt.plot(X1, dist2.pdf(X1),'k-')



# Виводимо підписи на осях
plt.xlabel('x')
plt.ylabel('Частота (ймовірність)')


# Малюємо сітку та гістограму.
plt.grid()
plt.show()

##########

import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import stats


N=len(value_data.Q106) # розмір вибірки
X_all = value_data.Q106


# формується 2 масиви: n - кількість елементів, що попали в інтервал, x - масив меж інтервалів



mean,std = stats.norm.fit(X)
X= []
for i in range(len(X_all)):
  if 0<X_all[i]<3:
    X.append(1);
  if 3<=X_all[i]<=8:
    X.append(2);
  if 9<=X_all[i]<=10:
    X.append(3);
print(np.histogram(X, bins=3))
n,x=np.histogram(X, bins=3)



k2,pvalue = stats.normaltest(X) # тест на нормальний розподіл (k2 - сума квадратів коефіцієнтів асиметрії і ексцесу)
print (f"Перевірка на відповідність нормальному розподілу: {k2},pvalue = {pvalue}>0.05") # наприклад, якщо pvalue > 0.05, то це не нормальний розподіл


# масив початків інтервалів (прибрали останнє, найбільше значення)
xmin=x[:-1]


# ширина інтервалу (різниця двох послідовних стовпчиків).
dx=x[1]-x[0]


# емпірична приведена частота: частка від кількості елементів в інтервалі та загальної кількості елементів.
y=n/N


# масив центрів інтервалів
xmid=xmin+dx/2
# виводимо емпіричну гістограму приведених частот
plt.bar(xmid, y, width=dx, color='y')


X1=np.linspace(-2,10,1000)
dist2 = stats.norm(loc=mean, scale=std)
plt.plot(X1, dist2.pdf(X1),'k-')



# Виводимо підписи на осях
plt.xlabel('x')
plt.ylabel('Частота (ймовірність)')


# Малюємо сітку та гістограму.
plt.grid()
plt.show()