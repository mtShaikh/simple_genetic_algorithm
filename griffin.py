"""
Simple Genetic Algorithm Implementation

Author: M.Taha Shaikh
"""
from individual import Individual
import random
import matplotlib.pyplot as plt

x_bound1 = [-5, 5]
y_bound1 = [-5, 5]

x_bound2 = [-2, 2]
y_bound2 = [-1, 3]


def main():
    fitness_function = f_function
    fps_with_truncation(fitness_function)


def binary_with_binary(fitness_function):
    avg_best = [0] * 40
    avg_avg = [0] * 40
    for i in range(40):
        for j in range(10):
            best_fitness, avg_fitness = loop("binary", "binary", fitness_function)
            avg_best[i] += best_fitness[i]
            avg_avg[i] += avg_fitness[i]
        avg_best[i] = avg_best[i] / 10
        avg_avg[i] = avg_avg[i] / 10
    avg_avg.sort()
    avg_best.sort()
    fig = plt.figure()
    fig.suptitle('binary with binary', fontsize=20)
    plt.plot(avg_best, label="average best")
    plt.plot(avg_avg, label="average average")
    plt.legend(loc='upper left')
    plt.show()


def rbs_with_binary(fitness_function):
    avg_best = [0] * 40
    avg_avg = [0] * 40
    for i in range(40):
        for j in range(10):
            best_fitness, avg_fitness = loop("rbs", "binary", fitness_function)
            avg_best[i] += best_fitness[i]
            avg_avg[i] += avg_fitness[i]
        avg_best[i] = avg_best[i] / 10
        avg_avg[i] = avg_avg[i] / 10
    avg_avg.sort()
    avg_best.sort()
    fig = plt.figure()
    fig.suptitle('rbs with binary', fontsize=20)
    plt.plot(avg_best, label="average best")
    plt.plot(avg_avg, label="average average")
    plt.legend(loc='upper left')
    plt.show()


def fps_with_binary(fitness_function):
    avg_best = [0] * 40
    avg_avg = [0] * 40
    for i in range(40):
        for j in range(10):
            best_fitness, avg_fitness = loop("fps", "binary", fitness_function)
            avg_best[i] += best_fitness[i]
            avg_avg[i] += avg_fitness[i]
        avg_best[i] = avg_best[i] / 10
        avg_avg[i] = avg_avg[i] / 10
    avg_avg.sort()
    avg_best.sort()
    fig = plt.figure()
    fig.suptitle('fps with binary', fontsize=20)
    plt.plot(avg_best, label="average best")
    plt.plot(avg_avg, label="average average")
    plt.legend(loc='upper left')
    plt.show()


def binary_with_truncation(fitness_function):
    avg_best = [0] * 40
    avg_avg = [0] * 40
    for i in range(40):
        for j in range(10):
            best_fitness, avg_fitness = loop("binary", "trunc", fitness_function)
            avg_best[i] += best_fitness[i]
            avg_avg[i] += avg_fitness[i]
        avg_best[i] = avg_best[i] / 10
        avg_avg[i] = avg_avg[i] / 10
    avg_avg.sort()
    avg_best.sort()
    fig = plt.figure()
    fig.suptitle('binary with truncation', fontsize=20)
    plt.plot(avg_best, label="average best")
    plt.plot(avg_avg, label="average average")
    plt.legend(loc='upper left')
    plt.show()


def rbs_with_truncation(fitness_function):
    avg_best = [0] * 40
    avg_avg = [0] * 40
    for i in range(40):
        for j in range(10):
            best_fitness, avg_fitness = loop("rbs", "trunc",fitness_function)
            avg_best[i] += best_fitness[i]
            avg_avg[i] += avg_fitness[i]
        avg_best[i] = avg_best[i] / 10
        avg_avg[i] = avg_avg[i] / 10
    avg_avg.sort()
    avg_best.sort()
    fig = plt.figure()
    fig.suptitle('rbs with truncation', fontsize=20)
    plt.plot(avg_best, label="average best")
    plt.plot(avg_avg, label="average average")
    plt.legend(loc='upper left')
    plt.show()


