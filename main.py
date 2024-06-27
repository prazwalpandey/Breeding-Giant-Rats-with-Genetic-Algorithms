import time
import random
import statistics

#Defining Constants (weight in gms).
goal = 50000 # 50kg of mutated rat
num_rats = 20 # How many rats undergo experiment in the lab
initial_min_wt = 200 #Minimum lab rat weight
initial_max_wt = 600 #Maximum lab rat weight
initial_mode_wt = 350 ##Moderate lab rat weight
mutate_odds= 0.01 #Probability of mutation
mutate_min= 0.5 #Scalar on rat weight of least beneficial mutation
mutate_max= 0.2 #Scalar on rat weight of most beneficial mutation
litter_size= 8 #Pups per pair of mutating rats
litters_per_year= 10 #No of litters per year per pair of mating rats
generation_limit = 500 #Generational cutoff to stop breeding program