print("===== EV DISCHARGING SIMULATOR =====")

capacity = float(input("Enter battery capacity (kWh): "))
soc = float(input("Enter initial battery percentage: "))
distance = float(input("Enter distance driven (km): "))
consumption = float(input("Enter energy consumption (kWh/km): "))

initial_energy = capacity * soc / 100

energy_used = distance * consumption

remaining_energy = initial_energy - energy_used

if remaining_energy >= 0:

    remaining_soc = remaining_energy / capacity * 100

    remaining_range = remaining_energy / consumption

    print("\n===== RESULTS =====")
    print("Energy Used:", energy_used, "kWh")
    print("Remaining Energy:", remaining_energy, "kWh")
    print("Remaining SOC:", round(remaining_soc, 2), "%")
    print("Remaining Range:", round(remaining_range, 2), "km")

else:
    print("Warning: Insufficient battery energy!")