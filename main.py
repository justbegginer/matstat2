from utils import uni, binom, geom, pois

def main():
    options = {
        "1": uni.Uniform(),
        "2": geom.Geometric(),
        "3": binom.Binomial(),
        "4": pois.Poisson()
    }

    while True:
        print("Меню:")
        print("1. Равномерное распределение")
        print("2. Геометрическое распределение")
        print("3. Биномиальное распределение")
        print("4. Пуассоновское распределение")
        print("5. Выход")

        choice = input("Выберите опцию: ")

        if choice in options:
            options[choice].modeling_accuracy()
        elif choice == "5":
            print("Goodbye")
        else:
            print("Ошибка: Некорректный выбор. Пожалуйста, введите число от 1 до 5.")


if __name__ == "__main__":
    main()
