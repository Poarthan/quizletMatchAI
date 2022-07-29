#!/usr/bin/env python3


import time
start=time.time()
import sys, pyautogui

#import mouse
import random
from PIL import ImageGrab
#import pyscreenshot as ImageGrab
from math import sqrt, pow, exp

#import cv2
import pytesseract
from pynput.mouse import Button, Controller
mouse = Controller()

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#def main():
#    cd=time.time()
#    setup()
#    oldmain()
#    cdd=time.time()
#    print(cdd-cd)

def main():
    #time.sleep(0.1)
    pyautogui.hotkey('alt','tab')
    
    #waitstart()
    #startstart=time.time()
    #print("start", startstart)
    setup()
    imagetext=getimageinfo(screenshotlist)
    check=time.time()
    #print(imagetext)
    print("ss check:", check-start)
    
    wordlist=matchlist()
    #print(wordlist)
    
    positions, badlist=textparse(wordlist, imagetext)
    check2=time.time()

    print("calc check2", check2-check)
    speedclick(positions)
    time.sleep(0.1)
    c4=time.time()
    print("click check", c4-check2)
    if len(badlist) <3:
        oldmain()
    if len(badlist )>2:
        print("__test__")
        newpos=similaritytest(wordlist, badlist)
        check3=time.time()
        print("calc check3", check3-c4)
        speedclick(newpos)
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
    #postclick(badlist)
    end=time.time()
    print('done')
    print(end-start)

   #positions=textparser(wordlist, unusual, imagetext)

#def waitstart():
#    test=1953,752
#    lol=ImageGrab.grab()
#    ca, cb, cc=lol.getpixel(coordinate)
#        if ca < 150:
#            if cb < 150:
#                if cc < 150:
#                    pops.append(x)
#    print("wait")
   
def jaccard_similarity(x,y):
    """ returns the jaccard similarity between two lists """
    #print(x,y)
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)

def similaritytest(wordl, pairl):
    pairlist=[]
    finallist=[]
    poplist=[]
    badlist=[]
    cleared=False
    global pops
    while cleared == False:
        pops=0
        for pops in range(len(pairl)):
            #print(pairl[pops][0])
            if pairl[pops][0] == '':
                pairl.pop(pops)
                break
        if pops+1 == len(pairl):
            cleared = True
    #print("\n\n WHAT IN TARNATION \n\n\n", pairl)
    for asdf in pairl:
        score=0
        final="hello"
        #print(len(wordl))
        for asdf2 in wordl:
            test1=str(asdf[0])
            test1=test1.split(" ")
            #print("\n\n\n\n", asdf2, "--------------------------------------------------------------")
            test2=str(asdf2[0])
            test2=test2.split(" ")
            score2=jaccard_similarity(test1, test2)
            #print("\n", str(score2)+"%", asdf2[0],"\n", asdf[0], "_____________________________\n\n")
            if score2>score:
                #print(str(score*100)+"%", asdf2[0], "_____________________________")
                score=score2
                final=asdf2[0]
            test1=str(asdf[0])
            test1=test1.split(" ")
            #print("\n\n\n\n", asdf2, "--------------------------------------------------------------")
            try:
                test2=str(asdf2[1])
            except:
                #print(asdf2, "__________________________________________________________________________")
                test2=str(asdf2[0])
            test2=test2.split(" ")
            score2=jaccard_similarity(test1, test2)
            #print("\n", str(score2)+"%", asdf2[1],"\n", asdf[0], "_____________________________\n\n")
            if score2>score:
                #print(str(score*100)+"%", asdf2[1], "_____________________________")
                score=score2
                final=asdf2[1]
        #print(asdf, str(score)+"%", final, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        asdfasdf=final, asdf[1]
        finallist.append(asdfasdf)
    for word in finallist:
        wordval=word[1]
        word=word[0]
        wordfound = False
        for match in wordl:
            if word in match:
                wordfound=True
                
                matchindex, listindex=match.index(word), wordl.index(match)
                pairindex=(matchindex+1)%2
                matched=False
                for matchpos in pairl:
                    if match[pairindex]==matchpos[0]:
                        pairval=matchpos[1]
                        if pairval not in pairlist and wordval not in pairlist:
                            pairlist.append(wordval)
                            pairlist.append(pairval)
                else:
                    tmpbad=[word[0], wordval]
                    badlist.append(tmpbad)
        if wordfound==False:
            tmpbad=[word[0], word[1]]
            badlist.append(tmpbad)
    return pairlist
        
    
   
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
    #print(alllist)
    #print(screenshotlist)
    
    
