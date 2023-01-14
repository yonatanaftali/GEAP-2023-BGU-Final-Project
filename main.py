from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.creators.ga_creators.bit_string_vector_creator import GABitStringVectorCreator
from eckity.genetic_operators.crossovers.vector_k_point_crossover import VectorKPointsCrossover
from eckity.genetic_operators.mutations.vector_random_mutation import IntVectorOnePointMutation
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation

from analyze_results import show_statistics, STATISTICS_FILE
from maze_evaluator import MazeEvaluator, MAX_SOLUTION_LENGTH

POPULATION_SIZE = 100

algo = SimpleEvolution(
    Subpopulation(creators=GABitStringVectorCreator(length=MAX_SOLUTION_LENGTH, bounds=(0, 3)),
                  population_size=POPULATION_SIZE,
                  evaluator=MazeEvaluator(),
                  higher_is_better=False,
                  operators_sequence=[
                      VectorKPointsCrossover(k=1),
                      IntVectorOnePointMutation(probability=0.2, arity=10),
                  ],
                  selection_methods=[
                      (TournamentSelection(tournament_size=4, higher_is_better=False), 1)
                  ]),
    breeder=SimpleBreeder(),
    max_workers=1,
    max_generation=200,
    statistics=BestAverageWorstStatistics(output_stream=open(STATISTICS_FILE, 'w'))
)

# evolve the generated initial population
algo.evolve()

# Execute (show) the best solution
print(algo.execute())

# Show the statistics
show_statistics()
