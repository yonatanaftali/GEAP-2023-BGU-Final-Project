import re
import random
from typing import List

import numpy as np
from matplotlib import pyplot as plt

STATISTICS_FILE = "statistics.txt"


def _extract_fitness_data():
    with open(STATISTICS_FILE) as f:
        text = f.read()
    data = []
    paragraphs = text.strip().split("\n\n")
    for paragraph in paragraphs:
        try:
            print(paragraph)
            lines = paragraph.split("\n")
            generation_line = lines[0]
            average_fitness_line = lines[-1]
            match = re.search(r'\d+', generation_line)
            if match:
                generation = int(match.group())
            else:
                raise Exception("Could not find generation number")
            average_fitness = float(average_fitness_line.split()[-1])
            data.append([generation, average_fitness])
        except:
            print("An exception occurred while parsing the paragraph")

    return data


def _plot_graph(gen_to_fitness: List[List[int]]):
    data = np.array(gen_to_fitness)
    x, y = data.T
    plt.xlabel("Generation #")
    plt.ylabel("Average Fitness")
    plt.plot(x, y)
    plt.axhline(color='r')
    plt.show()


def show_statistics():
    data = _extract_fitness_data()
    _plot_graph(data)
