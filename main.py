#~~ Dice game made by Ivan (Username: Tuxuis). Open-sourced and commented. ~~
# Context: The goal of this game is to throw 3 dices, each with 6 sides and the user will guess
#          what the sum of all those numbers will be.


# Importing in "ranint" straight from "random" as we do not need the entire module "random"
from random import randint

# main function to store our code
def main():

    # function named "generate" that will generate the amount of numbers we want to throw and return a list of those numbers.
    def generate(n: int) -> list:
        # a list called "num" which will store our numbers.
        num = []
        # for loop using range which will loop 'n' times, the amount of numbers that we want.
        for i in range(n):
            # randomizing a number between 1-6 and storing it in a variable called "random_number"
            random_number = randint(1,6)
            # adding the previous variable to our list "num" so that we can return it later
            num.append(random_number)
        # returning out list
        return num
    
    
    # This will be our welcome message and menu, I will keep it simple.
    print("Welcome to my dice game!")
    # I will get the users name and store it in a variable called "name"
    name = input("What is your name?: ")
    print("Welcome, " + name + "!")
    # I will also get the users guess on what they think the sum will be and store it in a variable called "guess". I will also convert the input to 'int'
    guess = int(input("Pick a number between 3-18: "))
    # Adding an 'if' statement to check if the user has inputed a negative number, if so then I will convert it back to positive using the 'abs()' function.
    if guess < 0:
        guess = abs(guess)
    # making a line to separate the next part
    print("------------------------")
    
    # Creating a variable named "numbers" which will hold a list that is generated by "generate()" function, in this case I will use the argument "n" to generate 3 numbers.
    numbers = generate(3)
    # Creating a variable named "answer" which will hold the sum of all the numbers in my list "numbers". I will use the "sum()" function to add all the numbers up toghter.
    answer = sum(numbers)

    # Printing out our numbers one by one
    for i in numbers:
        print(str(i))

    # making an if statement to check if the user has answered correctly or not.
    if guess == answer:
        print("Wow! You have answered correctly!")
    else:
        # Otherwise, if the user has not answered correctly then we will give them the answer and tell him how far off they were.
        print("Oh no! You answered wrong. Better luck next time.")
        print("The answer is: " + str(answer))
        print("Your off by: " + str(abs(guess - answer)))


# checking to see if file is ran as script not module
if __name__ == "__main__":
    # if all checks out, then execute our main function.
    main()
