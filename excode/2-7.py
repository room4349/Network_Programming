import random

words = ["hangman", "python", "network", "socket"]


def show_word(word, guessed):
    return " ".join(letter if letter in guessed else "_" for letter in word)


def play_game():
    word = random.choice(words)
    guessed = []
    trials = 4

    while trials > 0:
        print(show_word(word, guessed))

        if all(letter in guessed for letter in word):
            print("Good Job!")
            return

        letter = input("글자를 입력하세요: ").strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            print("한 글자만 입력하세요")
            continue

        if letter in guessed:
            print("이미 입력한 글자입니다")
            continue

        guessed.append(letter)

        if letter not in word:
            trials -= 1
            print(f"Nope! {trials} trials left")

    print("Fail!")


while True:
    play_game()
    answer = input("게임을 계속하시겠습니까? (y/n): ").strip().lower()
    if answer != "y":
        break
