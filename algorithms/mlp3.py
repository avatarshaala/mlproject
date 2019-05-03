from math import exp
from random import seed
from random import random
import math
import numpy as np
class mlp1:
    def __init__(self, architecture=None,bias=False, weights=None, biases=None):

        # architecture = [5, 7, 9, 3] #means 5 input units , 7 units in hidden layer, 9 units in hidden layer and 3 output units
        self.architecture = architecture
        self.layers = list();

        #weights are arrays of weight matrices of each layer
        for i in range(len(self.architecture)):
            # initialize all activations with zeros
            layer = {}
            if i > 0: #except input layer
                if weights is not None:
                    # i-1 because first layer is input layer and i = 0 is for input layer
                    # but weights are only for hidden layers and output layers and index of the weights arguments should start from 0
                    layer['weights'] = weights[i-1]
                else:#randomly generate the weights
                    layer['weights'] = np.random.rand(self.architecture[i], self.architecture[i - 1])
                if bias and biases is not None:
                    layer['biases'] = biases[i-1]
                elif biases: #generate random bias
                    layer['biases'] = np.random.rand(self.architecture[i])


            layer['activations'] = np.zeros(self.architecture[i], dtype=np.double) #initialize activations with zero
            self.layers.append(layer)


    def activation(self,input,function='SIG'):

        if function == 'SIG':
            return 1 / (1 + np.exp(-input))
        elif function == 'TANH':
            return np.tanh(input)

    def activate(self,input):

        for i in range(len(self.layers)):
            layer = self.layers[i]
            # print("Layer[{}]: ".format(i),layer)
            if i == 0:#input layer
                layer['activations'] = input
            else:#hidden layers
                #net vector is calculated by multiplying input vector with weight matrix
                W = self.layers[i]['weights']
                X = self.layers[i-1]['activations']
                ip = W.dot(X)
                b = layer['biases']
                net = ip + b
                # print(net)

                self.layers[i]['activations'] = self.activation(net,function='SIG')

        #update the outputs of network with calculated outputs above after activations of each layers
        self.outputs = self.layers[len(self.layers) - 1]['activations']

    def activation_derivative(self, x, function='SIG'):
        if function == 'SIG':
            output = 1/(1 + np.exp(-x))
            return output*(1-output)
        elif function == 'TANH':
            return (1-(np.tanh(x))**2) #derivative of tanh(X) = 1- tanh^2(x)

    def cost_derivative(self,output, target, function='SSE'):
        if function == 'SSE':
            return target - output
        elif function == "CROSS_ENTROPY":
            return (output - target)/(output - output**2)



    def back_propagate(self,target):
        # backward pass from output layer all the way to first hidden layer omitting input layer;
        # range starts from 1
        for i in reversed(range(1,len(self.layers))):

            layer = self.layers[i]

            layer_ip = layer['weights'].dot(self.layers[i-1]['activations']) + layer['biases'] #net of each neuron in a layer
            f_prime = self.activation_derivative(layer_ip, function="SIG")#derivative of activation function

            if i == len(self.layers) - 1:#for output layer
                # operr = target - layer['activations']
                cost_prime = self.cost_derivative(layer['activations'],target, function='SSE')#target - layer['activations'] in case of SSE
                layer['deltas'] = cost_prime * f_prime

            else: #other layers
                layer['deltas'] = (self.layers[i + 1]['weights'].T).dot( self.layers[i + 1]['deltas']) * f_prime

            #print for diagnostic purpose
            self.print_layer(layer,i)


    #this function is for diagnostic purpose
    def print_layer(self, layer, id):
        print("======Layer: {} ===========".format(id))
        #print weights
        print("---weights---")
        print(layer['weights'])
        #print bias
        print("---bias---")
        print(layer["biases"])
        #print activations
        print("---activations---")
        print(layer["activations"])
        #print deltas
        print("---deltas---")
        print(layer['deltas'])


    def update_weights(self,eta):
        # update the weight
        # we know, dE/dw = neuron delta * neuron inputs
        # = neuron delta * neuron activations of previous layers neurons
        for i in range(len(self.layers)):
            if i != 0:  # only for hidden layers (not for input layer)
                deltas = self.layers[i]['deltas']

                activations = self.layers[i - 1]['activations']

                # since deltas and activations are vectors,
                # convert activations to row matrix and deltas to column matrix and get matrix product
                # the reshaping is needed becauses the weights matrix is a 2D matrix and numpy can multiply 2d matrices to get 2d matrices
                self.layers[i]['weights'] += eta * (deltas.reshape(len(deltas), 1)).dot(
                    activations.reshape(1, len(activations)))
                self.layers[i]['biases'] += eta * deltas

    def update_inputs(self, eta):

        for i in range(len(self.layers)):
            if i != 0: #only for hidden layers (not for input layer)
                layer = self.layers[i]
                activations = layer['activations']
                self.layers[i-1]['activations'] += eta * ((self.layers[i]['weights'].T).dot(self.layers[i]['weights']))

    #fit the model with training data
    def fit(self, data, epoch=100,eta=0.05):
        n_outputs = self.architecture[len(self.layers)-1]
        for itr in range(epoch):
            print("++++++++++++++++++++EPOCH++++++++++++++++++++++++++++")
            sum_error = 0
            for row in data:
                #separate input and targets from data set

                input = row[:-1]

                #******* feed forward *******#
                self.activate(input)
                outputs = self.outputs
                #*******************#

                target = [0 for i in range(n_outputs)]
                target[row[-1].astype(np.int)] = 1
                sum_error += np.sum([(target[i] - outputs[i]) ** 2 for i in range(len(target))])
                print("------------------------row----------------------------")
                self.back_propagate(target)
                self.update_weights(eta)
            # print('>epoch=%d, lrate=%.3f, error=%.3f' % (itr, eta, sum_error))



