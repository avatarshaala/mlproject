from math import exp
from random import seed
from random import random

class mlp1:
    def __init__(self, layers=None):



        self.network = list()

        for i in range(len(layers)):
            layer = None;
            if i >0: #except input layer
                layer = [{'weights': [random() for i in range(layers[i-1])]} for i in range(layers[i])]
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