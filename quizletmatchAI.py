#!/usr/bin/env python3


import time
start=time.time()
import sys, pyautogui

#import mouse
import random
from PIL import ImageGrab
#import pyscreenshot as ImageGrab

#import gtk.gdk

#import cv2
import pytesseract
from pynput.mouse import Button, Controller
mouse = Controller()

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def main():
    #time.sleep(0.1)
    pyautogui.hotkey('alt','tab')
    setup()
    imagetext=getimageinfo(screenshotlist)

    wordlist=matchlist()
    print(wordlist)
    positions, badlist=textparse(wordlist, imagetext)
    speedclick(positions)
    time.sleep(0.1)
    
    if len(badlist) <3 and len(badlist) > 1:
        oldmain()
    else:
        newlist=similaritytest(wordlist, badlist)
        positions, badlist=textparse(wordlist, imagetext)
        speedclick(positions)
        oldmain()
#        if len(badlist)>6:
#            lol=ImageGrab.grab()
            #filepath='debugpic'+str(random.randint(1000,1999))+'.png'
            #lol.save(filepath, 'PNG')
#    else:
#        lol=ImageGrab.grab()
        #filepath='debugpic'+str(random.randint(5000,5999))+'.png'
        #lol.save(filepath, 'PNG')
        #oldmain()

    print(badlist)
    #postclick(badlist)
    end=time.time()
    print('done')
    print(start-end)

   #positions=textparser(wordlist, unusual, imagetext)

def jaccard_similarity(x,y):
    """ returns the jaccard similarity between two lists """
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)

def similaritytest(pairl, wordl):
    score=0
    final="hello"
    finallist=[]
    for asdf in pairl:
        for asdf2 in wordl:
            score2=jaccard_similarity(asdf, asdf2)
            if score2>score:
                score=score2
                final=asdf
        finallist.append(final)
    return finallist
        
    
   
def setup():
    global alllist, savedlist, originlist, screenshotlist  
    with open('coordfile.txt') as file:
        lines = [line.rstrip() for line in file]
    coords=[]
    for i in lines:
        nn1, nn2=i.split(",")
        coords.append(nn1)
        coords.append(nn2)
    ab=coords[0], coords[1]
    bb=coords[0], coords[3]
    cb=coords[0], coords[5]
    db=coords[0], coords[7]
    eb=coords[8], coords[1]
    fb=coords[8], coords[3]
    gb=coords[8], coords[5]
    hb=coords[8], coords[7]
    ib=coords[10], coords[1]
    jb=coords[10], coords[3]
    kb=coords[10], coords[5]
    lb=coords[10], coords[7]
    a1=coords[12], coords[13], coords[14], coords[15]
    b1=coords[12], coords[17], coords[14], coords[19]
    c1=coords[12], coords[21], coords[14], coords[23]
    d1=coords[12], coords[25], coords[14], coords[27]
    e1=coords[28], coords[13], coords[30], coords[15]
    f1=coords[28], coords[17], coords[30], coords[19] 
    g1=coords[28], coords[21], coords[30], coords[23]
    h1=coords[28], coords[25], coords[30], coords[27]
    i1=coords[32], coords[13], coords[34], coords[15]
    j1=coords[32], coords[17], coords[34], coords[19]
    k1=coords[32], coords[21], coords[34], coords[23]
    l1=coords[32], coords[25], coords[34], coords[27]
    #listfinished=False
    alllist=[]
    screenshotlist=[]
    originlist=[ab, bb, cb, db, eb, fb, gb, hb, ib, jb, kb, lb]
    sslist=[a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1]
    for ll in originlist:
        x=int(ll[0]), int(ll[1])
        alllist.append(x)
    for jj in sslist:
        x=int(jj[0]), int(jj[1]), int(jj[2]), int(jj[3])
        screenshotlist.append(x)
    originlist=alllist
    savedlist=alllist
    print(alllist)
    print(screenshotlist)
    
    
def getimageinfo(sslist):
    sstextlist=[]
    for xyxy in sslist:
        #print(xyxy)
        matchImage=ImageGrab.grab(bbox=(xyxy[0],xyxy[1],xyxy[2],xyxy[3]))
        #matchImage.save(f"tmp{xyxy}.png") ###for debugging
        #img = cv2.imread("tmp.png")
        #time.sleep(10)
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
        print(coordinates)
        posx=int(coordinates[0])
        posy=int(coordinates[1])
        print(posx, posy)
        #mouseclick(posx, posy)
        #mouse.click()
        #pyautogui.click(x=posx, y=posy)
        mouse.position=(posx, posy)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.1)
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
                    badlist.append(match[pairindex]+str(wordval))
        if wordfound==False:
            badlist.append(wordfound)

    print(pairlist, badlist)
    return pairlist, badlist


def solveandcheck():
    global alllist, savedlist, originlist  
    originlist=[a, b, c, d, e, f, g, h, i, j, k, l]
    savedlist=originlist
    troll=False
    pops=[]
    lol=ImageGrab.grab()
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
if __name__ == "__main__":
    main()


