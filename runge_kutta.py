print("===== EV BATTERY CHARGING SIMULATOR =====")

capacity = 60
initial_soc = 30
max_power = 7
efficiency = 0.90

# Differential equation
def f(t, soc):

    power = max_power * (1 - soc / 100)

    return (100 * power * efficiency) / capacity


# RK4 Method
def runge_kutta(t, soc, h):

    k1 = h * f(t, soc)

    k2 = h * f(t + h/2, soc + k1/2)

    k3 = h * f(t + h/2, soc + k2/2)

    k4 = h * f(t + h, soc + k3)

    return soc + (k1 + 2*k2 + 2*k3 + k4)/6


# Simulation
t = 0
h = 0.5

print("\nTime (hours)     Battery SOC")

while t <= 5:

    print(round(t, 2), "hours         ",
          round(initial_soc, 2), "%")

    initial_soc = runge_kutta(t, initial_soc, h)

    t += h