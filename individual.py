#!/usr/bin/python
import random


class Individual(object):

    def __init__(self):
        self._chromosome = [0.0, 0.0]
        self._fitness = 0.0
        self.is_selected = False
        self._x_bounds = [0.0, 0.0]
        self._y_bounds = [0.0, 0.0]

    def initialize(self, x_bounds, y_bounds):
        self._x_bounds = x_bounds
        self._y_bounds = y_bounds
        x_rand = random.uniform(x_bounds[0], x_bounds[1])
        y_rand = random.uniform(y_bounds[0], y_bounds[1])
        self._chromosome = [x_rand, y_rand]

    def mutate(self):
        mutate_val = random.uniform(0, 1)
        value = random.uniform(-0.25, 0.25)
        mutation_rate_for_mutation = 0.01
        mutated_x = 0
        mutated_y = 0
        # mutates only 1% of the time
        if mutate_val < mutation_rate_for_mutation:
            mutated_x += value
            mutated_y -= value
            if mutated_x in self._x_bounds:
                self._chromosome[0] = mutated_x
            if mutated_y in self._y_bounds:
                self._chromosome[1] = mutated_y

    @property
    def chromosome(self):
        return self._chromosome

    @chromosome.setter
    def chromosome(self, value):
        self._chromosome = value

    @property
    def fitness(self):
        return self._fitness

    def calculate_fitness(self, ffunction):
        self._fitness = ffunction(self._chromosome)

    def __str__(self):
        return str(self._chromosome)

    __repr__ = __str__


