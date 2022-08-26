import numpy as np
import random
import copy


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = np.zeros((rows, cols))

    def copy(self):
        matrix = copy.deepcopy(self)
        return matrix

    def toArray(self):
        lst = list(self.matrix)
        for count in range(0, len(lst)):
            lst[count] = list(lst[count])
        return lst

    def add(self, a):
        if isinstance(a, int) or isinstance(a, float):
            mObj = self.copy()
            for y in range(0, self.rows):
                for x in range(0, self.cols):
                    mObj.matrix[y][x] += a
        else:
            matrix = np.add(self.matrix, a.matrix)
            mObj = Matrix(self.rows, self.cols)
            mObj.matrix = matrix
        return mObj

    def randomize(self):
        for y in range(0, self.rows):
            for x in range(0, self.cols):
                self.matrix[y][x] = (random.random() * 2) - 1

    def printMatrix(self):
        print(self.matrix)

    def multiplySelf(self, nM):   
        if isinstance(nM, float) or isinstance(nM, int):
            matrix = np.multiply(nM, self.matrix)
        else:
            try:
                matrix = np.multiply(self.matrix, nM.matrix)
            except:
                matrix = self.matrix @ nM.matrix
        shape = matrix.shape
        rows = shape[0]
        try:
            cols = shape[1]
        except IndexError:
            cols = 1
        mObj = Matrix(rows, cols)
        mObj.matrix = matrix
        return mObj


    def map(self, func):
        matrix = self.copy()
        for y in range(0, self.rows):
            for x in range(0, self.cols):
                val = matrix.matrix[y][x]
                matrix.matrix[y][x] = func(val)

        return matrix

    @staticmethod
    def fromArray(data):
        rows = len(data)
        try:
            cols = len(data[0])
        except TypeError:
            cols = 1
            lst = []
            for i in data:
                lst.append([i])
            data = lst
        mObj = Matrix(rows, cols)
        mObj.matrix = np.array(data)
        return mObj

    @staticmethod
    def multiply(nO, nM):
        matrix = np.dot(nO.matrix, nM.matrix)
        shape = matrix.shape
        rows = shape[0]
        try:
            cols = shape[1]
        except IndexError:
            cols = 1
        mObj = Matrix(rows, cols)
        mObj.matrix = matrix
        return mObj

    @staticmethod
    def mapMF(matrix, func):
        return matrix.map(func)

    @staticmethod
    def subtractMatrices(a, b):
        matrix = np.subtract(a.matrix, b.matrix)
        rows = np.size(matrix)
        cols = np.size(matrix, 1)
        mObj = Matrix(rows, cols)
        mObj.matrix = matrix
        return mObj

    @staticmethod
    def addMatrices(a, b):
        matrix = np.add(a.matrix, b.matrix)
        rows = np.size(matrix)
        cols = np.size(matrix, 1)
        mObj = Matrix(rows, cols)
        mObj.matrix = matrix
        return mObj

    @staticmethod
    def transposeMatrix(n):
        matrix = np.transpose(n.matrix)
        rows = n.cols
        cols = n.rows
        mObj = Matrix(rows, cols)
        mObj.matrix = matrix
        return mObj    