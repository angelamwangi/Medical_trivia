Correct_answer1="C"
scores=0
def display_score(current_score):
    print(f"Total: {current_score}")
Num1=(input("Which of the following is not a component of the cardiovascular system? "
            "A=Heart\n"
            "B=Blood vessels\n"
            "C=Lungs\n"
            "D=Blood\n"))
if Num1==Correct_answer1:
    print("Correct!")
    scores+=1
else:
    print("Wrong! the answer is C")
display_score(scores)

Correct_answer2="C"
Num2=(input("Which part of the human body heals the fastest? " 
            "A=Bone\n"
            "B=Skin\n"
            "C=Tongue\n"
            "D=Hair\n"))
if Num2==Correct_answer2:
    print("Correct!")
    scores+=1
else:
    print("Wrong! The answer is C")
display_score(scores)

Correct_answer3="B"
Num3=(input("What is the primary site of nutrient absorption in the digestive system?"
            "A=Stomach\n"
            "B=Small intestine\n"
            "C=Large intestine\n"
            "D=Esophagus\n"))
if Num3==Correct_answer3:
    print("Correct!")
    scores+=1
else:
    print("Wrong! the answer is C")
display_score(scores)

Correct_answer4="B"
Num4=(input("Which part of the brain controls balance and coordination?"
            "A=Cerebrum\n"
            "B=Cerebellum\n"
            "C=Brainstem\n"
            "D=Hypothalamus\n"
            ))
if Num4==Correct_answer4:
    print("Correct!")
    scores+=1
else:
    print("Wrong! The answer is B")
display_score(scores)

Correct_answer5="D"
Num5=(input("Which blood type is considered the universal donor?"
            "A=A\n"
            "B=B\n"
            "C=AB\n"
            "D=O\n"))
if Num5==Correct_answer5:
    print("Correct!")
    scores+=1
else:
    print("Wrong! The answer is D")
display_score(scores)
print(f"You have scores {scores} out of 5 questions! ")

