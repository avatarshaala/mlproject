from myutils.csvtrainingdatareader import read_training_data, read_target_weight
from myutils.perceptroninputformatter import append_bias_vector
from algorithms.perceptron import *

__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

'''The main program'''



def main():
	trainingfilename = "hw1-data/d-500.csv"
	weightsfilename = "hw1-data/A-500.csv"

	#read the instances and target output from training file
	instances,targets = read_training_data(trainingfilename)
	#convert targets to float
	targets = [float(x) for x in targets]
	#generate bias vector
	bias = generate_bias_vector(len(instances))
	#append biase term to each of the instances, hence dimension of an instance increase by 1
	instances = append_bias_vector(instances,bias)
	weights, message = train(instances,targets, 0.1,100, stop_after_convergence=True)
	targetweights = read_target_weight(weightsfilename)
	error = sse(weights, targetweights)
	print(error)
	print(message)


if __name__ == "__main__": main()