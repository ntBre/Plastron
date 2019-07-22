# plastron.py
import numpy as np

def print_xyz(filename):
    """ Prints the contents of a file """

    infile = open(filename, 'r')
    for line in infile:
        print line[:-1]
    infile.close()


def read_xyz(filename):
    """ Reads the contents of an .xyz file and returns a tuple of the number of
        the number of atoms, the comment line, a list of the atoms, and a numpy
        array of the atomic coordinates """

    atoms = []
    coords = []
    infile = open(filename, 'r')
    num_atoms = int(infile.readline())
    comment = infile.readline()
    for line in infile:
        split = line.split()
        atoms.append(split[0])
        coords.append(map(float, split[1:]))
    infile.close()
    return num_atoms, comment, atoms, np.array(coords)


def write_xyz(filename, num_atoms, comment, atoms, coords):
    """ Writes an .xyz file using the passed arguments """

    coords = coords.tolist()
    new_file = "new-" + filename
    outfile = open(new_file, 'w')
    outfile.writelines(str(num_atoms) + '\n' + comment)
    for atom in range(len(atoms)):
        atom_coord = '\t'.join(map(str, coords[atom]))
        outfile.writelines(str(atoms[atom]) + '\t' +
                     atom_coord + '\n')
    outfile.close()


def move_atoms(coord_array):
    """ Takes a numpy array of atomic coordinates as an argument and returns
        an updated array after moving the atoms """

    return coord_array


def main():
    
    write_xyz("pyridine.xyz", *read_xyz("pyridine.xyz")) # * explodes tuple


main()

