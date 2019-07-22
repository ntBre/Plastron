# plastron.py


def print_xyz(filename):

    infile = open(filename, 'r')
    for line in infile:
        print line[:-1]
    infile.close()


def write_xyz(filename):

    outfile = open(filename, 'w')
    outfile.close()


def main():
    
    print_xyz("./pyridine.xyz")

main()
