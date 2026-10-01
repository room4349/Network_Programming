while True:
    filename = input("읽을 파일명을 입력하세요 (종료: Enter): ").strip()
    if not filename:
        break

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("파일이 없습니다. 다른 파일명을 입력하세요.")
        continue
    except (OSError, UnicodeError) as error:
        print(f"파일을 읽을 수 없습니다: {error}")
        continue

    text = "".join(lines)

    # 띄어쓰기, 탭, 줄바꿈 등 공백 문자는 글자 수에서 제외합니다.
    characters = sum(1 for character in text if not character.isspace())
    words = len(text.split())
    line_count = len(lines)

    print(f"characters : {characters}")
    print(f"words      : {words}")
    print(f"lines      : {line_count}")
    break
