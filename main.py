import os
import time

from dotenv import load_dotenv
from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.creators.ga_creators.bit_string_vector_creator import GABitStringVectorCreator
from eckity.genetic_operators.crossovers.vector_k_point_crossover import VectorKPointsCrossover
from eckity.genetic_operators.mutations.vector_random_mutation import IntVectorOnePointMutation
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation

from analyze_results import show_statistics
from maze_evaluator import MazeEvaluator

global MAZE_ROWS, MAZE_COLS, MAX_SOLUTION_LENGTH, POPULATION_SIZE, MUTATION_RATE, MUTATION_ARITY, GENERATIONS, \
    STRICT, INVALID_SOLUTION_PENALTY, WALL_PENALTY, RUN_START_TIME, STATISTICS_FILE


def main():
    global MAZE_ROWS, MAZE_COLS, MAX_SOLUTION_LENGTH, POPULATION_SIZE, MUTATION_RATE, MUTATION_ARITY, GENERATIONS, \
        STRICT, INVALID_SOLUTION_PENALTY, WALL_PENALTY, RUN_START_TIME, STATISTICS_FILE
    f = open(STATISTICS_FILE, 'w')
    algo = SimpleEvolution(
        Subpopulation(creators=GABitStringVectorCreator(length=MAX_SOLUTION_LENGTH, bounds=(0, 3)),
                      population_size=POPULATION_SIZE,
                      higher_is_better=False,
                      evaluator=MazeEvaluator(n=MAZE_ROWS, m=MAZE_COLS, strict=STRICT,
                                              invalid_solution_penalty=INVALID_SOLUTION_PENALTY,
                                              wall_penalty=WALL_PENALTY, run_start_time=RUN_START_TIME),
                      selection_methods=[
                          (TournamentSelection(tournament_size=4, higher_is_better=False), 1)
                      ],
                      operators_sequence=[
                          VectorKPointsCrossover(k=1),
                          IntVectorOnePointMutation(probability=MUTATION_RATE,
                                                    arity=MUTATION_ARITY),
                      ]),
        breeder=SimpleBreeder(),
        max_workers=1,
        max_generation=GENERATIONS,
        statistics=BestAverageWorstStatistics(output_stream=f)
    )

    algo.evolve()

    print(algo.execute())

    f.close()
    show_statistics(STATISTICS_FILE)


def load_environment():
    global MAZE_ROWS, MAZE_COLS, MAX_SOLUTION_LENGTH, POPULATION_SIZE, MUTATION_RATE, MUTATION_ARITY, GENERATIONS, \
        STRICT, INVALID_SOLUTION_PENALTY, WALL_PENALTY, RUN_START_TIME, STATISTICS_FILE
    load_dotenv()
    MAZE_COLS = 5 if os.getenv('MAZE_COLS') is None else int(os.getenv('MAZE_COLS'))
    MAZE_ROWS = 5 if os.getenv('MAZE_ROWS') is None else int(os.getenv('MAZE_ROWS'))
    MAX_SOLUTION_LENGTH = 100 if os.getenv("MAX_SOLUTION_LENGTH") is None else int(os.getenv("MAX_SOLUTION_LENGTH"))
    POPULATION_SIZE = 100 if os.getenv("POPULATION_SIZE") is None else int(os.getenv("POPULATION_SIZE"))
    MUTATION_RATE = 0.2 if os.getenv("MUTATION_RATE") is None else float(os.getenv("MUTATION_RATE"))
    MUTATION_ARITY = 10 if os.getenv("MUTATION_ARITY") is None else int(os.getenv("MUTATION_ARITY"))
    GENERATIONS = 200 if os.getenv("GENERATIONS") is None else int(os.getenv("GENERATIONS"))
    STRICT = True if os.getenv("STRICT") is None else bool(os.getenv("STRICT"))
    INVALID_SOLUTION_PENALTY = 100 if os.getenv("INVALID_SOLUTION_PENALTY") is None else int(
        os.getenv("INVALID_SOLUTION_PENALTY"))
    WALL_PENALTY = 1 if os.getenv("WALL_PENALTY") is None else int(os.getenv("WALL_PENALTY"))
    RUN_START_TIME = str(round(time.time() * 1000))
    STATISTICS_FILE = f"./output/{RUN_START_TIME}_statistics.txt"


def print_intro():
    global MAZE_ROWS, MAZE_COLS, MAX_SOLUTION_LENGTH, POPULATION_SIZE, MUTATION_RATE, MUTATION_ARITY, GENERATIONS, \
        STRICT, INVALID_SOLUTION_PENALTY, WALL_PENALTY, STATISTICS_FILE
    print(r"""    
   _____            __  __                  _____       _                
  / ____|   /\     |  \/  |                / ____|     | |               
 | |  __   /  \    | \  / | __ _ _______  | (___   ___ | |_   _____ _ __ 
 | | |_ | / /\ \   | |\/| |/ _` |_  / _ \  \___ \ / _ \| \ \ / / _ \ '__|
 | |__| |/ ____ \  | |  | | (_| |/ /  __/  ____) | (_) | |\ V /  __/ |   
  \_____/_/    \_\ |_|  |_|\__,_/___\___| |_____/ \___/|_| \_/ \___|_|                                                                                                                                                             
    """)
    print("------------RUN DETAILS-----------")
    print("Run Started At: " + RUN_START_TIME)
    print("Maze Size: ", MAZE_ROWS * MAZE_COLS)
    print("MAX_SOLUTION_LENGTH: ", MAX_SOLUTION_LENGTH)
    print("POPULATION_SIZE: ", POPULATION_SIZE)
    print("MUTATION_RATE: ", MUTATION_RATE)
    print("MUTATION_ARITY: ", MUTATION_ARITY)
    print("GENERATIONS: ", GENERATIONS)
    print("STRICT: ", STRICT)
    print("INVALID_SOLUTION_PENALTY: ", INVALID_SOLUTION_PENALTY)
    print("WALL_PENALTY: ", WALL_PENALTY)
    print("Statistics File: ", STATISTICS_FILE)
    print("--------------------------------\n")


if __name__ == '__main__':
    load_environment()
    print_intro()
    main()
