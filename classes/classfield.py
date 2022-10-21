import random
import pandas as pd
import matplotlib.pyplot as plt



class Flowerfield:
    def __init__(self):
        self.flowers = self.grow_flowers()
    
    def grow_flowers(self):
        df = pd.read_csv('flowerData.csv')
        subset = df[['x', 'y']]
        
        flowers = [tuple(x) for x in subset.to_numpy()]
        del df
        return flowers
    
    def show_field(self):
        plt.figure(0)
        plt.scatter(*zip(*self.flowers), c = 'blue', label='Flowers')
        plt.scatter(500, 500, c = 'red', label ='Hive')
        plt.legend()
        plt.show()


f=Flowerfield()
f.show_field()

