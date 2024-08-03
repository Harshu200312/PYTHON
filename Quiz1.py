def new_game():
    guesses=[]
    correct_guesses=0
    question_num=1

    for key in questions:
        print("----------------")
        print(key)
        for i in options[question_num-1]:
            print(i)

        guess=input("Enter (A B C Or D) : ")
        guess=guess.upper()
        guesses.append(guess)
        correct_guesses +=check_answer(questions.get(key),guess)
        question_num +=1
    display_score(correct_guesses,guesses)
# ---------------------------------------------
def check_answer(answer,guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("Wrong")
        return 0
# -----------------------------------------------
def display_score(correct_guesses,guesses):
    print("--------------------")
    print("RESULTS")
    print("--------------------")
    print("Answers: ",end=" ")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    print("Guesses :",end=" ")
    for i in guesses:
        print(i,end=" ")
    print()


    score=int(correct_guesses/len(questions)*100)
    print("your score is: "+str(score)+"%")
# --------------------------------

def play_again():

    response=input("Do you want to play again (yes or no):").upper()
    if response == "YES":
        return True
    else:
        return False

# -------------------------------------------------------

questions={
    "National animal of India ?":"B",
    "capital of India?":"A",
    "National flower of india ?":"A",
    "capital of Maharashtra?":"C"
}

options= [["A. Lion","B.Tiger","C.Elephant","D.Bear"],
          ["A.Delhi","B.Hariyana","C.panjab","D.Maharashtra"],
          ["A:Lotus","B.Rose","C.JAsmine","D.Marigold"],
          ["A.pune","B.Nagpur","C.Mumbai","D.Beed"]]

new_game()
while play_again():
    new_game()


print("bye !!!!")