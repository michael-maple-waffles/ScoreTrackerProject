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
    #if it does ask if they would like to login instead of to choose a different username
    #create dictionary with username set to their chosen username
    #ask user for password
    #import my previous password strength checker
    #check password strength and ask if they want to confirm the password 

    #user encrypt function to encript their password 
    #save encypted password into the dictionary under password

    #update csv file with writer writing the dictionary
    #set username variable as their chosen username
    #return username variable

#user login password
    #open user_info csv file in r mode
    #create reader
    #ask user for desired username
    #read to check if any other user names match 
    #if they dont tell user the dont and loop

    #if they do save the index of the username
    #sak user for password
    #use encypt to encrypt their password 
    #check 