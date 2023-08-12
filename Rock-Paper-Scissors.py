import random
user_search = input("Введите: камень, ножницы или бумага:")
user_search = user_search.lower()
random_number = random.randint(1, 30)

if random_number in range(1, 11):
    random_number = 'камень'
elif random_number in range(11, 21):
    random_number = 'ножницы'
elif random_number in range(21, 31):
    random_number = 'бумага'

if random_number == user_search:
    print(f'Вы ввели: {user_search}, робот ввел: {random_number}.')
    print("Ничья!")
elif user_search == 'камень' and random_number == 'ножницы':
    print(f'Вы ввели: {user_search}, робот ввел: {random_number}.')
    print("Вы победили!")
elif user_search == 'камень' and random_number == 'бумага':
    print(f'Вы ввели: {user_search}, робот ввел: {random_number}.')
    print("Вы проиграли!")
elif user_search == 'ножницы' and random_number == 'камень':
    print(f'Вы ввели: {user_search}, робот ввел: {random_number}.')
    print("Вы проиграли!")
elif user_search == 'ножницы' and random_number == 'бумага':
    print(f'Вы ввели: {user_search}, робот ввел: {random_number}.')
    print("Вы победили!")
elif user_search == 'бумага' and random_number == 'камень':
    print(f'Вы ввели: {user_search}, робот ввел: {random_number}.')
    print("Вы победили!")
elif user_search == 'бумага' and random_number == 'ножницы':
    print(f'Вы ввели: {user_search}, робот ввел: {random_number}.')
    print("Вы проиграли!")
else:
    print("Введите правильное значение!!!")
    
a = input()
