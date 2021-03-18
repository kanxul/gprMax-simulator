import os
from gprMax.gprMax import api
import matplotlib.pyplot as plt

from tools.outputfiles_merge import merge_files, get_output_data
from tools.plot_Bscan import get_output_data, mpl_plot

clear = lambda : os.system('clear')

def create_working_foldes(path):
    for root , dirs , files in os.walk(path, topdown=False):
        print("A", root, dirs, files)
    for file in files:
        try:
            path = os.path.join(root, file.removesuffix('.in'))
            os.mkdir(path)
            source = os.path.join(root, file)
            target = path
            os.system('cp {0} {1}'.format(source, target))
        except OSError as error:
            pass
    path = os.path.join(root, 'images')
    os.mkdir(path)

def read_inputfiles(path):
    for root , dirs , files in os.walk(path, topdown=False):
        pass
    return root, dirs, files
    
def generate_Ascan_Bscan(path):
    print("Start simulate A-Scan: ")
    api(path, n = 60, geometry_only = False)
    merge_file = path.removesuffix('.in')    
    merge_files(merge_file)


def plot_radargramm(path):
    print("Plotting Radargramm")
    merged_file = path.removesuffix('.in') + '_merged.out'
    print(merged_file)
    rxnumber = 1
    rxcomponent = 'Ez'
    outputdata, dt = get_output_data(filename = merged_file, rxnumber = rxnumber, rxcomponent = rxcomponent)

    #plt = mpl_plot(filename = output_filepath, outputdata = outputdata, dt = dt, rxnumber = rxnumber, rxcomponent = rxcomponent)

    plt.imshow(outputdata, extent =[0,240,0,210], cmap = "Greys")   
    plt.axis('off')
    
    plt.savefig(path.removesuffix('.in') + '.png', bbox_inches = 'tight', pad_inches = 0)
    #plt.show()




def main():
    clear()
    path = 'processing'

    create_working_foldes(path)
    root, dirs, files = read_inputfiles(path)
    for file in files:
        input_path = os.path.join(root, file.removesuffix('.in'), file)
        generate_Ascan_Bscan(input_path)    
        plot_radargramm(input_path)



if __name__ == '__main__':
    main()