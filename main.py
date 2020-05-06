from data_utils import generate_data
from plot_data import interactive_plot

train, test = generate_data()

xmin, xmax = interactive_plot(train)
print(xmin, xmax)
