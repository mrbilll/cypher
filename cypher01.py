#!/usr/bin/env python

""" help decode byte swap cypher """
import string
import random

# constants/variables for this module
cypherAlphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')


class Cypher1:
    

    def __init__(self, initstring = 'There was no input... Solve This!'):
        self.curVer     = list()        # current version of the cypher
        self.oldVer     = list()        # previous version of the cypher
        self.origVer    = list()        # original version of the cypher
        self.history    = list()        # history of valid cypher input
        self.case       = list()        # case of each element in origVer
                                        # values: u=upper l=lower   n=neither
        self.newValue(initstring)
        
    def __del__(self):
        pass
    
    def newValue(self, initstring):
        """ evaluate & save new cypher """
        self.origVer = list(initstring)
        self.oldVer  = list(initstring.upper())
        self.curVer  = self.oldVer[:]
        self.history = list()
        self.case    = list()
          
        for curletter in self.origVer:
            if curletter.islower():
                self.case.append('l')
            elif curletter.isupper():
                self.case.append('u')
            else:
                self.case.append('n')
            
        return 0
        
    def scramble(self):
        cypherScrambleAlphabet = cypherAlphabet[:]
        random.shuffle(cypherScrambleAlphabet)
        for i in range(9):
            for j in range(len(cypherAlphabet)):
                self.swap(cypherAlphabet[j], cypherScrambleAlphabet[j])
                self.history.pop()
    
    def swap(self, swapFrom, swapTo):
        """ swap all occurences of swapFrom <--> swapTo """
        uFrom = swapFrom.upper()
        uTo = swapTo.upper()
        if (uFrom not in cypherAlphabet) or (uTo not in cypherAlphabet):
            return 1                        # invalid argument
        
        self.oldVer = self.curVer[:]        # save before updating        
        for i in range(len(self.curVer)):
            if self.oldVer[i] == uFrom:
                self.curVer[i] = uTo
            if self.oldVer[i] == uTo:
                self.curVer[i] = uFrom
                
        self.history.append([uFrom, uTo])
                
        return 0
     
   
    def undo(self):
        """ undo last swap
            note: re-do the last swap is same as undo
            can't just use oldVer - can undo only once
        """
        if len(self.history) == 0:
            return 1
        
        uPop = self.history.pop()
        uFrom = uPop[0]
        uTo   = uPop[1]
        self.oldVer = self.curVer[:]        # save before updating        
        for i in range(len(self.curVer)):
            if self.oldVer[i] == uFrom:
                self.curVer[i] = uTo
            if self.oldVer[i] == uTo:
                self.curVer[i] = uFrom
                
        return 0       

    def getCypher(self):
        """ return the current value of the cypher in a string"""
        outstr = ''
        if len(self.curVer) == 0:
            return outstr
        
        for i in range(len(self.curVer)):
            if self.case[i] == 'u':
                outstr += self.curVer[i].upper()
            elif self.case[i] == 'l':
                outstr += self.curVer[i].lower()
            else:
                outstr += self.curVer[i]
                
        return outstr
"""
# *****************************************************************************    
# test no init + new
myC = Cypher1()
myC.newValue('The quick brown fox jumped over the Lazy dog')
# myC.newValue('Tbr gjzck aflwn eld ujmprx lvrf tbr Ohiy xlq')
print 'Original-->', myC.getCypher()
myC.scramble()
print 'Revised--->' , myC.getCypher()

#test swap
myC.swap('l','3')                       
print 'l3<-->     ',myC.getCypher()
myC.swap('c','d')
print 'cd<-->     ',myC.getCypher()
myC.swap('2','k')
print '2k<-->     ',myC.getCypher()

# test swap-undo
myC.swap('c','x')
myC.undo()
print 'cx-undo<-->',myC.getCypher()

print 'Final-->   ', myC.getCypher()


#test no init
myD = Cypher1()
print 'Original-->', myD.getCypher()
myD.scramble()
print 'Revised--->' , myD.getCypher()

#test swap
myD.swap('l','3')                       
print 'l3<-->     ',myD.getCypher()

"""

