import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
def dsigmoid(x):
    return x * (1 - x)
class NeuralNetwork:
    def __init__(self, inputLayer=2, hiddenLayer=2, outputLayer=1, learningRate=0.0001, epochs=100):
        self.inputLayer = inputLayer
        self.hiddenLayer = hiddenLayer
        self.outputLayer = outputLayer
        self.weights_ih = np.random.random((hiddenLayer, inputLayer)) * 2 - 1
        self.weights_ho = np.random.random((outputLayer, hiddenLayer)) * 2 - 1
        
        self.bias_h = np.random.random((hiddenLayer)) * 2 - 1
        self.bias_o = np.random.random((outputLayer)) * 2 - 1

        self.learningRate = learningRate
        self.epochs = epochs
    def feedforward(self, input):
        #Generating the hidden outputs
        hidden = self.weights_ih @ input
        hidden += self.bias_h
        #Activation function
        hidden = sigmoid(hidden)
        
        #Generating the outputs on last layer
        output = self.weights_ho @ hidden
        output += self.bias_o
        output = sigmoid(output)

        #Sending back to the caller
        return output
    
    def train(self, inputs, targets):
         #Generating the hidden outputs
        hidden = self.weights_ih @ inputs
        hidden += self.bias_h
        #Activation function
        hidden = sigmoid(hidden)
        
        #Generating the outputs on last layer
        outputs = self.weights_ho @ hidden
        outputs += self.bias_o
        outputs = sigmoid(outputs)

        #Calculate the error
        output_errors = targets - outputs
        
        #Calculate hidden gradient
        gradients = dsigmoid(outputs)
        gradients = gradients @ output_errors
        gradients *= self.learningRate
        #print(hidden)
        #Updating hidden to output weights
        weights_ho_deltas = hidden * gradients
        #print(hidden)
        self.weights_ho += weights_ho_deltas
        self.bias_o += gradients

        #calculating hidden errors
        who_t = self.weights_ho.transpose()
        hidden_errors = who_t @ output_errors


        #Calculating Hidden Gradient
        hidden_gradient = dsigmoid(hidden)
        hidden_gradient = hidden_gradient * hidden_errors
        hidden_gradient *= self.learningRate

        #Updating input to hidden weights
        inputs_T = inputs.reshape(1, self.inputLayer)
        hidden_gradient_aux = hidden_gradient.reshape(self.hiddenLayer, 1)
        weights_ih_deltas = hidden_gradient_aux @ inputs_T
        self.weights_ih += weights_ih_deltas
        self.bias_h += hidden_gradient
    def fit(self, X, y):
        for _ in range(self.epochs):
            for i, value in enumerate(X):
                self.train(value, y[i])        
        return self
    def predict(self, X):
        output_list = []
        inputSize = X.shape[0]
        for i in range(inputSize):
            output = self.feedforward(X[i])
            output_list.append(output)
        output_array = np.array(output_list)
        return output_array

    def mutate(self, mutationRate):
        ratio = np.random.random()
        weights_ho_reshaped = self.weights_ho.flatten()
        for i, weight in enumerate(weights_ho_reshaped):
            if ratio < mutationRate:
                weights_ho_reshaped[i] += np.random.normal(loc=0, scale=0.1)
        self.weights_ho = weights_ho_reshaped.reshape((self.outputLayer, self.hiddenLayer))

        weights_ih_reshaped = self.weights_ih.flatten()
        for i, weight in enumerate(self.weights_ih):
            if ratio < mutationRate:
                weights_ih_reshaped += np.random.normal(loc=0, scale=0.1)
        self.weights_ih = weights_ih_reshaped.reshape((self.hiddenLayer, self.inputLayer))

        for i, weight in enumerate(self.bias_h):
            if ratio < mutationRate:
                self.bias_h[i] += np.random.normal(loc=0, scale=0.1)

        for i, weight in enumerate(self.bias_o):
            if ratio < mutationRate:
                self.bias_o[i] += np.random.normal(loc=0, scale=0.1)
                
