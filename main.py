from data_utils import generate_data 
from plot_data import plot_data

train, test = generate_data()

plot_data(train)