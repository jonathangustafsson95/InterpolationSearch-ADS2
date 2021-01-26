from Experiment import experiment_run
from Visuals import Visualizer
from Input import input_gen
import numpy as np


def main():
    n = np.arange(1000, 11000, 1000).tolist()       #Adjust input size, step size and size of arrays

    experiment_dict = {}
    experiment_dict['algorithms'] = ['BinarySearch', 'InterpolationSearch']
    experiment_dict['searches'] = []

    data = {'Random uniform data', 'Sorted data with abnormally big element last',
            'Sorted data, normal distribution',
            'Sorted data, uniform distribution'}
    i = 0
    for title in data:
        experiment_dict['data'] = get_data(title, n)

        results = experiment_run.run(experiment_dict)
        Visualizer.plot_results(results, title)
        i += 1


def get_data(title, n):
    if title == 'Random uniform data':
        return [input_gen.random_uniform_dist(j) for j in n]
    elif title == 'Sorted data with abnormally big element last':
        return [input_gen.big_element_last(j) for j in n]
    elif title == 'Sorted data, normal distribution':
        return [input_gen.normal_distribution(j) for j in n]
    elif title == 'Sorted data, uniform distribution':
        return [input_gen.best_case_distribution(j) for j in n]


if __name__ == "__main__":
    main()