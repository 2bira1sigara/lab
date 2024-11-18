scores = eval(input())

team1_points = 0
team2_points = 0
team1_total = 0
team2_total = 0
print(type(scores[0]))
for score in scores:
    team1_total += score[0]
    team2_total += score[1]

    if score[0] > score[1]:
        team1_points += 3
    elif score[1] > score[0]:
        team2_points += 3
    else:
        team1_points += 1
        team2_points += 1

print(f"\ntakim 1 total: {team1_total}")
print(f"takim 2 total: {team2_total}")
print(f"takim 1 puan: {team1_points}")
print(f"takim 2 puan: {team2_points}")

if team1_points > team2_points:
    print("takim 1 kazandi")
elif team2_points > team1_points:
    print("takim2 kazandi")
else:
    print("berabere")

scores = [(3, 2), (1, 2), (4, 2)]
