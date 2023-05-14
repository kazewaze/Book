# Cool Code Snippets
-------

## Create vector of same length as input:

```py
# Element-wise Multiplication (vectors):
def ele_mul(number, vector):
    # Replace code below:
    output = [0, 0, 0]
    assert(len(output) == len(vector))

    # With this:
    output = [0] * len(vector) # It is uh very nice :) yes. 

    for k in range(len(vector)):
        output[k] = number * vector[k]
    
    return output
```