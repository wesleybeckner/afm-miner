import numpy as np
import pandas as pd
from afmMiner import selfCompare
from afmMiner import crossCompare
from afmMiner import afmSetup
from afmMiner import afmTrainTest
from afmMiner import afmModel
from afmMiner import afmImageShow
"""
selfCompare and crossCompare make calls to the following functions 
they are not tested directly since their output is a matplotlib figure.
Consequently that final function, afmImageShow is not tested here either.
"""
x_input1=['../afmMiner/data/MABr.1.Ht', '../afmMiner/data/MABr.1.Po',\
     '../afmMiner/data/MABr.1.Ph', '../afmMiner/data/MABr.1.Am']
y_input1='../afmMiner/data/MABr.1.Pl'
x_input2=['../afmMiner/data/Ht', '../afmMiner/data/Po', '../afmMiner/data/Ph',\
    '../afmMiner/data/Am']
y_input2='../afmMiner/data/Pl'

def test_afmSetup():
    pixelContext, depths, trees = afmSetup(x_input1, y_input1, n_trees=5,\
        n_depth=5, n_feature_vector=4)
    assert len(pixelContext) == 9
    'pixel context array is not the correct length'
    return 'test passed'
def test_afmTrainTest():
    pixelContext, depths, trees = afmSetup(x_input1, y_input1, n_trees=5,\
        n_depth=5, n_feature_vector=4)
    Xtest, Ytest, x, y, Pl = afmTrainTest(x_input2, y_input2, pixelContext, \
        depths, trees, train=False, test=True)
    assert x*2==y 
    'input images are of different dimensions'
    return 'test passed'
def test_afmModel():
    pixelContext, depths, trees = afmSetup(x_input1, y_input1, n_trees=5,\
        n_depth=5, n_feature_vector=4)
    Xtrain, Ytrain, x, y, Pl = afmTrainTest(x_input2, y_input2, pixelContext, \
        depths, trees, train=True, test=False)
    Xtest, Ytest, x, y, Pl = afmTrainTest(x_input2, y_input2, pixelContext, \
        depths, trees, train=False, test=True)
    Pl_predict, clf, roundscore = afmModel(Xtrain, Ytrain, Xtest, Ytest, \
        depths, trees, x, y, pixelContext)
    assert len(str(roundscore))==5 
    'roundscore is not working correctly'
    return 'test passed'
    
