from Anneal import Anneal
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# create an instance of the annealing function with the input and temp specified
forge = Anneal('Program2Input.txt', 4000)

# create a dataframe to record epoch stats
stats1 = pd.DataFrame(columns=['temp', 'objective', 'weight', 'percent_annealed'])

# loop through, calling the anneal function, recording epoch results, and adjusting temp till no changes were made
# in the 40000 loops
while (forge.sucessful_changes != 0):
    forge.anneal()
    stats1 = pd.concat([stats1, pd.DataFrame({'temp': [forge.temp], 'objective': [forge.objective],
                                              'weight': [(forge.data[:, [2]] * forge.data[:, [1]]).sum(axis=0)[0]],
                                              'percent_annealed': \
                                                  (forge.annealed_changes / (forge.looped - (
                                                              forge.sucessful_changes - forge.annealed_changes)))})],
                       ignore_index=True)

    # UNCOMMENT THE COOLING SCHEDULE YOU WOULD LIKE TO USE
    # MAKE SURE TO COMMENT THE OTHERS

    # attempt 1 geometric cooling with .9
    forge.temp = forge.temp*0.9

    # attempt 2 geometric cooling with .85
    # forge.temp = forge.temp*0.85

    # attempt 3 linear cooling drop by 100 degrees till 100 then 10 degrees, then 1, then at one
    # drop by .01 till .5, at point 5 switch to .9 geometric
    '''
    if (forge.temp > 100):
        forge.temp -= 100
    elif (forge.temp > 10):
        forge.temp -= 10
    elif (forge.temp > 1):
        forge.temp -= 1
    elif (forge.temp > 0.5):
        forge.temp -= 0.01
    else:
        forge.temp *= .9
    '''
output1 = pd.DataFrame(forge.data, columns=['objective', 'weight', 'included'])
print(forge.objective)
print(forge.get_weight())

# DONT UNCOMMENT UNLESS YOU CREATE NEW OUTPUT FILES

output1.to_csv('ouput4.txt')
stats1.to_csv('stats(4).txt')

print(output1)

