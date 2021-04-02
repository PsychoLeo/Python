import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

def lineplt (data) :
    pass

def scatterplt (data) :
    pass


if __name__ == '__main__' :
    mode = input('Plotting mode (plot, scatter, bar, barh, pie, histogram, stackplot) : ')
    while mode not in ['plot', 'scatter', 'bar', 'barh', 'pie', 'histogram', 'stackplot'] :
        print ('Invalid mode input')
        mode = input('Plotting mode (plot, scatter, bar, barh, pie, histogram, stackplot) : ')
    file = input ('Enter the path to the file /path/filename.extension : ')
    while not os.path.isfile (file) :
        print ('File does not exist')
        file = input('Enter the path to the file /path/filename.extension : ')
    data = pd.read_csv (file)
    if mode == 'line' :
        lineplt (data)
    #### code not finished at all ####