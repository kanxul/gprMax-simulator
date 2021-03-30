import pycuda.driver as drv

from mpi4py import MPI

drv.init()

print("Detected {} CUDA Capable device(s)".format(drv.Device.count()))

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

print(comm)
print(size)
print(rank)