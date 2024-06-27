import time
import random
import statistics

# Defining Global Constants (weight in gms).
goal = 50000  # 50kg of mutated rat
num_rats = 20  # How many rats undergo experiment in the lab
initial_min_wt = 200  # Minimum lab rat weight
initial_max_wt = 600  # Maximum lab rat weight
initial_mode_wt = 350  ##Moderate lab rat weight
mutate_odds = 0.01  # Probability of mutation
mutate_min = 0.5  # Scalar on rat weight of least beneficial mutation
mutate_max = 0.2  # Scalar on rat weight of most beneficial mutation
litter_size = 8  # Pups per pair of mutating rats
litters_per_year = 10  # No of litters per year per pair of mating rats
generation_limit = 500  # Generational cutoff to stop breeding program
"""Making sure the the number of rats in even number for mating pair."""
if num_rats % 2 != 0:
    num_rats += 1


# ===================================================================================================
def main():
    """Firstly lets initialize population, select, breed and mutate, display results."""
    generations = 0
    parents = population(num_rats, initial_min_wt, initial_max_wt, initial_mode_wt)
    print(f"Initial population weights = {parents}")
    population_fitness = fitness(parents, goal)
    print(f"Initial Population fitness = {population_fitness}")
    print(f"Number to retain = {num_rats}")

    """
    At the end of the project we will plot a graph between the avg_wt of each generation through out the years.
    """
    avg_wt = []

    while population_fitness < 1 and generations < generation_limit:
        # Firstly we will select a particular range of rats. Genetic algorithm tends to us the process of natural selction.
        selected_females, selected_males = selection(parents, num_rats)
        # Now, proceeding for the children breeding among the selected population.
        children = breeding(selected_females, selected_males, litter_size)
        # After breeding let's take mutation into account if feasible by algorithm.
        children = mutating(children, mutate_odds, mutate_min, mutate_max)
        parents = selected_males + selected_females + children
        population_fitness = fitness(parents, goal)
        print(f"Generation {generations} fitness = {population_fitness}")
        avg_wt.append(int(statistics.mean(parents)))
        # We have accounted for GENERATION LIMIT OF 500 and through each loop we will go for
        generations += 1

    print(f"Average weight per generation =  {avg_wt}")
    print(f"\n Number of Generations = {generations}")
    print(f"\n Number fo years = {int(generations/litters_per_year)}")


def population(num_rats, min_wt, max_wt, mod_wt):
    """Initializint the weight of the population using random.triangular to skew the larger weigth to the moderate weight ones."""
    return [int(random.triangular(min_wt, max_wt, mod_wt)) for i in range(num_rats)]


def fitness(population, goal):
    # Calulating the avg(mean) population fitness.
    avg = statistics.mean(population)
    return avg / goal


def selection(population, to_retain):
    """Culling a population to retain only a specified number of members."""
    sorted_population = sorted(population)
    # Getting the heaviest weight.
    to_retain_by_sex = to_retain // 2
    # We do this so that heaviest of the population is from both the sex else the heaviest would be only from the males one.
    members_per_sex = len(sorted_population) // 2
    # Here, assuming the heaviest of female is of less weight than lightest of male.
    females = sorted_population[:members_per_sex]
    males = sorted_population[members_per_sex:]
    # Now, Retaining only the heaviest of the both sex.
    retained_females = females[-to_retain_by_sex:]
    retained_males = males[-to_retain_by_sex:]
    return retained_females, retained_males


def breeding(selected_females, selected_males, lit_size):
    """Crossover genes among members(weights) of a population."""
    random.shuffle(selected_males)
    random.shuffle(selected_females)
    children = []
    for female, male in zip(selected_females, selected_males):
        for child in range(litter_size):
            child = random.randint(female, male)
            children.append(child)
    return children


def mutating(children, mutation_prob, min_odd, max_odd):
    """Randomly alter rat weights using input odds & fractional changes."""
    for index, rat in enumerate(children):
        # if the odds in favor
        if mutate_odds >= random.random():
            # children gets mutated.
            children[index] = round(rat * random.uniform(min_odd, max_odd))
    return children


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"\n Runtime for this program was {end_time - start_time} seconds.")
