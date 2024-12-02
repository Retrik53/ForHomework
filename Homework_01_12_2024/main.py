from Homework_01_12_2024 import Funcs
from Funcs import get_user_level, base_program, get_result, levels, words_easy, words_medium, words_hard
import json
if __name__ == "__main__":
    username = input("Пожалуйста, введите ваше имя: ")

    test_words = get_user_level()

    test_answers = base_program(test_words)

    result = get_result(test_answers, levels)

    filename = f"{username}_results.json"
    with open(filename, 'w', encoding='UTF-8') as file:
        json.dump({"username": username, "answers": test_answers, "result": result}, file)

    print(f"\nВаш ранг:\n{result}")