from data_utils import generate_data
from plot_data import interactive_plot

train, test = generate_data()

interactive_plot(train)
