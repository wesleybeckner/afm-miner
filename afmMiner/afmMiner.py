def selfCompare(x_input, y_input, n_trees=5, n_depth=5, n_feature_vector=1):
	###dictionary in this function; config paparamter that is a dictionary
	###that contains all the other default settings
	###hiearcahy of variables to change
	###need to add raise exceptions for uninformed/naughty users. 
    """
    selfCompare trains and tests a random forest on the same array of
    input images (x_input and y_input).
   
    selfCompare depends on afmSetup, afmTrainTest, afmModel and
    afmImageShow functions

    selfCompare will train an random forrest on the top half of a set 
    of input images and use the bottom half to make a prediction of the 
    photoluminescence of the same material. 

    Parameters
    ------------------
    n_trees : int, optional 
	Number of trees to include in the ensemble (default 5)

    n_depth : int, optional
	Maximum depth of each tree in the ensembel (default 5)

    n_feature_vector : int, optional
	Describes the feature vector for each input image can be up
	to an array of up to 4x4 (default 1)

    x_input : str, list
	Give the name(s) of the input file(s) for train/testing

    y_input: str
	Give the name of the target image to be predicted

    Returns
    ------------------
    Figure : matplotlib.plot()

    """
    ###import modules
    import numpy as np
    from sklearn import metrics
    from sklearn.ensemble import RandomForestRegressor
    import matplotlib.pyplot as plt
    
    ###begin subcalls and variable assignments
    pixelContext, depths, trees = afmSetup(x_input, y_input, n_trees=5, \
        n_depth=5, n_feature_vector=1)
    Xtrain, Ytrain, x, y, Pl = afmTrainTest(x_input, y_input,\
        pixelContext, depths, trees, train=True, test=False)
    Xtest, Ytest, x, y, Pl = afmTrainTest(x_input, y_input,\
        pixelContext, depths, trees, train=False, test=True)
    Pl_predict, clf, roundscore = afmModel(Xtrain, Ytrain, Xtest, Ytest, \
        depths, trees, x, y, pixelContext)
    afmImageShow(Pl_predict, n_feature_vector, n_depth, n_trees, \
        roundscore, Pl)

def crossCompare(x_input1, y_input1, x_input2, y_input2, n_trees=5, n_depth=5, \
        n_feature_vector=1, split=1):
    """
    crossCompare trains and tests a random forest on the separate arrays of
    input images (x_input1, x_input2, y_input1, and y_input2).
   
    crossCompare depends on afmSetup, afmTrainTest, afmModel and
    afmImageShow functions

    crossCompare will train an random forrest on the top half of a set 
    of input images and use the bottom half of a second set of images 
    to make a prediction of the photoluminescence of the second
    material. 

    Parameters
    ------------------
    n_trees : int, optional 
	Number of trees to include in the ensemble (default 5)

    n_depth : int, optional
	Maximum depth of each tree in the ensembel (default 5)

    n_feature_vector : int, optional
	Describes the feature vector for each input image can be up
	to an array of up to 4x4 (default 1)

    x_input1 : str, list
	Give the name(s) of the input file(s) for training

    y_input1: str
	Give the name of the target image for training

    x_input1 : str, list
	Give the name(s) of the input file(s) for testing

    y_input1: str
	Give the name of the target image to be predicted
	(this is used only to print to screen as a comparison)

    Returns
    ------------------
    Figure : matplotlib.plot()

    """
    ###import modules
    import numpy as np
    from sklearn import metrics
    from sklearn.ensemble import RandomForestRegressor
    import matplotlib.pyplot as plt

    ###begin subcalls and variable assignments
    pixelContext, depths, trees = afmSetup(x_input1, y_input1, n_trees=5,\
        n_depth=5, n_feature_vector=1)
    Xtrain, Ytrain, x, y, Pl = afmTrainTest(x_input1, y_input1, pixelContext, \
        depths, trees, train=True, test=False)
    Xtest, Ytest, x, y, Pl = afmTrainTest(x_input2, y_input2, pixelContext, \
        depths, trees, train=False, test=True)
    Pl_predict, clf, roundscore = afmModel(Xtrain, Ytrain, Xtest, Ytest, \
        depths, trees, x, y, pixelContext)
    afmImageShow(Pl_predict, n_feature_vector, n_depth, n_trees, roundscore,\
         Pl)

