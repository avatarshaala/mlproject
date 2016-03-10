__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''


def read_training_data(filename):
	file = open(filename,"r")
	cnt = 0
	instances = []
	target_outputs = []
	for line in file.readlines():
		if cnt == 0:
			cnt += 1
			continue
		input = line.strip().split(",")
		instance = input[0:len(input)-1]
		target_output = input[-1]
		instances.append([float(x) for x in instance])
		#target_outputs.append(int(target_output))
		target_outputs.append(target_output)
	file.close()
	return instances,target_outputs


def read_target_weight(filename):
	file = open(filename,"r")
	weights = []
	for line in file.readlines():
		input = line.strip().split(",")
		weights += [float(x) for x in input]
	file.close()
	return weights