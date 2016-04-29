

class Perceptron:

    def __init__(self, inp, threshold=None, weights=[]):
        self.input_layer = inp
        self.weights = weights
        if threshold != None:
            self.threshold = threshold

    def fire(self, inputs_fire_function):
        total = 0
        index = 0
        for i in inputs_fire_function:
            total += i * self.weights[index]
            index += 1

        if total > self.threshold:
            return 1
        else:
            return 0

out1 = Perceptron(False, 1.5, [-1, 2, -1, 2, -1, 2, -1, 2, -1, 2])
out2 = Perceptron(False, 1.5, [-1, -1, 2, 2, -1, -1, 2, 2, -1, -1])
out4 = Perceptron(False, 1.5, [-1, -1, -1, -1, 2, 2, 2, 2, -1, -1])
out8 = Perceptron(False, 1.5, [-1, -1, -1, -1, -1, -1, -1, -1, 2, 2])

num = int(input("Enter a number between 0 and 9: "))

ff = []

if num == 0:
    ff = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
elif num == 1:
    ff = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
elif num == 2:
    ff = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
elif num == 3:
    ff = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
elif num == 4:
    ff = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
elif num == 5:
    ff = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
elif num == 6:
    ff = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
elif num == 7:
    ff = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
elif num == 8:
    ff = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
elif num == 9:
    ff = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
else:
    print("Please enter a number between 0 and 9")

num1 = out1.fire(ff)
num2 = out2.fire(ff)
num3 = out4.fire(ff)
num4 = out8.fire(ff)

print("Binary Representation Is: " + str(num4) + str(num3) + str(num2) + str(num1))
