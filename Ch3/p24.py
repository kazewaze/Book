from alva import Alva
alv = Alva()

# Input data:
number_of_toes = [8.5, 9.5, 10, 9]
# Weight for the data:
weight = 0.1

def neural_network(input, weight):
    pred = input * weight
    return pred

alv.show_percentage(neural_network(number_of_toes[0], weight))