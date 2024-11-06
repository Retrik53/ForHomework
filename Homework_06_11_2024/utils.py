import re


def get_reg_data():
    return {
        'username': r'^[A-Za-zА-Яа-яЁё]+$',
        'surname': r'^[A-Za-zА-Яа-яЁё]+$',
        'phone': r'\+\d{1,3}\(\d{1,2}\)\d{7}$',
        'email': r'[A-Za-z0-9_]+@yandex\.ru+$'
    }


def check_unique_data(user_data, data_to_check, users_list):
    for user in users_list:
        if user.get(data_to_check) == user_data[data_to_check]:
            return False
    return True


def reg_check(user_data, reg_pattern, users_list, data_to_check=None):
    patterns = get_reg_data()
    is_valid = re.fullmatch(patterns[reg_pattern], user_data[reg_pattern])
    if data_to_check and users_list:
        is_unique = check_unique_data(user_data, data_to_check, users_list)
        return is_valid and is_unique
    return is_valid


def get_user_input(users_list):
    user_data = {}
    while True:
        username = input("Введите имя: ")
        if reg_check({'username': username}, 'username', users_list, 'username'):
            user_data['username'] = username
            break
        else:
            print("Некорректное или не уникальное имя пользователя! Попробуйте еще раз.")

    while True:
        surname = input("Введите фамилию: ")
        if reg_check({'surname': surname}, 'surname', users_list, 'surname'):
            user_data['surname'] = surname
            break
        else:
            print("Некорректная или не уникальная фамилия пользователя! Попробуйте еще раз.")

    while True:
        phone = input("Введите номер телефона (+***(**)*******): ")
        if reg_check({'phone': phone}, 'phone', users_list, 'phone'):
            user_data['phone'] = phone
            break
        else:
            print("Некорректный или не уникальный номер телефона! Попробуйте еще раз.")

    while True:
        email = input("Введите email (******@yandex.ru): ")
        if reg_check({'email': email}, 'email', users_list, 'email'):
            user_data['email'] = email
            break
        else:
            print("Некорректный или не уникальный адрес электронной почты! Попробуйте еще раз.")

    return user_data