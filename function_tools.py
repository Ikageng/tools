"""
@Created: 12/06/2019
@Project: Eskom Training
@Version: 1.0.2v
@Author: Ikageng Mokwena
@Revised: 
@Description: 
"""
import tkinter
from tkinter import filedialog

def select_files():
    '''
    Opens a dialogue box to select files.
    Returns list of files names with the directory
    '''
    root = tkinter.Tk()
    root.withdraw()
    
    return filedialog.askopenfilenames(parent=root)

def select_file():
    '''
    Opens a dialogue box to select a file.
    Returns a file names with the directory
    '''
    root = tkinter.Tk()
    root.withdraw()
    
    return filedialog.askopenfilename(parent=root)
