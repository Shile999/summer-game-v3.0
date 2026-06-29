import time
import random

name = input("Как тебя зовут? ")
print(f"Привет, {name}")

while True:
    try:
        age = int(input("Сколько тебе лет? "))
        break
    except ValueError:
        print("Введи число, а не буквы!")

print(f"Целых {age} лет")
time.sleep(2)

while True:
    try:
        money = float(input("Сколько у тебя с собой денег? "))
        break
    except ValueError:
        print("Это не похоже на число... попробуй снова.")

print(f"{money} достаточно")
time.sleep(2)

print(f"Ты пошёл в магазин, и с собой у тебя {money} рублей")
time.sleep(2)

days = 0
inventory = []

while days < 3:
    days += 1
    print(f"\n {days} день лета...")
    time.sleep(2)

    event = random.randint(1, 3)
    if event == 1:
        print("Пошёл дождь. Ты остался дома.")
        time.sleep(2)
        continue
    elif event == 2:
        print("Ты встретил друга. Поболтали о жизни.")
        time.sleep(2)
        continue
    else:
        print("Ты снова пошёл в магазин.")
        time.sleep(2)

    price = random.randint(50, 300)
    discount = random.choice([0.1, 0.2, 0.3])
    final = price * (1 - discount)

    print(f"Цена чипсов: {price} руб., скидка {discount * 100:.0f}%, будет {final:.2f} руб.")
    time.sleep(2)

    choice = input("Купить чипсы? (да/нет): ")

    if choice == "да" and money >= final:
        money -= final
        inventory.append("чипсы")
        print(f"Ты купил чипсы. Осталось {money:.2f} руб.")
    elif choice == "да" and money < final:
        print("Денег не хватает. Идёшь домой")
    else:
        print("Ты решил сэкономить")

    time.sleep(2)
    print(f"В инвентаре: {inventory if inventory else 'пока пусто'}")
    time.sleep(2)

print("\n Лето прошло...")
time.sleep(2)

if len(inventory) == 0:
    print("Ты ничего не купил за всё лето. Пустота...")
elif len(inventory) >= 3:
    print("Ты хорошо запасался. Лето запомнится надолго")
else:
    print("Ты кое-что купил. Лето было, но пролетело незаметно")

print("Так незаметно и проходит беззаботное Лето")