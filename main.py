from random import random

numquestion=int(input("How many question do you want? "))
#ask the user what the lowest number is
low=1
#ask the user what the highest number is
high=10
#ask them which operation they want: 1 -add, 2 - subtract, 3 - multipy, 4 - divide

#loop:
for question in range(1,numquestion+1):
    print(f"Question  {question}:")
# - pick two random numbers, ask the user question
    num1 = random.randint(low,high)
    num2 = random.randint(low,high)
    num1 = num1*num2
    ans =num1//num2

    print(f"{num1} / {num2} = ?")
    userAns = int(input())
    if userAns == ans :
        print("Yup")
    else :
        print("Nope",ans)
