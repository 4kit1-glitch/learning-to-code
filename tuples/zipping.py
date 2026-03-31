scores1 = [2, 3, 1, 5]
scores2 = [5, 2, 4, 4]

# looping by pairs

for pair in zip(scores1, scores2, strict= True):
    print(pair)


# unpacking pairs
sum1 = 0
sum2 = 0
for s1, s2 in zip(scores1, scores2):
    sum1 += s1
    sum2 += s2

if sum1 > sum2:
    print("team 1 wins")
elif sum1 < sum2:
    print("team 2 wins")
else:
    print("draw")