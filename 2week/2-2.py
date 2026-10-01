student = {"id": [], "name": []}


def add_student():
    while True:

        student_id = input("학번을 입력하세요 (끝내려면 0): ")
        if student_id == "0":
            break
        name = input("이름을 입력하세요 (끝내려면 none): ")
        if name== "none":
            break

        if not student_id or not name:
            print("학번과 이름을 모두 입력하세요.")
            continue

        student["id"].append(student_id)
        student["name"].append(name)


def print_student():
    while True:
        student_id = input("조회할 학생의 학번을 입력하세요 (끝내려면 quit): ").strip()

        if student_id.lower() == "quit":
            break

        if student_id in student["id"]:
            index = student["id"].index(student_id)
            print(f"학번: {student['id'][index]}, 이름: {student['name'][index]}")
        else:
            print("not found")


add_student()
print_student()
