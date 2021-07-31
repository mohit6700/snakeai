from genetic_algo import *
from snake_game import *

# n_x -> no. of input units
# n_h -> no. of units in hidden layer 1
# n_h2 -> no. of units in hidden layer 2
# n_y -> no. of output units

no_of_chromosomes = 50
no_of_weights = n_x*n_h + n_h*n_h2 + n_h2*n_y

pop_size = (no_of_chromosomes,no_of_weights)

new_population = np.random.choice(np.arange(-1,1,step=0.01),size=pop_size,replace=True)

num_generations = 100

num_parents_mating = 3
max_score = []
max_fitness = []
for generation in range(num_generations):
    print('##############        GENERATION ' + str(generation)+ '  ###############' )

    fitness , score= cal_pop_fitness(new_population)
    print('#######  fittest chromosome in generation ' + str(generation) +' is having fitness value:  ' + str(np.max(fitness)) + " max score is " + str(np.max(score)))
    max_score.append(np.max(score))
    max_fitness.append(np.max(fitness)) 
  
    parents = select_mating_pool(new_population, fitness, num_parents_mating)

    offspring_crossover = crossover(parents, offspring_size=(pop_size[0] - parents.shape[0], no_of_weights))

    offspring_mutation = mutation(offspring_crossover)

    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation


print(max_score)
print(max_fitness)
