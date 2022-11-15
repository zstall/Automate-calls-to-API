#!/usr/bin/python3
import re
import subprocess as sp

# Function that appends to the end of a file
def appendFile(file, txt):
    # This opens a file to be written to. The 'a' option is for append to the end of the file
    with open(file, 'a') as myfile:
        myfile.write(txt)

# Function that searches a file for a string that matches the txt variable
def searchFile(file, txt):
    with open(file, 'r') as file:
        # Function iterates through the file line by line, so the match must be for an entire line
        for line in file.readlines():
            # using re to search each line to match the string stored in txt. re.I is to ignore case
            if re.search(txt, line, re.I):
                # return true if we get a match
                return(True)
        # return false if the string is not in the file        
        return False



def main():
    # get where terminal shell value
    trm = sp.getoutput('echo $SHELL')
    # get home dir for user
    home = sp.getoutput('echo ~/')

    
    # Using terminal shell, set bash or zsh. For anything else ask the user
    if trm=='/bin/bash':
        file = home + '.bashrc'
    elif trm == '/bin/zsh':
        file = home + '.zshrc'
    else:
        # Ask user for file path to there alias rc file (defaults to mine :) )
        file = input("Enter the path to you bash/zsh file (ex /Users/zach.stall/.zshrc): ")
        if file == '':
            file="/Users/zach.stall/.zshrc"

    # This is an array of the aliases to be added. One for each dogq env us1, eu1, us3, and us5
    aliases = [
        "alias dogq-us1='ddtool clusters use centurion.us1.prod.dog && kbash -n datadog dogq'", 
        "alias dogq-eu1='ddtool clusters use spirou.eu1.prod.dog && kbash -n datadog dogq'",
        "alias dogq-us3='ddtool clusters use plain4.us3.prod.dog && kbash -n datadog dogq'",
        "alias dogq-us5='ddtool clusters use hypno.us5.prod.dog && kbash -n datadog dogq'"
        ]

    # Looping through the array, working on one alias at a time
    for a in aliases:
        # Search the rc file for the current alias. If the alias is found, the function returns True
        fnd = searchFile(file,a)
        # If the alias is NOT in the rc file, the function above returns False. 
        # So, if fnd is False, we want to add the alias to the rc file
        # That is why the not opperator is used, if fnd is false, then the alias is missing and we want to add it
        if not (fnd):
            print("Adding: " + a )
            # Add the alias to the file
            appendFile(file, a + "\n")
        else:
            print("Already exists: " + a)
    
    
    # Warning, for the aliases to load, you must restart your terminal session!
    reload="source " + file

    print("Aliases script has completed")
    print("Please quit and repoen terminal for aliases to load")

if __name__=="__main__":
    main()
