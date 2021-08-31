# put your python code here
on_axis = []
quarters = {"Первая четверть": 0, "Вторая четверть": 0, "Третья четверть": 0, "Четвертая четверть": 0}

for i in range(int(input())):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        quarters["Первая четверть"] += 1
    elif x < 0 and y > 0:
        quarters["Вторая четверть"] += 1
    elif x < 0 and y < 0:
        quarters["Третья четверть"] += 1
    elif x > 0 and y < 0:
        quarters["Четвертая четверть"] += 1
    else:
        on_axis.append((x, y))

print(*[f"{k}: {v}" for k, v in quarters.items()], sep='\n')