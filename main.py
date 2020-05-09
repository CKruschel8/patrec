from data_utils import generate_data, dataset
from plot_data import interactive_plot

train, test = generate_data()

xmin, xmax = interactive_plot(train)
print(xmin, xmax)


dataset = dataset()
dataset.add_data(train, xmin, xmax, 1)
