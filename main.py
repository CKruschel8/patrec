from data_utils import generate_data, dataset, find_candidates
from plot_data import interactive_plot, display_candidates

train, test = generate_data()

xmin, xmax = interactive_plot(train)
print(xmin, xmax)

dataset = dataset()
dataset.add_data(train, xmin, xmax, 1)

ind_list = find_candidates(train, xmin, xmax)
display_candidates(train, xmax, ind_list)