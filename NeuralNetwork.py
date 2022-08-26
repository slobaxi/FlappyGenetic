import math
import copy
import json
import random

from Matrix import Matrix


class ActivationFunction:
    def __init__(self, func, dFunc):
        self.func = func
        self.dFunc = dFunc


def sigmoid(e):
    return 1 / (1 + math.exp(-e))

def sigmoidDeriv(e):
    return e * (1 - e)

def tanh(e):
    return math.tanh(e)

def tanhDeriv(e):
    return 1 - (e * e)


class NeuralNetwork:
    def __init__(self, in_nodes, hidden_nodes, out_nodes):
        # Assign numbers to node layer count.
        self.input_nodes = in_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes= out_nodes

        # Create the needed variables.
        self.weights_ih = Matrix(self.hidden_nodes, self.input_nodes)
        self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes)
        self.weights_ih.randomize()
        self.weights_ho.randomize()

        self.bias_h = Matrix(self.hidden_nodes, 1)
        self.bias_o = Matrix(self.output_nodes, 1)
        self.bias_h.randomize()
        self.bias_o.randomize()

        # Set defaults
        self.setActivationFunction()

    def copy(self):
        return copy.deepcopy(self)

    def setActivationFunction(self, func = sigmoid, dFunc = sigmoidDeriv):
        self.activation_function = ActivationFunction(func, dFunc)
    
    def predict(self, input_array):
        inputs = Matrix.fromArray(input_array)
        
        hidden = Matrix.multiply(self.weights_ih, inputs) \
                .add(self.bias_h) \
                .map(self.activation_function.func)
    
        output = Matrix.multiply(self.weights_ho, hidden) \
                .add(self.bias_o) \
                .map(self.activation_function.func)

        return output.toArray()

    def mutate(self, func):
        self.weights_ih = self.weights_ih.map(func)
        self.weights_ho = self.weights_ho.map(func)
        self.bias_h = self.bias_h.map(func)
        self.bias_o = self.bias_o.map(func)

