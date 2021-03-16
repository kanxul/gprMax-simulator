## gprMax Simulator

import os
from gprMax.gprMax import api
import matplotlib.pyplot as plt

from tools.outputfiles_merge import merge_files, get_output_data
from tools.plot_Bscan import get_output_data, mpl_plot

import inspect

from PIL import Image

# Variables
filename = 'cylinder_Bscan_2D'

clear = lambda : os.system('clear')

def inspect_methods():
    print(inspect.getargspec(merge_files))
    print(inspect.getargspec(api))
    print(inspect.getargspec(get_output_data))
    print(inspect.getargspec(mpl_plot))

def generate_Ascan_Bscan(filename):
    input_filepath = os.path.join('processing/', filename + '.in')
    api(input_filepath, n = 60, geometry_only = False)
    merge_filepath = os.path.join('processing/', filename)
    merge_files(merge_filepath)

# Plot time-traces Radargramm
def plot_radargramm(filename):
    print("Plotting Radargramm")

    output_filepath = os.path.join('processing/', filename + '_merged.out')

    rxnumber = 1
    rxcomponent = 'Ez'
    outputdata, dt = get_output_data(filename = output_filepath, rxnumber = rxnumber, rxcomponent = rxcomponent)

    #plt = mpl_plot(filename = output_filepath, outputdata = outputdata, dt = dt, rxnumber = rxnumber, rxcomponent = rxcomponent)
    #print(plt.savefig("test.png"))

    print(outputdata)
    save_filepath = os.path.join('processing/', filename + '.png')
    print(save_filepath)
    im = plt.imsave(save_filepath, outputdata, cmap = "seismic")

    img = Image.open(save_filepath)
    img.resize((240,210), Image.ANTIALIAS)
    img.save("resized.png")

    



def main():

    clear()

    print("Greeting from Main-Method")

    #inspect_methods()

    #generate_Ascan_Bscan(filename)
    
    plot_radargramm(filename)


if __name__ == '__main__':
    main()