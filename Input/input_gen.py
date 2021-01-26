import numpy as np


def random_uniform_dist(n):                             # Uniform random distribution
    a_list = np.random.randint(low=0, high=n, size=n)
    a_list.sort()
    return a_list.tolist()


def big_element_last(n):                                # Sequential data with huge element last
    a = np.arange(n)
    a_list = np.append(a, n**3)
    a_list.sort()
    return a_list.tolist()


def normal_distribution(n):                             # Normally distributed data
    a_list = np.random.normal(n//2, n//3, n).round().astype(np.int)
    a_list.sort()
    return a_list.tolist()


def best_case_distribution(n):                          # Sequential data
    a_list = np.arange(n).tolist()
    return a_list




