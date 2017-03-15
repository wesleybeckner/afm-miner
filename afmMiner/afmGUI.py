from tkinter import *
from tkinter import ttk

def afmGUI():
    def calculate(**kwargs):
        """
        calculate
    
        calculate defines the calculate button on the GUI so that it runs either the selfCompare or crossCompare function with the 
        inputted parameters.
        
        First, it tests to see if all the entries in the right panel if empty. If they are, it will run the selfCompare function 
        later. If not, it will run the crossCompare function. It also makes sure there is at least one yvector inputted. Finally, 
        it sets up all the inputs for entry into the functions, ignoring all the empty entries.
    
        calculate(**kwargs)
    
        Takes any arguments. Mainly it takes all the x_inputs, y_inputs, n_trees, n_depth, and n_feature_vector to input into 
        the functions. 
        """
        ###import modules
        from afmMiner import crossCompare
        from afmMiner import selfCompare
        
        x_train=[xvector1A.get(),xvector2A.get(),xvector3A.get(),xvector4A.get(),xvector5A.get(),xvector6A.get(),xvector7A.get()]
        x_test =[xvector1B.get(),xvector2B.get(),xvector3B.get(),xvector4B.get(),xvector5B.get(),xvector6B.get(),xvector7B.get()]
        
        sum_B=0
        for x in x_test:
            if x != '':
                sum_B+=1
            else:
                pass
        
        if yvectorA.get() == '':
            print('Need to input y training data!')
        
        x_inA=[]
        for entry in x_train:
            if entry == '' :
                pass
            else:
                x_inA.append(entry)
            
        if sum_B == 0:
            selfCompare(x_input=x_inA, y_input=yvectorA.get(), n_trees=trees.get(), n_depth=depths.get(),\
                    n_feature_vector=feature_vector.get())
        else:
            x_inB=[]
            for entry in x_test:
                if entry == '' :
                    pass
                else:
                    x_inB.append(entry)
            crossCompare(x_input1=x_inA, y_input1=yvectorA.get(), x_input2=x_inB, y_input2=yvectorB.get(), n_trees=trees.get(),\
                    n_depth=depths.get(), n_feature_vector=feature_vector.get())
            
    root = Tk()
    root.title("AFM Random Forest Tree Regressor")
    
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    
    trees = IntVar()
    depths = IntVar()
    feature_vector = IntVar()
    xvector1A = StringVar()
    xvector2A = StringVar()
    xvector3A = StringVar()
    xvector4A = StringVar()
    xvector5A = StringVar()
    xvector6A = StringVar()
    xvector7A = StringVar()
       
    xvector1B = StringVar()
    xvector2B = StringVar()
    xvector3B = StringVar()
    xvector4B = StringVar()
    xvector5B = StringVar()
    xvector6B = StringVar()
    xvector7B = StringVar()
    
    yvectorA = StringVar()
    yvectorB = StringVar()
    ttk.Label(root, text="--------------------------------------------------------------------------------------------------------------------------------------").grid(column=1,row=2,columnspan=7)
    
    xinput1A = ttk.Entry(root, textvariable=xvector1A).grid(column=2,row=5)
    xinput2A = ttk.Entry(root, textvariable=xvector2A).grid(column=2,row=6)
    xinput3A = ttk.Entry(root, textvariable=xvector3A).grid(column=2,row=7)
    xinput4A = ttk.Entry(root, textvariable=xvector4A).grid(column=2,row=8)
    xinput5A = ttk.Entry(root, textvariable=xvector5A).grid(column=2,row=9)
    xinput6A = ttk.Entry(root, textvariable=xvector6A).grid(column=2,row=10)
    xinput7A = ttk.Entry(root, textvariable=xvector7A).grid(column=2,row=11)
    ttk.Label(root, text="--------------------------").grid(column=2,row=12)
    
    yinputA = ttk.Entry(root, textvariable=yvectorA).grid(column=2,row=13)
    ttk.Label(root, text="X inputs into regressor: ").grid(column=1,row=5)
    ttk.Label(root, text="Y inputs into regressor: ").grid(column=1,row=13)
    ttk.Label(root, text="Input up to 7 X's").grid(column=3,row=5)
        
    xinput1B = ttk.Entry(root, textvariable=xvector1B).grid(column=6,row=5)
    xinput2B = ttk.Entry(root, textvariable=xvector2B).grid(column=6,row=6)
    xinput3B = ttk.Entry(root, textvariable=xvector3B).grid(column=6,row=7)
    xinput4B = ttk.Entry(root, textvariable=xvector4B).grid(column=6,row=8)
    xinput5B = ttk.Entry(root, textvariable=xvector5B).grid(column=6,row=9)
    xinput6B = ttk.Entry(root, textvariable=xvector6B).grid(column=6,row=10)
    xinput7B = ttk.Entry(root, textvariable=xvector7B).grid(column=6,row=11)
    ttk.Label(root, text="--------------------------").grid(column=6,row=12)
    
    yinputB = ttk.Entry(root, textvariable=yvectorB).grid(column=6,row=13)
    ttk.Label(root, text="X inputs into regressor: ").grid(column=5,row=5)
    ttk.Label(root, text="Y inputs into regressor: ").grid(column=5,row=13)
    ttk.Label(root, text="Input up to 7 X's").grid(column=7,row=5)
    
    trees_entry = Spinbox(root, from_=1.0, to=20.0, textvariable=trees).grid(column=2, row=1, sticky=W)
    depths_entry= Spinbox(root, from_=1.0, to=20.0, textvariable=depths).grid(column=4, row=1, sticky=W)
    features_entry= Spinbox(root, from_=1.0, to=3.0, textvariable=feature_vector).grid(column=6,row=1)
    
    ttk.Button(root, text="CALCULATE", command=calculate).grid(column=4, row=15, sticky=W)
    ttk.Button(root, text="Quit", command=root.destroy).grid(column=7,row=15)
    
    ttk.Label(root, text="Depth of Trees: ").grid(column=1, row=1, sticky=E)
    ttk.Label(root, text="Number of Trees: ").grid(column=3, row=1,  sticky=E)
    ttk.Label(root, text="Size of Feature Vector:").grid(column=5, row=1, sticky=(W,E))
    ttk.Label(root, text=":Training Image Inputs:").grid(column=2,row=4)
    ttk.Label(root, text=":Testing Image Inputs:").grid(column=6,row=4)
    ttk.Label(root, text="ONLY USE PANELS ON LEFT IF USING SELFCOMPARE").grid(column=1,row=3,columnspan=7) 
        
    for child in root.winfo_children(): child.grid_configure(padx=5, pady=5)
    
    root.mainloop()
