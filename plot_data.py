import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector, Button

coords = dict()
coords['min'] = None
coords['max'] = None

sim_ix = 1
unsim_ix = -1
bSimilar = True

class Index(object):

    def close(self, event):
        plt.close()

    def next(self, event):
        if bSimilar:
            if bGotMark:
                plt.axvspan(sorted_list[ix], sorted_list[ix]+length, facecolor='white', alpha=1)
                ix += 1
                plt.axvspan(sorted_list[ix], sorted_list[ix] + length, facecolor='yellow', alpha=0.5)
                plt.subplot(2, 1, 2)
                plt.plot(train)
                plt.xlim([sorted_list[ix]-tol, sorted_list[ix]+length+100])


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


def interactive_plot(data):
    global ax1

    fig, ax1 = plt.subplots(1, figsize=(8, 6))

    ax1.plot(data)
    ax1.set_title('Markiere mit der linken Maustaste einen Bereich')
    callback = Index()
    axprev = plt.axes([0.8, 0.01, 0.1, 0.075])
    bclose = Button(axprev, 'Schließen')

    span1 = SpanSelector(
        ax=ax1, onselect=onselect, direction='horizontal',
        useblit=True, minspan=2, button=1,
        rectprops=dict(alpha=0.5, facecolor='red'))

    span2 = SpanSelector(
        ax=ax1, onselect=offselect, direction='horizontal',
        useblit=True, minspan=2, button=3,
        rectprops=dict(alpha=0.5, facecolor='red'))

    bclose.on_clicked(callback.close)

    plt.show()
    del span1, span2
    return np.int(coords['min']), np.int(coords['max'])

def display_candidates(train, xmax, sorted_list):
    global unsim_ix

    length = xmax - sorted_list[0]
    b = True
    bGotMark = False

    def close(event):
        plt.close()

    def next(event):
        global sim_ix, unsim_ix

        if bSimilar:
            if sim_ix != len(sorted_list):
                sim_ix += 1
            ix = sim_ix
        else:
            if unsim_ix != 0:
                unsim_ix -= 1
            ix = unsim_ix
        ax1.axvspan(sorted_list[ix], sorted_list[ix]+length, facecolor='yellow', alpha=0.5)
        ax2.set_xlim([sorted_list[ix]-tol, sorted_list[ix]+length+tol])
        print(sorted_list[ix])

    def previous(event):
        global sim_ix, unsim_ix

        if bSimilar:
            if sim_ix != 0:
                sim_ix -= 1
            ix = sim_ix
        else:
            if unsim_ix != len(sorted_list):
                unsim_ix += 1
            ix = unsim_ix
        
        ax1.axvspan(sorted_list[ix], sorted_list[ix]+length, facecolor='yellow', alpha=0.5)
        ax2.set_xlim([sorted_list[ix]-tol, sorted_list[ix]+length+tol])
        print(sorted_list[ix])
 
    def unsimilar(event):
        global bSimilar
        bSimilar = False
        bunsim.color = 'white'
        bsim.color = '0.85'
        print(bSimilar)

    def similar(event):
        global bSimilar
        bSimilar = True
        bsim.color = 'white'
        bunsim.color = '0.85'
        print(bSimilar)


    tol = 100
    callback = Index()
    
    unsim_ix = len(sorted_list)

    plt.figure()
    ax1 = plt.subplot(2, 1, 1)
    plt.plot(train)
    plt.axvspan(sorted_list[0], xmax, facecolor='orange', alpha=0.5)
    
    ix = sim_ix
    plt.axvspan(sorted_list[ix], sorted_list[ix] + length, facecolor='yellow', alpha=0.5)
    ax2 = plt.subplot(2, 1, 2)
    plt.plot(train)
    ax2.set_xlim([sorted_list[ix]-tol, sorted_list[ix]+length+tol])

    axprev1 = plt.axes([0.8, 0.01, 0.1, 0.075])
    bclose = Button(axprev1, 'Schließen')
    bclose.on_clicked(close)

    axprev2 = plt.axes([0.7, 0.01, 0.1, 0.075])
    bnext = Button(axprev2, 'Nächstes')
    bnext.on_clicked(next)

    axprev3 = plt.axes([0.6, 0.01, 0.1, 0.075])
    bfalse = Button(axprev3, 'Label False', color='red')

    axprev4 = plt.axes([0.5, 0.01, 0.1, 0.075])
    btrue = Button(axprev4, 'Label True', color='green')

    axprev5 = plt.axes([0.4, 0.01, 0.1, 0.075])
    bprev = Button(axprev5, 'Voriges')
    bprev.on_clicked(previous)

    axprev6 = plt.axes([0.2, 0.01, 0.1, 0.075])
    bunsim = Button(axprev6, 'Unähnliche')
    bunsim.on_clicked(unsimilar)

    axprev7 = plt.axes([0.1, 0.01, 0.1, 0.075])
    bsim = Button(axprev7, 'Ähnliche')
    bsim.color = 'white'
    bsim.on_clicked(similar)

    plt.show()