def afmSetup(x_input, y_input, n_trees=5, n_depth=5, n_feature_vector=1):
    """
    afmSetup creates the necessary arrays and variables for the rest
    of the afmMiner module
    """

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

def afmTrainTest(x_input, y_input, pixelContext, depths, trees, train, test,\
    split=0.5):
    """
    afmTrainTest creates flattened arrays of the input pixel values.
    it's primary job is organizing the arrays in accordance with the
    feature vector size chosen by the user
    """
    ###import modules
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn import preprocessing
    
    ###Load data and scale
    inputs=np.zeros(len(x_input), dtype=object)
    Pl=preprocessing.scale(np.loadtxt('%s.txt' % y_input,\
        skiprows=0, dtype=np.float64))
    for h,i in enumerate(x_input):
        inputs[h] = preprocessing.scale(np.loadtxt('%s.txt' \
            % i,skiprows=0, dtype=np.float64))
        
    ###Decide how to parse inputs (train+test, train, or test)   
    y = inputs[0].shape[1]
    x = int(inputs[0].shape[0]*split)
    if train: 
        start=max(pixelContext)
        stop=int(inputs[0].shape[0]*split) 
    if test:
        start=int(inputs[0].shape[0]*(1-split))
        stop=inputs[0].shape[0]-max(pixelContext)

    X=np.zeros(((y-(max(pixelContext)*2))*(x-max(pixelContext)),\
             (len(pixelContext)*len(pixelContext)*len(inputs))))
    current_feature_vector=0
    for row in range(start,stop):
        for column in range(max(pixelContext),y-max(pixelContext)):
            current_feature=0
            for index, input_value in enumerate(inputs):
                for row_surrounding in pixelContext:
                    for column_surrounding in pixelContext:
                        X[current_feature_vector,current_feature]\
                        =input_value[(row+row_surrounding),\
                        (column+column_surrounding)]
                        current_feature+=1  
            current_feature_vector+=1
    Y=np.zeros(((y-(max(pixelContext)*2))*(x-max(pixelContext))))
    current_target=0 
    for row in range(start,stop):
        for column in range(max(pixelContext),y-max(pixelContext)):
            Y[current_target]=Pl[row,column]
            current_target+=1
    return X, Y, x, y, Pl

def afmModel(Xtrain, Ytrain, Xtest, Ytest, depths, trees, x, y, pixelContext, \
        selfCompare=True):
    """ 
    afmModel trains sklearn.ensemble RandomForestRegressor on the 
    input arrays provided by afmTrainTest. It also runs a prediction
    and stores the output in Pl_predict
    """
    ###import modules
    from sklearn import metrics
    from sklearn.ensemble import RandomForestRegressor
    import numpy as np

    k=0
    prediction = []

    clf = RandomForestRegressor(max_depth=depths, n_estimators=trees,\
        bootstrap=True)
    clf.fit(Xtrain, Ytrain)
    hold = clf.predict(Xtest)
    score = metrics.mean_squared_error(Ytest, hold)
    roundscore = myround(score, 0.001)

    prediction.append(hold)
    k+=1
    
    k=0
    merge = (np.array(prediction).flatten())
    Pl_predict = np.zeros(((x-max(pixelContext))*1,(y-(max(pixelContext)*2))*1))
    for l in range(1):
        for i in range((x-max(pixelContext))*1):
            for j in range (y-(max(pixelContext)*2)):
                Pl_predict[i,j+(l*(y-(max(pixelContext)*2)))] = merge[k]
                k+=1
    return Pl_predict, clf, roundscore

def afmImageShow(Pl_predict, n_feature_vector, n_depth, n_trees, roundscore, Pl):
    """
    afmImageShow generates the image of the Photoluminescence prediciton 
    alongside the actual photoluminescence image
    """
    ###import modules
    import matplotlib.pyplot as plt       

    fig = plt.figure(figsize=(10,10))   
    pl_ax = fig.add_subplot(121)
    pl_ax.imshow(Pl_predict.T, cmap='viridis')
    pl_ax.text(-10,275,'%s x %s Feature Vector, %s depth, %s trees; score: %s'\
        %(n_feature_vector,n_feature_vector,n_depth,\
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
    return plt

def myround(x, base):
    """
    myround is a simple round tool
    """
    return (float(base) * round(float(x)/float(base)))
