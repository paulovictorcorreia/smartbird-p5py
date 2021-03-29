import numpy as np
from numba import njit, vectorize, float64, jit

@vectorize([float64(float64)])
def sigmoid(x):
    return 1/(1+np.exp(-x))

# @vectorize([float64(float64)])
@njit
def dsigmoid(x):
    return x * (1 - x)

# @vectorize([float64(float64)])
@njit
def tanh(x):
    return np.tanh(x)

@vectorize([float64(float64)])
def dtanh(x):
    return 1 / np.cosh(x) / np.cosh(x)

@vectorize([float64(float64)])
def relu(x):
    return x * (x > 0)

@vectorize([float64(float64)])
def drelu(x):
    return 1. * (x > 0)

@njit
def mutate_matrix(array, mutation_rate):
    for i in range(array.size):
        row_idx = int(i / array.shape[1])
        col_idx = i % array.shape[1]
        rand = np.random.random()
        rand_val = np.random.normal()*0.5
        if rand <= mutation_rate:
            array[row_idx, col_idx] += rand_val

@njit
def mutate_array(array, mutation_rate):
    for i in range(array.size):
        rand = np.random.random()
        rand_val = np.random.normal()*0.5
        if rand <= mutation_rate:
            array[i] += rand_val


class NeuralNetwork:
    def __init__(self, inputLayer=2, hiddenLayer=2, outputLayer=1):
        self.inputLayer = inputLayer
        self.hiddenLayer = hiddenLayer
        self.outputLayer = outputLayer
        self.weights_ih = np.random.random(size=(hiddenLayer, inputLayer))
        self.weights_ho = np.random.random(size=(outputLayer, hiddenLayer))
        self.bias_h = np.random.random(size=(hiddenLayer))
        self.bias_o = np.random.random(size=(outputLayer))

        self.activation = sigmoid
        self.dactivation = dsigmoid

    def feedforward(self, input):
        #Generating the hidden outputs
        hidden = np.matmul(self.weights_ih, input)
        hidden += self.bias_h
        #Activation function
        hidden = self.activation(hidden)
        
        #Generating the outputs on last layer
        output = np.matmul(self.weights_ho, hidden)
        output += self.bias_o
        output = self.activation(output)

        #Sending back to the caller
        return output
    
    # @jit
    def mutate(self, mutationRate):
        mutate_matrix(self.weights_ho, mutationRate)
        mutate_matrix(self.weights_ih, mutationRate)
        mutate_array(self.bias_h, mutationRate)
        mutate_array(self.bias_o, mutationRate)
    
    
    def copy(self):
        return NeuralNetwork(self.inputLayer, self.hiddenLayer, self.outputLayer)


