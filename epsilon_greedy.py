#based on lazy_programmer
#Programmer : Farhad-UPC
from __future__ import print_function, division
from builtins import range
# update your version of future --- >  sudo pip install -U future

import numpy as np
import matplotlib.pyplot as plt


#"__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. 
#This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
#The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.

class Bandit:
  def __init__(self, true_mean):   #The constructor takes in one parameter as true mean / set the instance variables, mean and N, to zero
    self.true_mean = true_mean
    self.mean = 0    #our estimate of the bandit's mean
    self.N = 0
  #simulates pulling the bandit's arm
  def pull(self):
    return np.random.randn() + self.true_mean
  #update function which takes an X -> the latest sample received from the bandit.
  #Tip: mean_x = (1 - N) mean_x_N-1  + 1/N x_N    ---->    calculate the mean in a computationally efficient way.
  def update(self, x):
    self.N += 1
    self.mean = (1 - 1.0/self.N)*self.mean + 1.0/self.N*x


def experiment(mean_1, mean_2, mean_3, eps, N):
  bandits = [Bandit(mean_1), Bandit(mean_2), Bandit(mean_3)]
  #N : the number of times we put.
  data = np.empty(N)   # keep our results in an array called data of size N.
  # generate a random number P between zero and one. If P is less than epsilon, we choose a bandit at random. Otherwise, we choose the bandit with the best current sample mean.
  for i in range(N):
    p = np.random.random()
    if p < eps:
      j = np.random.choice(3)
    else:
      j = np.argmax([b.mean for b in bandits])
    x = bandits[j].pull()
    bandits[j].update(x)

    data[i] = x   
  # calculate the cumulative average.
  cumulative_average = np.cumsum(data) / (np.arange(N) + 1)  #numpy.cumsum (Return the cumulative sum of the elements along a given axis)

  for b in bandits:
    print(b.mean)

  return cumulative_average



#different epsilon : 10%, 5%, and 1%.
#if __name__ == '__main__':    --->    the main block of a module is executed when it is imported for the first time, ...>
# ...> But if we want the block to run only if the module was started as a stand-alone program, but not if it was imported from another module

if __name__ == '__main__':
  c_1 = experiment(1.0, 2.0, 3.0, 0.1, 100000)
  c_05 = experiment(1.0, 2.0, 3.0, 0.05, 100000)
  c_01 = experiment(1.0, 2.0, 3.0, 0.01, 100000)
  
  # log scale plot
  plt.plot(c_1, label='eps = 0.1')
  plt.plot(c_05, label='eps = 0.05')
  plt.plot(c_01, label='eps = 0.01')
  plt.legend()
  plt.xscale('log')
  plt.show()


  # linear plot
  plt.plot(c_1, label='eps = 0.1')
  plt.plot(c_05, label='eps = 0.05')
  plt.plot(c_01, label='eps = 0.01')
  plt.legend()
  plt.show()







	

	



		
	    

	 






	      
	
	



  




