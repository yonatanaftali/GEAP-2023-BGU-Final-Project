import re

import numpy as np
from matplotlib import pyplot as plt


def extract_fitness_data(statistics_file_name):
    with open(statistics_file_name) as f:
        data = {
            'Average Fitness': [],
            'Best Fitness': [],
        }
        generation, average_fitness, best_fitness = None, None, None
        for line in f:
            if line.startswith("generation"):
                match = re.search(r'\d+', line)
                if match:
                    generation = int(match.group())
            elif line.startswith("average fitness"):
                average_fitness = float(line.split()[-1])
            elif line.startswith("best fitness"):
                best_fitness = float(line.split()[-1])

            if generation is not None and average_fitness is not None:
                data['Average Fitness'].append([generation, average_fitness])
                average_fitness = None
            if generation is not None and best_fitness is not None:
                data['Best Fitness'].append([generation, best_fitness])
                best_fitness = None
            generation = None
    return data


def print_all_data(statistics_file_name):
    with open(statistics_file_name) as f:
        for line in f:
            print(line.strip())


def plot_graphs(statistics_data, statistics_file_name):
    print("\n-------------SUMMARY--------------")
    print(f"Full statistics file saved to: {statistics_file_name}")
    for key in statistics_data:
        data = np.array(statistics_data[key])
        x, y = data.T
        plt.plot(x, y)
        plt.xlabel("Generation #")
        plt.ylabel(key)
        plt.axhline(color='g', linestyle='--')
        statistics_graph_file = statistics_file_name.replace(".txt", f'_{key.replace(" ", "_").lower()}.png')
        plt.savefig(statistics_graph_file)
        plt.close()
        print(f'{key} graph saved to {statistics_graph_file}')
    print("----------------------------------")


def show_statistics(statistics_file_name):
    data = extract_fitness_data(statistics_file_name)
    plot_graphs(data, statistics_file_name)
    # print_all_data(statistics_file_name)
