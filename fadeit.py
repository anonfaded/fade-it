#!/usr/bin/env python3

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
    changed_text = input_text.replace('o', '0').replace('i', '!').replace('israel', '!sr@3l')
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
        user_input = input("\n\n Enter text (or press Enter to exit):\n   ")
        
        if user_input == "":
            print("Goodbye!")
            break  # Exit the loop if the user presses Enter without input
        
        changed_result = change_text(user_input)
        print("\n Bypassed text:\n  ", changed_result)