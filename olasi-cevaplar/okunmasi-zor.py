scores = eval(input())

team1_points = 0
team2_points = 0
team1_total = 0
team2_total = 0
leng = len(scores)
for i in range(leng):
    team1_total += scores[i][0]
    team2_total += scores[i][1]

    if scores[i][0] > scores[i][1]:
        team1_points += 3
    elif scores[i][1] > scores[i][0]:
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
