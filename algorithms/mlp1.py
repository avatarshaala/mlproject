from math import exp
from random import seed
from random import random

class mlp1:
    def __init__(self, layers=None):

        # layers = [5, 7, 9, 3] means 5 input units , 7 units in hidden layer, 9 units in hidden layer and 3 output units
        self.layers = layers
        self.network = list()


        for i in range(len(self.layers)):
            layer = None;
            if i >0: #except input layer
                layer = [{'weights': [random() for i in range(self.layers[i-1])]} for i in range(self.layers[i])]

            self.network.append(layer)

        #     hidden_layer = [{'weights': [random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
        #     print("H_layer: ", hidden_layer)
        #     network.append(hidden_layer)
        #     output_layer = [{'weights': [random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
        #     print("OP_layer: ", output_layer)
        #     network.append(output_layer)
        #     return network
        # pass

    def initialize(self,layers=None):
        pass

    def train(self):

        for i in range(self.layers):

