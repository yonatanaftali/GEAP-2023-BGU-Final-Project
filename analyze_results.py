import re

import numpy as np
from matplotlib import pyplot as plt


def _extract_fitness_data(statistics_file_name):
    with open(statistics_file_name) as f:
        data = []
        generation, average_fitness = None, None
        for line in f:
            if line.startswith("generation"):
                match = re.search(r'\d+', line)
                if match:
                    generation = int(match.group())
            elif line.startswith("average fitness"):
                average_fitness = float(line.split()[-1])

            if generation is not None and average_fitness is not None:
                data.append([generation, average_fitness])
                generation, average_fitness = None, None
    return data


def _print_all_data(statistics_file_name):
    with open(statistics_file_name) as f:
        for line in f:
            print(line.strip())


def _plot_graph(gen_to_fitness, statistics_file_name):
    data = np.array(gen_to_fitness)
    x, y = data.T
    plt.xlabel("Generation #")
    plt.ylabel("Average Fitness")
    plt.plot(x, y)
    plt.axhline(color='g', linestyle='--')
    statistics_graph_file = statistics_file_name.replace(".txt", ".png")
    plt.savefig(statistics_graph_file)
    print(f'\n\nStatistics graph saved to {statistics_graph_file}\n\n')


def show_statistics(statistics_file_name):
    data = _extract_fitness_data(statistics_file_name)
    _plot_graph(data, statistics_file_name)
    _print_all_data(statistics_file_name)
