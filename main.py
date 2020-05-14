from data_utils import generate_data, dataset, find_candidates, print_candidate_list
from plot_data import interactive_plot, display_candidates
import time

train, test = generate_data()

xmin, xmax = interactive_plot(train)
print(xmin, xmax)

dataset = dataset()
dataset.add_data(train, xmin, xmax, 1)

ind_list_dtw = find_candidates(train, xmin, xmax, distance='dtw')

#print_candidate_list(ind_list_dtw, train, xmax-xmin, distance='dtw')

display_candidates(train, xmax, ind_list_dtw)