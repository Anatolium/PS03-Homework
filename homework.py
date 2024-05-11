import requests
from bs4 import BeautifulSoup
from googletrans import Translator

translator = Translator()


def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        # Чтобы получить слово, нам нужны тэг "div" и id="random_word"
        english_word = soup.find("div", id="random_word").text.strip()
        # Чтобы получить описание слова, нам нужны тэг "div" и id="random_word_definition"
        english_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "word": english_word,
            "definition": english_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        if word_dict is None:
            break

        word = word_dict.get("word", "")
        word_definition = word_dict.get("definition", "")

        russian_word = translator.translate(word, dest="ru").text
        russian_definition = translator.translate(word_definition, dest="ru").text

        print(f"Значение слова: {russian_definition}")
        n_opened = 0
        while True:
            answer = input("Что это за слово? (нажмите пробел для подсказки): ")
            if answer.strip():
                break

            n_opened += 1
            if n_opened == len(russian_word):
                break

            print(f"Слово начинается с букв '{russian_word[:n_opened]}…'")

        if answer == russian_word:
            print("**** Ответ верный! ****")
        else:
            print(f"Ответ неверный, было загадано слово *** {russian_word} ({word}) ***")
        print()
        play_again = input("Хотите сыграть еще раз? (введите 0, если нет): ")
        if play_again == "0":
            print("**** Спасибо за игру! ****")
            break

word_game()
