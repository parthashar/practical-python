# bounce.py
#
# Exercise 1.5

ball_height = int(100)

count = 10
i = 0

while i < count:
    i = i + 1
    ball_height = (ball_height * 3) / 5
    print (round(ball_height, 4))