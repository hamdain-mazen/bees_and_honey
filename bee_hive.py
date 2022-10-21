import pandas as pd
import copy
import random
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
import time

start_time = time.time()

class Bee:
    """classe Bee avec l'index, les gènes et score """
    def __init__(self, id):
        self.id = id
        self.genome = self.get_genes()
        self.score = self.get_score()


    def get_genes(self):
        """ retourne les gènes sous forme de tuple """
        data = pd.read_csv("flowerData.csv", delimiter=',')
        df = pd.DataFrame(data, columns=['x','y']) 
            
        tuple_gene = [tuple((df.loc[q])) for q in range(len(df))]
        np.random.shuffle(tuple_gene)
        return tuple_gene 

    def get_score (self):
        """Retourne la distance entre deux points avec la méthode de Manhatan"""
        dist = 0
        coord_ruche = (500,500)
        parcours = [coord_ruche] + self.genome +  [coord_ruche ]
        #[(500,500) ] + [(),()] + [(500,500) ]
        for i in range(len(parcours) - 1):
            dist_ligne=  abs(parcours[i][0]- parcours[i+1][0]) + abs(parcours[i][1]-parcours[i+1][1])
            dist += dist_ligne
            
        return dist

class BeeHive ():
    """ Classe ruche qui représente notre population d'abeilles """
    def __init__(self):
        self.population = [Bee(i) for i in range(100)]   # population constituée de 100 Aabeilles
        self.scores = self.get_score_hive()     

    def get_score_hive(self):
        """ Retourne des scores qui sont la somme des  distances"""
        scores=[]
        for beee in self.population:
            beee.score
            scores.append(beee.score)
            
            #sorted_scores = sorted(self.scores)
        return scores

    def get_mean(self) :
        """ Retourne la moyenne des scores de la ruche"""
        score_mean = np.mean(self.scores)
        return score_mean

    def selection(self):
        """ Sélection à partir de la populaion de base des meilleurs abeilles selon leurs scores """
        
        self.new_population = deepcopy(self.population)   # copier la population pour éviter la modification de la populatio de base
        self.new_population.sort(key = lambda x: x.score,reverse=False)
        #self.population.sort(key = lambda x: self.get_score_hive(),reverse=True)
        self.new_population = self.new_population[:50]    # Récupération des 50 meilleures abeilles
        
        return self.new_population
        
    def cross_over(self):
        """ Croisement enre les gènes issus de la sélection"""
        children = []
        for p in range(0, len(self.new_population), 2):
            P1 = self.new_population[p].genome            # Choix des parents par paire
            P2 = self.new_population[p+1].genome
            child1 = P1[:25]
            child2 = P2[:25]
            child1 += P2[25:]
            child2.extend(P1[25:])
            children.extend([child1, child2] )

        new_population = [bee.genome for bee in self.new_population ]+ children # Reconstitution de la nouvelle population avec les gènes nouvellement formés et les 50 meilleurs abeilles issus de la sélection
        for i, bee in enumerate(self.population) :
            bee.genome = new_population[i] 
            bee.score = bee.get_score()

        self.scores = self.get_score_hive()
        return new_population

    def mutation(self):
        """Appliquer  la mutation à  une séquence de gènes par inversion """
        new_population = self.cross_over()
        lenght = 40
        for child in new_population :
            start_part = random.randint(0, len(child)- lenght + 2)  #Début mutation
            portion = child[start_part : start_part + lenght]
            portion.reverse()
            mutant = child[0:start_part] + portion + child[start_part+lenght:len(child)]  #gène mutant
            child = mutant

        for i, bee in enumerate(self.population) :
            bee.genome = new_population[i] 
            bee.score = bee.get_score()

        self.scores = self.get_score_hive()
        return new_population


    def evolution(self , generation):
        """Tourner le process de la sélection, cross-over à n génération """
        mean_liste =[]
        generations =[]
        #BeeHive()
        i = 0
        while i <= generation:
            meann = self.get_mean()
            mean_liste.append(meann)
            generations.append(i)
            # print("Génération ", i)
            # print("Moyenne de la génération ", meann)
            # [ print (bee.genome[0]) for bee in self.population[:2] ]
            #print(self.scores)
            
            self.selection()
            self.cross_over()
            if i ==  5 :
                self.mutation()
            i += 1

        plt.plot(generations, mean_liste)
        plt.xlabel("Nombre de génération")
        plt.ylabel("fitness")
        print('Exécution time ', round(time.time() -start_time, 2), "s")
        plt.show()


   
# bee = BeeHive()

# bee.get_score_hive()
# bee.get_mean()
# bee.selection()
# print(bee.cross_over())
# bee.mutation()
# bee.evolution( 100)








       

    











































