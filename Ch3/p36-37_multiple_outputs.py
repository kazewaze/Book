'''
Multiple Outputs (Chapter 3 - Page 36-37):
'''

# Weights:
weights = [0.3, 0.2, 0.9]

# Data:
wlrec = [0.65, 0.8, 0.8, 0.9]

# Input:
input = wlrec[0]

# Element-wise Multiplication (vectors):
def ele_mul(number, vector):
    output = [0, 0, 0]

    assert(len(output) == len(vector))

    for k in range(len(vector)):
        output[k] = number * vector[k]

    return output

def neural_network(input, weights):
    pred = ele_mul(input, weights)

    return pred

# Prediction:
print(neural_network(input, weights))