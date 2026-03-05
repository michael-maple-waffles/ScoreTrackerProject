from rps import gam
from highscore_functions import submittingScores
from helpers.seth_code import login
from helpers.seth_code import logout
from helpers.seth_code import register

username=''

def menu():
    while True:
        if username:
            inp=input("What would you like to do\n(1) Play Rock Paper Scissors\n(2) View score board\n(3) Logout")
            match inp:
                case '1':
                    gam()
                    break
                case '2':
                    
                    break
                case '3':
                    username=logout(username)
                    break
                case _:
                    continue
        else: 
            inp=input("What would you like to do\n(1) Login\n(2) Register")
            match inp:
                case '1':
                    username=login()
                    break
                case '2':
                    username=register()
                    break
                case _:
                    continue



