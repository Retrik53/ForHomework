from utils import get_user_input

users_list = []

for _ in range(3):
    user_data = get_user_input(users_list)
    users_list.append(user_data)
    print("\nДанные пользователя успешно добавлены:")
    for key, value in user_data.items():
        print(f'{key.capitalize()}: {value}')
    print("-------------------\n")

print("Список всех пользователей:")
for index, user in enumerate(users_list, start=1):
    print(f"Пользователь {index}")
    for key, value in user.items():
        print(f'{key.capitalize()}: {value}')
    print("-------------------\n")