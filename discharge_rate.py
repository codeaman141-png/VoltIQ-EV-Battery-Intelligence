print("===== EV BATTERY DISCHARGE RATE =====")

time = [0, 1, 2, 3, 4]

soc = [100, 90, 78, 64, 48]

print("\nTime    Battery SOC    Discharge Rate")

for i in range(len(time) - 1):

    h = time[i + 1] - time[i]

    rate = (soc[i + 1] - soc[i]) / h

    print(time[i], "hr   ", soc[i], "%       ",
          abs(rate), "%/hour")