from itertools import combinations


fruits = ['🍎', '🍊', '🍌', '🍒', '🍆', '🥕', '🥝', '🍍']
number = 3

for item in combinations(fruits, number):
    temp = " ".join(word for word in item)
    print(temp)
