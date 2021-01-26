from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

import matplotlib, math
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def plot_results(results, title, filename = None):

    fig, (ax1) = plt.subplots(1, 1)
    fig2, (plt1, plt2) = plt.subplots(1, 2, sharey='all')

    for key in results:
        ops = []
        n = []
        searches_interpolation = []
        searches_binary = []

        for i in range(len(results[key])):
            ops.append(results[key][i]['ops'])
            n.append(results[key][i]['n'])

            if key == 'BinarySearch':
                searches_binary += results[key][i]['searches']
            else:
                searches_interpolation += results[key][i]['searches']

        ax1.plot(n, ops, label=key)
        plt1.hist(searches_binary, rwidth=0.95, label=key)
        plt2.hist(searches_interpolation, rwidth=0.95, label=key)
        plt2.legend()

    ax1.set_title('Average Ops/Size')
    ax1.set_ylabel('Average ops (#)')
    ax1.set_xlabel('Size (n)')
    ax1.legend()

    fig2.suptitle('Histogram of searches per element: ' + title +
                  '\nY = Frequency of searches for an element'
                    '\nX = Amount of searches')

    fig.suptitle(title)

    plt.show()
