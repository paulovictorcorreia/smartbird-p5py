import torch
import torch.nn as nn
import numpy as np


class NeuralNetworkTorch(nn.Module):
  def __init__(self, inputLayer=2, hiddenLayer=2, outputLayer=1,):
    super(NeuralNetworkTorch, self).__init__()
    
    self.inputLayer = inputLayer
    self.hiddenLayer = hiddenLayer
    self.outputLayer = outputLayer


    self.relu = nn.ReLU(inplace=True)
    self.out_activation = nn.ReLU()
    self.linear1 = nn.Linear(inputLayer, hiddenLayer)
    self.output = nn.Linear(hiddenLayer, outputLayer)


  def forward(self, x):
    x = torch.tensor(x)
    x = self.relu(self.linear1(x))
    x = self.out_activation(self.output(x))
    # print(self.linear1.weight)
    return x

  def mutate(self, mutationRate):
    for i, weights in enumerate(self.linear1.weight):
      for j, weight in enumerate(weights):
        ratio = np.random.random()
        if ratio < mutationRate:
          self.linear1.weight[i, j] += np.random.normal(0, 0.1)
    
    for i, weights in enumerate(self.output.weight):
      for j, weight in enumerate(weights):
        ratio = np.random.random()
        if ratio < mutationRate:
          self.output.weight[i, j] += np.random.normal(0, 0.15)
        
  def copy(self):
    return NeuralNetworkTorch(self.inputLayer, self.hiddenLayer, self.outputLayer)