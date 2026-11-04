print("===== EV BATTERY CALCULATOR =====")

battery_capacity = float(input("Enter battery capacity (kWh): "))

soc = float(input("Enter current battery percentage: "))

charging_power = float(input("Enter charging power (kW): "))

remaining_energy = battery_capacity * soc / 100

required_energy = battery_capacity - remaining_energy

charging_time = required_energy / charging_power

print("\n===== BATTERY ANALYSIS =====")

print("Battery Capacity:", battery_capacity, "kWh")
print("Current SOC:", soc, "%")
print("Remaining Energy:", remaining_energy, "kWh")
print("Required Energy:", required_energy, "kWh")
print("Charging Time:", round(charging_time, 2), "hours")