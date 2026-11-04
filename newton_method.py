import math

print("===== EV CHARGING TIME PREDICTOR =====")

target_soc = 80

def f(t):
    return 100 - 70 * math.exp(-0.1 * t) - target_soc

def derivative(t):
    return 7 * math.exp(-0.1 * t)

# Initial guess
t = 10

# Newton-Raphson
for i in range(10):

    t_new = t - f(t) / derivative(t)

    print("Iteration", i + 1, ":", round(t_new, 6))

    if abs(t_new - t) < 0.000001:
        t = t_new
        break

    t = t_new

print("-----------------------------")
print("Required Charging Time:", round(t, 2), "hours")