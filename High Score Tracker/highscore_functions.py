#MW_CP2 High score tracker, High Scores using csv

import csv

def gettingScores(username, scores_csv, mode):
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
    read_info[username].append(new_scores)
    writeable_info = []
    for item in read_info:
        #print(item)
        #piece = {'Username' : item}
        pass


    """try:
        with open('/workspaces/ScoreTrackerProject/documents/scores.csv', 'w'):
            feildnames = ['Username', 'Scores']
            writer = csv.DictWriterwriter()"""
    


submittingScores('PersonOne', [12,17])
            

            
        
    
print(gettingScores("PersonOne", "/workspaces/ScoreTrackerProject/documents/scores.csv", 'spec'))



