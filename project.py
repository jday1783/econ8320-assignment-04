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
                matrix = []
                for i in range(dim): 
                    row = []
                    for j in range(dim): 
                        row.append(1)
                    matrix.append(row)

                self.value = matrix
                self.shape = dim
    
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

    
   