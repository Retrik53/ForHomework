from Funcs import get_user_level, base_program, get_result
import json

# Основной блок программы
if __name__ == "__main__":
    # Загрузка данных из JSON-файла
    with open('questions.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    username = input("Пожалуйста, введите ваше имя: ")

    test_words = get_user_level(data)

    test_answers = base_program(test_words)

    result = get_result(test_answers, data['levels'])

    filename = f"{username}_results.json"
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump({"username": username, "answers": test_answers, "result": result}, file, ensure_ascii=False)

    print(f"\nВаш ранг:\n{result}")