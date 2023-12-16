import random
list=["apple","banana","potato"]
lives=6
choose=random.choice(list)
print(choose)
display=[]
for i in range(len(choose)):#0 1 2 3 4 5 #apple
    display+='_'
print(display)
game_over=False
while not game_over:
    guessed=input("guess a letter:").lower()#p_p p _ _
    for position in range(len(choose)):#0 1 2 3 4
        letter=choose[position]
        if letter==guessed:#p==x
            display[position]=guessed
    print(display)
    
    if guessed not in choose:
        lives -=1
        if lives==0:
            game_over=True
            print("you lose!")
    if '_' not in display:
        game_over=True
        print("you win")
