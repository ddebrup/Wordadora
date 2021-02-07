import json
from tkinter import *
def read():
    global wordle
    if 'wordle' not in globals():
        wordle = {}  
    with open("./../wordlist.txt") as words:
        wordle = json.load(words)
#clustering
from typing import Tuple, Iterable, Sequence, List, Dict, DefaultDict
from random import sample
from math import fsum, sqrt
from collections import defaultdict
from functools import partial

Point = Tuple[int, ...]
Centroid = Point

def mean(data: Iterable[float]) -> float:
    'Accurate arithmetic mean'
    data = list(data)
    return fsum(data) / len(data)

def dist(p: Point, q: Point, sqrt=sqrt, fsum=fsum, zip=zip) -> float:
    'Euclidean distance'
    return sqrt(fsum((x - y) ** 2.0 for x, y in zip(p, q)))

def assign_data(centroids: Sequence[Centroid], data: Iterable[Point]) -> Dict[Centroid, Sequence[Point]]:
    'Assign data the closest centroid'
    d = defaultdict(list)             # type: DefaultDict[Point, List[Point]]
    for p in data:
        centroid = min(centroids, key=partial(dist, p))  # type: Point
        d[centroid].append(p)
    return dict(d)

def compute_centroids(groups: Iterable[Sequence[Point]]) -> List[Centroid]:
    'Compute the centroid of each group'
    return [tuple(map(mean, zip(*pts))) for pts in groups]

def k_means(data: Iterable[Point], k:int=2, iterations:int=10) -> List[Point]:
    'Return k-centroids for the data'
    data = list(data)
    centroids = sample(data, k)
    for i in range(iterations):
        labeled = assign_data(centroids, data)
        centroids = compute_centroids(labeled.values())
    return centroids
#clustering controller
def clus():
    score = list(wordle.values())
    points = [(x,) for x in score]
    centroids = k_means(points, k=3, iterations=100)
    clusters = assign_data(centroids, points).values()
    group_val=[]
    for cluster in clusters: 
        stretch = []
        stretch.append(min(cluster)[0])
        stretch.append(max(cluster)[0])
        group_val.append(stretch)
        #print(f'{min(cluster)[0]} to {max(cluster)[0]}')
    return group_val
        
# Sort the tuples using second element of sublist Function 

def Sort(sub_li): 

    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of 
    return(sorted(sub_li, key = lambda x: x[1]))	 

# Grouping controller
def select(group_val):
    #group_val=Sort(group_val) 
    global sc
    if 'sc' not in globals():
        sc = {}  
    for i in range(len(group_val)):
        sc[i+1]=group_val[i]
    

# Difficulty Selecter module 1

def sel():
    #selection = "Value = " + str(var.get())
    global label
    selection = "Value = " + str(sc[var.get()])
    label.config(text = selection)
    
def callback():
    global x
    selection = var.get()
    x=selection

# Difficulty Selecter module 1 GUI
def diff():
    group_val = clus()
    select(group_val)
    global var, label
    root = Tk()
    var = DoubleVar()
    scale = Scale( root, variable = var, from_=1, to=len(sc))
    scale.pack(anchor=CENTER)

    button = Button(root, text="Get Range", command=sel)
    button.pack(anchor=CENTER)

    button1 = Button(root, text="Select", command=callback)
    button1.pack()

    #button2=Button(root, text="ghost", command=foo)
    # Button for closing 
    exit_button = Button(root, text="Exit", command=root.destroy) 
    exit_button.pack(pady=20) 

    label = Label(root)
    label.pack()
    
    root.mainloop()
    #print(x)

# Select Difficulty module 2 using PySimpleGui
def diffi():
    import PySimpleGUI as sg

    event, values = sg.Window('Choose difficulty', [[sg.Text('Select one->'), sg.Listbox(list(sc.keys()), size=(40, 10), key='LB')],
        [sg.Button('Ok'), sg.Button('Cancel')]]).read(close=True)

    if event == 'Ok':
        sg.popup(f'You chose {values["LB"][0]}')
        return values["LB"][0]
    else:
        select1()