#====================== following are the codes to verify the correctness of implementation ========================
def do_unit_test():

    '''
    values produced should be as follows
    [layer 1:
        [ 0.2000195  -0.09995451]
        [ 0.29996771 -0.30007534]
    biases:
        [ 0.10006499 -0.20010763]
    activations:
        [ 0.52248482  0.42067575]
    ]
    [layer 2:
        [-0.20019727 -0.30015883]
        [-0.10096643  0.29922188]
    biases:
        [ 0.09962244  0.19815031]
    activations:
        [ 0.46737151  0.56806341]
    ]
    [layer 3:
        [-0.10546661  0.29335565]
        [-0.19372243 -0.29236997]
    biases:
        [ 0.18830351  0.11343165]

    activations:
        [ 0.58022129  0.45911814]

    ]
    '''
    weights = np.array([
        [
            [0.2, -0.1],
            [0.3, -0.3]
        ],  # first hidden layer
        [
            [-0.2, -0.3],
            [-0.1, 0.3]
        ],  # second hidden layer
        [
            [-0.1, 0.3],
            [-0.2, -0.3]
        ]  # third hidden layer (output layer)
    ])

    biases = np.array([[0.1, -0.2],
                       [0.1, 0.2],
                       [0.2, 0.1]])

    architecture = [2, 2, 2, 2]  # means 2 input units , 2 units in hidden layer, 2 units in hidden layer and 2 output units
    network = mlp1(architecture=architecture, bias=True, weights=weights, biases=biases)
    input = np.array([0.3,0.7])
    target = np.array([0.1,1.0])
    #feed forward
    network.activate(input)
    #back propagate
    network.back_propagate(target)
    network.update_weights(0.1)#0.1 is learning rate

    print("======================== AFTER UPDATE =======================")
    network.print_layer(network.layers[1],1) # starts from 1 because 0 is the input layer (input units)
    network.print_layer(network.layers[2],2)
    network.print_layer(network.layers[3],3)

def training_example():
    # Test training backprop algorithm
    seed(1)
    dataset = np.array([[2.7810836, 2.550537003, 0],
               [1.465489372, 2.362125076, 0],
               [3.396561688, 4.400293529, 0],
               [1.38807019, 1.850220317, 0],
               [3.06407232, 3.005305973, 0],
               [7.627531214, 2.759262235, 1],
               [5.332441248, 2.088626775, 1],
               [6.922596716, 1.77106367, 1],
               [8.675418651, -0.242068655, 1],
               [7.673756466, 3.508563011, 1]])



    weights = np.array([
        [
            [0.13436424411240122, 0.8474337369372327],
            [0.2550690257394217, 0.49543508709194095]
        ],
        [
            [0.651592972722763, 0.7887233511355132],
            [0.02834747652200631, 0.8357651039198697]
        ]
    ])
    biases = np.array([[0.763774618976614,0.4494910647887381],
                       [0.0938595867742349,0.43276706790505337]])

    architecture=[2,2,2]#means 2 input units , 2 units in hidden layer,  and 2 output units


    network = mlp1(architecture=architecture,bias=True,weights=weights,biases=biases)
    network.fit(dataset, epoch=20,eta=0.5)




if __name__ == "__main__":
    training_example()
    # do_unit_test()

