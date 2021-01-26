from Algorithms import BinarySearch
from Algorithms import InterpolationSearch


def run(experiment_dict):
    results = {}

    for i in range(len(experiment_dict['algorithms'])):
        results[experiment_dict['algorithms'][i]] = []

        for j in range(len(experiment_dict['data'])):
            total_count = 0
            search_count = []

            for k in range(len(experiment_dict['data'][j])):
                if experiment_dict['algorithms'][i] == 'BinarySearch':
                    search_ops = BinarySearch.search(experiment_dict['data'][j], experiment_dict['data'][j][k])
                    search_count.append(search_ops)
                    total_count += search_ops
                else:
                    search_ops = InterpolationSearch.search(experiment_dict['data'][j], experiment_dict['data'][j][k])
                    search_count.append(search_ops)
                    total_count += search_ops

            ops = total_count / len(experiment_dict['data'][j])
            n = len(experiment_dict['data'][j])
            results[experiment_dict['algorithms'][i]] += [{'ops': ops, 'n': n, 'searches': search_count}]

    return results
