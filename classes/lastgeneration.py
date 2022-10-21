
import pandas as pd
import copy
import random
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
import time
start_time = time.time()






class Bee:
    def __init__(self, id):
        
        self.id = id
        self.genome = self.get_genes()
        self.score = self.get_score()


    def get_genes(self):
        data = pd.read_csv("flowerData.csv", delimiter=',')
        df = pd.DataFrame(data, columns=['x','y']) 
            
        tuple_gene = [tuple((df.loc[q])) for q in range(len(df))]
        np.random.shuffle(tuple_gene)

       

        return tuple_gene 

    def get_score (self):
        dist = 0
        coord_ruche = (500,500)
        parcours = [coord_ruche] + self.genome +  [coord_ruche ]
        #[(500,500) ] + [(),()] + [(500,500) ]
        for i in range(len(parcours) - 1):
            dist_ligne=  abs(parcours[i][0]- parcours[i+1][0]) + abs(parcours[i][1]-parcours[i+1][1])
            dist += dist_ligne
            
        return dist

class BeeHive ():
    def __init__(self):
        self.population = [Bee(i) for i in range(100)]
        self.scores = self.get_score_hive()
        self.memory_evolution = []

    
    # def create_population(self):

    #     population = [Bee(i) for i in range(100)]
    #     return population

    def get_score_hive(self):
        scores=[]
        for beee in self.population:
            beee.score
            scores.append(beee.score)
            
            #sorted_scores = sorted(self.scores)
        
            
            #sorted_scores = np.argsort(slf.scores)
         
        return scores

    def get_mean(self) :

       score_mean = np.mean(self.scores)
       return score_mean

    
    
    def selection(self, nb_selection = 50):
        
        self.new_population = deepcopy(self.population) 
       
        self.new_population.sort(key = lambda x: x.score,reverse=False)
        #self.population.sort(key = lambda x: self.get_score_hive(),reverse=True)
        self.new_population = self.new_population[:nb_selection]
           
        return self.new_population
        
    def cross_over(self):
        new_population = self.selection()
        children = []
        for p in range(0, len(self.new_population), 2):
            P1 = self.new_population[p].genome
            P2 = self.new_population[p+1].genome
        
            child1, child2 = [] , []
            child1 = P1[:25]
            child2 = P2[:25]
    
            child1 += P2[25:]
        #child2 += P1[25:]
            child2.extend(P1[25:])
            children.extend([child1, child2] )

        new_population = self.new_population + children
        return new_population
        

    
    def mutation(self, nb_mutation=5):
        
        new_pop = self.selection(nb_selection= 100- nb_mutation)
        new_Bees = [Bee(k) for k in range(nb_mutation)]  # self.cross_over()
        
        return new_pop + new_Bees

    def evolution(self, nb_gene=1000):
        liste_perf = []
        
        for i in range(nb_gene):
            
            self.memory_evolution.append(self.population)
            self.population = self.mutation(nb_mutation=abs(100-int(i/10)))   # on écrase l'ancienne population avec la nouvelle
            
            
            self.scores = self.get_score_hive()   #  Calculer le score de la nouvelle population
            new_score = self.get_mean()           #
            liste_perf.append(new_score)
        
        return liste_perf



    def plot_performance(self, nb_gene=1000):
        performance= self.evolution(nb_gene=nb_gene)
        plt.plot(performance)
        plt.xlabel('Generation of bees')
        plt.ylabel('Fitness score')
        plt.title('fitness score for n generations')
        print('Execution time',round(time.time()-start_time,2),'s') 
        plt.show()




bee = BeeHive()
#print(bee.mutation()[50][0])    #Bee(0), ....  , [(x,y) ..... ]] 

bee.plot_performance(nb_gene=1000) 
           