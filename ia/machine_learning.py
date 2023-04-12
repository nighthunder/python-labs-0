# In this example, we define a simple artificial neural network with one hidden layer and one output layer, and use backpropagation to train the network to solve the XOR problem. We start by defining the input features and corresponding labels, and then define the neural network architecture and weights. We use the sigmoid activation function for both the hidden and output layers.

# We then train the neural network using backpropagation, by iteratively feeding forward the input data, calculating the error between the predicted output and the true label, and then updating the weights using the error derivatives. We repeat this process for a fixed number of iterations, specified by the num_iterations variable.

# Finally, we use the trained neural network to make predictions on new data. We define a new set of input data and pass it through the network, using the sigmoid function to apply the activation function to the hidden layer and output layer weights, and then print the resulting predictions to the console.

import numpy as np

# Define the input features and corresponding labels
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Define the neural network architecture
num_inputs = 2
num_hidden = 4
num_outputs = 1

# Define the weights for the hidden and output layers
hidden_weights = np.random.randn(num_inputs, num_hidden)
output_weights = np.random.randn(num_hidden, num_outputs)

# Define the sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Train the neural network using backpropagation
learning_rate = 0.1
num_iterations = 10000

for i in range(num_iterations):
    # Feed forward
    hidden_layer = sigmoid(np.dot(X, hidden_weights))
    output_layer = sigmoid(np.dot(hidden_layer, output_weights))

    # Backpropagation
    output_error = y - output_layer
    output_delta = output_error * sigmoid_derivative(output_layer)

    hidden_error = output_delta.dot(output_weights.T)
    hidden_delta = hidden_error * sigmoid_derivative(hidden_layer)

    # Update weights
    output_weights += learning_rate * hidden_layer.T.dot(output_delta)
    hidden_weights += learning_rate * X.T.dot(hidden_delta)

# Make predictions on new data
new_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
predictions = sigmoid(np.dot(sigmoid(np.dot(new_data, hidden_weights)), output_weights))

print(predictions)
