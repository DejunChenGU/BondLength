import numpy
import sys

def calculate_distance(atom1, atom2):
    bond_length = numpy.sqrt((atom1[0]-atom2[0])**2 + (atom1[1]-atom2[1])**2 + (atom1[2]-atom2[2])**2)
    
    return bond_length

def bond_check(distance, minimum=0, maximum=1.5):
    if distance > minimum and distance <= maximum:
        return True
    else: 
        return False

def print_bond(atom_symbol, atom_coord):
    for i, atomA in enumerate(atom_coord):
        for j, atomB in enumerate(atom_coord):
            if j>i: 
                bond_length_AB = calculate_distance(atomA, atomB)
                if bond_check(bond_length_AB):
                    print(F'{atom_symbol[i]} to {atom_symbol[j]} is {bond_length_AB}')
                else:
                    print(F'{atom_symbol[i]} to {atom_symbol[j]} is {bond_length_AB} --> not bonded')
            if j==i:
                print(F'{atom_symbol[i]} to {atom_symbol[j]} is the same atom')
            if j<i:
                print(F'{atom_symbol[i]} to {atom_symbol[j]}  is evaluated')
                          
def open_xyz(filename):
    xyz_file = numpy.genfromtxt(fname=filename, skip_header=2, dtype='unicode')
    symbols = xyz_file[:,0]
    coord = xyz_file[:,1:]
    coord = coord.astype(numpy.float)
    return symbols, coord


if __name__ == "__main__": 
    if len(sys.argv) != 2:
        print('Incorrect Input, Try Again')
        exit()
        
    file_location = sys.argv[1]
    
    symbols, coord = open_xyz(file_location)
    print_bond(symbols, coord)