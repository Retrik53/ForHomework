import json
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично"
}

def get_user_level():
    user_input = input("Выберите уровень сложности \nлегкий, средний, сложный.\n").lower().strip()

    if user_input == 'легкий':
        print("Выбрана сложность - легкий.")
        return words_easy
    elif user_input == 'средний':
        print("Выбрана сложность - средний.")
        return words_medium
    elif user_input == 'сложный':
        print("Выбрана сложность - сложный.")
        return words_hard
    else:
        print("Ошибка ввода, выбрана сложность по умолчанию - легкий.")
        return words_easy


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

    result = levels[min(correct_count, max(levels.keys()))]

    print("\nПравильно отвечены слова:")
    for word, is_correct in answers.items():
        if is_correct:
            print(word.title())

    print("\nНеправильно отвечены слова:")
    for word, is_correct in answers.items():
        if not is_correct:
            print(word.title())

    return result