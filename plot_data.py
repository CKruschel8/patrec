import matplotlib.pyplot as plt

def plot_data(data):
    plt.figure()
    plt.plot(data)
    x = plt.ginput(2)

    plt.show()
    print(x)
