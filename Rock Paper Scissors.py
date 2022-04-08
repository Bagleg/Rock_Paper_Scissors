import random
import math

def game(win):
    cpu_pts = 0
    p1_pts = 0
    options = "rock", "paper", "scissors"
    cc = random.choice(options)
    while p1_pts < int(win) and cpu_pts < int(win):
        cc = random.choice(options)
        cp_choice = input("Will you throw rock, paper, or scissors? ")
        p_choice = cp_choice.lower()
        if p_choice == "rock" and cc == "paper" or p_choice == "paper" and cc == "scissors" or p_choice == "scissors" and cc == "rock":
            cpu_pts += 1
            p1_lose(p1_pts, cpu_pts, cc, win)
        elif p_choice == "rock" and cc == "rock" or p_choice == "paper" and cc == "paper" or p_choice == "scissors" and cc == "scissors":
            draw(cc)
        elif p_choice == "rock" and cc == "scissors" or p_choice == "paper" and cc == "rock" or p_choice == "scissors" and cc == "paper":
            p1_pts += 1
            p1_win(p1_pts, cpu_pts, cc, win)
        else:
            print("Invalid input. Please choose rock, paper, or scissors.")

def win_condition(p1_pts, cpu_pts, win):
    if cpu_pts >= win:
        print("Game over, CPU wins!")
    elif p1_pts >= win:
        print("Congratulations, you win!")

def p1_win(p1_pts, cpu_pts, cc, win):
    print("Your opponent chose " + cc)
    print("You win!")
    print("The score is: " + str(p1_pts) + "   " + str(cpu_pts))
    if p1_pts >= win:
        win_condition(p1_pts, cpu_pts, win)

def p1_lose(p1_pts, cpu_pts, cc, win):
    print("Your opponent chose " + cc)
    print("You lose!")
    print("The score is: " + str(p1_pts) + "   " + str(cpu_pts))
    if cpu_pts >= win:
        win_condition(p1_pts, cpu_pts, win)

def draw(cc):
    print("Your opponent chose " + cc)
    print("It's a draw!")

def main():
    rounds = input("How many rounds would you like to play? ")
    r = rounds.isdigit()
    if r == False:
        print("Please input a number")
    else:
        if int(rounds) % 2 == 1:
            win = math.ceil(int(rounds)/2)
            game(win)
        else:
            win = (int(rounds)/2) + 1
            game(win)

main()