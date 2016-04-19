__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''


def read_csv_file(filename, hasheader=True):
    file = open(filename, "r")
    cnt = 0
    instances = []
    # target_outputs = []
    headers = []
    for line in file.readlines():
        if hasheader and cnt == 0:  # extract headers
            headers = line.strip().split(",")
            cnt += 1
            continue
        input = line.strip().split(",")
        instance = input[0:len(input)]
        instances.append([x for x in instance])
    file.close()
    if hasheader:
        return headers, instances
    else:
        return instances


def read_training_data(filename):
    file = open(filename, "r")
    cnt = 0
    instances = []
    target_outputs = []
    for line in file.readlines():
        if cnt == 0:
            cnt += 1
            continue
        input = line.strip().split(",")
        instance = input[0:len(input) - 1]
        target_output = input[-1]
        instances.append([x for x in instance])
        # target_outputs.append(int(target_output))
        target_outputs.append(target_output)
    file.close()
    return instances, target_outputs


def read_target_weight(filename):
    file = open(filename, "r")
    weights = []
    for line in file.readlines():
        input = line.strip().split(",")
        weights += [float(x) for x in input]
    file.close()
    return weights
