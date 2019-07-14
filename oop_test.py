import random
from urlib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is_a %%%.", 
    "class %%%(object):\n\tdef __init___(self, ***)" :
        "class %%% has-a __init___ that takes self and *** params.", 
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class has-a function *** that takes self and @@@ params.", 
    "*** = %%%()":
        "Set *** to an instance of class %%%",
    "***.***(@@@)":
        "From  *** get the *** function, call it with params self, @@@.", 
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'"
}

# do the want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

    