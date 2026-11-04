print("===== EV BATTERY DATA PREDICTION =====")

# Known sensor readings
time = [0, 1, 3]

soc = [100, 90, 60]

# Missing reading time
x = 2

# Lagrange Interpolation
def lagrange(x, time, soc):

    result = 0

    n = len(time)

    for i in range(n):

        term = soc[i]

        for j in range(n):

            if i != j:

                term = term * (
                    (x - time[j]) /
                    (time[i] - time[j])
                )

        result += term

    return result


predicted_soc = lagrange(x, time, soc)

print("Missing Time:", x, "hours")

print("Predicted Battery SOC:",
      round(predicted_soc, 2), "%")