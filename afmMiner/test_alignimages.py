import numpy as np 
from afmMiner import alignImage
   
#define path of data files 
MAPI01HeightPath='../afmMiner/data/MAPI_01.txt'
MAPI00HeightPath='../afmMiner/data/MAPI_00.txt'
#load in txt files corresponding to height
MAPI01Height=np.loadtxt(MAPI01HeightPath, delimiter="\t", dtype='float')
MAPI00Height=np.loadtxt(MAPI00HeightPath, delimiter="\t", dtype='float')


def test_alignimage():

    #define inputs
    static=MAPI00Height
    moving=MAPI01Height
    level_iters = [200, 100, 50, 25]

    assert static.shape[0]==moving.shape[0] and static.shape[1]==moving.shape[1]
    return 'Static and Moving have the same number of rows and columns!'

