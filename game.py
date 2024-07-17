import random

word_dict = {
    
    1: "rock",
    2: "scissors",
    3: "paper"

}

number_dict = {
    
    "rock": 1,
    "scissors": 2,
    "paper": 3
}

while True:
    X = input(" rock, paper, scissors!: ")

    if X.lower()== 'stop' or X.lower()== 'quit':
        print("Game Over")
        break
    X = number_dict.get(X.lower())
    Y = random.randint(1, 3)
    Opp = word_dict.get(Y)
       
    if X == None:

        print("Inavlid input! Please choose between rock, paper, scissors")
        continue

    else:
        print("Your opponent chose", Opp) 
        
        if X==1 and Y==2 or X==2 and Y==3 or X==3 and Y==1 :

            print("You Win!")    

        if Y==1 and X==2 or Y==2 and X==3 or Y==3 and X==1 :

            print("You Lose!")

        if X==Y:

            print("Tie Game")

       


