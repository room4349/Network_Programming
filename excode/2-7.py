import random

words = ["apple", "banana", "cherry", "date", "elderberry"]


def show_word(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter
        else:
            result += "_"
    return result


def game():
    print("Hangman Game Start")

    game_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        word_on_screen = show_word(game_word, guessed_letters)
        print(f"단어: {word_on_screen}")

        if word_on_screen == game_word:
            print("축하합니다! 모든 글자를 맞추셨습니다.")
            break

        print(f"남은 시도 횟수: {attempts}")
        print(f"입력했던 글자들: {guessed_letters}")
        guess = input("글자를 입력해주세요: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("영문자 한 글자만 입력하세요.")
        elif guess in guessed_letters:
            print("이미 입력한 글자입니다. 다른 글자를 입력해주세요.")
        else:
            guessed_letters.append(guess)
            if guess in game_word:
                print(f"정답입니다! '{guess}' 글자가 포함되어 있습니다.")
            else:
                print(f"틀렸습니다! '{guess}' 글자가 포함되어 있지 않습니다.")
                attempts -= 1
    else:
        print(f"게임 오버! 정답은 '{game_word}'입니다.")

def main():
    while True:
        i = input("게임을 종료 하시려면 0을 입력해주세요")
        if i == "0":
            print("게임을 종료합니다.")
            break
        else:
            game()


main()