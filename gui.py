from tkinter import *
import os
import sys
import numpy as np
from tkinter import filedialog

curr = ''

def setPath():

    def findpath():
        global curr
        curr = plotEntry.get("1.0", 'end')
        curr = curr.rstrip()

    input2 = Toplevel(root)
    input2.geometry("780x200")
    input2.resizable(0, 0)

    closeButtonI1 = Button(input2, text="Close", command=input2.destroy)
    closeButtonI1.config(background='red', fg='white', font=('courier', 10, 'bold'))
    closeButtonI1.place(x=680, y=160)

    saveButtonI1 = Button(input2, text="Set", command=findpath)
    saveButtonI1.config(background='green', fg='white', font=('courier', 10, 'bold'))
    saveButtonI1.place(x=620, y=160)


    PlotLabel = Label(input2, text="Set path")
    PlotLabel.config(background='dark blue', fg='white', font=('courier', 16, 'bold'))
    PlotLabel.place(x=10, y=5)

    scrollbar1 = Scrollbar(input2)
    scrollbar1.pack(side=RIGHT, fill=Y)
    plotEntry = Text(input2, yscrollcommand=scrollbar1.set)
    plotEntry.config(font=('Courier', 14, 'normal'), height=5, width=65, background='gray', undo = True, autoseparator = True, maxundo = -1)
    plotEntry.place(x=30, y=40)
    
    
def cluster_output():
    global curr
    os.chdir(curr)
    os.chdir('BIBM')
    os.chdir('Output')
    os.system('rm -r *')
    os.chdir(curr)
    os.system('zip -r BIBM.zip BIBM')
    os.system('mv BIBM.zip BIBM')

    os.chdir('BIBM')
    os.system('mv BIBM.zip Output')
    os.chdir(curr)


def openfile():


    
    filename = filedialog.askopenfilename()
    if filename:
        data = open(filename, "rb").read()
        reactionRulesEntry = input_2()
        reactionRulesEntry.delete('1.0', 'end')
        reactionRulesEntry.insert('1.0', data)
    


def Run():

    global curr
    os.chdir(curr)
    os.chdir(curr + '/BIBM')
    os.system('python3 Main.py')
    os.chdir(curr)

def Output():

    global curr
    os.chdir(curr)
    os.chdir(curr + '/BIBM')
    os.chdir('Output')
    os.system('gedit logfile.pcl')
    os.chdir(curr)
    
def aboutUs():

    global curr
    os.chdir(curr)
    os.system('gedit aboutUs.pcl')
    os.chdir(curr)

def exit():
  sys.exit()


def doNothing():
    print("ok ok I won't...")



def analysis():

    def runPlot():

        global curr
        os.chdir(curr)
        os.chdir('BIBM')
        os.system('python3 analysis.py')
        os.system('python3 plot22.py')
        os.chdir(curr)


    def write_file():
        entry1 = plotEntry.get("1.0",END)

        with open(curr + "BIBM/plot_rules.pcl", "w") as f:  # open file
            f.write(entry1)


    input2 = Toplevel(root)
    input2.geometry("800x400")
    input2.resizable(0, 0)

    closeButtonI1 = Button(input2, text="Close", command=input2.destroy)
    closeButtonI1.config(background='red', fg='white', font=('courier', 16, 'bold'))
    closeButtonI1.place(x=680, y=355)

    saveButtonI1 = Button(input2, text="Run", command=runPlot)
    saveButtonI1.config(background='green', fg='white', font=('courier', 16, 'bold'))
    saveButtonI1.place(x=615, y=355)

    compileButtonI1 = Button(input2, text="Compile Model", command=write_file)
    compileButtonI1.config(background='blue', fg='white', font=('courier', 16, 'bold'))
    compileButtonI1.place(x=420, y=355)

    PlotLabel = Label(input2, text="Plot Rules")
    PlotLabel.config(background='dark blue', fg='white', font=('courier', 16, 'bold'))
    PlotLabel.place(x=10, y=6)

    scrollbar1 = Scrollbar(input2)
    scrollbar1.pack(side=RIGHT, fill=Y)
    plotEntry = Text(input2, yscrollcommand=scrollbar1.set)
    plotEntry.config(font=('Courier', 14, 'normal'), height=14, width=65, background='gray', undo = True, autoseparator = True, maxundo = -1)
    plotEntry.place(x=30, y=40)




