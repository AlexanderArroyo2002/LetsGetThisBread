import random

def main():
      print("Hello! Im going to pick a random number and you have to guess what it is.")
      print("The catch is, you only have 3 tries")
      count = 0
      start = input("Are you ready to start? [Y/N]: ")
      number = random.randint(1, 5)
      while True:
          try:
              if start == "Y":
                  answer = int(input("What is your guess?: "))
                  if answer < number:
                      count += 1
                      if count == 3:
                          print("You ran out of tries!")
                          break
                      else: 
                          print("Too low, try again")
                  elif answer > number:
                      count += 1
                      if count == 3:
                          print("You ran out of tries!")
                          break
                      else: 
                          print("Too high, try again")
                  elif answer == number:
                      print("Congrats! You got it")
                      break
                  else:
                      print("Error")
              elif start == "N":
                  print("Come back soon!")
                  exit()
              else:
                  print("Please enter a valid answer!\n")
                  main()
          except ValueError:
               print("Rip u suck")
main()
          
