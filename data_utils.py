import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean
import os
import matplotlib.pyplot as plt
from dtaidistance import dtw



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

    data_slidingwindow = np.ndarray(
        (data.shape[0]-window_length, window_length))
    for ix in range(data.shape[0]-window_length):
        data_slidingwindow[ix, :] = data[ix:ix+window_length]
        
    return data_slidingwindow


def find_candidates(data, xmin, xmax, distance='euclidean'):

    if distance == 'dtw':
        distance_func = dtw.distance_fast
    else:
        distance_func = euclidean

    length = xmax - xmin

    dist_array = np.ndarray((data.shape[0]-length))
    for ix in range(data.shape[0]-length):
        dist_array[ix] = distance_func(data[xmin:xmax], data[ix:ix+length])

    return np.argsort(dist_array)


def print_candidate_list(sorted_list, data, length, distance='euclidean'):

    try:
        os.mkdir('sortedlist')
    except:
        pass

    if distance == 'dtw':
        distance_func = dtw.distance_fast
    else:
        distance = 'euclidean'
        distance_func = euclidean

    for ix in range(len(sorted_list)):
        plt.figure()
        plt.plot(
            list(range(sorted_list[ix], sorted_list[ix]+length)),
            data[sorted_list[ix]:sorted_list[ix]+length])
        plt.title(
            str(distance_func(data[sorted_list[0]:sorted_list[0]+length], data[sorted_list[ix]:sorted_list[ix]+length])))
        plt.savefig(
            'sortedlist/'+distance+'_'+str(ix)+'_'+str(sorted_list[ix])+'.png')
        plt.close()

