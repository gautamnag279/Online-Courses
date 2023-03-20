#For choosing random words from the list
import random

#Ask for participant name and print it
name = input("Enter player name:")
print('Welcome' , name , '!')

#List of words
words = ['flexanimous', 'jungermania', 'science', 'astrophotonic', 
		'python', 'geology', 'player', 'condition', 
		'hofstadter', 'wolowitz', 'board', 'beethoven' , 'sherlock']

#Choose a random word from the above list
word = random.choice(words)

#Prompting the letters
print('Begin!')
guesses = ''

#Defining the difficulty
print('Type b for beginner ; i for Intermediate ; d for difficult')
diff = input('Choose your difficulty:') 

#Counting the number of turns
if diff == 'b':
    turns = 10
    while turns > 0:
        
        #Counting the number of times the user failed
        failed  = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print('__\n')
                #for every failure, there will be an +1 increment in failure
                failed += 1
        
        #If all character are guessed, the user wins
        if failed == 0:
            print("You Win!")
            print('The word is:' , word)
            break
        
        # if user has input the wrong alphabet then it will ask user to enter another alphabet
        guess = input("Guess a character: ")
        guesses += guess
        
        #If guessed incorrectly, a turn will be lost
        if guess not in word:
            turns -= 1
            print("WRONG!")
            print("You have" , +turns , "attempts left")
            
            if turns == 0:
                print('You lose!')
                print('The word is:' , word)
                
                
if diff == 'i':
    turns = 5
    while turns > 0:
        
        #Counting the number of times the user failed
        failed  = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print('__')
                #for every failure, there will be an +1 increment in failure
                failed += 1
        
        #If all character are guessed, the user wins
        if failed == 0:
            print("You Win!")
            print('The word is:' , word)
            break
        
        # if user has input the wrong alphabet then it will ask user to enter another alphabet
        guess = input("Guess a character: ")
        guesses += guess
        
        #If guessed incorrectly, a turn will be lost
        if guess not in word:
            turns -= 1
            print("WRONG!")
            print("You have" , +turns , "attempts left")
            
            if turns == 0:
                print('You lose!')
            
if diff == 'd':
    turns = 3
    while turns > 0:
        
        #Counting the number of times the user failed
        failed  = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print('__')
                #for every failure, there will be an +1 increment in failure
                failed += 1
        
        #If all character are guessed, the user wins
        if failed == 0:
            print("You Win!")
            print('The word is:' , word)
            break
        
        # if user has input the wrong alphabet then it will ask user to enter another alphabet
        guess = input("Guess a character: ")
        guesses += guess
        
        #If guessed incorrectly, a turn will be lost
        if guess not in word:
            turns -= 1
            print("WRONG!")
            print("You have" , +turns , "attempts left")
            
            if turns == 0:
                print('You lose!')