def input_2():

    def save_file():
        filename = filedialog.asksaveasfilename(defaultextension=".pcl")
        #filename = None
        if filename:
            f = open(filename, "w")
            data = reactionRulesEntry.get("1.0", 'end')
            f.write(data)
            f.close()

    def write_file():
        entry1 = reactionRulesEntry.get("1.0",END)

        with open(curr + "BIBM/rules_input.pcl", "w") as f:  # open file
            f.write(entry1)



        with open(curr + "BIBM/Output/model.pcl", "w") as f:  # open file
            f.write(entry1)


    input2 = Toplevel(root)
    input2.geometry("1024x700")
    input2.resizable(0, 0)

    closeButtonI1 = Button(input2, text="Close", command=input2.destroy)
    closeButtonI1.config(background='red', fg='white', font=('courier', 16, 'bold'))
    closeButtonI1.place(x=910, y=650)

    saveButtonI1 = Button(input2, text="Save", command=save_file)
    saveButtonI1.config(background='green', fg='white', font=('courier', 16, 'bold'))
    saveButtonI1.place(x=832, y=650)

    compileButtonI1 = Button(input2, text="Compile Model", command=write_file)
    compileButtonI1.config(background='blue', fg='white', font=('courier', 16, 'bold'))
    compileButtonI1.place(x=640, y=650)

    reactionRulesLabel = Label(input2, text="Model Rules")
    reactionRulesLabel.config(background='dark blue', fg='white', font=('courier', 16, 'bold'))
    reactionRulesLabel.place(x=10, y=10)

    scrollbar1 = Scrollbar(input2)
    scrollbar1.pack(side=RIGHT, fill=Y)
    reactionRulesEntry = Text(input2, yscrollcommand=scrollbar1.set)
    reactionRulesEntry.config(font=('Courier', 14, 'normal'), height=27, width=88, background='gray', undo = True, autoseparator = True, maxundo = -1)
    reactionRulesEntry.place(x=30, y=45)
    scrollbar1.config(command=reactionRulesEntry.yview)

    return reactionRulesEntry







#########################################################################################################



#############################################################################################

#Initialize
root = Tk()
#root.configure(weidth = 300, height = 300)
root.geometry("900x38")
root.resizable(0, 0)
root.title("ParCell")
root.configure(background = "bisque")

#############################################################################################
# ***** Main Menu *****

menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open File", command=openfile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit)

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About us", command=aboutUs)

setPath()

##############################################################################################

# ***** The Toolbar *****
toolbar = Frame(root, bg="gray")
modelGeneratorButton = Button(toolbar, text="Model Generator", command=input_2)
modelGeneratorButton.pack(side=LEFT, padx=4, pady=4)
modelGeneratorButton.config(background='blue', fg='white', font=('courier', 20, 'bold'))

runButton = Button(toolbar, text="Run", command=Run)
runButton.pack(side=LEFT, padx=4, pady=4)
runButton.config(background='green', fg='white', font=('courier', 20, 'bold'))

outputButton = Button(toolbar, text="Output", command=Output)
outputButton.pack(side=LEFT, padx=4, pady=4)
outputButton.config(background='blue', fg='white', font=('courier', 20, 'bold'))

analysisButton = Button(toolbar, text="Analysis", command=analysis)
analysisButton.pack(side=LEFT, padx=4, pady=4)
analysisButton.config(background='green', fg='white', font=('courier', 20, 'bold'))

clusterOutputButton = Button(toolbar, text="Cluster Output", command=cluster_output)
clusterOutputButton.pack(side=LEFT, padx=4, pady=4)
clusterOutputButton.config(background='blue', fg='white', font=('courier', 20, 'bold'))

toolbar.pack(side=TOP, fill=X)


#############################################################################################

###############################################################################################




root.mainloop()
