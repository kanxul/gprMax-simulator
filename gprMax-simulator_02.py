import os
from gprMax.gprMax import api
import matplotlib.pyplot as plt

from tools.outputfiles_merge import merge_files, get_output_data
from tools.plot_Bscan import get_output_data, mpl_plot

def generate_Bscan(filepath, traces):
    os.system('mpirun -n 10 python -m gprMax {} -n {} --mpi-no-spawn -gpu 0 1'.format(filepath + '.in', traces))


def plot_radargram(filepath):
    print("Plotting Radargramm")

    output_filepath =  filepath + '_merged.out'

    rxnumber = 1
    rxcomponent = 'Ez'
    outputdata, dt = get_output_data(filename = output_filepath, rxnumber = rxnumber, rxcomponent = rxcomponent)

    plt = mpl_plot(filename = output_filepath, outputdata = outputdata, dt = dt, rxnumber = rxnumber, rxcomponent = rxcomponent)
    plt.set_cmap('gray')
    plt.show()


def main():
    filepath = 'processing/cylinder_Bscan_2D_02'
    os.system('mpirun -n 10 python -m gprMax {} -n 149 --mpi-no-spawn -gpu 0 1'.format(filepath + '.in'))
    
    os.system('python -m tools.outputfiles_merge {}'.format(filepath))
    
    plot_radargram(filepath)
    
    #os.system('python -m tools.plot_Bscan {} Ez'.format(filepath + '_merged.out'))

if __name__ == '__main__':
    main()




