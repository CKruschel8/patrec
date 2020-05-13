import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean


NAME = r"dataset\ECG.csv"


class dataset():

    def __init__(self):
        self.no_data = True
        self.length = 0

    def add_data(self, timeseries, x_start, x_stop, label):
        start_pos = int(x_start)
        stop_pos = int(x_stop)
        if self.no_data:
            self.no_data = False

            self.length = stop_pos - start_pos
            self.data = np.ndarray((1, self.length, 1))
            self.data[0, :, 0] = timeseries[start_pos:stop_pos]

            self.label = np.ndarray((1))
            self.label[0] = label


def generate_data():
    dataset = pd.read_csv(NAME)
    y = [e for e in dataset.hart]

    train = y[:2350]
    test = y[2350:]

    return np.array(train), np.array(test)


def build_window_dataset(data, window_length):

    data_slidingwindow = np.ndarray((data.shape[0]-window_length, window_length))
    for ix in range(data.shape[0]-window_length):
        data_slidingwindow[ix, :] = data[ix:ix+window_length]
        
    return data_slidingwindow


def find_candidates(data, xmin, xmax, distance = 'euclidean', datatransform = 'data'):

    length = xmax - xmin

#    if datatransform == 'data+gradient':
#        data = np.append(data, np.gradient(data))
#    elif datatransform == 'gradient':
#        data = np.gradient(data)

    dist_array = np.ndarray((data.shape[0]-length))
    if distance == 'euclidean':
        for ix in range(data.shape[0]-length):
            dist_array[ix] = euclidean(data[xmin:xmax], data[ix:ix+length])

    return np.argsort(dist_array)

