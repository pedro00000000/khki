import math
import os
import random
import re
import sys






def transformSentence(sentence):
    import string
    def listalphabet():
        return list(string.ascii_lowercase)
    
    for x in sentence:
     result = sentence.index(x)
     print(result)           






if __name__ == '__main__':
    

    sentence = input()

    result = transformSentence(sentence)

    

   