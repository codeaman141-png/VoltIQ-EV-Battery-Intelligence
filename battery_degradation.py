print("===== EV BATTERY DEGRADATION PREDICTION =====")

# Historical battery data
months = [0, 3, 6, 9]

health = [100, 98, 96, 93]

n = len(months)

# Calculate required sums
sum_x = sum(months)
sum_y = sum(health)

sum_xy = sum(
    months[i] * health[i]
    for i in range(n)
)

sum_x2 = sum(
    x ** 2 for x in months
)

# Calculate slope
b = (
    n * sum_xy - sum_x * sum_y
) / (
    n * sum_x2 - sum_x ** 2
)

# Calculate intercept
a = (sum_y - b * sum_x) / n

# Prediction after 12 months
future_month = 12

predicted_health = a + b * future_month

print("\nSlope:", round(b, 4))
print("Intercept:", round(a, 4))

print(
    "Predicted Battery Health after 12 months:",
    round(predicted_health, 2), "%"
)