def getimageinfo(sslist):
    sstextlist=[]
    txt=""
    while txt == "":
        xyxy=sslist[0]
        matchImage=ImageGrab.grab(bbox=(xyxy[0],xyxy[1],xyxy[2],xyxy[3]))
        #matchImage.save(f"tmp{xyxy}.png") ###for debugging
        #img = cv2.imread("tmp.png")
        #time.sleep(10)
        txt=pytesseract.image_to_string(matchImage)
        print(txt)
        txt=txt.replace("\n", " ")
        txt=txt.strip()
    xstart=time.time()
    print(xstart-start)
    sstextlist.append(txt)
        #print(text)
    for numi in range(len(sslist)-1):
        #print(xyxy)
        xyxy=sslist[numi+1]
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
    #print(indecies)
    for indice in indecies:
        coordinates=originlist[indice]
        #print(coordinates)
        posx=int(coordinates[0])
        posy=int(coordinates[1])
        #print(posx, posy)
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
                    tmpbad=[word, wordval]
                    badlist.append(tmpbad)
        if wordfound==False:
            tmpbad=[word, imagestuff.index(word)]
            badlist.append(tmpbad)

    #print(pairlist, "\n\n------------------------------------------------------------------------\n", badlist)
    return pairlist, badlist


def solveandcheck():
    global alllist, savedlist, originlist  
    originlist=savedlist
    savedlist=originlist
    troll=False
    pops=[]
    lol=ImageGrab.grab()
    #filepath='debugpic'+str(random.randint(0,1299202))+'.png'
    #lol.save(filepath, 'PNG')
    for x in range(len(originlist)):
        coordinate=originlist[x]
        #print(lol.getpixel(coordinate))
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
    #print(originlist, savedlist, alllist)
    return troll
    
def mouseclick(asdf, asdf2):
    sdf=mouse.get_position()
    abc=asdf-sdf[0], asdf2-sdf[1]
    mouse.move(abc[0], abc[1], absolute=False, duration=0)
    
def oldmain():
    m=0
    n=0
    listfinished=False
#    print(len(savedlist))
    while listfinished==False:
        troll=solveandcheck()
        if troll==True:
            m=0
            n=0
            o=len(alllist)
        o=len(alllist)
#        print(o, alllist)
        if len(alllist)<1:
#            print("??????????????????????????????????////")
            troll=solveandcheck()
            #print(len(alllist))
            if troll==True:
                m=0
                n=0
                o=len(alllist)
            if len(alllist) < 1:
                listfinished=True
                break
            else:
                pass
        if n>len(alllist)-1:
            m+=1
            n=0
        if m> len(alllist)-1:
            m=0
            #break
        if m==n:
            n+=1
        p=(o-n)%o
        if p > len(alllist)-1:
            p=0
        if p==m and p+1 < len(alllist)-1:
            p+=1
            # print(alllist[m], alllist[p])
        #print(m)
        posx=alllist[m][0]
        posy=alllist[m][1]
        mouse.position=(posx, posy)
        mouse.press(Button.left)
        mouse.release(Button.left)
        #mouseclick(alllist[m][0], alllist[m][1])
        # time.sleep(0.1)

        posx=alllist[p][0]
        posy=alllist[p][1]
        mouse.position=(posx, posy)
        mouse.press(Button.left)
        mouse.release(Button.left)
        
        #mouse.click()
        #mouseclick(alllist[p][0], alllist[p][1])
        # time.sleep(0.1)
        #mouse.click()
        n+=1
if __name__ == "__main__":
    main()


