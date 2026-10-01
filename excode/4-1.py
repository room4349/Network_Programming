from pathlib import Path


while True:
    filename = input("읽을 파일명을 입력하세요 (종료: Enter): ").strip()
    if not filename:
        break

    path = Path(filename)

    try:
        with path.open("r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("파일이 없습니다. 다른 파일명을 입력하세요.")
        continue
    except (OSError, UnicodeError) as error:
        print(f"파일을 읽을 수 없습니다: {error}")
        continue

    # 각 줄 앞에 1부터 시작하는 줄 번호를 붙입니다.
    numbered_text = "".join(
        f"{number} {line}" for number, line in enumerate(lines, start=1)
    )
    print(numbered_text, end="" if numbered_text.endswith("\n") else "\n")

    save_path = path.with_suffix(".sav")
    if save_path == path:
        save_path = path.with_name(path.name + ".sav")

    try:
        with save_path.open("w", encoding="utf-8") as file:
            file.write(numbered_text)
        print(f"저장 완료: {save_path}")
    except OSError as error:
        print(f"파일을 저장할 수 없습니다: {error}")

    break
