#for i in range(10):
#    print("Hello, world")

#x = 10
#while x > 5:
#    print("x is more than 5")
#    x = x - 1
#print("x is 5 right now")    
    
#python libraries - 
##random(standing on the shoulders of others)
#import - keyword

#random.choice(seq)
#import random

#coin = random.choice(["heads", "tails"])
#print(coin)

#random.randint(a, b)
#number = random.randint(1,10)
#print(number)

#random.shuffle(x)
#cards = ["jack", "queen", "king"]
#random.shuffle(cards)
#for card in cards:
#    print(card)
    
##statistics
#import statistics
#statistic.mean() - average
#print(statistics.mean([100, 90]))    
    
##sys
import sys
#sys.argv[] - argument vector
#try:
#    print("hello, my name is", sys.argv[1])
#except IndexError:
#    print("Too few argument")

#sys.exit
#if len(sys.argv) < 2:
#    sys.exit("Too few arguments")
#elif len(sys.argv) > 2:
#    sys.exit("Too many arguments")    

#print("hello, my name is", sys.argv[1])


###############################
def is_power_of_two(number):
  # Check if the number is 0 or negative
  if number <= 0:
    return False

  # This while loop checks if the "number" can be divided by two
  # without leaving a remainder. The loop will continue as long as
  # "number" is greater than 1.
  while number > 1:
    # If the number is not divisible by 2, it is not a power of 2
    if number % 2 != 0:
      return False
    number = number // 2

  # If after dividing by 2 "number" equals 1, then "number" is a power
  # of 2.
  return True


# Calls to the function
print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False


#MY First Game 
import random
def Quodos_game():
  secret_num = random.randint(0,2)
  my_guess = int(input("Guess the number: "))
  
  if my_guess == secret_num:
    print("Weldone bro, You got it!")
  else:
    print("Opps! You loss")

for i in range(3):
  Quodos_game()

