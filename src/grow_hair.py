import pymesh
import os
import numpy as np
import struct

def read_from_data(filename):
    with open(filename, mode='rb') as file:
        filecontent = file.read()
        print(filecontent[20:24])
        # body = struct.unpack("h", filecontent[20:24])

    return body

if __name__ == "__main__":
    body = read_from_data('../data/hairstyles/strands00001.data')
    print(body)
