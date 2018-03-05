# -*- coding: utf-8 -*-
"""
@author: Madison, Andrew
@title: Test Code
@date: 20170727
"""
#opens txt file
states=open("C:/testcode/states.txt", "r")
#takes first item of list out and separates it from the rest of the list
combo = []
head, *tail = states
#iterates through head of each list
for i in range(len(tail)):
    #iterates through all items in the tail
    for i in range(len(tail)):
        #adds each combination to 'combo' array
        add = head + tail[i]
        combo.append(add)
    #cycles through current tail to make all availble combinations of states with out duplicates
    head, *tail = tail
#begins same cycle of iteration to make comparison of all combinations of states within list
head, *tail = combo
match=[]
for i in range(len(tail)):
    for i in range(len(tail)):
        #takes combinations, converts to lower caps and arranges them in alphabetical order for easy comparison
        h = ''.join(sorted(head.lower())).strip()
        t = ''.join(sorted(tail[i].lower())).strip()
        #comparisons made here for matches
        if(h == t):
            #if match is made it is appended to new list
            match = []
            match.append(head)
            match.append(tail[i])
    head, *tail = tail
#formats match list for output
match = [i.replace('\n', ' ') for i in match]
print("Combo 1:", match[0])
print("Combo 2:", match[1])
print("Combo 1:", ''.join(sorted(match[0].lower())).strip())
print("Combo 2:", ''.join(sorted(match[1].lower())).strip())
