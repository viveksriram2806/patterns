#1
import random
random_no = random.randint(1,10)
guesses = 0
while True:
    user_input = int(input())
    guesses += 1
    if user_input < random_no:
        print("Higher! Try again.")
    elif user_input > random_no:
        print("Lower! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {random_no} in {guesses} random_noattempts.")
        break


#2
l=[6,8,10,12,14]
for i in l:
    print(i,i**2)

#3
for i in range(1,101):
    if i%3==0 and i%5==0:
        print('fizzbuzz',i)
    elif i%3==0:
        print('fizz of 3',i)
    elif i%5==0:
        print('buzz of 5',i)
    else:
        print('not divisible by 3 and 5')

