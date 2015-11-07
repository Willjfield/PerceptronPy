import math
import numpy as np

#Each tuple has (input t/f,input t/f, inputa)
#### SEPARATE trainSetOR inputs from answers, change p.train() function accordingly
trainSetOR = 	[[1,1,1],
		[1,0,1],
		[0,1,1],
		[0,0,1]
		]
trainSetORa = [1,1,1,0]

#Inputs are a random set of test values
#inputs = np.random.randint(-1,1,size=(2))
#inputs = np.append(inputs,1)


class Perceptron:
	weights = np.random.randint(-1,1,size=(3))
	c = .001
	
	def activate(_sum):
		if(_sum>0):
			return 1
		else:
			return -1
	
	def feedForward(_inputs=[]):
		fSum = 0
		for i in _inputs:
			fSum+=_inputs[i]*weights[i]
		return activate(fSum)
			
	def train(_inputs=[],desired=[]):
		for i in _inputs:
			#_inputsxy=_inputs[1:2]
			error = desired[i]-feedForward(_inputs)
			weights[i]+=error*c*i
p = Perceptron()
#for i in trainSetOR:
#	p.train(trainSetOR[i],trainSetORa[i])
#p.train(inputs,1)
#print(p.weights)
#print(p.inputs)
#print(trainSetOR[0][0])
theSum = p.feedForward(trainSetOR)
