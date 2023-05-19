'''
Multiple Inputs & Outputs Experiment (Chapter 3 - Pages 38-41)
  - Extended Code (Not the original code in book)
  - "I extended the original code to include every game."
'''

# Weights: #toes  %win  #fans
weights = [ [0.1, 0.1, -0.3], # hurt?
            [0.1, 0.2, 0.0],  # win?
            [0.0, 1.3, 0.1] ] # sad?

number_of_games = 4

final_prediction = [0] * number_of_games

# Helper Function for printing predictions neatly:
def pretty_print(pred):
    for i in range(len(pred)):
        print("\nGame " + str(i+1) + ": " + str(pred[i]) + "\n")

# Simple Function for returning input for every game:
def input_for_every_game(idx):
    # Data:
    toes = [8.5, 9.5, 9.90, 9.00]
    wlrec = [0.65, 0.8, 0.8, 0.9]
    nfans = [1.2, 1.3, 0.50, 1.0]

    # Current Input:
    return [toes[idx], wlrec[idx], nfans[idx]]

# Weighted Sum (Dot Product) Function:
def w_sum(a, b):
    assert(len(a) == len(b))

    output = 0

    for k in range(len(a)):
        output += (a[k] * b[k])

    return output

# Vector-Matrix Multiplication Function:
def vec_mat_mul(vector, matrix):
    assert(len(vector) == len(matrix))

    output = [0] * len(vector)

    for k in range(len(vector)):
        output[k] = w_sum(vector, matrix[k])

    return output

# Neural Network Function:
def neural_network(input, weights):
    game_pred = vec_mat_mul(input, weights)

    return game_pred

# Predict every game:
for w in range(len(weights)+1):
    current_input = input_for_every_game(w)

    current_pred = neural_network(current_input, weights)

    final_prediction[w] = current_pred

# Prediction:
print(pretty_print(final_prediction))