def fps_with_truncation(fitness_function):
    avg_best = [0] * 40
    avg_avg = [0] * 40
    for i in range(40):
        for j in range(10):
            best_fitness, avg_fitness = loop("fps", "trunc", fitness_function)
            avg_best[i] += best_fitness[i]
            avg_avg[i] += avg_fitness[i]
        avg_best[i] = avg_best[i] / 10
        avg_avg[i] = avg_avg[i] / 10
    avg_avg.sort()
    avg_best.sort()
    fig = plt.figure()
    fig.suptitle('fps with truncation', fontsize=20)
    plt.plot(avg_best, label="average best")
    plt.plot(avg_avg, label="average average")
    plt.legend(loc='upper left')
    plt.show()


def loop(selection_scheme, survival_scheme, fitness_function):
    generation_num = 0
    parents = initialize(fitness_function)
    best_fitness = [] * 40
    avg_fitness = [] * 40
    population = parents
    while generation_num < 40:
        offspring = generation(population, selection_scheme)
        new_offspring = []
        for individual in offspring:
            individual.mutate()
            individual.calculate_fitness(fitness_function)
            new_offspring.append(individual)
        new_population = population + new_offspring
        population = survival(new_population, survival_scheme)
        fitness = get_fitness(population)
        best_fitness.append(max(fitness))
        avg_fitness.append(mean(fitness))
        generation_num += 1
    return best_fitness, avg_fitness


def survival(population, stype):
    survivors = []
    for i in range(0, 10):
        if stype == "binary":
            survivors.append(binary_tournament(population))
        elif stype == "fps":
            survivors.append(fitness_proportionate(population))
        elif stype == "trunc":
            survivors.extend(truncation(population))
            break
        elif stype == "rank":
            pop = rank_based(population)
            survivors.extend(pop[:int(len(pop)/2)])
            break
    return survivors


def get_fitness(population):
    fitness = []
    for i in population:
        fitness.append(i.fitness)
    return fitness


def random_select(population):
    return population[random.randint(0, len(population)-1)]


def generation(population, stype):
    offspring = []
    for i in range(0, int(len(population)/2)):
        if stype == "binary":
            offspring.extend(crossover(binary_tournament(population), binary_tournament(population)))
        elif stype == "fps":
            offspring.extend(crossover(fitness_proportionate(population), fitness_proportionate(population)))
        elif stype == "trunc":
            parent_1 = random_select(truncation(population))
            parent_2 = random_select(truncation(population))
            offspring.extend(crossover(parent_1, parent_2))
        elif stype == "rank":
            parent_1 = random_select(rank_based(population))
            parent_2 = random_select(rank_based(population))
            offspring.extend(crossover(parent_1, parent_2))
    return offspring


def binary_tournament(population):
    parent_1 = random_select(population)
    parent_2 = random_select(population)
    return parent_1 if parent_1.fitness > parent_2.fitness else parent_2


def fitness_proportionate(population):
    total_fitness = sum(c.fitness for c in population)
    random_num = random.uniform(0, 1)
    value = random_num * total_fitness
    for i in range(len(population)-1):
        value -= population[i].fitness
        if value <= 0:
            return population[i]
    return population[len(population)-1]


def truncation(population):
    population.sort(key=lambda x: x.fitness, reverse=True)
    truncate_percent = 0.5
    i = int(len(population) * truncate_percent)
    return population[:i]


def rank_based(population):
    population.sort(key=lambda x: x.fitness, reverse=True)
    return population


def initialize(fitness_function):
    parents = [None] * 10
    for i in range(0, 10):
        parents[i] = Individual()
        parents[i].initialize(x_bound2, y_bound2)
        parents[i].calculate_fitness(fitness_function)
    return parents


def crossover(parent_1, parent_2):
    offspring_1, offspring_2 = Individual(), Individual()
    # first offspring
    offspring_1.chromosome[0] = parent_1.chromosome[0]
    offspring_1.chromosome[1] = parent_2.chromosome[1]
    # second offspring
    offspring_2.chromosome[0] = parent_2.chromosome[0]
    offspring_2.chromosome[1] = parent_1.chromosome[1]
    return [offspring_1, offspring_2]


def f_function(value):
    x = value[0]
    y = value[1]
    return (x**2) + (y**2)


def f_function2(value):
    x = value[0]
    y = value[1]
    return 100 * (((x**2) - y)**2) + ((1 - x)**2)


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

if __name__ == "__main__":
    main()
