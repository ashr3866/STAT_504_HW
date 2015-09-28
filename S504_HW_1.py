# -*- coding: utf-8 -*-

"""
Python Code corresponding to Homework #1 in STAT504 Analytics
Mohammad Ashrafuzzaman

"""

import string
import random
import os.path
import os
import glob
import re
from collections import Counter

def Check_For_Words(title, listfilename):
    global checklist
    global words
    
    # Sanitize wordlist to check against
    if os.path.isfile(listfilename): 
        print 'filename = ' + listfilename + ' is valid\n'
    else:
        print 'filename = ' + listfilename + ' is not valid\n'
        return
    chFile = open(listfilename)
    checklist = chFile.readlines()
    length = len(checklist)
    chars_removing = re.compile(r'([^A-Za-z \'])')
    for i in range(0, length):
        checklist[i] = checklist[i].strip()
        checklist[i] = " ".join(checklist[i].split())
        checklist[i] = chars_removing.sub("", checklist[i])
        checklist[i] = checklist[i].lower()   
    
    checklist = filter(None, checklist)
    checklist = " ".join(checklist)
    checklist = " ".join(checklist.split())
    checklist = re.split(" ", checklist)
    
    length = len(checklist)
    for i in range(0, length):
        words[:] = (value for value in words if value != checklist[i])
    
    k = input("Enter value of k :  ")   
    k = k-1
    
    print 'Total number of words in the ' + title + ' is = ' + str(len(words))    
    count = Counter(words)
    clen = len(words)
    print 'Total number of unique words in the ' + title + ' is = ' + str(clen)

    frequent_words = dict((keynum, value) for keynum, value in count.items() if value > k)
    sorted_freq_words = sorted(frequent_words.items(), key = lambda(key, value): value, reverse = True)
    print sorted_freq_words

    chFile.close()

    # -------- End of Check_For_Words()


def Count_Word_Frequency(title):
    global words
    global lines
    
    k = input("Enter value of k :  ")   
    k = k-1
    print 'Total number of words in the ' + title + ' is = ' + str(len(words))    
    count = Counter(words)
    print 'Total number of unique words in the ' + title + ' is = ' + str(len(count))
    
    frequent_words = dict((keynum, value) for keynum, value in count.items() if value > k)
    sorted_freq_words = sorted(frequent_words.items(), key = lambda(key, value): value, reverse = True)
    print sorted_freq_words
    # ------- End Count_Word_Frequency()
    
def Remove_WS_Puncs():
    global words
    global lines
    
    length = len(lines)
    chars_removing = re.compile(r'([^A-Za-z \'])')
    
    for i in range(0, length):
        lines[i] = lines[i].strip()
        lines[i] = " ".join(lines[i].split())
        lines[i] = chars_removing.sub("", lines[i])
        lines[i] = lines[i].lower()   
    
    lines = filter(None, lines)
    lines = " ".join(lines)
    lines = " ".join(lines.split())
    words = re.split(" ", lines)
    # --------- -End of Remove_WS_Puncs():
    
def Stat504_HW1_Ex_1_1():
    """
    Exercise 1
    Write a program that reads a file, breaks each line into words, 
    strips whitespace and punctuation from the words, 
    and converts them to lowercase. 
    """
    global lines
    global words
    filename = 'ReliabilityIssuesinWAVE.txt'
    if os.path.isfile(filename): 
        print 'filename = ' + filename + ' is valid\n'
    else:
        print 'filename = ' + filename + ' is not valid\n'
        return
    inFile = open(filename)
    lines = inFile.readlines()
    Remove_WS_Puncs()
    print words
    inFile.close()

    


def Stat504_HW1_Ex_2(testament): 
    """
    Exercise 2
    This function reads The King James Bible from Gutenberg Project, 
    skips over the header information at the beginning of the file, 
    and process the rest of the words as in Exercise 1.
    It does it for both Old Testamment and New Testament books.
    """

    global lines   
    filename = 'gutenberg_cache_epub_10_pg10.txt'
    if os.path.isfile(filename): 
        print 'filename = ' + filename + ' is valid\n'
    else:
        print 'filename = ' + filename + ' is not valid\n'

    inFile = open(filename)
    lines = inFile.readlines()

    if (testament == 'Old'):
        # Remove Header information for Old Testament
        i = 0
        while not lines[i].startswith('The Old Testament of the'):
            del lines[i]
        del lines[i]

        # Remove New Testament portion from the file
        i = len(lines)-1
        while not lines[i].startswith('The New Testament of the'):
            del lines[i]
            i = i -1
        del lines[i]
        title = 'Old Testament'
        Remove_WS_Puncs()
        Count_Word_Frequency(title)
    elif (testament == 'New'):
        # Remove Header information and the Old Testament part leaving the New Testament part
        i = 0
        while not lines[i].startswith('The New Testament of the'):
            del lines[i]
        del lines[i]
        title = 'New Testament'
        Remove_WS_Puncs()
        Count_Word_Frequency(title)
    else:
        print 'Error: Invalid argument.'
        inFile.close()
        return
            
    inFile.close()
    # ------------------------- End of Stat504_HW1_Ex_2

    
def Stat504_HW1_Ex_3(testament, wordsfile): 
    """
    Exercise 3
    This function reads The King James Bible from Gutenberg Project, 
    Then in addition to the tasks in Exercise 2, it reads a word list given in a file
    and then prints all the words in the Old Testament that are not in the word list, 
    where this word list is user-input.
    
    It does the same for both Old Testamment and New Testament books.
    """

    global lines
    
    filename = 'gutenberg_cache_epub_10_pg10.txt'
    if os.path.isfile(filename): 
        print 'filename = ' + filename + ' is valid\n'
    else:
        print 'filename = ' + filename + ' is not valid\n'

    inFile = open(filename)
    lines = inFile.readlines()

    if (testament == 'Old'):
        # Remove Header information for Old Testament
        i = 0
        while not lines[i].startswith('The Old Testament of the'):
            del lines[i]
        del lines[i]

        # Remove New Testament portion from the file
        i = len(lines)-1
        while not lines[i].startswith('The New Testament of the'):
            del lines[i]
            i = i -1
        del lines[i]
        title = 'Old Testament'
        Remove_WS_Puncs()
        Check_For_Words(title, wordsfile)
    elif (testament == 'New'):
        # Remove Header information and the Old Testament part leaving the New Testament part
        i = 0
        while not lines[i].startswith('The New Testament of the'):
            del lines[i]
        del lines[i]
        title = 'New Testament'
        Remove_WS_Puncs()
        Check_For_Words(title, wordsfile)
    else:
        print 'Error: Invalid argument.'
        inFile.close()
        return
            
    inFile.close()
    # ------------------------- End of Stat504_HW1_Ex_3

    


   

if __name__ == '__main__':
    """
    This is the main() routine that calls functions for performing the different
    Exercises in the Homework.
    """
    global words
    global lines
    global checklist
    words = []
    lines = []
    checklist = []
    
    # DO IT -- This value needs to be changed accordingly
    workingdir = '/Users/dukeashrafuzzaman/Dropbox/MeAndMe/IP_Notebooks/STAT504_HW_1'
    os.chdir(workingdir)
    print 'Current Working Directory = ' + os.getcwd() + '\n'

    Stat504_HW1_Ex_1_1()
    Stat504_HW1_Ex_2('Old')
    Stat504_HW1_Ex_2('New')
    Stat504_HW1_Ex_3('Old', 'wordlist.txt')
    Stat504_HW1_Ex_3('New', 'wordlist.txt')
# End of the program
    
    