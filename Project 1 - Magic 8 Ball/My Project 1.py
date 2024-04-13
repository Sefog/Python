#import modules
import sys
import random
#variables
questions = True
responses = ["IT IS CERTAIN" , "YOU MAY RELY ON IT" , "AS I SEE IT, YES"
             "OUTLOOK LOOKS GOOD", "MOST LIKELY" , "IT IS DECIDELY SO" , "WITHOUT A DOUBT" , "YES, DEFINETLY"]
#loop
while questions:
    ques = input("Ask a Question, (Press ENTER to Quit)")
    magic_response = responses [random.randint(0,7)]
    if ques == "":
        sys.exit()
    else:
        print(magic_response)
                                
                    
