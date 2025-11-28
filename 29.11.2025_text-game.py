inventory = []
def scene(inventory):
    while True:
        print(f"ваш инвентарь: {inventory}")
        print()
        print("Вы в комнате. Видите две двери и сундук.")
        print("что будете делать?")
        print("  1 - попытаться открыть первую дверь")
        print("  2 - открыть сундук")
        print("  3 - попытаться открыть вторую дверь")

        choice = input("  выберите действие: ")
        if choice == "1":
            if "ключ" in inventory:
                print("вы открыли дверь.")
                break
            else:
                print("дверь заперта! нужен ключ.")
                print()
        elif choice == "2":
            if "ключ" not in inventory:
                print()
                print("вы открыли сундук и нашли ключ!")
                inventory.append("ключ")
            else:
                print()
                print("сундук пустой..")
        elif choice == "3":
            print()
            print("внутри темно..")
            print("что будете делать?")
            print("  1 - вернуться назад")
            print("  2 - пройти внутрь")
            choice2 = input("  выберите действие: ")
            if choice2 == "1":
                print("вы вернулись назад.")
            else:
                print("вы зашли внутрь и вас съел монстр!")
                print("вы умерли..")
                break
        else:
            print()
            print("выберите 1 или 2")
scene(inventory)