import json


def load_data(file_path):
    """Загрузка данных из файла."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        # Если файл не найден, создаем пустой словарь
        print("Файл не найден. Создан новый пустой словарь.")
        data = {}
    return data


def save_data(data, file_path):
    """Сохранение данных в файл."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def add_artist_album(data, artist, album):
    """Добавление нового альбома к существующему артисту или создание нового артиста."""
    if artist in data:
        data[artist].append(album)
    else:
        data[artist] = [album]
    return data


def remove_artist(data, artist):
    """Удаление артиста вместе со всеми его альбомами."""
    if artist in data:
        del data[artist]
    return data


def find_albums_by_artist(data, artist):
    """Поиск всех альбомов указанного артиста."""
    albums = []
    if artist in data:
        albums = data[artist]
    return albums


def edit_artist_name(data, old_artist, new_artist):
    """Редактирование имени артиста."""
    if old_artist in data:
        data[new_artist] = data.pop(old_artist)
    return data


def list_artists_and_albums(data):
    """Показывает список всех артистов и их альбомов."""
    if data:
        for artist, albums in sorted(data.items()):
            print(f"{artist}:")
            for album in sorted(albums):
                print(f"\t{album}")
    else:
        print("Нет данных для отображения.")


def show_menu():
    print("Меню:")
    print("1. Добавить артиста и альбом")
    print("2. Удалить артиста")
    print("3. Найти альбомы артиста")
    print("4. Изменить имя артиста")
    print("5. Список артистов и альбомов")  # Новый пункт меню
    print("0. Выход")


def get_user_choice():
    choice = input("Введите номер пункта меню: ")
    while not choice.isdigit() or int(choice) < 0 or int(choice) > 6:
        print("Неверный ввод. Попробуйте снова.")
        choice = input("Введите номер пункта меню: ")
    return int(choice)


def handle_adding(data):
    artist = input("Введите имя артиста: ").strip().title()
    album = input("Введите название альбома: ").strip().title()
    data = add_artist_album(data, artist, album)
    print(f"{album} успешно добавлен к {artist}.")
    return data


def handle_removing(data):
    artist = input("Введите имя артиста для удаления: ").strip().title()
    data = remove_artist(data, artist)
    print(f"{artist} удален.")
    return data


def handle_finding(data):
    artist = input("Введите имя артиста для поиска: ").strip().title()
    albums = find_albums_by_artist(data, artist)
    if albums:
        print(f"Альбомы {artist}:")
        for album in albums:
            print(f"- {album}")
    else:
        print(f"У {artist} пока нет альбомов.")


def handle_editing(data):
    old_artist = input("Введите старое имя артиста: ").strip().title()
    new_artist = input("Введите новое имя артиста: ").strip().title()
    data = edit_artist_name(data, old_artist, new_artist)
    print(f"Имя артиста изменено с {old_artist} на {new_artist}.")
    return data


def main():
    file_path = "Artists.json"
    music_data = load_data(file_path)

    while True:
        show_menu()
        choice = get_user_choice()

        if choice == 0:
            break
        elif choice == 1:
            music_data = handle_adding(music_data)
        elif choice == 2:
            music_data = handle_removing(music_data)
        elif choice == 3:
            handle_finding(music_data)
        elif choice == 4:
            music_data = handle_editing(music_data)
        elif choice == 5:
            list_artists_and_albums(music_data)

        save_data(music_data, file_path)


if __name__ == "__main__":
    main()