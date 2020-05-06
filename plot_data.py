import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector

coords = dict()
coords['min'] = None
coords['max'] = None


def plot_data_standard(data):
    plt.figure()
    plt.plot(data)
    x = plt.ginput(2)

    plt.show()
    print(x)


def onselect(xmin, xmax):
    global ax

    if xmin > xmax:
        tmp = xmin
        xmin = xmax
        xmax = tmp

    if coords['min'] is None:
        coords['min'] = xmin
        coords['max'] = xmax

    else:
        if coords['min'] > xmin and coords['min'] < xmax:
            coords['min'] = xmin

        if coords['max'] < xmax and coords['max'] > xmin:
            coords['max'] = xmax

    ax = ax1.axvspan(coords['min'], coords['max'], facecolor='#2ca02c')
    print(coords['min'])
    print(coords['max'])


def offselect(xmin, xmax):
    global ax

    if xmin > xmax:
        tmp = xmin
        xmin = xmax
        xmax = tmp

    if coords['min'] is not None:

        if xmin <= coords['min'] and xmax > coords['min']:
            coords['min'] = xmax

        if xmax >= coords['max'] and xmin < coords['max']:
            coords['max'] = xmin

        if coords['min'] >= coords['max']:
            coords['min'] = None
            coords['max'] = None

    ax.remove()

    if coords['min'] is not None:
        ax = ax1.axvspan(coords['min'], coords['max'], facecolor='#2ca02c')

    print(coords['min'])
    print(coords['max'])


def interactive_plot(data):
    global ax1

    fig, ax1 = plt.subplots(1, figsize=(8, 6))
#    ax1.set(facecolor='#FFFFCC')

    ax1.plot(data)
    ax1.set_title('Markiere mit der linken Maustaste einen Bereich')

    SpanSelector(
        ax=ax1, onselect=onselect, direction='horizontal',
        useblit=True, minspan=2, button=1,
        rectprops=dict(alpha=0.5, facecolor='red'))

    SpanSelector(
        ax=ax1, onselect=offselect, direction='horizontal',
        useblit=True, minspan=2, button=3,
        rectprops=dict(alpha=0.5, facecolor='red'))

    plt.show()
