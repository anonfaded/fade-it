#!/usr/bin/env python3

import re


# Author information
Tool = "Fade-It"
Author = "Faded"
Github = "https://github.com/anonfaded/fade-it"
Usage = "Beat social media filters.\n  Enter text, we'll handle the rest. 🪄📝🔓🌟"
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
header_text = "Censored Words Bypasser"
header_text = "Censored Words Bypasser"
divider_length = 48  # Total length of the line

# Calculate the number of equal signs needed on each side
equals_count = (divider_length - len(header_text)) // 2

# Construct the header text with green color
header = f"\033[32m{header_text}\033[0m"

# Construct the left and right sides of the divider with red equal signs
left_divider = "\033[31m" + "=" * equals_count + "\033[0m"
right_divider = "\033[31m" + "=" * equals_count + "\033[0m"

# Construct the full divider line
divider = left_divider + header + right_divider

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
    print("\033[31m" + logo + "\033[0m")
    print(divider)
    print(f"\033[31m Tool:\033[0m {Tool}\n\033[31m Author:\033[0m {Author}\n\033[31m GitHub:\033[0m {Github}\n\033[31m Usage:\033[0m\n \033[33m {Usage}\033[0m ")
    
# Test ANSI escape codes, we use these ansi character escapes to change the color:
# Change the color of the text to red
# print("\033[31mThis is red text\033[0m")    

# Change the color of the text to green
# print("\033[32mThis is green text\033[0m")

    print("\033[31m" + h2 + "\033[0m")

 #   user_input = input("\n Enter text:\n\t")
 #   changed_result = change_text(user_input)
    
#    print("\n Bypassed text:\n\t", changed_result)
    while True:
        user_input = input("\033[32m\n - Enter text: \033[31m(or press Enter to exit)\033[32m\n >>>\033[0m  ")

        
        if user_input == "":
            print("\033[31m\n\t<<< \033[0m \033[32mGoodbye!😢 \033[0m \033[31m>>>\n\n \033[0m")


            break  # Exit the loop if the user presses Enter without input
        
        changed_result = change_text(user_input)
        print("\033[32m\n - Bypassed text:\n >>> \033[0m", changed_result)
        print("\n\t \033[33m ^^^Copy the modified text above^^^\033[0m")