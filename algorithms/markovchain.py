__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

import numpy as np

class markovchain:
    """
    elementarray = a 2D square array of either raw count or
     probability of state transitions.
     states = list of string names of states
    isprobability = a boolean to indicate if elementarray is probability array
    """
    def __init__(self, elemarray, states=None,isprobability=True):

        if states == None:
            states = []
        #create enumeration of states
        self.states = {}
        if len(states) == 0:
            states = [i for i in range(len(elemarray)) ]
        for i in range(len(states)):
            self.states[states[i]] = i

        self.BUFF_SIZE = 100
        self.buff = [] #buffer to store n steps transition matrices

        if type(elemarray) is np.ndarray:
            self.transitionmatrix = elemarray
        else:
            self.transitionmatrix = np.matrix(elemarray)
        # print(self.transitionmatrix)
        self.buff.append(self.transitionmatrix)
        row,col = np.shape(self.transitionmatrix)
        if not isprobability:
            #Build transition probability
            for i in range(row):
                sum_ = np.sum(self.transitionmatrix[i])
                self.transitionmatrix[i] /= float(sum_)

    #n = number of transitions
    def n_transition_matrix(self, n):

        #multiply transition matrices subsequently and append in buffer
        while n > len(self.buff) and self.BUFF_SIZE > len(self.buff):
            buflen = len(self.buff)
            self.buff.append(self.buff[buflen-1] * self.transitionmatrix)

        #if still some steps are remained for transition
        if n > len(self.buff):
            buflen = len(self.buff)
            return self.buff[buflen-1] * (self.transitionmatrix ** (n-buflen))

        #else return last element of buffer
        return self.buff[n-1].copy()

    def n_convergence_matrix(self):
        prev_matrix = None
        transition_count = 1
        current_matrix = self.n_transition_matrix(transition_count)
        while not np.array_equal(prev_matrix,current_matrix):
            prev_matrix = current_matrix.copy()
            transition_count += 1
            current_matrix = self.n_transition_matrix(transition_count)

        return transition_count-1, current_matrix

    def n_convergence_probability_vector(self):
        iterations, matrix = self.n_convergence_matrix()
        return iterations, matrix[0]

    #the source and destination could be the indices or the name of the states
    def n_transitionprobability(self, source, destination, n):
        i = self.states[source]
        j = self.states[destination]
        return self.n_transition_matrix(n)[i,j].copy()

    def n_transition_probability_vector(self, priors, n):
        return priors * self.n_transition_matrix(n)



'''
#test example below
t = [[0.5, 0.25, 0.25],[0.5, 0, 0.5],[0.25,0.25, 0.5]]

mchain = markovchain(t, states=["rain","nice","snow"],isprobability=True)

cnt, tmat = mchain.n_convergence_matrix()
print(cnt, "\n", tmat)

cnt, vect = mchain.n_convergence_probability_vector()

print("\n________________")
print(cnt, "\n", vect)
print("\n________________")

x = mchain.n_transition_matrix(100)
print(x)


p = mchain.n_transitionprobability("rain","nice",100)
print(p)

'''

