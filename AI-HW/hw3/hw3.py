import math
import random

# Define the objective function (example: maximize f(x) = -x^2 + 5x - 6)
def objective_function(x):
    return -x**2 + 5*x - 6

# Simulated Annealing Algorithm for Maximization
def simulated_annealing_maximize(f, x0, max_iterations, initial_temperature, cooling_rate):
    x = x0  # Start from the initial solution
    current_value = f(x)
    for iteration in range(max_iterations):
        temperature = initial_temperature / (1 + cooling_rate * iteration)
        
        neighbor_x = x + random.uniform(-1, 1)  # Generate a random neighbor solution
        neighbor_value = f(neighbor_x)
        
        if neighbor_value > current_value or random.random() < math.exp((neighbor_value - current_value) / temperature):
            x = neighbor_x
            current_value = neighbor_value
    return x

# Runtime Case 1
result1 = simulated_annealing_maximize(objective_function, 2.0, 1000, 100.0, 0.01)
print("Simulated Annealing (Runtime Case 1) - Maximum found at x =", result1)

# Runtime Case 2
result2 = simulated_annealing_maximize(objective_function, -2.0, 1000, 100.0, 0.01)
print("Simulated Annealing (Runtime Case 2) - Maximum found at x =", result2)

# Define the objective function (example: maximize f(x) = -x^2 + 5x - 6)
def objective_function(x):
    return -x**2 + 5*x - 6

# Hill Climbing Algorithm for Maximization
def hill_climbing_maximize(f, x0, step_size, max_iterations):
    x = x0  # Start from the initial solution
    for _ in range(max_iterations):
        current_value = f(x)
        neighbor_x = x + random.uniform(-step_size, step_size)  # Generate a random neighbor solution
        neighbor_value = f(neighbor_x)
        
        if neighbor_value > current_value:
            x = neighbor_x  # Move to the neighbor solution if it's better
    return x

# Runtime Case 1
result1 = hill_climbing_maximize(objective_function, 2.0, 0.1, 100)
print("Hill Climbing (Runtime Case 1) - Maximum found at x =", result1)

# Runtime Case 2
result2 = hill_climbing_maximize(objective_function, -2.0, 0.1, 100)
print("Hill Climbing (Runtime Case 2) - Maximum found at x =", result2)

print("Objective Function for both was -x**2 + 5*x - 6")