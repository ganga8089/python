'''
name:ganga
date:17-12-2024
version1.1
'''
def stick_game():
    player1=input("Enter name of first player:")
    player2=input("Enter name of second player:")
    no_sticks=16
    while True:
        choice1=int(input(f"{player1} Pick 1 or 2 or 3"))
        if choice1>3 or choice1>no_sticks:
            print(f"{player1} You break rules")
            continue
        no_sticks=no_sticks-choice1
        print("Remaining sticks are:",no_sticks)
        if no_sticks==0:
            print(f"{player1} You lose!")
        choice2=int(input(f"{player2} Pick 1 or 2 or 3"))
        if choice2>3 or choice2>no_sticks:
            print(f"{player2} You break rules")
            continue
        no_sticks=no_sticks-choice2
        print("Remaining sticks are:",no_sticks)
        if no_sticks==0:
            print(f"{player2} You lose!")
            break
stick_game()