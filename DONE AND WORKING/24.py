#define a function make_3sg_form() which given a verb in infinitive form returns its third person singular form.
#Test your function with words like try, brush, run and fix.
#Note however that the rules must be regarded as heuristic,
#in the sense that you must not expect them to work for all cases.
#Tip: Check out the string method endswith().

inp = raw_input("please enter a verb: ")
"""Import regular experssions libary"""
import re
"""define function"""
def sg_form(verb):
    es = ('o', 'ch', 's', 'sh', 'x', 'z',) #DEFINES OTHER VERB CASES 
    if verb.endswith('y'):
        return verb.replace('y' , 'ies') #USE BUILT IN REPLACE FUNCTION NOT RE.SUB 
    elif verb == "quiz":
        return "quizzes" #BECAUSE ENGLISH KINDA SUCKS
    elif verb.endswith(es):
        return verb + 'es' #VERBS WITH ENDS IN VARIABLE DEFINED CAN BE ENDED IN 'ES'
    else:
        return verb + 's' #ALL OTHER VERB CASES COVERD BY SUFFIX OF S

sg_form(inp)

print ("Your verb in third person singular form is:")
print (sg_form(inp.lower())#Deals with capitalization in user input

