import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom, chi2

# Параметры гипергеометрического распределения
M = 25  # Общее количество элементов
N = 8   # Количество успехов в популяции
n = 10  # Количество элементов для выборки

# Функция для вычисления вероятностей с использованием рекуррентной формулы
def compute_hypergeom_pmf_recursively(M, n, N):
    pmf = np.zeros(N + 1)
    pmf[0] = hypergeom.pmf(0, M, N, n)  # Начальное значение p_0
    for k in range(N):
        r_k = (N - k) * (n - k) / ((k + 1) * (M - N - n + k + 1))
        pmf[k + 1] = pmf[k] * r_k
    return pmf

# Генерация выборки
def generate_sample_from_pmf(pmf, size=100):
    return np.random.choice(len(pmf), size=size, p=pmf)

# Вычисление PMF
pmf_recursive = compute_hypergeom_pmf_recursively(M, n, N)
sample_recursive = generate_sample_from_pmf(pmf_recursive, 100)

# Построение гистограммы
k = np.arange(0, N + 1)
bins = np.arange(k.min(), k.max() + 2) - 0.5
plt.figure(figsize=(12, 6))
plt.hist(sample_recursive, bins=bins, density=True, alpha=0.7, label='Эмпирическое распределение')
plt.stem(k, pmf_recursive, 'r', markerfmt='ro', basefmt=" ", label='Теоретическое распределение')
plt.title('Гистограмма и теоретическое PMF гипергеометрического распределения')
plt.xlabel('Количество успехов')
plt.ylabel('Вероятность')
plt.legend()
plt.show()

# Вычисление критерия Пирсона
observed_frequencies, _ = np.histogram(sample_recursive, bins=bins, density=False)
expected_frequencies = pmf_recursive * 100
chi2_stat = ((observed_frequencies - expected_frequencies)**2 / expected_frequencies).sum()
p_value = chi2.sf(chi2_stat, df=len(observed_frequencies)-1)

# Вывод результатов проверки гипотезы
print(f"Значение статистики Пирсона: {chi2_stat}")
print(f"p-значение: {p_value}")
