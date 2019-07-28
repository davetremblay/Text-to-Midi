#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:38:48 2018

You must provide a text file with the name "textinput.txt".
The text file should include only letters, without diacritics, and spaces.
No punctuation or line breaks should be included.

The program returns three .mid files, for melody, chord, and bass parts.

At the moment, the chord part is not working.

@author: DaveTremblay
"""

import midi
import os

letters = "eoviqcfajzphbysrkdtlxmngwu"

edop = {
        "e":48,
        "o":48,
        "v":49,
        "i":49,
        "q":50,
        "c":50,
        "f":51,
        "a":51,
        "j":52,
        "z":52,
        "p":53,
        "h":53,
        "b":53,
        "y":54,
        "s":54,
        "r":55,
        "k":55,
        "d":56,
        "t":56,
        "l":57,
        "x":57,
        "m":58,
        "n":58,
        "g":59,
        "w":59,
        "u":59
        }

edos = {
        "e":-442,
        "o":1448,
        "v":-757,
        "i":1133,
        "q":-1072,
        "c":818,
        "f":-1387,
        "a":503,
        "j":-1702,
        "z":188,
        "p":-2017,
        "h":-127,
        "b":1764,
        "y":-442,
        "s":1448,
        "r":-757,
        "k":1133,
        "d":-1072,
        "t":818,
        "l":-1387,
        "x":503,
        "m":-1702,
        "n":188,
        "g":-2017,
        "w":-127,
        "u":1764
        }

edoc = {
        "e":0,
        "o":1,
        "v":2,
        "i":3,
        "q":4,
        "c":5,
        "f":6,
        "a":7,
        "j":8,
        "z":9,
        "p":10,
        "h":11,
        "b":12,
        "y":0,
        "s":1,
        "r":2,
        "k":3,
        "d":4,
        "t":5,
        "l":6,
        "x":7,
        "m":8,
        "n":9,
        "g":10,
        "w":11,
        "u":12
        }
if not os.path.isfile("textinput.txt"):
    text = input("Enter text: ")
else:
    filename = "textinput.txt"

    f = open(filename, "r")

    text = f.read()

noreturn = text.replace("\n","").replace(": "," ").replace(":"," ")
clean_text = noreturn
for character in noreturn:
    if character.lower() not in letters and character != " ":
        clean_text = clean_text.replace(character,"")
words = clean_text.split(" ")
words = list(filter(lambda a: a != "", words))
print(words)

#pitch=midi.PitchWheelEvent(tick=0,pitch=edos["j"])
#tra.append(pitch)
#noteon=midi.NoteOnEvent(tick=0,velocity=70,pitch=midi.E_3)
#tra.append(noteon)
#noteoff = midi.NoteOffEvent(tick=110,pitch=midi.E_2)
#tra.append(noteoff)

#pattern = midi.read_midifile("Untitled.mid")
#print (pattern)

#melody
pat = midi.Pattern()
tra = midi.Track()
pat.append(tra)

pitch = midi.PitchWheelEvent(tick=0,channel=edoc["e"],pitch=edos["e"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["o"],pitch=edos["o"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["v"],pitch=edos["v"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["i"],pitch=edos["i"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["q"],pitch=edos["q"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["c"],pitch=edos["c"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["f"],pitch=edos["f"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["a"],pitch=edos["a"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["j"],pitch=edos["j"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["z"],pitch=edos["z"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["p"],pitch=edos["p"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["h"],pitch=edos["h"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["b"],pitch=edos["b"])
tra.append(pitch)

first = 1

for w in words:
    for l in w:
        l = l.lower()
        if l in letters and first == 1:
            noteon = midi.NoteOnEvent(tick=0,channel=edoc[l],velocity=70,pitch=edop[l]+12)
            tra.append(noteon)
        elif l in letters and first != 1:
            noteon = midi.NoteOnEvent(tick=1,channel=edoc[l],velocity=70,pitch=edop[l]+12)
            tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=109,channel=edoc[l],pitch=edop[l]+12)
        tra.append(noteoff)
        first += 1
        
noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
tra.append(noteon)
noteoff = midi.NoteOffEvent(tick=880,channel=16,velocity=1,pitch=0)
tra.append(noteoff)
          
trackend = midi.EndOfTrackEvent(tick=1)
tra.append(trackend)
midi.write_midifile("melody-edo.mid", pat)

#chord1
pat = midi.Pattern()
tra = midi.Track()
pat.append(tra)

let1 = "evqfjpyrdlmg"

pitch = midi.PitchWheelEvent(tick=0,channel=edoc["e"],pitch=edos["e"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["v"],pitch=edos["v"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["q"],pitch=edos["q"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["f"],pitch=edos["f"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["j"],pitch=edos["j"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["p"],pitch=edos["p"])
tra.append(pitch)

first = 1

for w in words:
    wordletters = []
    for l in w:
        l = l.lower()
        if l in letters:
            wordletters.append(l)
    chord = list(set(wordletters))

    firstchord = 1
    for l in chord:
        if l in let1 and first == 1:
            noteon = midi.NoteOnEvent(tick=0,channel=edoc[l],velocity=70,pitch=(edop[l]))
            tra.append(noteon)
            firstchord += 1
            first += 1
        elif l in let1 and first != 1:
            if firstchord == 1:
                noteon = midi.NoteOnEvent(tick=1,channel=edoc[l],velocity=70,pitch=(edop[l]))
                tra.append(noteon)
                firstchord += 1
                first += 1
            elif firstchord != 1:
                noteon = midi.NoteOnEvent(tick=0,channel=edoc[l],velocity=70,pitch=(edop[l]))
                tra.append(noteon)
                firstchord += 1
                first += 1
                
    firstchord = 1
    for l in chord:
        if l in let1 and firstchord == 1:
            noteoff = midi.NoteOffEvent(tick=((len(w)*110)-1),channel=edoc[l],pitch=(edop[l]))
            tra.append(noteoff)
            firstchord += 1
        elif l in let1 and firstchord != 1:
            noteoff = midi.NoteOffEvent(tick=0,channel=edoc[l],pitch=(edop[l]))
            tra.append(noteoff)
            firstchord += 1
    
    eq = 0
    for l in chord:
        if l in let1:
            eq+=1
    
    if eq == 0 and first == 1:
        noteon = midi.NoteOnEvent(tick=0,channel=16,velocity=1,pitch=0)
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=((len(w)*110)-1),channel=16,pitch=0)
        tra.append(noteoff)  
        first += 1        
    elif eq == 0 and first != 1:
        noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=((len(w)*110)-1),channel=16,pitch=0)
        tra.append(noteoff)
        first += 1        
        
noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
tra.append(noteon)
noteoff = midi.NoteOffEvent(tick=880,channel=16,velocity=1,pitch=0)
tra.append(noteoff)

trackend = midi.EndOfTrackEvent(tick=1)
tra.append(trackend)
midi.write_midifile("chord1-edo.mid", pat)

#chord2
pat = midi.Pattern()
tra = midi.Track()
pat.append(tra)

let2 = "oicazhsktxnw"

pitch = midi.PitchWheelEvent(tick=0,channel=edoc["o"],pitch=edos["o"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["i"],pitch=edos["i"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["c"],pitch=edos["c"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["a"],pitch=edos["a"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["z"],pitch=edos["z"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["h"],pitch=edos["h"])
tra.append(pitch)

first = 1

for w in words:
    wordletters = []
    for l in w:
        l = l.lower()
        if l in letters:
            wordletters.append(l)
    chord = list(set(wordletters))

    firstchord = 1
    for l in chord:
        if l in let2 and first == 1:
            noteon = midi.NoteOnEvent(tick=0,channel=edoc[l],velocity=70,pitch=(edop[l]))
            tra.append(noteon)
            firstchord += 1
            first += 1
        elif l in let2 and first != 1:
            if firstchord == 1:
                noteon = midi.NoteOnEvent(tick=1,channel=edoc[l],velocity=70,pitch=(edop[l]))
                tra.append(noteon)
                firstchord += 1
                first += 1
            elif firstchord != 1:
                noteon = midi.NoteOnEvent(tick=0,channel=edoc[l],velocity=70,pitch=(edop[l]))
                tra.append(noteon)
                firstchord += 1
                first += 1
                
    firstchord = 1
    for l in chord:
        if l in let2 and firstchord == 1:
            noteoff = midi.NoteOffEvent(tick=((len(w)*110)-1),channel=edoc[l],pitch=(edop[l]))
            tra.append(noteoff)
            firstchord += 1
        elif l in let2 and firstchord != 1:
            noteoff = midi.NoteOffEvent(tick=0,channel=edoc[l],pitch=(edop[l]))
            tra.append(noteoff)
            firstchord += 1
    
    eq = 0
    for l in chord:
        if l in let2:
            eq+=1
    
    if eq == 0 and first == 1:
        noteon = midi.NoteOnEvent(tick=0,channel=16,velocity=1,pitch=0)
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=((len(w)*110)-1),channel=16,pitch=0)
        tra.append(noteoff)  
        first += 1        
    elif eq == 0 and first != 1:
        noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=((len(w)*110)-1),channel=16,pitch=0)
        tra.append(noteoff)
        first += 1
        
noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
tra.append(noteon)
noteoff = midi.NoteOffEvent(tick=880,channel=16,velocity=1,pitch=0)
tra.append(noteoff)
        
trackend = midi.EndOfTrackEvent(tick=1)
tra.append(trackend)
midi.write_midifile("chord2-edo.mid", pat)

#chord3
pat = midi.Pattern()
tra = midi.Track()
pat.append(tra)

let3 = "bu"

pitch = midi.PitchWheelEvent(tick=0,channel=edoc["b"],pitch=edos["b"])
tra.append(pitch)

first = 1

for w in words:
    wordletters = []
    for l in w:
        l = l.lower()
        if l in letters:
            wordletters.append(l)
    chord = list(set(wordletters))

    firstchord = 1
    for l in chord:
        if l in let3 and first == 1:
            noteon = midi.NoteOnEvent(tick=0,channel=edoc[l],velocity=70,pitch=(edop[l]))
            tra.append(noteon)
            firstchord += 1
            first += 1
        elif l in let3 and first != 1:
            if firstchord == 1:
                noteon = midi.NoteOnEvent(tick=1,channel=edoc[l],velocity=70,pitch=(edop[l]))
                tra.append(noteon)
                firstchord += 1
                first += 1
            elif firstchord != 1:
                noteon = midi.NoteOnEvent(tick=0,channel=edoc[l],velocity=70,pitch=(edop[l]))
                tra.append(noteon)
                firstchord += 1
                first += 1
                
    firstchord = 1
    for l in chord:
        if l in let3 and firstchord == 1:
            noteoff = midi.NoteOffEvent(tick=((len(w)*110)-1),channel=edoc[l],pitch=(edop[l]))
            tra.append(noteoff)
            firstchord += 1
        elif l in let3 and firstchord != 1:
            noteoff = midi.NoteOffEvent(tick=0,channel=edoc[l],pitch=(edop[l]))
            tra.append(noteoff)
            firstchord += 1
    
    eq = 0
    for l in chord:
        if l in let3:
            eq+=1
    
    if eq == 0 and first == 1:
        noteon = midi.NoteOnEvent(tick=0,channel=16,velocity=1,pitch=0)
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=((len(w)*110)-1),channel=16,pitch=0)
        tra.append(noteoff)  
        first += 1        
    elif eq == 0 and first != 1:
        noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=((len(w)*110)-1),channel=16,pitch=0)
        tra.append(noteoff)
        first += 1
        
noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
tra.append(noteon)
noteoff = midi.NoteOffEvent(tick=880,channel=16,velocity=1,pitch=0)
tra.append(noteoff)        
        
trackend = midi.EndOfTrackEvent(tick=1)
tra.append(trackend)
midi.write_midifile("chord3-edo.mid", pat)

#bass
pat = midi.Pattern()
tra = midi.Track()
pat.append(tra)

pitch = midi.PitchWheelEvent(tick=0,channel=edoc["e"],pitch=edos["e"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["o"],pitch=edos["o"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["v"],pitch=edos["v"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["i"],pitch=edos["i"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["q"],pitch=edos["q"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["c"],pitch=edos["c"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["f"],pitch=edos["f"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["a"],pitch=edos["a"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["j"],pitch=edos["j"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["z"],pitch=edos["z"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["p"],pitch=edos["p"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["h"],pitch=edos["h"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["b"],pitch=edos["b"])
tra.append(pitch)

first = 1

for w in words:
    tickval = len(w)*110
    let = 1
    for l in w:
        l = l.lower()
        if l in letters and let == 1 and first == 1:
            noteon = midi.NoteOnEvent(tick=0,channel=edoc[l],velocity=70,pitch=(edop[l]-24))
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=(tickval-1),channel=edoc[l],pitch=(edop[l]-24))
            tra.append(noteoff)
        elif l in letters and let == 1 and first != 1:
            noteon = midi.NoteOnEvent(tick=1,channel=edoc[l],velocity=70,pitch=(edop[l]-24))
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=(tickval-1),channel=edoc[l],pitch=(edop[l]-24))
            tra.append(noteoff)
        let += 1
        first += 1
            
noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
tra.append(noteon)
noteoff = midi.NoteOffEvent(tick=880,channel=16,velocity=1,pitch=0)
tra.append(noteoff)

trackend = midi.EndOfTrackEvent(tick=1)
tra.append(trackend)
midi.write_midifile("bass-edo.mid", pat)

#26-JI
letters = "eoviqcfajzphbysrkdtlxmngwu"

##xenh
#edop = {
#        "e":48,
#        "o":48,
#        "v":49,
#        "i":49,
#        "q":50,
#        "c":50,
#        "f":51,
#        "a":51,
#        "j":52,
#        "z":52,
#        "p":53,
#        "h":53,
#        "b":53,
#        "y":54,
#        "s":54,
#        "r":55,
#        "k":55,
#        "d":56,
#        "t":56,
#        "l":57,
#        "x":57,
#        "m":58,
#        "n":58,
#        "g":58,
#        "w":59,
#        "u":59
#        }
#
#edos = {
#        "e":-442,
#        "o":1740,
#        "v":-1078,
#        "i":1632,
#        "q":-282,
#        "c":835,
#        "f":-1799,
#        "a":199,
#        "j":-1003,
#        "z":995,
#        "p":-1639,
#        "h":-522,
#        "b":1660,
#        "y":-1158,
#        "s":1552,
#        "r":-362,
#        "k":755,
#        "d":-1159,
#        "t":1218,
#        "l":-1083,
#        "x":915,
#        "m":-1719,
#        "n":279,
#        "g":1580,
#        "w":355,
#        "u":1472
#        }
#
#edoc = {
#        "e":0,
#        "o":0,
#        "v":1,
#        "i":1,
#        "q":2,
#        "c":2,
#        "f":3,
#        "a":3,
#        "j":4,
#        "z":4,
#        "p":5,
#        "h":5,
#        "b":5,
#        "y":6,
#        "s":6,
#        "r":7,
#        "k":7,
#        "d":8,
#        "t":8,
#        "l":9,
#        "x":9,
#        "m":10,
#        "n":10,
#        "g":10,
#        "w":11,
#        "u":11
#        }

#29
edop = {
        "e":48,
        "o":48,
        "v":49,
        "i":49,
        "q":50,
        "c":50,
        "f":51,
        "a":51,
        "j":52,
        "z":52,
        "p":53,
        "h":53,
        "b":53,
        "y":54,
        "s":54,
        "r":55,
        "k":55,
        "d":56,
        "t":56,
        "l":57,
        "x":57,
        "m":58,
        "n":58,
        "g":58,
        "w":59,
        "u":59
        }

edos = {
        "e":-442,
        "o":1962,
        "v":191,
        "i":529,
        "q":-891,
        "c":529,
        "f":-1450,
        "a":689,
        "j":-1493,
        "z":450,
        "p":-1332,
        "h":87,
        "b":1966,
        "y":-463,
        "s":1330,
        "r":-1182,
        "k":871,
        "d":-2054,
        "t":609,
        "l":-1573,
        "x":567,
        "m":-1379,
        "n":770,
        "g":2683,
        "w":-112,
        "u":1250
        }

edoc = {
        "e":0,
        "o":0,
        "v":1,
        "i":1,
        "q":2,
        "c":2,
        "f":3,
        "a":3,
        "j":4,
        "z":4,
        "p":5,
        "h":5,
        "b":5,
        "y":6,
        "s":6,
        "r":7,
        "k":7,
        "d":8,
        "t":8,
        "l":9,
        "x":9,
        "m":10,
        "n":10,
        "g":10,
        "w":11,
        "u":11
        }

noreturn = text.replace("\n","").replace(": "," ").replace(":"," ")
clean_text = noreturn
for character in noreturn:
    if character.lower() not in letters and character != " ":
        clean_text = clean_text.replace(character,"")
words = clean_text.split(" ")

#pitch=midi.PitchWheelEvent(tick=0,pitch=edos["j"])
#tra.append(pitch)
#noteon=midi.NoteOnEvent(tick=0,velocity=70,pitch=midi.E_3)
#tra.append(noteon)
#noteoff = midi.NoteOffEvent(tick=110,pitch=midi.E_2)
#tra.append(noteoff)

#pattern = midi.read_midifile("Untitled.mid")
#print (pattern)

#melody1
pat = midi.Pattern()
tra = midi.Track()
pat.append(tra)

letters = "eoviqcfajzphb"

pitch = midi.PitchWheelEvent(tick=0,channel=edoc["e"],pitch=edos["e"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["o"],pitch=edos["o"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["v"],pitch=edos["v"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["i"],pitch=edos["i"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["q"],pitch=edos["q"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["c"],pitch=edos["c"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["f"],pitch=edos["f"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["a"],pitch=edos["a"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["j"],pitch=edos["j"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["z"],pitch=edos["z"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["p"],pitch=edos["p"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["h"],pitch=edos["h"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["b"],pitch=edos["b"])
tra.append(pitch)

first = 1

for w in words:
    for l in w:
        l = l.lower()
        if l in letters and first == 1:
            noteon = midi.NoteOnEvent(tick=0,channel=edoc[l],velocity=70,pitch=edop[l]+12)
            tra.append(noteon)
        elif l in letters and first != 1:
            noteon = midi.NoteOnEvent(tick=1,channel=edoc[l],velocity=70,pitch=edop[l]+12)
            tra.append(noteon)
        elif l not in letters and first == 1:
            noteon = midi.NoteOnEvent(tick=0,channel=16,velocity=1,pitch=0)
            tra.append(noteon)
        elif l not in letters and first != 1:
            noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
            tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=109,channel=edoc[l],pitch=edop[l]+12)
        tra.append(noteoff)
        first += 1
        
noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
tra.append(noteon)
noteoff = midi.NoteOffEvent(tick=880,channel=16,velocity=1,pitch=0)
tra.append(noteoff)
          
trackend = midi.EndOfTrackEvent(tick=1)
tra.append(trackend)
midi.write_midifile("melody1-ji.mid", pat)

#melody2
pat = midi.Pattern()
tra = midi.Track()
pat.append(tra)

letters = "ysrkdtlxmngwu"

pitch = midi.PitchWheelEvent(tick=0,channel=edoc["y"],pitch=edos["y"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["s"],pitch=edos["s"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["r"],pitch=edos["r"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["k"],pitch=edos["k"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["d"],pitch=edos["d"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["t"],pitch=edos["t"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["l"],pitch=edos["l"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["x"],pitch=edos["x"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["m"],pitch=edos["m"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["n"],pitch=edos["n"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["g"],pitch=edos["g"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["w"],pitch=edos["w"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["u"],pitch=edos["u"])
tra.append(pitch)

first = 1

for w in words:
    for l in w:
        l = l.lower()
        if l in letters and first == 1:
            noteon = midi.NoteOnEvent(tick=0,channel=edoc[l],velocity=70,pitch=edop[l]+12)
            tra.append(noteon)
        elif l in letters and first != 1:
            noteon = midi.NoteOnEvent(tick=1,channel=edoc[l],velocity=70,pitch=edop[l]+12)
            tra.append(noteon)
        elif l not in letters and first == 1:
            noteon = midi.NoteOnEvent(tick=0,channel=16,velocity=1,pitch=0)
            tra.append(noteon)
        elif l not in letters and first != 1:
            noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
            tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=109,channel=edoc[l],pitch=edop[l]+12)
        tra.append(noteoff)
        first += 1
        
noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
tra.append(noteon)
noteoff = midi.NoteOffEvent(tick=880,channel=16,velocity=1,pitch=0)
tra.append(noteoff)
          
trackend = midi.EndOfTrackEvent(tick=1)
tra.append(trackend)
midi.write_midifile("melody2-ji.mid", pat)

#chord1
pat = midi.Pattern()
tra = midi.Track()
pat.append(tra)

let1 = "evqfjpyrdlmw"

pitch = midi.PitchWheelEvent(tick=0,channel=edoc["e"],pitch=edos["e"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["v"],pitch=edos["v"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["q"],pitch=edos["q"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["f"],pitch=edos["f"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["j"],pitch=edos["j"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["p"],pitch=edos["p"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["y"],pitch=edos["y"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["r"],pitch=edos["r"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["d"],pitch=edos["d"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["l"],pitch=edos["l"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["m"],pitch=edos["m"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["w"],pitch=edos["w"])
tra.append(pitch)

first = 1

for w in words:
    wordletters = []
    for l in w:
        l = l.lower()
        if l in letters:
            wordletters.append(l)
    chord = list(set(wordletters))

    firstchord = 1
    for l in chord:
        if l in let1 and first == 1:
            noteon = midi.NoteOnEvent(tick=0,channel=edoc[l],velocity=70,pitch=(edop[l]))
            tra.append(noteon)
            firstchord += 1
            first += 1
        elif l in let1 and first != 1:
            if firstchord == 1:
                noteon = midi.NoteOnEvent(tick=1,channel=edoc[l],velocity=70,pitch=(edop[l]))
                tra.append(noteon)
                firstchord += 1
                first += 1
            elif firstchord != 1:
                noteon = midi.NoteOnEvent(tick=0,channel=edoc[l],velocity=70,pitch=(edop[l]))
                tra.append(noteon)
                firstchord += 1
                first += 1
                
    firstchord = 1
    for l in chord:
        if l in let1 and firstchord == 1:
            noteoff = midi.NoteOffEvent(tick=((len(w)*110)-1),channel=edoc[l],pitch=(edop[l]))
            tra.append(noteoff)
            firstchord += 1
        elif l in let1 and firstchord != 1:
            noteoff = midi.NoteOffEvent(tick=0,channel=edoc[l],pitch=(edop[l]))
            tra.append(noteoff)
            firstchord += 1
    
    eq = 0
    for l in chord:
        if l in let1:
            eq+=1
    
    if eq == 0 and first == 1:
        noteon = midi.NoteOnEvent(tick=0,channel=16,velocity=1,pitch=0)
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=((len(w)*110)-1),channel=16,pitch=0)
        tra.append(noteoff)  
        first += 1        
    elif eq == 0 and first != 1:
        noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=((len(w)*110)-1),channel=16,pitch=0)
        tra.append(noteoff)
        first += 1        
        
noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
tra.append(noteon)
noteoff = midi.NoteOffEvent(tick=880,channel=16,velocity=1,pitch=0)
tra.append(noteoff)

trackend = midi.EndOfTrackEvent(tick=1)
tra.append(trackend)
midi.write_midifile("chord1-ji.mid", pat)

#chord2
pat = midi.Pattern()
tra = midi.Track()
pat.append(tra)

let2 = "oicazhsktxnu"

pitch = midi.PitchWheelEvent(tick=0,channel=edoc["o"],pitch=edos["o"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["i"],pitch=edos["i"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["c"],pitch=edos["c"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["a"],pitch=edos["a"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["z"],pitch=edos["z"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["h"],pitch=edos["h"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["s"],pitch=edos["s"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["k"],pitch=edos["k"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["t"],pitch=edos["t"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["x"],pitch=edos["x"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["n"],pitch=edos["n"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["u"],pitch=edos["u"])
tra.append(pitch)

first = 1

for w in words:
    wordletters = []
    for l in w:
        l = l.lower()
        if l in letters:
            wordletters.append(l)
    chord = list(set(wordletters))

    firstchord = 1
    for l in chord:
        if l in let2 and first == 1:
            noteon = midi.NoteOnEvent(tick=0,channel=edoc[l],velocity=70,pitch=(edop[l]))
            tra.append(noteon)
            firstchord += 1
            first += 1
        elif l in let2 and first != 1:
            if firstchord == 1:
                noteon = midi.NoteOnEvent(tick=1,channel=edoc[l],velocity=70,pitch=(edop[l]))
                tra.append(noteon)
                firstchord += 1
                first += 1
            elif firstchord != 1:
                noteon = midi.NoteOnEvent(tick=0,channel=edoc[l],velocity=70,pitch=(edop[l]))
                tra.append(noteon)
                firstchord += 1
                first += 1
                
    firstchord = 1
    for l in chord:
        if l in let2 and firstchord == 1:
            noteoff = midi.NoteOffEvent(tick=((len(w)*110)-1),channel=edoc[l],pitch=(edop[l]))
            tra.append(noteoff)
            firstchord += 1
        elif l in let2 and firstchord != 1:
            noteoff = midi.NoteOffEvent(tick=0,channel=edoc[l],pitch=(edop[l]))
            tra.append(noteoff)
            firstchord += 1
    
    eq = 0
    for l in chord:
        if l in let2:
            eq+=1
    
    if eq == 0 and first == 1:
        noteon = midi.NoteOnEvent(tick=0,channel=16,velocity=1,pitch=0)
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=((len(w)*110)-1),channel=16,pitch=0)
        tra.append(noteoff)  
        first += 1        
    elif eq == 0 and first != 1:
        noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=((len(w)*110)-1),channel=16,pitch=0)
        tra.append(noteoff)
        first += 1
        
noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
tra.append(noteon)
noteoff = midi.NoteOffEvent(tick=880,channel=16,velocity=1,pitch=0)
tra.append(noteoff)
        
trackend = midi.EndOfTrackEvent(tick=1)
tra.append(trackend)
midi.write_midifile("chord2-ji.mid", pat)

#chord3
pat = midi.Pattern()
tra = midi.Track()
pat.append(tra)

let3 = "bg"

pitch = midi.PitchWheelEvent(tick=0,channel=edoc["b"],pitch=edos["b"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["g"],pitch=edos["g"])
tra.append(pitch)

first = 1

for w in words:
    wordletters = []
    for l in w:
        l = l.lower()
        if l in letters:
            wordletters.append(l)
    chord = list(set(wordletters))

    firstchord = 1
    for l in chord:
        if l in let3 and first == 1:
            noteon = midi.NoteOnEvent(tick=0,channel=edoc[l],velocity=70,pitch=(edop[l]))
            tra.append(noteon)
            firstchord += 1
            first += 1
        elif l in let3 and first != 1:
            if firstchord == 1:
                noteon = midi.NoteOnEvent(tick=1,channel=edoc[l],velocity=70,pitch=(edop[l]))
                tra.append(noteon)
                firstchord += 1
                first += 1
            elif firstchord != 1:
                noteon = midi.NoteOnEvent(tick=0,channel=edoc[l],velocity=70,pitch=(edop[l]))
                tra.append(noteon)
                firstchord += 1
                first += 1
                
    firstchord = 1
    for l in chord:
        if l in let3 and firstchord == 1:
            noteoff = midi.NoteOffEvent(tick=((len(w)*110)-1),channel=edoc[l],pitch=(edop[l]))
            tra.append(noteoff)
            firstchord += 1
        elif l in let3 and firstchord != 1:
            noteoff = midi.NoteOffEvent(tick=0,channel=edoc[l],pitch=(edop[l]))
            tra.append(noteoff)
            firstchord += 1
    
    eq = 0
    for l in chord:
        if l in let3:
            eq+=1
    
    if eq == 0 and first == 1:
        noteon = midi.NoteOnEvent(tick=0,channel=16,velocity=1,pitch=0)
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=((len(w)*110)-1),channel=16,pitch=0)
        tra.append(noteoff)  
        first += 1        
    elif eq == 0 and first != 1:
        noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=((len(w)*110)-1),channel=16,pitch=0)
        tra.append(noteoff)
        first += 1
        
noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
tra.append(noteon)
noteoff = midi.NoteOffEvent(tick=880,channel=16,velocity=1,pitch=0)
tra.append(noteoff)        
        
trackend = midi.EndOfTrackEvent(tick=1)
tra.append(trackend)
midi.write_midifile("chord3-ji.mid", pat)

#bass1
pat = midi.Pattern()
tra = midi.Track()
pat.append(tra)

letters = "eoviqcfajzphb"

pitch = midi.PitchWheelEvent(tick=0,channel=edoc["e"],pitch=edos["e"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["o"],pitch=edos["o"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["v"],pitch=edos["v"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["i"],pitch=edos["i"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["q"],pitch=edos["q"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["c"],pitch=edos["c"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["f"],pitch=edos["f"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["a"],pitch=edos["a"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["j"],pitch=edos["j"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["z"],pitch=edos["z"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["p"],pitch=edos["p"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["h"],pitch=edos["h"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["b"],pitch=edos["b"])
tra.append(pitch)

first = 1

for w in words:
    tickval = len(w)*110
    let = 1
    for l in w:
        l = l.lower()
        if l in letters and let == 1 and first == 1:
            noteon = midi.NoteOnEvent(tick=0,channel=edoc[l],velocity=70,pitch=(edop[l]-24))
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=(tickval-1),channel=edoc[l],pitch=(edop[l]-24))
            tra.append(noteoff)
        elif l in letters and let == 1 and first != 1:
            noteon = midi.NoteOnEvent(tick=1,channel=edoc[l],velocity=70,pitch=(edop[l]-24))
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=(tickval-1),channel=edoc[l],pitch=(edop[l]-24))
            tra.append(noteoff)
        elif l not in letters and let == 1 and first == 1:
            noteon = midi.NoteOnEvent(tick=0,channel=16,velocity=1,pitch=0)
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=(tickval-1),channel=16,pitch=0)
            tra.append(noteoff)
        elif l not in letters and let == 1 and first != 1:
            noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=70,pitch=0)
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=(tickval-1),channel=16,pitch=0)
            tra.append(noteoff)
        let += 1
        first += 1
            
noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
tra.append(noteon)
noteoff = midi.NoteOffEvent(tick=880,channel=16,velocity=1,pitch=0)
tra.append(noteoff)

trackend = midi.EndOfTrackEvent(tick=1)
tra.append(trackend)
midi.write_midifile("bass1-ji.mid", pat)

#bass2
pat = midi.Pattern()
tra = midi.Track()
pat.append(tra)

letters = "ysrkdtlxmngwu"

pitch = midi.PitchWheelEvent(tick=0,channel=edoc["y"],pitch=edos["y"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["s"],pitch=edos["s"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["r"],pitch=edos["r"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["k"],pitch=edos["k"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["d"],pitch=edos["d"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["t"],pitch=edos["t"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["l"],pitch=edos["l"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["x"],pitch=edos["x"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["m"],pitch=edos["m"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["n"],pitch=edos["n"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["g"],pitch=edos["g"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["w"],pitch=edos["w"])
tra.append(pitch)
pitch = midi.PitchWheelEvent(tick=0,channel=edoc["u"],pitch=edos["u"])
tra.append(pitch)

first = 1

for w in words:
    tickval = len(w)*110
    let = 1
    for l in w:
        l = l.lower()
        if l in letters and let == 1 and first == 1:
            noteon = midi.NoteOnEvent(tick=0,channel=edoc[l],velocity=70,pitch=(edop[l]-24))
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=(tickval-1),channel=edoc[l],pitch=(edop[l]-24))
            tra.append(noteoff)
        elif l in letters and let == 1 and first != 1:
            noteon = midi.NoteOnEvent(tick=1,channel=edoc[l],velocity=70,pitch=(edop[l]-24))
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=(tickval-1),channel=edoc[l],pitch=(edop[l]-24))
            tra.append(noteoff)
        elif l not in letters and let == 1 and first == 1:
            noteon = midi.NoteOnEvent(tick=0,channel=16,velocity=1,pitch=0)
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=(tickval-1),channel=16,pitch=0)
            tra.append(noteoff)
        elif l not in letters and let == 1 and first != 1:
            noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=70,pitch=0)
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=(tickval-1),channel=16,pitch=0)
            tra.append(noteoff)
        let += 1
        first += 1
            
noteon = midi.NoteOnEvent(tick=1,channel=16,velocity=1,pitch=0)
tra.append(noteon)
noteoff = midi.NoteOffEvent(tick=880,channel=16,velocity=1,pitch=0)
tra.append(noteoff)

trackend = midi.EndOfTrackEvent(tick=1)
tra.append(trackend)
midi.write_midifile("bass2-ji.mid", pat)

    
    
    
    
    
    
    
    
