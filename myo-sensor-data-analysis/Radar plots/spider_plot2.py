from matplotlib import pyplot as plt
from collections import deque
from threading import Lock, Thread

import myo
import numpy as np
import csv
from math import pi
import pandas as pd



class EmgCollector(myo.DeviceListener):
  """
  Collects EMG data in a queue with *n* maximum number of elements.
  """

  def __init__(self, n):
    self.n = n
    self.lock = Lock()
    self.emg_data_queue = deque(maxlen=n)

  def get_emg_data(self):
    with self.lock:
      return list(self.emg_data_queue)

  # myo.DeviceListener

  def on_connected(self, event):
    event.device.stream_emg(True)

  def on_emg(self, event):
    with self.lock:
      self.emg_data_queue.append((event.timestamp, event.emg))


class Plot(object):

  def __init__(self, listener):
    self.n = listener.n
    self.listener = listener
    self.fig = plt.figure()

    #Create the axes in a polar format, and initialise with 0's
    self.axes = [self.fig.add_subplot(111, polar=True)]
    [(ax.set_ylim([-100, 100])) for ax in self.axes]
    self.graphs = [ax.plot(np.arange(self.n), np.zeros(self.n))[0] for ax in self.axes]
    plt.ion()

  def update_plot(self):
    emg_data = self.listener.get_emg_data()
    emg_data = np.array([x[1] for x in emg_data]).T
    print emg_data
    np.savetxt("foo.csv", emg_data, delimiter=",")

    #Crate a Pandas Dataframe of the different EMG leads
    df = pd.DataFrame({
    'emg1': emg_data[0],
    'emg2': emg_data[1],
    'emg3': emg_data[2],
    'emg4': emg_data[3],
    'emg5': emg_data[4],
    'emg6': emg_data[5],
    'emg7': emg_data[6],
    'emg8': emg_data[7]
    })

    #Determine number of "categories"
    categories=list(df)[1:]
    N = len(categories)

    #Find angle range
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]



    for g, data in zip(self.graphs, df):
      if len(data) < self.n:
        # Fill the left side with zeroes.
        data = np.concatenate([np.zeros(self.n - len(data)), data])
      g.set_ydata(df)
    plt.draw()

  def main(self):
    while True:
      self.update_plot()
      plt.pause(1.0 / 30)


def main():
  myo.init(sdk_path='/Users/harvinderpower/GitHub/ichealthhack18/myo-sensor-data-analysis/sdk/')
  hub = myo.Hub()
  listener = EmgCollector(512)
  with hub.run_in_background(listener.on_event):
    Plot(listener).main()



if __name__ == '__main__':
  main()

'''

    self.df = pd.DataFrame({
    'emg1': emg_data[0],
    'emg2': emg_data[1],
    'emg3': emg_data[2],
    'emg4': emg_data[3],
    'emg5': emg_data[4],
    'emg6': emg_data[5],
    'emg7': emg_data[6],
    'emg8': emg_data[7]
    })

# number of variable
categories=list(df)[1:]
N = len(categories)

values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
values

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

fig = plt.figure(figsize=(20, 10))
# Initialise the spider plot
ax = plt.subplot(111, polar=True)

# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories, color='grey', size=8)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
plt.ylim(0,10)

# Plot data
ax.plot(angles, values, linewidth=1, linestyle='solid')

'''
