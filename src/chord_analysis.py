import numpy as np
import pyace.pyace as pyace

def chord_analysis(flist):
    for mp3 in (flist.read()).split():
        pyace.deepace(mp3, '../chord.txt', 'rnn', '../model/lstmrnn512/CJKURB.cg.model')
