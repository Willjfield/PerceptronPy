#Following tutorial by Danlio Bargen
#https://blog.dbrgn.ch/2013/3/26/perceptrons-in-python/

from random import choice
from numpy import array, dot, random

#This is the activate function that will "fire" if the input (x) is 1 or not if it's 0
def unit_step(x):
	if x<0:
		return 0
	else: 
		return 1
#The training array for OR statements. It contains True,False,Bias,Answer for each possible scenario
trainOR = [
	(array([0,0,1]),0),
	(array([0,1,1]),1),
	(array([1,0,1]),1),
	(array([1,1,1]),1),
	]
#Weights will be an array of 3 random numbers between 0 and 1 to serve as initial weightsthat will change based on results
weight = random.rand(3)

#c is the learning constant. How much each lesson matters.
c = 0.2
#n is the number of "lessons" to be taught
n = 4000

#for each lesson
for i in range(n):
	#expected equals one of the arrays, randomly chosen the trainOR set
	x, expected = choice(trainOR)
	#the result equals the expected times the weights
	#Works because the dot product equals E(a*b)
	result = dot(weight,x)
	#error is the expected minus whether the result triggered the "neuron"
	#this will either be 1,0, or -1
	error = expected - unit_step(result)
	#alter the weights to correct the next pass
	weight += c*error*x

#for each input from trainOR. WHY THE _ ????
for x,_ in trainOR:
	#results for trainOR inputs with FINAL weights. Basically, at the end of all these tests, which weights will give you the correct outputs?
	result = dot(x,weight)
	#python regexing to print the input, resulting weights and the predicted result (0 or 1)
	print("{}: {} -> {}".format(x[:2],result,unit_step(result)))


