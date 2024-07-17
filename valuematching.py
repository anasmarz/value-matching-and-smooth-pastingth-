import numpy as np
from scipy.optimize import fsolve

# Parameters
K = 100  # Example strike price

# Updated Option Value Function (example for a call option)
def option_value(S):
    return np.maximum(S - K, 0)

# Updated Payoff Function (example)
def payoff_function(S):
    return np.maximum(S - K, 0)

# Derivatives (using simple example; these should match your actual conditions)
def option_value_derivative(S):
    return 1 if S > K else 0

def payoff_derivative(S):
    return 1 if S > K else 0

# Value Matching Condition
def value_matching_condition(S):
    return option_value(S) - payoff_function(S)

# Smooth Pasting Condition
def smooth_pasting_condition(S):
    return option_value_derivative(S) - payoff_derivative(S)

# Combined Function for Solver
def combined_conditions(S_array):
    S = S_array[0]  # Extract scalar value from array
    result = np.array([
        value_matching_condition(S),
        smooth_pasting_condition(S)
    ])
    print(f"Conditions for S = {S}: {result}")  # Debug print
    return result

# Finding the optimal stopping boundary
def find_optimal_stopping_boundary(initial_guess=120):
    initial_guess = np.array([initial_guess])  # Ensure initial guess is a NumPy array

    # Use fsolve to find the root
    S_star, info, ier, msg = fsolve(combined_conditions, initial_guess, full_output=True)
    
    print(f"Solver info: {info}")  # Debug print
    print(f"Solver ier: {ier}")    # Debug print
    print(f"Solver msg: {msg}")    # Debug print
    
    if ier == 1:
        print(f"Optimal stopping boundary S*: {S_star[0]:.5f}")
    else:
        print(f"Solver did not converge: {msg}")
        
    return S_star[0]

# Find the optimal stopping boundary
optimal_S_star = find_optimal_stopping_boundary()
