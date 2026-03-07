from helpers.rps import gam
from helpers.highscore_functions import gettingScores
from helpers.highscore_functions import submittingScores
from helpers.highscore_functions import scoreDisplay
from helpers.seth_code import login
from helpers.seth_code import logout
from helpers.seth_code import register



def menu():
    username=''
    while True:
        if username:
            while True:
                inp=input("What would you like to do\n(1) Play Rock Paper Scissors\n(2) View score board\n(3) view your scores\n(4) Logout")
                match inp:
                    case '1':
                        score=list(gam()) 
                        submittingScores(username,score)
                        break
                    case '2':
                        scoreDisplay(read_scores = gettingScores())
                        break
                    case '3':
                        scores = gettingScores(username,'documents/scores.csv','spec')
                        if scores == "this username does not have any scores yet.":
                            print(scores)
                        else:
                            print(f"Your scores are: {scores}")
                            try:
                                scoreDisplay(mode = 'spec', username=username, read_scores = gettingScores())
                            except:
                                pass
                        break
                    case '4':
                        username=logout(username)
                        break
                    case _:
                        continue
        else: 
            while True:
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

menu()



