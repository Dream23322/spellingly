

import time
import random
import data.words1
import data.sentance1
import data.capital
import functions.suggestions

while True:
    spelling = 0
    capitals = 0
    slang = 0
    issues = 0
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ",", ".", "?", "[", "]", "`", '~', '<', ">", "/", "'", '"', "`"]
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', "0"]

    print("Input your more than 5 word sentence (must but under 30 words or there is a higher chance of errors happening)")
    text = input()

    list_of_words = text
    list1 = list_of_words
    list_of_words = list_of_words.split() 
    number1 = len(list_of_words)
    number3 = len(list_of_words)
    number1 -= 1
    print(number1)
    print(number3)
    print("This May Take A While\n")
    time.sleep(1)
    while True:
        word = list_of_words[number1].split()
        word1 = word[0]
        
        functions.suggestions.wordSuggestions()
        if number1 < 0:
            break

        if word1.lower() not in data.words1.words1:
            number1 -= 1
            
            letters = list(word1)
        
            number2 = len(letters)
            number2 -= 1
    
            letter_check = True
            no_symbol = False

            while letter_check == True:
                number2 -= 1
                if number2 < 0:
                    letter_check = False
                    

                if letters[number2] in symbols:
                    no_symbol = True
                    print("\nSymbol Detected In Word:", word1) 
                    letter_check = False
                elif letters[number2] in numbers:
                    no_symbol = True
                    letter_check = False
                    print("\nNumbers Detected In 'Word':", word1)
            

                
            if no_symbol == False:     
                
                print(f"\nThere is an issue with the word:", word1)
                spelling += 1
                issues += 1
                


        else:
            number1 -= 1


    get_number = list1.split()

    number5 = len(get_number)

    word1 = list_of_words[0]
    letters = list(word1)  

    if letters[0] not in data.capital.capitals:
        print("\nCappital needed in word:", word1)
        capitals += 1
        
        issues += 1

    number5 -= 1

    if text == "hello how are you":
        text = "Hello, how are you?"
        print(f"\n\nThis would sound better:\n{text}")
    
    functions.suggestions.suggestions1()

    print(f"\ndone!\n\nThere are/is {issues} detected issue(s) in your sentance!\n\n")
    if issues > 0:
        print(f"These {issues} issues include:")
    if spelling > 0:
        print(f"- Spelling: {spelling}")
    if capitals > 0:
        print(f"- Capitals: {capitals}")


    print("\n\n")
