from base_distribution import Distribution
import math
import random
import statistics


class Geometric(Distribution):
    def geometric_recurrence(self, p, n):
        result = []
        for _ in range(n):
            r = 0
            while random.random() > p:
                r += 1
            result.append(r)
        return result

    def geometric_direct(self, p, n):
        result = []
        for _ in range(n):
            u = random.random()
            r = 1
            while u > p:
                u = random.random()
                r += 1
            result.append(r)
        return result

    def geometric_improved(self, p, n):
        # Создаем список для хранения значений случайной величины
        result = []
        for _ in range(n):
            u = random.random()
            r = int(math.log(u) / math.log(1 - p)) + 1
            result.append(r)
        return result

    def math_exp_t(self, p):
        return 1 / p

    def variance_t(self, p):
        return (1 - p) / (p ** 2)

    def modeling_accuracy(self):
        p = 0.5
        n = 10000
        irngeo_1 = self.geometric_recurrence(p, n)
        irngeo_2 = self.geometric_direct(p, n)
        irngeo_3 = self.geometric_improved(p, n)

        print(f"Оценка\t\t IRNGEO_1 \t IRNGEO_2 \t IRNGEO_3 \tТеоретическое значение")
        print(f"Медиана\t\t  {statistics.median(irngeo_1):<6} \t {statistics.median(irngeo_2):<6}"
              f" \t {statistics.median(irngeo_3):<6} \t\t  {self.math_exp_t(p):.2f}")
        print(f"Дисперсия\t  {statistics.variance(irngeo_1):.3f} \t {statistics.variance(irngeo_2):.3f}"
              f" \t\t {statistics.variance(irngeo_3):.3f} \t\t\t  {self.variance_t(p):.2f}")
