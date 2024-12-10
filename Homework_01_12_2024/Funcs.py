import json


def get_user_level(data):
    user_input = input("Выберите уровень сложности (легкий, средний, сложный):\n").lower().strip()

    if user_input == 'легкий':
        print("Выбрана сложность - легкий.")
        return data['easy']
    elif user_input == 'средний':
        print("Выбрана сложность - средний.")
        return data['medium']
    elif user_input == 'сложный':
        print("Выбрана сложность - сложный.")
        return data['hard']
    else:
        print("Ошибка ввода, выбрана сложность по умолчанию - легкий.")
        return data['easy']


def base_program(test_words):
    answers = {}

    for word in test_words:
        print(
            f"Переводите слово: {word}, длина слова: {len(test_words[word])} букв, первая буква: {test_words[word][0].upper()}.")

        user_answer = input("Ваш перевод: ").lower().strip()

        if user_answer == test_words[word]:
            print(f"Верно! {word.title()} — это {test_words[word].title()}.")
            answers[word] = True
        else:
            print(f"Неверно. {word.title()} — это {test_words[word].title()}.")
            answers[word] = False

    return answers


def get_result(answers, levels):
    correct_count = sum(value for value in answers.values())

    result = levels[str(min(correct_count, len(levels)))]

    print("\nПравильно отвечены слова:")
    for word, is_correct in answers.items():
        if is_correct:
            print(word.title())

    print("\nНеправильно отвечены слова:")
    for word, is_correct in answers.items():
        if not is_correct:
            print(word.title())

    return result
