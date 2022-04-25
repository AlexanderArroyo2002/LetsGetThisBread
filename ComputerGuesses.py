import random

print("Hello there, in this program, we the computer is going to try to guess the number that you are thinkin of 1 - 10 \nHowever, we only get 5 guesses to gess your number.")

def main():
    guesses = 0
    count = 1
    x = 1
    y = 10
    
    userInp = input("Deal? [Y/N]: ")

    if userInp == "Y":
        guess = random.randint(1, 10)
        while True:
            try:
                answer = input(f"guess number {count} is {guess}. Is my answer <, >, or = to your guess?: ")
                if answer == ">":
                    count += 1
                    guesses += 1
                    y = guess
                    if guesses == 5:
                        print("Game over. I lost")
                        break
                    else:
                        guess = random.randint(x, y-1)
                elif answer == "<":
                    count += 1
                    guesses +=1
                    x = guess
                    if guesses == 5:
                        print("Game over. I lost")
                        break
                    else:
                        guess = random.randint(x+1, y)
                elif answer =="=":
                    print(f"Congrats, I win! It ony tok me {count} guesses")
                    break
                else:
                    print("Invalid input. Please try again")
            except ValueError:
                print("Ha caught u cheater!")
                break
            
    elif userInp == "N":
        print("Thank you have a good day!")
    else:
        print("Invalid response. Please pick a valid answer")
        main()
        
main()
        
