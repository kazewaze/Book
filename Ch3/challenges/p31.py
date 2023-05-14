'''
Vector Math Challenge (Chapter 3 - Page 31):
  def elementwise_multiplication(vec_a, vec_b)
  def elementwise_addition(vec_a, vec_b)
  def vector_sum(vec_a)
  def vector_average(vec_a)

  def w_sum(dataset, weights)
'''

# Challenge 1 - Data (write funcs):
vec_a, vec_b = [1, 2, 3], [4, 5, 6]

# Challenge 2 - Data (perform dot product with funcs):
dataset, weights = [8.5, 0.65, 1.2], [0.1, 0.2, 0.0]

# Challenge 1 (write funcs):
def elementwise_multiplication(vec_a, vec_b):
    assert(len(vec_a) == len(vec_b))

    result = []

    for k in range(len(vec_a)):
        result.append(vec_a[k] * vec_b[k])

    return result

def elementwise_addition(vec_a, vec_b):
    assert(len(vec_a) == len(vec_b))

    result = []

    for k in range(len(vec_a)):
        result.append(vec_a[k] + vec_b[k])

    return result

def vector_sum(vec_result):
    result = 0

    for k in range(len(vec_result)):
        result += vec_result[k]

    return result

def vector_average(vec_result):
    return vector_sum(vec_result) / len(vec_result)

# Challenge 2 (perform dot product or 'weighted sum' with funcs):
def w_sum(dataset, weights):
    predictions = elementwise_multiplication(dataset, weights)

    return vector_sum(predictions)

# Challenge 1 - Results (write funcs):
print(elementwise_multiplication(vec_a, vec_b)) # --> [4, 10, 18]
print(elementwise_addition(vec_a, vec_b)) # --> [5, 7, 9]
print(vector_sum(vec_a)) # --> 6
print(vector_average(vec_a)) # --> 2.0

# Challenge 2 - Results (perform dot product with funcs):
print(w_sum(dataset, weights)) # --> 0.9800000000000001