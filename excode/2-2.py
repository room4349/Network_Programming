students = {}

while True:
    student_id = input("학번을 입력하세요 (끝내려면 0): ").strip()
    if student_id == "0":
        break

    name = input("이름을 입력하세요 (끝내려면 None): ").strip()
    if name == "None":
        break

    students[student_id] = name

print(students)

while True:
    student_id = input("조회할 학번을 입력하세요 (끝내려면 quit): ").strip()
    if student_id == "quit":
        break

    if student_id in students:
        print(students[student_id])
    else:
        print("not found!")
