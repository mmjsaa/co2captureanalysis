# Import required packages for analysis
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
import pandas as pd

# Use pandas to read Excel datasheet with experimental values for pressure and amount adsorbed
df = pd.read_excel('TGAExpData.xlsx')
pressure_data = df['Abs press'].values
amount_adsorbed_data = df['Amt ads'].values

# Define the adsorption isotherm models being used, set each equaton parameter before returning
def freundlich_isotherm(params, p):
    kf, n = params
    return kf * np.power(p, 1/n)

def langmuir_isotherm(params, p):
    qmax, b = params
    return qmax * (b * p) / (1 + (b * p))

def sips_isotherm(params, p):
    qmax, n, b = params
    return qmax * ((b * p)**(1/n)) / (1 + ((b * p)**(1/n)))

def toth_isotherm(params, p):
    qmax, n, b = params
    return (qmax * (b * p)) / ((1 + (b * p)**n)**(1/n))

# Map isotherm models
isotherm_models = {
    'freundlich': freundlich_isotherm,
    'langmuir': langmuir_isotherm,
    'sips': sips_isotherm,
    'toth': toth_isotherm,
}

# Define the SSE error model variable to be used to calculate the optimal parameters for each adsorption isotherm model
def error_function(params, model, p, data):
    calculated = model(params, p)
    return (data - calculated)

def fit_isotherm_model(model_name, initial_guesses, pressure_data, amount_adsorbed_data):
    model = isotherm_models[model_name]

    # Fit the model to the data using least_squares, works in the same way as SSE
    result = least_squares(error_function, initial_guesses, args=(model, pressure_data, amount_adsorbed_data))

    # Extract the optimal parameter values
    optimal_params = result.x

    return optimal_params

# Calculate and print optimal parameters for the adsorption isotherm models
initial_guesses_freundlich = [1, 1]
optimal_params_freundlich = fit_isotherm_model('freundlich', initial_guesses_freundlich, pressure_data, amount_adsorbed_data)
print("Fruendlich parameters = Kf:", optimal_params_freundlich[0],", n:", optimal_params_freundlich [1])

initial_guesses_langmuir = [1, 1]
optimal_params_langmuir = fit_isotherm_model('langmuir', initial_guesses_langmuir, pressure_data, amount_adsorbed_data)
print("Langmuir parameters = qmax:", optimal_params_langmuir[0],", b:", optimal_params_langmuir[1])

initial_guesses_sips = [1, 1, 1]
optimal_params_sips = fit_isotherm_model('sips', initial_guesses_sips, pressure_data, amount_adsorbed_data)
print("Sips parameters = qmax:", optimal_params_sips[0],", n:", optimal_params_sips[1], ", b:", optimal_params_sips[2])

initial_guesses_toth = [1, 1, 1]
optimal_params_toth = fit_isotherm_model('toth', initial_guesses_toth, pressure_data, amount_adsorbed_data)
print("Toth parameters = qmax:", optimal_params_toth[0],", n:", optimal_params_toth[1], ", b:", optimal_params_toth[2])

# Define a custom colour palette for graph
colours = ["#82C272", "#00A88F", "#0087AC", "#005FAA", "#323B81"]

# Create data points for each adsorption isotherm model curve
freundlich_values = freundlich_isotherm(optimal_params_freundlich, pressure_data)
langmuir_values = langmuir_isotherm(optimal_params_langmuir, pressure_data)
sips_values = sips_isotherm(optimal_params_sips, pressure_data)
toth_values = toth_isotherm(optimal_params_toth, pressure_data)

# Plot adsorption isotherm model calculated data and experimental data
plt.plot(pressure_data, freundlich_values, label='Freundlich Isotherm', linestyle='--', color=colours[0])
plt.plot(pressure_data, langmuir_values, label='Langmuir Isotherm', linestyle='--', color=colours[1])
plt.plot(pressure_data, sips_values, label='Sips Isotherm', linestyle='--', color=colours[2])
plt.plot(pressure_data, toth_values, label='Toth Isotherm', linestyle='--', color=colours[3])
plt.scatter(pressure_data, amount_adsorbed_data, label='Experimental Data', color=colours[4], marker='o', s=15)

# Build graph of results
plt.xlabel('Pressure')
plt.ylabel('Amount Adsorbed')
plt.legend()
plt.show()
