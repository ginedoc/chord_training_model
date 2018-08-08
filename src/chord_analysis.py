import numpy as np
import pyace as pyace

def chord_analysis(flist):
    flist = open(flist, 'r')
    flist = (flist.read()).split()
    for mp3 in flist:
        pyace.deepace(mp3, '../chord.txt', 'rnn', '../model/lstmrnn512/CJKURB.cg.model')
        #pyace.simpleace(mp3, '../chord.txt')
