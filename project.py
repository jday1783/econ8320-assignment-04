#si-matrix

import pdb

""" 

This class is intended to create a way to store the values and shape of a 
matrix. The matrix can be imported as a list (matrix with single column, 
or vector), or as a list of lists (2-dimensional matrices) via the value argument. 
The class includes
an __init__ function to read in the matrix, or create a matrix of 1's of a 
specific dimensionality. The class also includes a __repr__ function to 
designate the method for printing the matrix to screen.

"""

class Matrix(object):
    """ 
    Read the matrix and store as part of the class object
    """
    def __init__(self, value=[], dim=(1, 1)):
        if isinstance(value, list):
            if len(value) > 0:
                if isinstance(value, (int, float)):
                    row = (int, float)
                else:
                    row = type(value)

                for i in value:
                    if not isinstance(i, (int, float, list)):
                        raise RuntimeError("Matrix is invalid. Please ensure that all elements share a type.")

                if row == list:
                    lenInner = len(value)
                    for i in value:
                        if len(i)!= lenInner:
                            raise RuntimeError("Matrix is invalid. Please ensure that all rows have uniform length.")
                    self.value = value
                    try:
                        self.shape = (len(value), len(value))
                    except:
                        self.shape = (len(value), 1)
                else:
                    self.value = value
                    self.shape = (len(value), 1)
            else:
                matrix = ()
                for i in range(dim):
                        row = ()
                        for j in range(dim):
                            row.append(1)
                        matrix.append(row)
                                
                value = matrix
                shape = dim
    
    def __repr__(self):
        string = " "
        for i in range(self.shape):
            if self.shape > 1: 
                if i < self.shape - 1:
                    string += "[ "
                for j in range(self.shape):
                    string += str(self.value[i][j]) + " "
                string += "]\n"
            else:
                string += "["
                for j in range(self.shape):
                    string += str(self.value[i][j]) + " "
                string += "]\n\n"
        return string
