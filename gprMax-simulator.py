## gprMax Simulator

import os
from gprMax.gprMax import api
import matplotlib.pyplot as plt

from tools.outputfiles_merge import merge_files, get_output_data
from tools.plot_Bscan import get_output_data, mpl_plot

# Variables
filename = 'cylinder_Bscan_2D_01'

clear = lambda : os.system('clear')


def generate_Ascan_Bscan(filename):
    print("Start simulate A-Scan: ")
    path = 'processing'
    try:
        os.mkdir(path + '/01')
    except FileExistsError as error:
        pass
    else:
        print("Successfully created the directory %s" % path)
    input_filepath = os.path.join(path, filename + '.in')
    print(input_filepath)
    api(input_filepath, n = 60, geometry_only = False, mpi = 3, mpi_no_spawn = True, gpu = [0,1])
    merge_filepath = os.path.join(path, filename)
    merge_files(merge_filepath)

# Plot time-traces Radargramm
def plot_radargramm(filename):
    print("Plotting Radargramm")

    output_filepath = os.path.join('processing/01/', filename + '_merged.out')

    rxnumber = 1
    rxcomponent = 'Ez'
    outputdata, dt = get_output_data(filename = output_filepath, rxnumber = rxnumber, rxcomponent = rxcomponent)

    #plt = mpl_plot(filename = output_filepath, outputdata = outputdata, dt = dt, rxnumber = rxnumber, rxcomponent = rxcomponent)

    print(type(outputdata))
    save_filepath = os.path.join('processing/', filename + '.png')
    print(save_filepath)
    
    
    plt.imshow(outputdata, extent =[0,240,0,210], cmap = "Greys")   
    plt.axis('off')
    plt.savefig(save_filepath, bbox_inches = 'tight', pad_inches = 0)
    plt.show()

  



def main():

    clear()

    print("Greeting from Main-Method")

    generate_Ascan_Bscan(filename)
    
    #plot_radargramm(filename)


if __name__ == '__main__':
    main()