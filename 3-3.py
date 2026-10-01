def count_vowel(string): 
    vowel = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowel:
            count += 1
    return count

string = input("문자열을 입력하세요: ")

print(f"모음의 개수: {count_vowel(string)}")