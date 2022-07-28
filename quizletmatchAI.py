#!/usr/bin/env python3


import time
start=time.time()
import pyautogui, sys
import mouse
import random
import PIL
import cv2
import pytesseract
from pynput.mouse import Listener

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pyautogui.hotkey('alt','tab')

global alllist, savedlist, originlist, screenshotlist  

with open('coordfile.txt') as file:
    lines = [line.rstrip() for line in file]




#listfinished=False
originlist=[a, b, c, d, e, f, g, h, i, j, k, l]
alllist=[a, b, c, d, e, f, g, h, i, j, k, l]
savedlist=[a, b, c, d, e, f, g, h, i, j, k, l]
screenshotlist=[a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1]

def main():
    imagetext=getimageinfo(screenshotlist)
    print(imagetext)
    wordlist=matchlist()
    print(wordlist)
    positions, badlist=textparse(wordlist, imagetext)
    speedclick(positions)
    time.sleep(0.1)

    if len(badlist) <3 and len(badlist) > 1:
        oldmain()
    if len(badlist)>6:
        lol=PIL.ImageGrab.grab()
        #filepath='debugpic'+str(random.randint(1000,1999))+'.png'
        lol.save(filepath, 'PNG')
    else:
        lol=PIL.ImageGrab.grab()
        #filepath='debugpic'+str(random.randint(5000,5999))+'.png'
        lol.save(filepath, 'PNG')
        oldmain()

    
    postclick(badlist)
    end=time.time()
    print('done')
    print(start-end)

    #positions=textparser(wordlist, unusual, imagetext)


    
def getimageinfo(sslist):
    sstextlist=[]
    for xyxy in sslist:
        matchImage=PIL.ImageGrab.grab(bbox=(xyxy[0],xyxy[1],xyxy[2],xyxy[3]))
        #img = cv2.imread(matchImage)
        text=pytesseract.image_to_string(matchImage)
        print(text)
        text=text.replace("\n", " ")
        text=text.strip()
        sstextlist.append(text)
        #print(text)
    return sstextlist

def matchlist():
    newlines=[]
    matchsplitchar="!!!!!"
    with open('quizletmatchlist.txt') as file:
        lines = [line.rstrip() for line in file]

    for stuff in lines:
        things=stuff.split(matchsplitchar)
        newlines.append(things)
        '''
    for things in newlines:
        for thing in things:
            if len(thing)>27:
                unusual.append(thing)
    '''
    return newlines #, unusual

def speedclick(indecies):
    for indice in indecies:
        coordinates=originlist[indice]
        mouseclick(coordinates[0], coordinates[1])
        mouse.click()

def textparse(thelist, imagestuff):
    pairlist=[]
    badlist=[]
    for word in imagestuff:
        wordfound = False
        for match in thelist:
            if word in match:
                wordfound=True
                wordval=imagestuff.index(word)
                matchindex, listindex=match.index(word), thelist.index(match)
                pairindex=(matchindex+1)%2
                if match[pairindex] in imagestuff:
                    pairval=imagestuff.index(match[pairindex])
                    
                    if pairval not in pairlist and wordval not in pairlist:
                        pairlist.append(wordval)
                        pairlist.append(pairval)
                else:
                    badlist.append(match[pairindex]+"p"+str(wordval))
        if wordfound==False:
            badlist.append(wordfound)

    print(pairlist, badlist)
    return pairlist, badlist


def jaccard_similarity(x,y):
    """ returns the jaccard similarity between two lists """
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)

def solveandcheck():
    global alllist, savedlist, originlist  
    originlist=[a, b, c, d, e, f, g, h, i, j, k, l]
    savedlist=originlist
    troll=False
    pops=[]
    lol=PIL.ImageGrab.grab()
    #filepath='debugpic'+str(random.randint(0,1299202))+'.png'
    #lol.save(filepath, 'PNG')
    for x in range(len(originlist)):
        coordinate=originlist[x]
        print(lol.getpixel(coordinate))
        #green=223,242,235
        #finished=245, 247, 251
        #red=255,220,214
        #yellow=255, 243, 200
        
        ca, cb, cc=lol.getpixel(coordinate)
        if ca < 250:
            if cb < 254:
                if cc < 254:
                    pops.append(x)
                               

    for index in sorted(pops, reverse=True):
        del savedlist[index]
    if len(savedlist)<len(alllist):
        troll=True 
    alllist=savedlist
    print(originlist, savedlist, alllist)
    return troll
    
def mouseclick(asdf, asdf2):
    sdf=mouse.get_position()
    abc=asdf-sdf[0], asdf2-sdf[1]
    mouse.move(abc[0], abc[1], absolute=False, duration=0)

def oldmain():
    m=0
    n=0
    listfinished=False
    while listfinished==False:
        troll=solveandcheck()
        if troll==True:
            m=0
            n=0
            o=len(alllist)
        o=len(alllist)
        if len(alllist)<2:
            listfinished=True
            break
        if n>len(alllist):
            m+=1
            n=0
        if m> len(alllist):
            break
        if m==n:
            n+=1
        p=(o-n)%o
        if p==m:
            p+=1
        print(alllist[m], alllist[p])
        mouseclick(alllist[m][0], alllist[m][1])
        # time.sleep(0.1)
        mouse.click()
        mouseclick(alllist[p][0], alllist[p][1])
        # time.sleep(0.1)
        mouse.click()
        n+=1
main()
