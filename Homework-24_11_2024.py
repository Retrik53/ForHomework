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

while True:
    user_input = input("Выберите уровень сложности (легкий, средний, тяжелый): ").lower().strip()

    if user_input in ("легкий", "средний", "тяжелый"):
        break
    else:
        print("Неизвестная сложность. Установлен уровень по умолчанию - легкий.")
        user_input = "легкий"

if user_input == "легкий":
    words = words_easy
elif user_input == "средний":
    words = words_medium
else:
    words = words_hard

answers = {}
for word in words:
    print(f"{word}, {len(word)} букв, начинается на '{words[word][0].upper()}'...")
    answer = input("Ваш перевод: ")

    if answer.lower().strip() == words[word]:
        print(f"Верно, {word} — это {words[word].title()}.")
        answers[word] = True
    else:
        print(f"Неверно. {word} — это {words[word].title()}.")
        answers[word] = False

correct_words = [word for word, result in answers.items() if result]
incorrect_words = [word for word, result in answers.items() if not result]

print("\nПравильно отвеченные слова:")
for word in correct_words:
    print(word.title())

print("\nНеправильно отвеченные слова:")
for word in incorrect_words:
    print(word.title())

correct_count = sum(answers.values())
rank = min(5, int((correct_count / len(words)) * 6))
print(f"\nВаш ранг: {levels[rank]}")