import os

def createInputfile():
    file = open("processing/test.in", "w")
    file.write('#title: B-scan from a metal cylinder buried in a dielectric half-space \n')
    file.writelines(["#test \n", "#test2 \n", "#test3 \n"])
    file.close()

def openInputfile(file):
    file = open(file, "r+")
    return file.read()


def main():
    #filepath = 'processing/cylinder_Bscan_2D_01.in'
    #os.system('mpirun -n 3 python -m gprMax {} -n 60 --mpi-no-spawn -gpu 0 1'.format(filepath))

    createInputfile()
    print(openInputfile("processing/test.in"))


if __name__ == '__main__':
    main()




