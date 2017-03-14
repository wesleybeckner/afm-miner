def myround(x, base):
    return (float(base) * round(float(x)/float(base)))

def afmSetup(x_input, y_input, n_trees=5, n_depth=5, n_feature_vector=1):

    ###Setup user defined variables
    x9x9 = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    x7x7 = [-3, -2, -1, 0, 1, 2, 3]
    x5x5 = [-2, -1, 0, 1, 2]
    x3x3 = [-1, 0, 1]
    pixel_handles = [x3x3, x5x5, x7x7, x9x9]    
    pixelContext = pixel_handles[n_feature_vector-1]   
    depths = n_depth
    trees = n_trees
    return pixelContext, depths, trees

def afmTrainTest(x_input, y_input, pixelContext, depths, trees, train, test):
    """

    selfCompare will train an random forrest on the top half of a set of input images 
    and use the bottom half to make a prediction of the photoluminescence of the same
    material. 

    selfCompare(n_trees, n_depth, n_feature_vector, x_input, y_input)

    n_trees: default 5

    n_depth: default 5

    n_feature_vector: default 1
        can be 1, 2, or 3 surrounding pixels

    x_input: no default, tuple of file names

    y_input: no default, file name
    """
    ###import modules
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn import preprocessing
    
    ###Load data and scale
    inputs=np.zeros(len(x_input), dtype=object)
    Pl=preprocessing.scale(np.loadtxt('./data/%s.txt' % y_input,skiprows=0, dtype=np.float64))
    for h,i in enumerate(x_input):
        inputs[h] = preprocessing.scale(np.loadtxt('./data/%s.txt' % i,skiprows=0, dtype=np.float64))
        
    ###Decide how to parse inputs (train+test, train, or test)   
    y = inputs[0].shape[1]
    x = int(inputs[0].shape[0]/2)
    x2 = inputs[0].shape[0]

    ###Create training and testing arrays
    if train==True:
        Xtrain = np.zeros(((y-(max(pixelContext)*2))*(x-max(pixelContext)),\
                 (len(pixelContext)*len(pixelContext)*len(inputs))))
        k=0
        for p in range(max(pixelContext),x):
            for q in range(max(pixelContext),y-max(pixelContext)):
                j=0
                for h, i in enumerate(inputs):

                    for l in pixelContext:
                        for m in pixelContext:
                            Xtrain[k,j]=i[(p+l),(q+m)]
                            j=j+1
                k = k + 1
        Ytrain = np.zeros(((y-(max(pixelContext)*2))*(x-max(pixelContext))))
        k=0 
        for p in range(max(pixelContext),x):
            for q in range(max(pixelContext),y-max(pixelContext)):
                Ytrain[k]=Pl[p,q]
                k = k + 1
    if test==True:
        Xtest = np.zeros(((y-(max(pixelContext)*2))*(x-max(pixelContext)),\
                (len(pixelContext)*len(pixelContext)*len(inputs))))
        k=0
        for p in range(x,x2-max(pixelContext)):
            for q in range(max(pixelContext),y-max(pixelContext)):
                j=0
                for h, i in enumerate(inputs):
                    for l in pixelContext:
                        for m in pixelContext:
                            Xtest[k,j]=i[(p+l),(q+m)]
                            j=j+1
                k = k + 1

        Ytest = np.zeros(((y-(max(pixelContext)*2))*(x-max(pixelContext))))
        k=0
        for p in range(x,x2-max(pixelContext)):
            for q in range(max(pixelContext),y-max(pixelContext)):
                Ytest[k]=Pl[p,q]
                k = k + 1
    if train==True & test==True:
        return Xtrain, Ytrain, Xtest, Ytest, x, y, Pl
    elif train==True:
        return Xtrain, Ytrain, x, y, Pl
    else:
        return Xtest, Ytest, x, y, Pl

