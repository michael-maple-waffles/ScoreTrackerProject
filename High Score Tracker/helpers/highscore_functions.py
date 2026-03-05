#MW_CP2 High score tracker, High Scores using csv

import csv

def gettingScores(username = '', scores_csv = '/workspaces/ScoreTrackerProject/documents/scores.csv', mode = 'all'):
    #try
    def reading():
        try:
            #with open scores_csv, mode = r as scores_by_username:
            with open(scores_csv, 'r') as scores_by_username:
                #reader = csv.reader(scores_by_username)
                reader = csv.reader(scores_by_username)
                user_scores = {}
                #for row in reader:
                next(reader)
                for i, row in enumerate(reader):
                    #scores = []
                    scores = []
                    #scores = row[1].split(',')
                    current_item = ''
                    workable_row = row[1].replace('[', '').replace(']','')
                    for char in workable_row:
                        if char != '[' and char!= '.' and char!= ' ':
                            current_item = f'{current_item}{char}'
                        else:
                            if current_item == '':
                                pass
                            else:
                                
                                scores.append(current_item)
                                current_item = ''
                        
                    scores.append(current_item)
                    user_scores[row[0]] = scores

        except:
            print("file doesn't exist")
        else:
            return user_scores
    
    if mode == 'spec':
        return reading()[username]
    elif mode == 'all':
        return reading()
    
def submittingScores(username, new_scores):
    read_info = gettingScores('NULL', '/workspaces/ScoreTrackerProject/documents/scores.csv', 'all')



    if username in read_info.keys():
        for item in new_scores:
            read_info[username].append(str(item))
        read_info[username] = list(set(read_info[username]))
        print(read_info[username])
    else:
        read_info[username] = list(set(new_scores))
        print(read_info[username])
    writeable_info = []
    for item in read_info:
        print(item)
        set_to_send = ''
        for score in read_info[item]:
            if set_to_send != '':
                set_to_send = f'{set_to_send}.{str(score)}'
            else:
                set_to_send = f"{set_to_send}{str(score)}"
        set_to_send = f"[{set_to_send}]"
        piece = {'Username' : item, 'Scores' : set_to_send}
        print(piece)
        writeable_info.append(piece)


    try:
        with open('/workspaces/ScoreTrackerProject/documents/scores.csv', 'w') as csv_file:
            fieldnames = ['Username', 'Scores']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(writeable_info)
    except:
        print("this file doesn't exist")
    else:
        print("scores have been updated.")

