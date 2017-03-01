This is where you will place all of your content regarding the big picture design
of your software. 
For this week, layout the use cases (1-3) and for each one, describe the component
specification.Feel free to use diagrams.


For this project, we plan on predicting the photoluminescence of AFM images from
other parameters and techniques. Wes already has some base code to work off of
but we have planned mutiple additions to upgrade the existing code.

First, we plan on enhancng this code to improve its performance through the
implementation of a 'double sweep' method to refine the clarity for high luminescent
regions of the material. To do this, the program will go through the image and characterize
the low luminescent regions. Then, the program will go through image and characterize
the high luminescent region with a regression attuned to the high luminescence regions.

Second, we will implement an 'auto-alignment' procedure to ensure the images are the same
and can be laid on top of each other for more accurate predictions of photoluminescence.
There will also be an alignment score to describe how close to aligned each of the images 
are to each other and determine how accurate the prediction is. This algorithm will look at
the topography file that is outputted from the AFM during each test to align the images.

Third, we plan on implementing a GUI/functionality interface for easy manipulation and 
visualization of the process. The parameters that a user could manipulate include the 
number of trees, depth of each tree, input images, parameter that adjusts 'double sweep' 
method (i.e. photoluminescence cutoff) and the size of array for the algorithm to draw 
extra data from. We will include a wrapper function that iterates through many different
tree numbers, tree depths, surrounding array size and double sweep parameter to output the 
'optimal' set. Some of the outputs from this would be the accuracy of the predictions to
the actual photoluminescence, visualization of random tree structure, optimal set of 
parameters, and the predicted vs. actual photoluminescence images.

