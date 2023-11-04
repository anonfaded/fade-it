#!/usr/bin/env python3

import re
# Author information
Tool = "Fade-It"
Author = "Faded"
Github = "https://github.com/anonfaded/fade-it"
Usage = "This tool prompts you to enter text or paragraphs and modifies the text to bypass censor filters on social media apps. :)"
Instructions = "To exit, simply press Enter without input."

# Logo and header
logo = """
        _____         _        ___ _   
       |  ___|_ _  __| | ___  |_ _| |_ 
       | |_ / _` |/ _` |/ _ \  | || __|
       |  _| (_| | (_| |  __/  | || |_ 
       |_|  \__,_|\__,_|\___| |___|\__|
           
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$ 
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P 
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$# 
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$* 
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R" 
        "*$bd$$$$      '*$$$$$$$$$$$o+#" 
             ''''          ''''''' 
"""
header = "============Censored Words Bypasser============"
h2 = "==============================================="



def change_text(input_text):
    # Replace full words first
    changed_text = input_text.replace('israel', '!sr@3l')
    changed_text = changed_text.replace('palestine', 'p@|-est!n3')
    changed_text = changed_text.replace('hamas', 'h@m-@s')
    changed_text = changed_text.replace('palestine', 'p@|-est!n3')
    changed_text = changed_text.replace('gaza', 'Ga-z@')
    changed_text = changed_text.replace('palestine', 'p@|-est!n3')
    changed_text = changed_text.replace('bomb', 'b0-mb')
    changed_text = changed_text.replace('genocide', 'g3n0$!d3')
    changed_text = changed_text.replace('falasteen', 'f@|ast!n3')
    changed_text = changed_text.replace('terrorist', 't3rr0-r!$t')
    changed_text = changed_text.replace('death', 'd3@-th')
    changed_text = changed_text.replace('gun', 'gu-n')
    changed_text = changed_text.replace('guns', 'gu-n$')
    changed_text = changed_text.replace('terror', 't3rr-04')
    changed_text = changed_text.replace('america', '@m3r!-c@')
    
       
    

    # Then, replace individual letters in a case-insensitive manner
    changed_text = re.sub(r'o', '0', changed_text, flags=re.IGNORECASE)
    changed_text = re.sub(r'i', '!', changed_text, flags=re.IGNORECASE)
    changed_text = re.sub(r'a', '@', changed_text, flags=re.IGNORECASE)
    changed_text = re.sub(r'e', '3', changed_text, flags=re.IGNORECASE)
    changed_text = re.sub(r'l', '|', changed_text, flags=re.IGNORECASE)
    changed_text = re.sub(r's', '$', changed_text, flags=re.IGNORECASE)

    return changed_text






if __name__ == "__main__":
    # Print header and logo
    print(logo)
    print(header)
    print(f"Tool: {Tool}\nAuthor: {Author}\nGitHub: {Github}\nUsage:\n{Usage}")
    print(h2)

 #   user_input = input("\n Enter text:\n\t")
 #   changed_result = change_text(user_input)
    
#    print("\n Bypassed text:\n\t", changed_result)
    while True:
        user_input = input("\n\n - Enter text (or press Enter to exit):\n >>>  ")
        
        if user_input == "":
            print("G00dby3!")
            break  # Exit the loop if the user presses Enter without input
        
        changed_result = change_text(user_input)
        print("\n - Bypassed text:\n >>> ", changed_result)