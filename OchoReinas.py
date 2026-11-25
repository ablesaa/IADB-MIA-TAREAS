import random 

def genetic_algorithm(pop_size, mutation_rate, generations):
    # Algoritmo genético principal
    population = []
    for _ in range(pop_size):
        chromosome = list(range(8))
        random.shuffle(chromosome)
        population.append(chromosome)

    for gen in range(generations):
        new_population = []
        for _ in range(pop_size):
            parents = select_parents(population, fitness, 2)
            child = crossover(parents[0], parents[1])
            child = mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population

    best_chromosome = max(population, key=fitness)
    return best_chromosome

def select_parents(population, fitness_fn, num_parents):
    parents = []
    for _ in range(num_parents):
        # Realizar la selección por ruleta
        total_fitness = sum(fitness_fn(chrom) for chrom in population)
        pick = random.uniform(0, total_fitness)
        current_fitness = 0
        for chrom in population:
            current_fitness += fitness_fn(chrom)
            if current_fitness > pick:
                parents.append(chrom)
                break

    if len(parents) < 2:
        parents = select_parents(population, fitness_fn, num_parents)

    return parents

def crossover(parent1, parent2):
    # Cruce de dos padres para producir un descendiente
    n = len(parent1)
    crossover_point = random.randint(1, n - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child
 
def mutate(chromosome, mutation_rate):
    # Mutación de un cromosoma con una cierta probabilidad
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = random.randint(0, len(chromosome) - 1)
    return chromosome
 
def fitness(chromosome):
    # Función de aptitud: cuántas reinas no se amenazan mutuamente
    n = len(chromosome)
    clashes = 0
    for i in range(n):
        for j in range(i+1, n):
            if chromosome[i] == chromosome[j] or abs(chromosome[i] - chromosome[j]) == j - i:
                clashes += 1
    return n - clashes

best_solution = genetic_algorithm(pop_size=100, mutation_rate=0.1, generations=20)
print("Mejor solución encontrada:", best_solution)
