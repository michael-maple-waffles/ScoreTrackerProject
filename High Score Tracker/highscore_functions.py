#MW_CP2 High score tracker, High Scores using csv

import csv

def submittingScores(username, scores_csv):
    #try
    try:
        #with open scores_csv, mode = r as scores_by_username:
        with open(scores_csv, 'r') as scores_by_username:
            #reader = csv.reader(scores_by_username)
            reader = csv.reader(scores_by_username)
            user_scores = {}
            #for row in reader:
            next(reader)
            for i, row in enumerate(reader):
                print(f"Row # {i}, {row}")
                #scores = []
                scores = []
                #scores = row[1].split(',')
                current_item = ''
                for char in row[1]:
                    if char != '[' or ',' or ' ':
                        current_item = f'{current_item}{char}'
                    else:
                        if current_item == '':
                            pass
                        else:
                            scores.append(current_item)
                            current_item = ''

                print(scores)
                user_scores[row[0]] = scores

    except:
        print("file doesn't exist")
    else:
        return user_scores[username]
    
print(submittingScores("PersonOne", "/workspaces/ScoreTrackerProject/documents/scores.csv"))

