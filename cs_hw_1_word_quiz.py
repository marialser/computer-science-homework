import random 
words = {"apple": "Apfel", 
         "house": "Haus",
         "dog": "Hund",
         "cat": "Katze",
         "tree": "Baum",
         "car": "Auto",
        "phone": "Handy"}

def german_to_english(score):
    word = random.choice(list(words.keys()))
    answer = input("Translate " + words[word] + " into English: ")
    return check_answer(answer, word, score)

def english_to_german(score):
    word = random.choice(list(words.keys()))
    answer = input("Translate " + word + " into German:")
    return check_answer (answer, words[word], score)

def check_answer(answer, correct_answer, score):
    if answer.title().strip(" ") == correct_answer.title().strip(" "):
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")
        print(correct_answer)
    return score

def play_again():
    answer = input("Do you want to play again? (yes/no): ")

    if answer.lower().strip(" ") == "yes":
        return True
    else:
        return False


score = 0
print ("Welcome to a German-English Quiz!")
while True:
    language = input("If you want to translate a word from German into English - type 1, from English into German - type 2: ")

    if language == "1":
        score = german_to_english(score)

    elif language == "2":
        score = english_to_german(score)

    else:
        print("Invalid choice.")
        continue

    if play_again() == False:
        print("Thanks for playing!")
        print("Your score is ", score)
        break
