from main import *
import matplotlib.pyplot as plt
import numpy as np


def even_rats(num_rats):
    """Making sure the the number of rats in even number for mating pair."""
    if num_rats % 2 != 0:
        num_rats += 1
    return num_rats


def plotting(num_rats=50, mutate_odds=0.01):
    generations = 0
    num_rats = even_rats(num_rats)
    parents = population(num_rats, initial_min_wt, initial_max_wt, initial_mode_wt)
    population_fitness = fitness(parents, goal)

    while population_fitness < 1 and generations < generation_limit:
        selected_females, selected_males = selection(parents, num_rats)
        children = breeding(selected_females, selected_males, litter_size)
        children = mutating(children, mutate_odds, mutate_min, mutate_max)
        parents = selected_males + selected_females + children
        population_fitness = fitness(parents, goal)
        generations += 1
    return int(generations / litters_per_year)


# ==================================================================================================
# ==================================================================================================


dic = {}
dic1 = {}
for i in np.arange(0.01, 1.01, 0.04):
    dic[i] = plotting(mutate_odds=i)
for i in np.arange(50, 2001, 50):
    dic1[i] = plotting(num_rats=i)
mutation_array = np.array(list(dic.keys()))
year_array = np.array(list(dic.values()))
mutation1_array = np.array(list(dic1.keys()))
no_array = np.array(list(dic1.values()))

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(mutation_array, year_array)
plt.ylim(0, 50)
plt.xlabel("Mutation Odds")
plt.ylabel("Number of Years")
plt.title("Number of Years to Reach Goal vs Mutation Odds")


plt.subplot(1, 2, 2)
plt.plot(mutation1_array, no_array)
plt.ylim(0, 50)
plt.xlabel("Number of Rats")
plt.ylabel("Number of Years")
plt.title("Number of Rats to Reach Goal vs Mutation Odds")

plt.tight_layout()
plt.show()
