def count_vowel(text):
    count = 0
    for character in text:
        if character in "aeiouAEIOU":
            count += 1
    return count


text = input("문자열을 입력하세요: ")
print(f"모음의 개수: {count_vowel(text)}")