def afmModel(Xtrain, Ytrain, Xtest, Ytest, depths, trees, x, y, pixelContext, selfCompare=True):
    from sklearn import metrics
    from sklearn.ensemble import RandomForestRegressor
    import numpy as np

    k=0
    prediction = []

    clf = RandomForestRegressor(max_depth=depths, n_estimators=trees, bootstrap=True)
    clf.fit(Xtrain, Ytrain)
    hold = clf.predict(Xtest)
    score = metrics.mean_squared_error(Ytest, hold)
    roundscore = myround(score, 0.001)

    prediction.append(hold)
    k = k + 1
    
    

    k=0
    merge = (np.array(prediction).flatten())
    Pl_predict = np.zeros(((x-max(pixelContext))*1,(y-(max(pixelContext)*2))*1))
    for l in range(1):
        for i in range((x-max(pixelContext))*1):
            for j in range (y-(max(pixelContext)*2)):
                Pl_predict[i,j+(l*(y-(max(pixelContext)*2)))] = merge[k]
                k = k + 1
    return Pl_predict, clf, roundscore

def afmImageShow(Pl_predict, n_feature_vector, n_depth, n_trees, roundscore, Pl):
    import matplotlib.pyplot as plt       
    fig = plt.figure(figsize=(10,10))
    
    pl_ax = fig.add_subplot(121)
    pl_ax.imshow(Pl_predict.T, cmap='viridis')
    pl_ax.text(-10,275,'%s x %s Feature Vector, %s depth, %s trees; score: %s' %(n_feature_vector,n_feature_vector,n_depth,\
        n_trees,roundscore), size=24)
    pl_ax.axes.get_xaxis().set_ticks([])
    pl_ax.axes.get_yaxis().set_ticks([])
    pl_ax.set_title('Prediction', size=30)
   
    pl_ax2 = fig.add_subplot(122)
    pl_ax2.set_title('Actual', size=30)
    pl_ax2.imshow(Pl[Pl.shape[0]/2:,:].T, cmap='viridis')
    pl_ax2.axes.get_xaxis().set_ticks([])
    pl_ax2.axes.get_yaxis().set_ticks([])
    fig.subplots_adjust(left=None, bottom=None, right=None, top=None,\
                        wspace=None, hspace=None)
    
    plt.show()

def selfCompare(x_input, y_input, n_trees=5, n_depth=5, n_feature_vector=1):
    ###import modules
    import numpy as np
    from sklearn import metrics
    from sklearn.ensemble import RandomForestRegressor
    import matplotlib.pyplot as plt
    pixelContext, depths, trees = afmSetup(x_input, y_input, n_trees=5, n_depth=5, n_feature_vector=1)

    Xtrain, Ytrain, Xtest, Ytest, x, y, Pl = afmTrainTest(x_input, y_input, pixelContext, depths, trees, train=True, test=True)
    Pl_predict, clf, roundscore = afmModel(Xtrain, Ytrain, Xtest, Ytest, depths, trees, x, y, pixelContext)
    
    afmImageShow(Pl_predict, n_feature_vector, n_depth, n_trees, roundscore, Pl)

def crossCompare(x_input1, y_input1, x_input2, y_input2, n_trees=5, n_depth=5, n_feature_vector=1):
    ###import modules
    import numpy as np
    from sklearn import metrics
    from sklearn.ensemble import RandomForestRegressor
    import matplotlib.pyplot as plt
    pixelContext, depths, trees = afmSetup(x_input1, y_input1, n_trees=5, n_depth=5, n_feature_vector=1)

    Xtrain, Ytrain, x, y, Pl = afmTrainTest(x_input1, y_input1, pixelContext, depths, trees, train=True, test=False)
    Xtest, Ytest, x, y, Pl = afmTrainTest(x_input2, y_input2, pixelContext, depths, trees, train=False, test=True)
    
    Pl_predict, clf, roundscore = afmModel(Xtrain, Ytrain, Xtest, Ytest, depths, trees, x, y, pixelContext)
    
    afmImageShow(Pl_predict, n_feature_vector, n_depth, n_trees, roundscore, Pl)

