# острой диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.
# import numpy as np
# random_array = np.random.rand(5)  # массив из 5 случайных чисел
# print(random_array)

import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(5)
y = np.random.rand(5)

print(x)
print(y)

# Создание диаграммы рассеяния
plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=50, c='red', edgecolor='black', alpha=0.7)
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(axis='both', alpha=0.75)
plt.show()
