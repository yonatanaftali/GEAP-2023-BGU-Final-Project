import re
from typing import List

import numpy as np
from matplotlib import pyplot as plt

STATISTICS_FILE = "statistics.txt"


def _extract_fitness_data():
    with open(STATISTICS_FILE) as f:
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


def _print_all_data():
    with open(STATISTICS_FILE) as f:
        for line in f:
            print(line.strip())


def _plot_graph(gen_to_fitness: List[List[int]]):
    data = np.array(gen_to_fitness)
    x, y = data.T
    plt.xlabel("Generation #")
    plt.ylabel("Average Fitness")
    plt.plot(x, y)
    plt.axhline(color='r')
    plt.savefig("statistics.png")
    print("\n\nStatistics graph saved to statistics.png!\n\n")


def show_statistics():
    data = _extract_fitness_data()
    _plot_graph(data)
    _print_all_data()
