import os
import numpy as np


def read_hair(filename):
    with open("../data/00001.txt", "r") as f:
        num_strands = f.readline()
        ret = []
        num_vertices = f.readline()
        count = 0
        while num_vertices:
            for i in range(int(num_vertices)):
                ret.append(f.readline().split(" "))
                count += 1
            num_vertices = f.readline()
    return np.array(ret, dtype=float)

def write_ply(fname, S):
    nV = S.shape[0]
    f = open(fname,'w')
    f.write('ply\n')
    f.write('format ascii 1.0\n')
    f.write('element vertex ' + str(nV) + '\n')
    f.write('property float x\n')
    f.write('property float y\n')
    f.write('property float z\n')
    f.write('property uchar red\n')
    f.write('property uchar green\n')
    f.write('property uchar blue\n')
    f.write('property list uchar int vertex_indices\n')
    f.write('end_header\n')
    for i in range(0,nV):
        f.write('%0.4f %0.4f %0.4f %d %d %d\n' % (S[i,0],S[i,1],S[i,2],225,225,125))

    f.close()
    return

def write_obj(fname, S):
    nV = S.shape[0]
    f = open(fname, 'w')
    for i in range(0, nV):
        f.write('v %0.4f %0.4f %0.4f\n' % (S[i,0],S[i,1],S[i,2]))
        # f.write('%0.4f %0.4f %0.4f %d %d %d\n' % (S[i,0],S[i,1],S[i,2],225,225,125))
    f.close()
    return

if __name__ == "__main__":
    ret = read_hair("../data/00001.txt")
    write_obj("../data/00001.obj", ret)
