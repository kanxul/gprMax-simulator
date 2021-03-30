# Notizen: 
# durchschnittliche Ausbreitungsgeschwindigkeit 0,146 m/ns (Skalierung für die Tiefe der Radargramme aus gprSlice)


import os
from gprMax.gprMax import api
import matplotlib.pyplot as plt

from tools.outputfiles_merge import merge_files, get_output_data
from tools.plot_Bscan import get_output_data, mpl_plot

clear = lambda : os.system('clear')

def generate_Bscan(filepath, traces, mpi = True, gpu = True):
    """
    Funktion berechnet mit gprMax die Wellenausbreitung innerhalb des zurvor definierten Simulationsraumes
    zunächst als A-Scan und fügt diese an anschließend mit tools.outputfiles_merge zu einem File zusammen. 
    Bei der Berechnung der Simulation werden standardmäßig parallelisiert die GPUs verwendet. 
    Hier soll noch eine Abfrage geschrieben werden, die die Anzahl der Nodes (Recheneinheiten) auf dem Rechner abfragt. 
    (mpi4py)
    """
    input_filepath = filepath + '.in'
    command_line_Ascan = f"mpirun -np 10 python -m gprMax {input_filepath} -n {traces} --mpi-no-spawn -gpu 0 1"
    print("Start: " + command_line_Ascan)
    os.system(command_line_Ascan)
    
    command_line_Bscan = f"python -m tools.outputfiles_merge {filepath}"
    print("Start: " + command_line_Bscan)
    os.system(command_line_Bscan)

def generate_output_data(filepath, rxnumber, rxcomponent):
    
    output_filepath =  filepath + '_merged.out'
    outputdata, dt = get_output_data(filename = output_filepath, rxnumber = rxnumber, rxcomponent = rxcomponent)
    return outputdata, dt, output_filepath

def plot_radargram(filepath):
    print("Plotting Radargramm")

    rxnumber = 1
    rxcomponent = "Ez"
    outputdata, dt, output_filepath = generate_output_data(filepath = filepath, rxnumber = rxnumber, rxcomponent = rxcomponent)

    plt = mpl_plot(filename = output_filepath, outputdata = outputdata, dt = dt, rxnumber = rxnumber, rxcomponent = rxcomponent)
    plt.set_cmap('gray')
    plt.show()


def main():
    clear()

    filepath = 'processing/cylinder_Bscan_2D_01'
    #filepath = 'processing/cylinder_Bscan_GSSI_1500'

    generate_Bscan(filepath = filepath, traces=54)
      
    plot_radargram(filepath)
    
    #os.system('python -m tools.plot_Bscan {} Ez'.format(filepath + '_merged.out'))

if __name__ == '__main__':
    main()




