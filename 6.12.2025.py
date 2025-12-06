while True:
    try:
        days = int(input("введите количество учебных дней: "))
        if days < 0:
            print("ошибка: число должно быть положительным")
        elif days > 7:
            print("ошибка: не может быть больше 7 дней")
        else:
            break
    except ValueError:
        print("ошибка: введите целое число")
    except KeyboardInterrupt:
        print("\nпрограмма прервана")
        break
total = 0
for a in range(1, days + 1):
    while True:
        try:
            hours = float(input(f"часов для дня {a}: "))
            if hours < 0:
                print("часы не могут быть отрицательными")
            else:
                total += hours
                break
        except ValueError:
            print("ошибка: введите число")
        except KeyboardInterrupt:
            print("\nпрограмма остановлена")
            break
print(f"всего часов: {total}")