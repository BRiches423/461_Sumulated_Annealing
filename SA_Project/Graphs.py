import pandas as pd
import matplotlib.pyplot as plt

# turning results into dataframes
st1 = pd.read_csv('stats(1).txt', index_col = [0])
st2 = pd.read_csv('stats(2).txt', index_col = [0])
st3 = pd.read_csv('stats(3).txt', index_col = [0])

# making plots for GEOMETRIC 0.9
plt.plot(st1['temp'])
plt.title("Geo.9Temperature/Iteration MinTemp: {}".format(min(st1['temp'])))
plt.show()
plt.plot(st1['temp'],st1['objective'])
plt.title("Geo.9Temperature/Objective Final Objective: {}".format(st1.loc[st1.shape[0]-1,['objective']][0]))
plt.show()
plt.plot(st1['temp'],st1['percent_annealed'])
plt.title("Geo.9temp/percent_annealed Max: {}".format(max(st1['percent_annealed'])))
plt.show()

#MAKING PLOTS FOR GEOMETRIC 0.85

plt.plot(st2['temp'])
plt.title("Geo.85Temperature/Iteration MinTemp: {}".format(min(st2['temp'])))
plt.show()
plt.plot(st2['temp'],st2['objective'])
plt.title("Geo.85Temperature/Objective Final Objective: {}".format(st2.loc[st2.shape[0]-1,['objective']][0]))
plt.show()
plt.plot(st2['temp'],st2['percent_annealed'])
plt.title("Geo.85temp/percent_annealed Max: {}".format(max(st2['percent_annealed'])))
plt.show()

# MAKING PLOTS FOR MODIFIED LINEAR

plt.plot(st3['temp'])
plt.title("MLinearTemperature/Iteration MinTemp: {}".format(min(st3['temp'])))
plt.show()
plt.plot(st3['temp'],st3['objective'])
plt.title("MLinearTemperature/Objective Final Objective: {}".format(st3.loc[st3.shape[0]-1,['objective']][0]))
plt.show()
plt.plot(st3['temp'],st3['percent_annealed'])
plt.title("MLineartemp/percent_annealed Max: {}".format(max(st3['percent_annealed'])))
plt.show()