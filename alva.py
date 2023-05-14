'''
Playing around with Python by making my own Dataset Toolkit
  - Kaycee Ingram <kazewaze>
'''

class Array:
    def __init__(self, array):
        self.array = array

    def dot(self, index, weights):
        assert(len(self.array[index]) == len(weights))

        output = 0

        for i in range(len(self.array[index])):
            output += (self.array[index][i] * weights[i])

        return output

    def shape(self):
        return (len(self.array), len(self.array[0]))

class Alva:
    @classmethod
    def array(self, array):
        return Array(array)

    @classmethod
    def zeros(self, dims):
        matrix = []

        for i in range(dims[0]):
            matrix.append([])
            for j in range(dims[1]):
                matrix[i].append(0)

        return matrix

    @classmethod
    def build_input(self, *input):
        input_build = []

        for a in range(0, len(input[0])):
            input_build.append([])
            for b in range(0, len(input)):
                input_build[a].append(input[b][a])

        return Array(input_build)

    @classmethod
    def show_results(self, calcs):
        results = ''

        for i in range(len(calcs)):
            results += ' \n Calc %(index)s: %(calc)s \n' % {"index": str(i+1), "calc": str(calcs[i])}

        return results

    @classmethod
    def show_percentage(self, result):
        if (isinstance(result, (int, float)) == True):
            print(str(result * 100) + '%')
        else:
            print("Error: Wrong output data type")