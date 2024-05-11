import requests
from bs4 import BeautifulSoup

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        # Смотрим html сайта: чтобы получить слово, нам нужны тэг "div" и id="random_word"
        english_words = soup.find("div", id="random_word").text.strip()
        # Чтобы получить описание слова, нам нужны тэг "div" и id="random_word_definition"
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except Exception as e:
        print(f"Произошла ошибка {e}")

def word_game():
    print("Добро пожаловать в игру!")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        print(f"Значение слова: {word_definition}")
        answer = input("Что это за слово? ")
        if answer == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово {word}")

        play_again = input("Хотите сыграть еще раз (y/n)? ")
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_game()
