import matplotlib.pyplot as plt

# Создаем линейный график 
x = [1, 4, 6, 7]
y = [3, 5, 8, 10]
plt.plot(x, y) #x, y с одной точкой (0, 0)
plt.title("Пример простого линейного графика")
plt.xlabel("x ось")
plt.ylabel("y ось")
plt.show()

# Создаем гистограмму из списка чисел
data = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 6]
plt.hist(data, bins=6)
plt.xlabel("x ось")
plt.ylabel("y ось")
plt.title("Тестовая гистограма")
plt.show()

plt.scatter(x, y)
plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Тестовая диаграмма рассеяния")
plt.show()

