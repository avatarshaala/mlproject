class tstcode:
    def __init__(self, k):
        self.k = k
        #print("value of k:", self.k)

    def get_data(self, data=[]):

        #print("CTR: ", len(data))
        # if data == None:
        #     data = []
        if(self.k == 2):
            #data = []
            # data = [1,2]
            data.append(1)
            data.append(2)
        else:
            #data = []
            # data = [4,5,6]
            data.append(4)
            data.append(5)
            data.append(6)


        return data


def caller(k):
    tcls = None
    tcls = tstcode(k)
    data = tcls.get_data()
    print(data)


caller(2)
caller(4)

