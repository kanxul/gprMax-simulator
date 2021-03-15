## gprMax Simulator

import os
from gprMax.gprMax import api
import matplotlib.pyplot as plt

from tools.outputfiles_merge import merge_files, get_output_data
from tools.plot_Bscan import get_output_data, mpl_plot

import inspect

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

# Plot time-traces  Radargramm
def plot_radargramm(filename):

    output_filepath = os.path.join('processing/', filename + '_merged.out')

    rxnumber = 1
    rxcomponent = 'Ez'
    outputdata, dt = get_output_data(filename = output_filepath, rxnumber = rxnumber, rxcomponent = rxcomponent)


    plt = mpl_plot(filename = output_filepath, outputdata = outputdata, dt = dt, rxnumber = rxnumber, rxcomponent = rxcomponent)
    plt.show()


def main():

    clear()

    print("Greeting from Main-Method")

    inspect_methods()

    generate_Ascan_Bscan(filename)
    
    plot_radargramm(filename)



if __name__ == '__main__':
    main()