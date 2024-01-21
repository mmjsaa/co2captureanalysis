# Import required packages for analysis
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
import pandas as pd

# Use pandas to read Excel datasheet with experimental values for time and uptake
df = pd.read_excel('VAAExpData.xlsx')
time_data = df['time'].values
uptake_data = df['uptake'].values

# Define the adsorption kinetic models being used, set each equaton parameter before returning
def avrami(params, t):
    qe, kA, nA = params
    return qe * (1 - np.exp(-kA * t**nA))

def pseudo_first_order(params, t):
    qe, kf = params
    return qe * (1 - np.exp(-kf * t))

def pseudo_second_order(params, t):
    qe, ks = params
    return (ks * t * qe**2) / (1 + (qe * ks * t))

# Map kinetic models
kinetic_models = {
    'avrami': avrami,
    'first': pseudo_first_order,
    'second': pseudo_second_order,
}

# Define the SSE error model variable to be used to calculate the optimal parameters for each adsorption kinetic model
def error_function(params, model, t, data):
    calculated = model(params, t)
    return (data - calculated)

def fit_kinetic_model(model_name, initial_guesses, time_data, uptake_data):
    model = kinetic_models[model_name]

    # Set bounds to prevent parameters from going below 0
    bounds = (0, np.inf)

    # Fit the model to the data using least_squares, works in the same way as SSE
    result = least_squares(error_function, initial_guesses, args=(model, time_data, uptake_data), bounds=bounds)

    # Extract the optimal parameter values
    optimal_params = result.x

    return optimal_params

# Calculate and print optimal parameters for the adsorption kinetic models
initial_guesses_avrami = [1, 1, 1]
optimal_params_avrami = fit_kinetic_model('avrami', initial_guesses_avrami, time_data, uptake_data)
print("Avrami parameters = Kf:", optimal_params_avrami[0],", n:", optimal_params_avrami [1],", nA:", optimal_params_avrami[2])

initial_guesses_first = [1, 1]
optimal_params_first = fit_kinetic_model('first', initial_guesses_first, time_data, uptake_data)
print("Psuedo First Order parameters = qmax:", optimal_params_first[0],", b:", optimal_params_first[1])

initial_guesses_second = [1, 1]
optimal_params_second = fit_kinetic_model('second', initial_guesses_second, time_data, uptake_data)
print("Psuedo Second Order parameters = qmax:", optimal_params_second[0],", n:", optimal_params_second[1])

# Define a custom colour palette for graph
colours = ["#003f5c", "#7a5195", "#ef5675", "#ffa600"]

# Create data points for each adsorption kinetic model curve
avrami_values = avrami(optimal_params_avrami, time_data)
first_values = pseudo_first_order(optimal_params_first, time_data)
second_values = pseudo_second_order(optimal_params_second, time_data)

# Plot adsorption kinetic model calculated data and experimental data
plt.plot(time_data, avrami_values, label='Avrami', linestyle='--', color=colours[0])
plt.plot(time_data, first_values, label='Pseudo First Order', linestyle='--', color=colours[1])
plt.plot(time_data, second_values, label='Pseudo Second Order', linestyle='--', color=colours[2])
plt.scatter(time_data, uptake_data, label='Experimental Data', color=colours[3], marker='o', s=5)

# Build graph of results
plt.xlabel('Time')
plt.ylabel('Uptake')
plt.legend()
plt.show()
