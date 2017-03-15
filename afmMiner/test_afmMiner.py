import numpy as np
import pandas as pd
from afmMiner import rowi_to_rowj
from afmMiner import rowi_to_all_rows
from afmMiner import pairwise_correlation
df = pd.DataFrame([[-1, 0, 1], [1, 0, -1], [.5, 0, .5]])

def test_rowi_to_rowj():
    assert rowi_to_rowj(df.iloc[0], df.iloc[1]), 'argument missing' 
    assert rowi_to_rowj(df.iloc[0], df.iloc[1]) == df.iloc[0].corr(df.iloc[1]),\
    'Anticorrelated elements not handled properly'
    assert int(rowi_to_rowj(df.iloc[0], df.iloc[0])) == 1,\
    'Diagonal elements not handled properly'
    assert int(rowi_to_rowj(df.iloc[0], df.iloc[2])) == 0,\
    'Correlated elements not handled properly'
    return 'test passed'
def test_rowi_to_all_rows():
    assert int(rowi_to_all_rows(df, 0, df.iloc[0], pd.DataFrame())[0][1]) ==\
    int(rowi_to_all_rows(df, 0, df.iloc[0], pd.DataFrame())[1][0]),\
    'Symmetry not handled properly'
    assert int(rowi_to_all_rows(df, 0, df.iloc[0], pd.DataFrame())[0][0]) == 1,\
    'Diagonal elements not handled properly'
    assert int(rowi_to_all_rows(df, 0, df.iloc[0], pd.DataFrame())[0][1]) == -1,\
    'Anticorrelated elements not handled properly'
    return 'test passed'
def test_pairwise_correlation():
    assert int(pairwise_correlation(df)[0][1]) ==\
    int(pairwise_correlation(df)[1][0]),\
    'Symmetry not handled properly'
    assert int(pairwise_correlation(df).shape[0]) ==\
    int(pairwise_correlation(df).shape[1]),'Output is not a square matrix'
    assert int(df.shape[0]) == int(df.shape[1]),\
    'Input is not a square matrix'
    return 'test passed'
