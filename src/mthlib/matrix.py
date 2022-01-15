# from array import array
#TODO: class is not generic. only works with int. Make class work with all numerical types
#TODO: add type annotations to every bit of this code
from numbers import Number
from random import randrange, randint, random


class Matrix(object):
    
    def __init__(self, rows: int, columns: int, fill_value: Number = 0):
        
        #error-check for size of matrix. Size must be integers
        if isinstance(rows, int) and isinstance(columns, int):
            self._rows = rows
            self._columns = columns
        else:
            raise TypeError("Matrix row and column length must be integers!")

        if isinstance(fill_value, Number):
            self._matrix = [[fill_value] * self._columns for _ in range(self._rows)]
        else:
            raise TypeError("Matrix elements must be of numeric type!")
       

    def __setitem__(self, idx: int, value: list):
        if isinstance(value, list) and isinstance(idx, int):
            self._matrix[idx] = value
        else:
            raise TypeError("A matrix object can only contain lists of numbers")
        return

    def __getitem__(self, idx: int):
        if isinstance(idx, int):
            return self._matrix[idx]
        else:
            raise TypeError("Matrix index must be an integer")


    def __repr__(self):
        '''Print the matrix row after row.'''
        prt = ""
        for row in self._matrix:
            prt += str(row)
            prt += "\n"
        return prt.rstrip()

    def __contains__(self, value: int):
        if isinstance(value, int):
            for row in self._matrix:
                for element in row:
                    if element == value:
                        return True
                    else:
                        pass
            return False
        else:
            raise TypeError("checking value must be numerical")

    def __add__(self, other: "Matrix") -> "Matrix":
        raise NotImplementedError

    def __mul__(self, other: "Matrix") -> "Matrix":
        raise NotImplementedError

    def __sub__(self, other: "Matrix") -> "Matrix":
        raise NotImplementedError

    def __div__(self, other: "Matrix") -> "Matrix":
        raise NotImplementedError


    # def identity(n):
    #     """
    #     Creates a n x n identity matrix.
    #     """
    #     I = zeroes(n, n)
    #     for i in range(n):
    #         I.g[i][i] = 1.0
    #     return I

    # @classmethod
    # def identity(cls, m):
    #     """ Make identity matrix of rank (mxm) """

    #     cls._matrix = [[0]*m for x in range(m)]
    #     idx = 0
        
    #     for row in rows:
    #         row[idx] = 1
    #         idx += 1

    #     return cls.fromList(rows)



    @classmethod
    def randomMat(cls,row_size, column_size, lower=0, upper=10):
        '''matrix with random elements of the same numerical type'''
        # if isinstance(row_size, int) and isinstance(column_size, int):
        newMatrix = Matrix(row_size, column_size)    
        for row in newMatrix:
            for i in range(newMatrix._columns):
                row[i] = randint(lower, upper)
        return newMatrix


if __name__ == "__main__":
        
    mat = Matrix(3, 3)
    # print(mat)
    print(mat[2][2])
    mat[2][2] = 34
    mat[0][0] = 20
    mat[0][1] = 10

    print(mat)
    mat1 = Matrix.randomMat(3, 3, 100, 200)
    print(mat1)