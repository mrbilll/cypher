#!/usr/bin/env python

""" line input for cypher01 """

import cypher01
# import string
import random


# *****************************************************************************    
saying = list()

saying.append("California, here I come")
saying.append("The quick brown fox jumped over the lazy dog")
saying.append("Twinkle Twinkle little star, how I wonder what you are")
saying.append("The golden rule: The one with the most GOLD... rules")
saying.append("Political correctness is tyranny with manners")
saying.append("There are no facts, only interpretations")
saying.append("Women might be able to fake orgasms. But men can fake a whole relationship")
saying.append("God is a comedian playing to an audience too afraid to laugh")
saying.append("I've had a wonderful time, but this wasn't it")
saying.append("Life is pleasant. Death is peaceful. It's the transition that's troublesome")

sayingRandom=random.shuffle(saying)
myC = cypher01.Cypher1(saying[0])
myC.scramble()
                       
endit = False
while endit == False:
    print myC.getCypher()
    myInp = raw_input('enter two(2) swap values or "quit" if done\n')
    myInpL = myInp.lower()
    if myInpL == 'quit':
        endit = True
        continue
    if len(myInpL) <> 2:
        print 'Invalid - use 2 characters'
        continue
    myC.swap(myInpL[0], myInpL[1])
    theAnswer = myC.getCypher()
    if theAnswer == saying[0]:
        print
        print theAnswer
        print
        print 'SOLVED --- Well Done!'
        endit = True
        continue