
# EV Battery Performance Predictor
# Integrated Battery Model

capacity = float(input("Enter battery capacity (kWh): "))
soc = float(input("Enter current battery SOC (%): "))
distance = float(input("Enter travelling distance (km): "))
consumption = float(input("Enter energy consumption (kWh/km): "))
charging_power = float(input("Enter charging power (kW): "))

# Input validation
if capacity <= 0 or consumption <= 0 or charging_power <= 0:
    print("Capacity, consumption and charging power must be positive.")

elif soc < 0 or soc > 100:
    print("SOC must be between 0 and 100.")

else:
    # 1. Calculate initial energy
    initial_energy = capacity * soc / 100

    # 2. Calculate energy used during travel
    energy_used = distance * consumption

    # 3. Calculate remaining energy
    remaining_energy = initial_energy - energy_used

    print("\n----- EV BATTERY REPORT -----")

    if remaining_energy < 0:
        print("Warning: Battery energy is insufficient!")
    else:
        # 4. Calculate remaining SOC
        remaining_soc = (remaining_energy / capacity) * 100

        # 5. Calculate remaining driving range
        remaining_range = remaining_energy / consumption

        # 6. Calculate charging time to full
        energy_needed = capacity - remaining_energy
        charging_time = energy_needed / charging_power

        print("Initial Energy:", initial_energy, "kWh")
        print("Energy Used:", energy_used, "kWh")
        print("Remaining Energy:", remaining_energy, "kWh")
        print("Remaining SOC:", remaining_soc, "%")
        print("Remaining Range:", remaining_range, "km")
        print("Charging Time:", charging_time, "hours")

# EV Battery Performance Predictor
# Integrated Battery Model

capacity = float(input("Enter battery capacity (kWh): "))
soc = float(input("Enter current battery SOC (%): "))
distance = float(input("Enter travelling distance (km): "))
consumption = float(input("Enter energy consumption (kWh/km): "))
charging_power = float(input("Enter charging power (kW): "))

# Input validation
if capacity <= 0 or consumption <= 0 or charging_power <= 0:
    print("Capacity, consumption and charging power must be positive.")

elif soc < 0 or soc > 100:
    print("SOC must be between 0 and 100.")

else:
    # 1. Calculate initial energy
    initial_energy = capacity * soc / 100

    # 2. Calculate energy used during travel
    energy_used = distance * consumption

    # 3. Calculate remaining energy
    remaining_energy = initial_energy - energy_used

    print("\n----- EV BATTERY REPORT -----")

    if remaining_energy < 0:
        print("Warning: Battery energy is insufficient!")
    else:
        # 4. Calculate remaining SOC
        remaining_soc = (remaining_energy / capacity) * 100

        # 5. Calculate remaining driving range
        remaining_range = remaining_energy / consumption

        # 6. Calculate charging time to full
        energy_needed = capacity - remaining_energy
        charging_time = energy_needed / charging_power

        print("Initial Energy:", initial_energy, "kWh")
        print("Energy Used:", energy_used, "kWh")
        print("Remaining Energy:", remaining_energy, "kWh")
        print("Remaining SOC:", remaining_soc, "%")
        print("Remaining Range:", remaining_range, "km")
        print("Charging Time:", charging_time, "hours")
