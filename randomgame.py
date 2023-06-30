from random import randint
import sys

#generate a number 1 - 10
answer = randint(sys.argv[1], sys.argv[10])
# input from user


#check that input is a number from 1 - 10
while True:
    try:
        print(answer)
        guess = int(input('guess a number 1-10: '))
        if 0 < guess < 11 :
            if guess == answer:
                print('hey you are a genius')
                break
        else:
            print('hey bozo! I said 1 to 10')
    except ValueError:
        print('please enter a number')
        continue

#check if number is the right guess. Otherwise ask again.