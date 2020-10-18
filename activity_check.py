from datetime import datetime as dt, timedelta
from db import query_user_last_seen, list_users

# Пользователь вводит мейл, на ввод мейла у него 3 попытки, после чего пауза
# на 10 секунд.

def get_email_from_user(attempts=3, sleep_duration=10):
    email = input("Введите e-mail: ")
    i = 1
    while (email.find("@") == -1):
        print("неправильный email. Попробуйте еще раз")
        i = i + 1
        email = input("Попытка " + str(i) + ". Введите e-mail: ")
        if i % attempts == 0:
            print("Переборщили с попытками. Подождите " + str(sleep_duration)
+ " секунд")
            time.sleep(sleep_duration)
    return email


email = get_email_from_user()

# Мейл преобразуется в логин по правилу: все, что до символа собаки, — это
# логин, а строка приводится к нижнему регистру.

username = email.split("@")[0].lower()




	#[хз как еще.  составляю [(),()..] 
registered_users = list_users()
list_n = []


k = 0
while k < len(registered_users):
    list_n.append(registered_users[k])
    k += 1



#вытскиваю [([0]), ([0])...]
names = [x[0] for x in list_n]


# Username проверяется по базе. Если в базе нет такого юзернейма,
# пользователю выводится строка «Вы с нами совсем недавно! Добро
# пожаловать».
# Если username в базе есть, то надо найти, когда пользователь логинился в
# последний раз. Если с момента последнего введения логина прошло более 180
# дней, вывести сообщение: «Вам надо подтвердить логин», если меньше 180
# дней, то вывести: «Ваш аккаунт подтвержден до...» и вместо
# многоточия сегодняшняя дата + 180 дней. Пример вывода: «Ваш аккаунт
# подтвержден до 2019-03-20».

def check_user_is_active():
    if username not in names:
        print('Вы с нами совсем недавно! Добро пожаловать')
    else:
        existing_username = username
        last_seen = query_user_last_seen(existing_username)
        print("Пользователь", existing_username, "последний раз заходил", last_seen)
        if ((dt.now() - last_seen).days > 180):
            print('Вам надо подтвердить логин')
        else:
    	    print('Ваш аккаунт подтвержден до:', dt.now() + timedelta(days = 180))
    return 0
check_user_is_active()