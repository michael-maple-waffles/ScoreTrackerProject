#import hashlib


#initialize fieldnames list [username,password]
#initialize username variable as an empty string

#encrypt function
    #create sha256 to encrypt passwords

    #username variable initialize
    #sha256 updates password string to encrypt the information
    #return sha256.hexdigest password

#user registration function
    #open user_info csv file in r+ mode
    #create reader
    #create writer
    #ask user for desired username
    #read to check if any other user names match 
    #if it does 
        #ask if they would like to login instead of to choose a different username
    #create dictionary with username set to their chosen username
    #ask user for password
    #import my previous password strength checker
    #check password strength and ask if they want to confirm the password 

    #user encrypt function to encrypt their password 
    #save encrypted password into the dictionary under password

    #update csv file with writer writing the dictionary
    #set username variable as their chosen username
    #return username variable

#user login password
    #open user_info csv file in r mode
    #create reader
    #username loop
        #ask user for desired username
        #read to check if any other user names match 
        #if they dont 
            #tell user they dont and loop

        #if they do 
            #save the index of the username
    #ask user for password
    #use encrypt to encrypt their password 
    #check inputted password against password associated with the inputted username
    #if it matches 
        #set inputted username to username variable
    #else 
        #tell the user the password didn't match and ask if they would like to continue trying to login
    #if they keep trying to log in 
        #restart loop 
    #else 
        #leave function

#user log out 
    #ask user if they are sure they want to log out
    #if yes
        #set username to an empty string
    #else
        #leave function