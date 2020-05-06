import pandas as pd

NAME = r"dataset\ECG.csv"


def generate_data():
    dataset = pd.read_csv(NAME)
    y = [e for e in dataset.hart]

    train = y[:2350]
    test = y[2350:]

    return train, test
