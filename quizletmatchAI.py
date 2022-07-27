import time
start=time.time()
import pyautogui, sys
import mouse
import random
# import random
# import pyperclip
# import codecs
# import os
# import shutil
import PIL
# import keyboard
# import threading
# import logging
# from win32gui import GetWindowText, GetForegroundWindow
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


###clickscreen for 175% zoom
a=1200, 700
b=1200, 900
c=1200, 1200
d=1200, 1450
e=1650, 700
f=1650, 900
g=1650, 1200
h=1650, 1450
i=2100, 700
j=2100, 900
k=2100, 1200
l=2100, 1450

a1=695, 471, 1328, 752
b1=695, 773, 1328, 1052
c1=695, 1080, 1328, 1357
d1=695, 1381, 1328, 1650
e1=1352, 471, 1980, 752
f1=1352, 773, 1980, 1052
g1=1352, 1080, 1980, 1357
h1=1352, 1381, 1980, 1650
i1=2007, 471, 2640, 752
j1=2007, 773, 2640, 1052
k1=2007, 1080, 2640, 1357
l1=2007, 1381, 2640, 1650


pyautogui.hotkey('alt','tab')

global alllist, savedlist, originlist, screenshotlist  

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
        filepath='debugpic'+str(random.randint(0,1299202))+'.png'
        lol.save(filepath, 'PNG')
    else:
        lol=PIL.ImageGrab.grab()
        filepath='debugpic'+str(random.randint(13000000,129920200))+'.png'
        lol.save(filepath, 'PNG')
        oldmain()
        
        #postclick(badlist)
    end=time.time()
    print('done')
    print(start-end)

    #positions=textparser(wordlist, unusual, imagetext)

def getimageinfo(sslist):
    sstextlist=[]
    for xyxy in sslist:
        lol=PIL.ImageGrab.grab(bbox=(xyxy[0],xyxy[1],xyxy[2],xyxy[3]))
        #img = cv2.imread(lol)
        
        text=pytesseract.image_to_string(lol)
        print(text)
        text=text.replace("\n", " ")
        text=text.strip()
        sstextlist.append(text)
    #print(text)
    return sstextlist

def matchlist():
    newlines=[]
    #unusual=[]
    matchsplitchar="!!!"
    with open('quizletmatchlist.txt') as file:
        lines = [line.rstrip() for line in file]
    #print(lines)

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


'''
def textparser(thelist, unusuals, textimage):
    #for word in unusuals:
     #   newlist=thelist.remove(word)
    #print(newlist)
    textimage=textimage.strip()
    textimage=textimage.replace('|', 'I')
    textimage=textimage.split("\n")
    textimage=[x for x in textimage if x]
    if len(textimage)>12:
        itUnusual=True
    else:
        itUnusual=False
    positions=[]
    weird=[]
    for term in textimage:
        thingfound=False
        for matches in thelist:
            if term in matches:
                matchindex, termindex=thelist.index(matches), matches.index(term)
                pairindex=(termindex+1)%2
                pairstring=thelist[matchindex][pairindex]
                if pairstring not in unusuals:
                    for i 
                    pair=textimage.index(pairstring)
                    positions.append(textimage.index(term), pair)
                thingfound=True
            else:
                weird.append(str(textimage.index(term))+'n')
                #thingfound=True
        if thingfound == False:
            weird.append(textimage.index(term))

    print(positions, weird)
    
    print(textimage)
    #[liney.rstrip() for liney in textimage]
    #print(textimage)
    #imagestuff=[line.rstrip() for line in textimage]
    #print(imagestuff)
'''
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
