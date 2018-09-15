import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy.signal as signal

input_file = './New-Datasets(August-2018)/8-august-george-post-contraction-relaxation/emg-1533748606.csv'

df = pd.read_csv(input_file)
#print df.head()

#TO-DO: Normalise the time to a standardised system.
N  = 2    # Filter order
Wn = 0.96 # Cutoff frequency (between 0-1, higher = less filtering)
B, A = signal.butter(N, Wn, btype='highpass', output='ba') #btype can be changed for "lowpass"

#Generation of data as a list
emg1_f = signal.filtfilt(B,A, df.emg1)

f, axs = plt.subplots(2,4,figsize=(15,15))
plt.subplot(2, 4, 1)
plt.plot(df.index, df.emg1, 'b-')
plt.plot(df.index, signal.filtfilt(B,A, df.emg1), 'r-', linewidth=2)
plt.title('EMG1')
plt.xlabel('time (s)')
plt.ylabel('Signal')

plt.subplot(2, 4, 2)
plt.plot(df.index, df.emg2, 'b-')
plt.plot(df.index, signal.filtfilt(B,A, df.emg2), 'r-', linewidth=2)
plt.title('EMG2')
plt.xlabel('time (s)')
plt.ylabel('Signal intensity')

plt.subplot(2, 4, 3)
plt.plot(df.index, df.emg3, 'b-')
plt.plot(df.index, signal.filtfilt(B,A, df.emg3), 'r-', linewidth=2)
plt.title('EMG3')
plt.xlabel('time (s)')
plt.ylabel('Signal intensity')

plt.subplot(2, 4, 4)
plt.plot(df.index, df.emg4, 'b-')
plt.plot(df.index, signal.filtfilt(B,A, df.emg4), 'r-', linewidth=2)
plt.title('EMG4')
plt.xlabel('time (s)')
plt.ylabel('Signal intensity')

plt.subplot(2, 4, 5)
plt.plot(df.index, df.emg5, 'b-')
plt.plot(df.index, signal.filtfilt(B,A, df.emg5), 'r-', linewidth=2)
plt.title('EMG5')
plt.xlabel('time (s)')
plt.ylabel('Signal intensity')

plt.subplot(2, 4, 6)
plt.plot(df.index, df.emg6, 'b-')
plt.plot(df.index, signal.filtfilt(B,A, df.emg6), 'r-', linewidth=2)
plt.title('EMG6')
plt.xlabel('time (s)')
plt.ylabel('Signal intensity')

plt.subplot(2, 4, 7)
plt.plot(df.index, df.emg7, 'b-')
plt.plot(df.index, signal.filtfilt(B,A, df.emg7), 'r-', linewidth=2)
plt.title('EMG7')
plt.xlabel('time (s)')
plt.ylabel('Signal intensity')

plt.subplot(2, 4, 8)
plt.plot(df.index, df.emg8, 'b-')
plt.plot(df.index, signal.filtfilt(B,A, df.emg8), 'r-', linewidth=2)
plt.title('EMG8')
plt.xlabel('time (s)')
plt.ylabel('Signal intensit')

f.savefig('full_figure.png', dpi=300)