# Final word stack controller
def words(group):
    from nltk.corpus import wordnet 
    global word
    if 'word' not in globals():
        word = {}  
    for words in wordle.keys():
        if sc[group][0] <= wordle[words] <= sc[group][1]:
            syns = wordnet.synsets(words.lower())
            if not syns:
                continue
            else:
                li = []
                li.append(syns[0].definition())
                li.append(syns[0].examples())
                word[words] = li

# Learn module

import random
from plyer.utils import platform
from plyer import notification

def learn():
    global word_displayed
    if 'word_displayed' not in globals():
        word_displayed = {}  
    word_ask={}
    words=random.choice(list(word.keys()))
    if words not in word_displayed.keys():
        word_displayed[words]=1
    else:
        word_displayed[words]+=1
    try:
        notification.notify(
            title=words,
            message='Meaning:'+str(word[words][0])+'\nUsage:'+str(word[words][1][0]),
            app_name='Wordadora',
            app_icon='path/to/the/icon.' + ('ico' if platform == 'win' else 'png')
        )
    except:
        notification.notify(
            title=words,
            message='Meaning:'+str(word[words][0]),
            app_name='Wordadora',
            app_icon='path/to/the/icon.' + ('ico' if platform == 'win' else 'png')
        )
    if word_displayed[words]==5:
        #word_ask[word]=wordle[word][0]
        word.pop(words, None)

# Main Select Control GUI

def select1():
    import PySimpleGUI as sg

    event, values = sg.Window('Choose an option', [[sg.Text('Select one->'), sg.Listbox(['Learn', 'Practice', 'Auto'], size=(40, 10), key='LB')],
        [sg.Button('Ok'), sg.Button('Cancel')]]).read(close=True)

    if event == 'Ok':
        sg.popup(f'You chose {values["LB"][0]}')
        if values["LB"][0]=='Learn':
            Learn_Controller()
        if values["LB"][0]=='Practice':
            Prac_Controller()
    else:
        sg.popup_cancel('User aborted')

# FOR LEARN Module
from pynput.keyboard import Listener
import time

def on_press(key):  # The function that's called when a key is pressed
    global run
    #print("Key pressed: {0}".format(key))
    if 'char' in dir(key):     #check if char method exists,
        if key.char == 'q':
            #print("quit")
            run = False
def timer():
    global run, listener, Listener
    run = True
    listener = Listener(on_press=lambda event: on_press(event))
    listener.start()

    while run:
        learn()
        time.sleep(2)
    
    #stop the listener...
    listener.stop()
    select1()
    
    
def Learn_Controller():
    
    group_val = clus()
    select(group_val)
    grp = diffi()
    
    #grp = diff()
    #print(grp)
    words(grp)
    #print(word)
    timer()

# FOR PRACTICE Module
def quest():
    import PySimpleGUI as sg
    import random
    from random import shuffle
    from nltk.corpus import wordnet 
    x = random.choice(list(wordle.keys()))
    syns = wordnet.synsets(x.lower())
    ques = syns[0].definition()
    #print(ques)
    n = 4
    answ = random.sample(list(wordle.keys()), n)
    answ.append(x)
    shuffle(answ)

    event, values = sg.Window('Choose the right answer!', [[sg.Text(ques), sg.Listbox(answ, size=(40, 10), key='LB')],
        [sg.Button('Ok'), sg.Button('Cancel')]]).read(close=True)

    if event == 'Ok' and values["LB"][0] == x:
        sg.popup('Hurray! You are correct')
        
    elif event == 'Ok' and values["LB"][0] != x:
        s1 = "{{'word:' {0},'def:' {1}}}"
        sg.popup('Incorrect!\n',s1.format(x+'\n',ques))
    else:
        return
    
    return

def Prac_Controller():
    global run, listener, Listener
    run = True
    listener = Listener(on_press=lambda event: on_press(event))
    listener.start()

    while run:
        quest()
        
    
    #stop the listener...
    listener.stop()
    select1()

# Main method
def main():
    read()
    select1()
    
    
if __name__=="__main__": 
    main() 
