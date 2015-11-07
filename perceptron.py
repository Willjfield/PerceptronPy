import math
import numpy as np

trainSetOR = 	[(1,1,1),
		(1,0,1),
		(0,1,1),
		(0,0,0)
		]

inputs = np.random.randint(-1,1,size=(2))
inputs = np.append(inputs,1)


class Perceptron:
	weights = np.random.randint(-1,1,size=(len(inputs)))
	weights = np.append(weights,1)
	fSum = 0
	c = .001
	
	def activate(_sum):
		if(_sum>0):
			return 1
		else:
			return -1
	
	def feedForward(_inputs):
		for i in _inputs:
			fSum+=_inputs[i]*weights[i]
		return activate(fSum)
			
	def train(_inputs, desired)
		for i in _inputs:
			error = desired-feedForward(_inputs)
			weights[i]+=error*c*_inputs[i]
p = Perceptron()
print(p.weights)
print(p.inputs)
