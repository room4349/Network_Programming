students = {
    "name": "Kim",
    "math": 80,
    "science": 90,
}

students["history"] = 90
del students["math"]
students["science"] = 100

average = (students["history"] + students["science"]) / 2
print(f"{students['name']}'s average score is {average:.0f}")
