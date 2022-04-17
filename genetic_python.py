import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class Gene:
    def _init_(self, input_array_x):
        self.input_array_x = input_array_x
        self.create_gene()
        
    def create_gene(self):    
        weight1 = np.random.uniform(low=-1, high=1,size=(3,2))
        weight2 = np.random.uniform(low=-1, high=1,size=(2,3))
        h_array = np.dot(self.input_array_x,weight1)
        f_array = np.dot(h_array,weight2)
        
        yield_calculated = f_array[0] + f_array[1] + f_array[2]
        yield_real = (self.input_array_x[0] + self.input_array_x[1] + self.input_array_x[2])/3
        error_calculated = yield_real - yield_calculated
        self.error_to_sum = math.sqrt(pow(error_calculated,2))
     
class Chromosome:        
    def _init_(self, input_values):
        self.input_values = input_values
        self.fitness = 0.00000000
        self.individual = []
        self.create_chromosome()
        self.calculate_fitness()

    def calculate_fitness(self): 
        for i in range(12):
            self.fitness += self.individual[i].error_to_sum 
        
    def create_chromosome(self):
        for j in range(12):
            i=np.random.randint(low=0, high=99)
            input_array_x = np.array([input_values[i][1],input_values[i][2],input_values[i][3]])
            self.individual.append(Gene(input_array_x))
            

    
class GeneticAlgorithm:
    def _init_(self,input_values):
        self.input_values = input_values
        self.pop = []
        
    def ga(self):
        self.init_pop()

    def init_pop(self):
        for i in range(16):
            chromosome = Chromosome(input_values)
            self.pop.append(chromosome)
        for k in range(16):   
            print(self.pop[k].fitness)
    
    def print_fitness_errors(self):
        print('Fitness errors of chromosomes\n[')
        print(self[0].fitness)    
        i=1
        for i in range(11):
            print(',')
            print(self[i].fitness)   
        print(']\n')

if _name_ == '_main_':
    df = pd.read_csv('C:\Users\hale.sahin\Desktop\sample_data.csv', sep=',')
    input_values = np.array(df).reshape(100,5)
    strt = GeneticAlgorithm(input_values)
    strt.ga()
    pass