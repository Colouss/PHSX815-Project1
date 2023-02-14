#visualizing the data
# main function for this Python code
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import math
if __name__ == "__main__":
    tru0 = []
    tru1 = []
    counter = 0
    counter1 = 0
    counter2 = 0
    file0 = open('H0.txt', 'r') # Opens up a text file
    trufile = file0.read().split() # Split the data into a readable format for the program
    for i in range(0,Ntoss): # Add the data from the text file to an array
        C = int(trufile[i])
        if C == 4 or C == 5: #Take note of the amount of super-rare rolled, and count the limited rares
          tru1.append(C)
          counter1 = counter1+1
          if C == 5:
            counter = counter+1
        else:
          if C == 0:
            counter2 = counter2+1 #Count the amount of super-rares rolled
          tru0.append(C)
    file0.close()
sns.histplot(tru0, stat="percent", discrete=True, shrink=0.3); #Plot the categorical proportion
plt.show()
print(" ")
plt.clf()
sns.histplot(tru1, stat="count", discrete=True, shrink=0.2); #Plot the Bernoulli proportion
plt.show()
counter3 = counter1 - counter

L01 = (0.02**counter2)*((1-0.02)**(500-counter2)) #Calculate the likelihood of getting a super-rare, as well as the likelihood that the super-rare is a limited time.
L02 = (0.25**counter)*((1-0.25)**(counter3))

#This is to create data for the second simulation
counter = 0
counter1 = 0
counter2 = 0
file0 = open('H1.txt', 'r') # Opens up a text file
trufile = file0.read().split() # Split the data into a readable format for the program
for i in range(0,Ntoss): # Add the data from the text file to an array
    C = int(trufile[i])
    if C == 4 or C == 5: #Take note of the amount of super-rare rolled, and count them up
      tru1.append(C)
      counter1 = counter1+1
      if C == 5:
        counter = counter+1
    else:
      if C == 0:
        counter2 = counter2+1 #Count the amount of super-rares rolled
      tru0.append(C)
file0.close()
sns.histplot(tru0, stat="percent", discrete=True, shrink=0.3); #Plot the categorical proportion
plt.show()
print(" ")
plt.clf()
sns.histplot(tru1, stat="count", discrete=True, shrink=0.2); #Plot the Bernoulli proportion
plt.show()
counter3 = counter1 - counter

L11 = (0.04**counter2)*((1-0.04)**(500-counter2)) #Calculate the likelihood of getting a super-rare, as well as the likelihood that the super-rare is a limited time.
L12 = (0.15**counter)*((1-0.15)**(counter3))
LR1 = L01/L11
LR2 = L02/L12
print("Likelihood ratio one :", LR1)
print("Likelihood ratio two :", LR2)
