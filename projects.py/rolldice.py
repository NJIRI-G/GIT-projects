import random

answer = input('roll the dice(y/n): ')
while True:
   if answer.lower() == 'y':
      dice1 = random.randint(1,6)
      dice2 = random.randint(1,6)
      print(f'({dice1},{dice2})')
   elif answer.lower() == 'n':
       print("Thanks for playing!")

