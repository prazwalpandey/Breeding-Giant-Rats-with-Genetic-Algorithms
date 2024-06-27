import time
import random
import statistics

#Defining Constants ( in gms).
goal = 50000 # 50kg of mutated rat
num_rats = 20 # How many rats undergo experiment in the lab
initial_min_wt = 200 #Minimum lab rat weight
initial_max_wt = 600 #Maximum lab rat weight
initial_mode_wt = 350 ##Moderate lab rat weight
mutate_odds= 0.01 #Probability of mutation
mutate_min= 0.5 #Scalar on rat weight of least beneficial mutation
mutate_max= 0.2 #
litter_size= 8
litters_per_year= 10
generation_limit = 500