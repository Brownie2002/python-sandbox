#!env python
# encoding: utf-8
'''
Analyse -- shortdesc

Analyse is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2016 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import argparse
import codecs
import datetime
import itertools
import logging
import os
import pickle
import random
import re
import time

def factorielle(n):
    return n * factorielle(n - 1) if n > 1 else 1

def main():
    nbCases = 6
    sommeCible = 37
    solution = []
    allSolutions = []

    # Solution initiale
    for n in range(9,9-nbCases,-1):
        solution.append(n)

    # Find all the solutions by modifying the last element.
    index = 5

    for value in range(solution[index], 1, -1):
        solution[index] = value
        print "??????> Solution testée !"
        printSolution(solution)
        if sum(solution) == sommeCible:
            allSolutions.append(solution)
            print "|_____> Solution validée à ", sum(solution)
        
    # Initialise the solution for the next index
    index = index - 1
    solution[index] = solution[index] - 1 
    for case in range(index + 1, len(solution)):
        solution[case] = solution[case - 1] - 1
    
    print "La prochaine iteration d'index sera :"
    printSolution(solution)

    print "fini"

def printSolution(solution):
    print "[",
    for i in solution:
        print i,
    print "] vaut ", sum(solution)

if __name__ == '__main__':
    main()
