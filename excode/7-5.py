# 연습 7-5: 리스트 컴프리헨션으로 모음 제거
text = "window programm"
consonants = [character for character in text if character not in "aeiou"]

print(consonants)
