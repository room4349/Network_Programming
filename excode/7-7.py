scores = {
    "Kim": [80, 90, 70],
    "Lee": [100, 90, 85],
    "Park": [95, 85, 100],
}

averages = {
    name: int(sum(score_list) / len(score_list))
    for name, score_list in scores.items()
}
names = [name for name, average in averages.items() if average >= 90]

print(averages)
print(names)
