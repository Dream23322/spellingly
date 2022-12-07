

import time
import random
import data.words1
import data.sentance1
import data.capital
import data.config
failed = False
newText = str
def YesOrNo():
    if(data.config.giveSuggestions["askToChange"] == True):
        print(f"\n\nThis would sound better:\n{newText}\n")
        print("Would you like to change it to this? Y or N")
        changeSentance = input(">> ")
        if(changeSentance.lower() == "y") :
            text = newText
        elif(changeSentance.lower() == "n"):
            print("Your Text Has Not Been Changed")
        else:
            print("Invalid Response Received")
    else:
        text = newText
        print(f"Your text has been changed to {text} as it would sound better") 
    if(data.config.giveSuggestions["resetIssues"] == True):
        issues = 0
        capitals = 0
        spelling = 0
    else:
        print("It is useful to turn on resetIssues in data/config/giveSuggestions/resetIssues to be more accurate")
    

while True:
    spelling = 0
    capitals = 0
    slang = 0
    no_full_stop = 0
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
        if failed == True:
            break
        try:
            word = list_of_words[number1].split()
            part_of_data = len(word)
            word1 = word[0]

        
        except:
            print("------------------------------------\nAn Error has happened while trying to split the paragraph / words")
            failed = True
            break

        
        if number1 < 0:
            break
        if(data.config.spellCheck["enabled"] == True):
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
                    if(data.config.spellCheck["checkForSymbols"] == True):   
                        try:
                            if letters[number2] in symbols:
                                no_symbol = True
                                print("\nSymbol Detected In Word:", word1) 
                                letter_check = False
                            elif letters[number2] in numbers:
                                no_symbol = True
                                letter_check = False
                                print("\nNumbers Detected In 'Word':", word1)
                        except:
                            print("------------------------------------\nAn Error has happened while trying to check for symbols!")
                            break
                    
                if no_symbol == False:     
                    
                    print(f"\nThere is an issue with the word:", word1)
                    if(data.config.spellCheck["validIssue"] == True):
                        spelling += 1
                        issues += 1
                    


            else:
                number1 -= 1
        else:
            print("Spell Check is disabled in 'data/config.py' and is highly recommended to be on!")
            break

    get_number = list1.split()

    number5 = len(get_number)
    if(data.config.capitalCheck["enabled"] == True) :
        word1 = list_of_words[0]
        letters = list(word1)  

        if letters[0] not in data.capital.capitals:
            print("\nCappital needed in word:", word1)
            if(data.config.capitalCheck["validIssue"] == True):
                capitals += 1
                
                issues += 1
    else:
        print("Capital Check is disabled in data/config.py' and is highly recommended to be on!")
        break
    number5 -= 1
    #try:
    list_of_words = text
    list1 = list_of_words
    list_of_words = list_of_words.split() 
    number1 = len(list_of_words)
    number3 = len(list_of_words)
    number1 -= 1
    word = list_of_words[number1]
    last_letter_1 = list(word)
    
    last_letter_2 = len(last_letter_1)
    last_letter_2 -= 1
    
    
    last_letter_3 = last_letter_1
   
    if(last_letter_3[last_letter_2] not in data.sentance1.end_sentance) :
        print("End of sentance statement needed in word:", word)
    #except:
    #    print("-----------------------------------------------------------\nAn error has occoured while running this part of the script!\n-----------------------------------------------------------")
    if(data.config.giveSuggestions["enabled"] == True):
        #If you wish to add your own suggestions. Follow this simple thing
        #First do an if statement on what the original text would have been
        #then change the variable 'newText' to what it will change to
        #Then call the YesOrNo function
        #Then test it out!

        #It will look like:
        if text == "hello how are you":
            newText = "Hello, how are you?"
            YesOrNo()
        # Ta-Da
        elif text == "how are you":
            newText = "How are you?"
            YesOrNo()
        elif text == "are you ok":
            newText = "Are you OK?"
            YesOrNo()
        elif text == "what are you doing":
            newText = "What are you doing?"
            YesOrNo()
    else:
        print("Suggestions are disabled!")
    
    if failed == True:
        break
    print(f"\ndone!\n\nThere are/is {issues} detected issue(s) in your sentance!\n\n")
    if issues > 0:
        print(f"These {issues} issues include:")
    if spelling > 0:
        print(f"- Spelling: {spelling}")
    if capitals > 0:
        print(f"- Capitals: {capitals}")


    print("\n\n")
