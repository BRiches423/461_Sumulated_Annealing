import numpy as np
import pandas as pd
import math
import random
import matplotlib.pyplot as plt

class Anneal:
    def __init__(self, data_link, initial_temp):
        #self.data = np.array([])
        #self.length = 0
        self.goal = 1000
        self.objective = 0
        self.weight = 0
        self.loop_size = 40000
        self.max_changes = 4000
        self.temp = initial_temp
        self.sucessful_changes = 10
        self.annealed_changes = 0
        self.looped = 0
        self.load(data_link)

    # returns the penalty for being overweight
    def penalty(self):
        return max(0, ((self.data[:, [2]] * self.data[:, [1]]).sum(axis=0)[0] - 500) * 20)

    # returns the CURRENT OBJECTIVE FUNCTION does not modify the objective variable in case
    # a change needs to be reverted
    def get_objective(self):
        return self.goal - (self.data[:, [2]] * self.data[:, [0]]).sum(axis=0)[0] + self.penalty()

    # returns the current weight of the array
    def get_weight(self):
        return (self.data[:, [2]] * self.data[:, [1]]).sum(axis=0)[0]

    # inverts the included/not-included binary string to change and revert changes
    def invert(self, index):
        self.data[index, 2] = abs(self.data[index, 2] - 1)

        # returns true if a dice roll is less than the change/temp probability function

    def prob_accept(self):
        cumulative = math.exp(-(abs(self.objective - self.get_objective())) / self.temp)
        return random.uniform(0, 1) <= cumulative

    # loads the data set and calls the randomizer function
    def load(self, link_name):
        self.data = np.loadtxt(link_name)
        self.length = self.data.shape[0]

        # adding the bit-string that indicates if an item is included or not
        self.data = np.append(self.data, np.repeat(0, self.length).reshape(self.length, 1), axis=1)
        self.initialize()

    # randomly assigns 1 to approximate 1/20th of the items 0.05
    def initialize(self):

        for i in range(self.length):
            if (random.uniform(0, 1) <= 0.05):
                self.data[i, 2] = 1

        self.objective = self.get_objective()
        self.weight = (self.data[:, [2]] * self.data[:, [1]]).sum(axis=0)[0]


    def anneal(self):
        # initializing the counters used for epoch evaluations

        self.sucessful_changes = 0
        self.annealed_changes = 0
        self.looped = 0

        for loop in range(self.loop_size):

            # this var is only used to track what percent of worse moves are accepted 'aka' annealed
            self.looped += 1

            # randomly select an item to change status, change the status and note the temporary new objective fn
            index_changed = random.randrange(0, self.length)
            self.invert(index_changed)
            temp_objective = self.get_objective()

            # if objective is less auto accept and break the loop if the stopping critera are met
            if (temp_objective < self.objective):
                self.objective = temp_objective
                self.sucessful_changes += 1

                if (self.sucessful_changes == self.max_changes):
                    break

                # if temp objective not less but probability allows change, accept the change and break if stopping
                # criteria is met
            elif (self.prob_accept()):
                self.objective = temp_objective
                self.annealed_changes += 1
                self.sucessful_changes += 1

                if (self.sucessful_changes == self.max_changes):
                    break
                # if neither of the critera are true just revert the change
            else:
                self.invert(index_changed)

