print("===== EV ENERGY ANALYSIS =====")

# Time readings in hours
time = [0, 1, 2, 3]

# Power readings in kW
power = [2, 3, 4, 3]

total_energy = 0

# Trapezoidal Rule
for i in range(len(time) - 1):

    h = time[i + 1] - time[i]

    area = (h / 2) * (power[i] + power[i + 1])

    total_energy += area

    print("Interval", i + 1, "Energy:", area, "kWh")

print("------------------------------")

print("Total Energy Consumed:",
      total_energy, "kWh")