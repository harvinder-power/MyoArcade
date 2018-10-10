from matplotlib import pyplot as plt
from collections import deque
from threading import Lock, Thread

import myo
import numpy as np
import pandas as pd
from math import pi


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

    self.categories=list(self.df)[:-1]
    self.N = len(self.categories)
    self.angles = [n / float(N) * 2 * pi for n in range(N)]
    self.angles += self.angles[:1]

    # Initialise the spider plot
    self.fig = plt.figure(figsize=(20, 10))
    self.ax = plt.subplot(111, polar=True)
    plt.xticks(angles[:-1], categories, color='grey', size=8)

    # Draw ylabels
    self.ax.set_rlabel_position(0)
    plt.yticks([], [], color="grey", size=7)
    plt.ylim(0,40)

    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')

    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)

    plt.ion()

  def update_plot(self):
    emg_data = self.listener.get_emg_data()
    emg_data = np.array([x[1] for x in emg_data]).T
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

    self.values=self.df.loc[0].drop('timestamp').values.flatten().tolist()
    self.values += self.values[:1]

    for g, data in zip(self.graphs, emg_data):
      if len(data) < self.n:
        # Fill the left side with zeroes.
        data = np.concatenate([np.zeros(self.n - len(data)), data])
      self.graphs[0].set_ydata(data)
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







# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:
values=df.loc[0].drop('timestamp').values.flatten().tolist()
values += values[:1]

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the spider plot
ax = plt.subplot(111, polar=True)

# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories, color='grey', size=8)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([], [], color="grey", size=7)
plt.ylim(0,40)

# Plot data
ax.plot(angles, values, linewidth=1, linestyle='solid')

# Fill area
ax.fill(angles, values, 'b', alpha=0.1)
