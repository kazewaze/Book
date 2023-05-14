'''
Simplest Neural Network (Chapter 3 - Pages 24-27):
  - Single Weight
  - Single Input Datapoint
'''

# Weight (single) ~ [knowledge]:
weight = 0.1

# Data:
number_of_toes = [8.5, 9.5, 10, 9]

# Input (single) ~ [information]:
input = number_of_toes[0]

# Neural Network:
def neural_network(input, weight):
    pred = input * weight
    return pred

# Prediction:
print(neural_network(input, weight))