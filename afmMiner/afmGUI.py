###import modules
from tkinter import *
from tkinter import ttk

    
def calculate(**kwargs):
    """
    Calculate

    Calculate defines the calculate button on the GUI so that it runs the selfCompare function with the inputted parameters.

    Calculate(**kwargs)

    Takes any arguments. Mainly it takes the x_inputs, y_input, n_trees, n_depth, and n_feature_vector to input into 
    the selfCompare function. 
    """
    from afmMiner import selfCompare
    
    x=[xvector1.get(),xvector2.get(),xvector3.get(),xvector4.get()]
    if xvector1.get() == '':
        print('Need to input x data!')
    if yvector.get() == '':
        print('Need to input y data!')
    
    x_in=[]
    for entry in x:
        if entry == '' :
            pass
        else:
            x_in.append(entry)
    
    selfCompare(x_input=x_in, y_input=yvector.get(), n_trees=trees.get(), n_depth=depths.get(),\
                n_feature_vector=feature_vector.get())


root = Tk()
root.title("AFM Random Forest Tree Regressor")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

trees = IntVar()
depths = IntVar()
feature_vector = IntVar()
xvector1 = StringVar()
xvector2 = StringVar()
xvector3 = StringVar()
xvector4 = StringVar()
xvector5 = StringVar()
xvector6 = StringVar()
xvector7 = StringVar()
xvector8 = StringVar()

yvector = StringVar()

xinput1 = ttk.Entry(root, textvariable=xvector1).grid(column=2,row=4)
xinput2 = ttk.Entry(root, textvariable=xvector2).grid(column=2,row=5)
xinput3 = ttk.Entry(root, textvariable=xvector3).grid(column=2,row=6)
xinput4 = ttk.Entry(root, textvariable=xvector4).grid(column=2,row=7)
xinput5 = ttk.Entry(root, textvariable=xvector5).grid(column=2,row=8)
xinput6 = ttk.Entry(root, textvariable=xvector6).grid(column=2,row=9)
xinput7 = ttk.Entry(root, textvariable=xvector7).grid(column=2,row=10)
ttk.Label(root, text="--------------------------").grid(column=2,row=11)

yinput = ttk.Entry(root, textvariable=yvector).grid(column=2,row=12)
ttk.Label(root, text="X inputs into regressor: ").grid(column=1,row=4)
ttk.Label(root, text="Y inputs into regressor: ").grid(column=1,row=12)
ttk.Label(root, text="Input as many X's as you want (up to 8)").grid(column=3,row=4)


trees_entry = Spinbox(root, from_=1.0, to=20.0, textvariable=trees)
depths_entry= Spinbox(root, from_=1.0, to=20.0, textvariable=depths)
features_entry= Spinbox(root, from_=1.0, to=3.0, textvariable=feature_vector)

depths_entry.grid(column=2, row=1, sticky=W)
trees_entry.grid(column=2, row=2, sticky=W)
features_entry.grid(column=3,row=2)

ttk.Button(root, text="Calculate", command=calculate).grid(column=2, row=13, sticky=W)
           
ttk.Label(root, text="Depth of Trees: ").grid(column=1, row=1, sticky=E)
ttk.Label(root, text="Number of Trees: ").grid(column=1, row=2,  sticky=E)
ttk.Label(root, text="Size of Feature Vector:").grid(column=3, row=1, sticky=(W,E))

for child in root.winfo_children(): child.grid_configure(padx=5, pady=5)

depths_entry.focus()

root.mainloop()
