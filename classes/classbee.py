import random
from classfield import *
import copy


class Bee():
    def __init__(self, index):
        self.index = index
        self.genes = self.path()
        self.score = 0
        
    def path(self):
        f = Flowerfield()
        genes = random.sample(f.flowers, 50)
        return genes
    def fitness(self):
        score = []
        for i in range(0, len(self.genes)-1):
            T1 = copy.copy(self.genes[i])
            T2 = copy.copy(self.genes[i+1])
            D = abs(T2[0]-T1[0]) + abs(T2[1]-T1[1])
            score.append(D)            
        self.score = sum(score)
        print(score)
    def plot_bee_trajectory(self):
        traj = self.genes
        plt.plot(*zip(*traj), c='orange', linestyle=':')
        plt.scatter(*zip(*traj), c = 'blue', label='Flowers')
        plt.title('Trajectory of the bee : '+str(self.index))
        #plt.show()    





b1 = Bee(1)
#b1.plot_bee_trajectory()
b1.fitness()