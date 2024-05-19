from base_distribution import Distribution
import statistics
import random


class Uniform(Distribution):
    def generate_sample(self, low, up, n):
        result = []
        n_values = up - low + 1
        for _ in range(n):
            u = random.random()
            r = int(n_values * u) + low
            result.append(r)
        return result

    def mean_t(self, low, up):
        return (low + up) / 2

    def variance_t(self, low, up):
        n = up - low + 1
        return (n ** 2 - 1) / 12

    def modeling_accuracy(self):
        low = 1
        up = 100
        n = 10000
        sample = self.generate_sample(low, up, n)

        mean = statistics.median(sample)
        theor_mean = self.mean_t(low, up)

        variance = statistics.variance(sample)
        theor_variance = self.variance_t(low, up)

        print(f"Оценка\t\t IRNUNI \t Погрешность \tТеоретическое значение")
        print(f"Медиана\t\t  {mean:<6}\t\t{mean - theor_mean:.3f}"
              f" \t\t  {self.mean_t(low, up):.2f}")
        print(f"Дисперсия\t  {variance:.3f} \t\t {variance - theor_variance:.3f}"
              f" \t\t{self.variance_t(low, up):.2f}")
