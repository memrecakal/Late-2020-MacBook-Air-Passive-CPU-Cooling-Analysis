import matplotlib.pyplot as plt
data = open("log.chtfoam.txt", "r")
data_fixed = open("log.chtfoamfixed.txt", "r")
data_yuzotuzdokuz = open("log.chtfoam139.txt", "r")
data_bin = open("log.chtfoam1000.txt", "r")

time_matrix = []
temp_matrix = []
heater_temp_matrix = []
clockTime_matrix = []

time_matrix_fixed = []
temp_matrix_fixed = []
heater_temp_matrix_fixed = []
clockTime_matrix_fixed = []

time_matrix_yuz = []
temp_matrix_yuz = []
heater_temp_matrix_yuz = []
clockTime_matrix_yuz = []

time_matrix_bin = []
temp_matrix_bin = []
heater_temp_matrix_bin = []
clockTime_matrix_bin = []




for line in data:
    line = line.replace("\n", "")
    if line.count("Time = ") == 1:
        time_matrix.append(float(line[7:]))

    elif line.count("Min/max T:"):
        try:
            temp_matrix.append(float(line[-7:]))
        except:
            temp_matrix.append(float(line[line.rfind("30"):]))

    elif line.count("ExecutionTime ="):
        clockTime_matrix.append(float(line[(line.rfind("=")) + 2:-2])/3600)


for i in range(len(temp_matrix)):
    if (i+1) % 6 == 3:
        heater_temp_matrix.append(temp_matrix[i])

print(len(time_matrix), len(clockTime_matrix))


#fixed


for line in data_fixed:
    line = line.replace("\n", "")
    if line.count("Time = ") == 1:
        time_matrix_fixed.append(float(line[7:]))

    elif line.count("Min/max T:"):
        try:
            temp_matrix_fixed.append(float(line[-7:]))
        except:
            temp_matrix_fixed.append(float(line[line.rfind("30"):]))

    elif line.count("ExecutionTime ="):
        clockTime_matrix_fixed.append(float(line[(line.rfind("=")) + 2:-2])/3600)


for i in range(len(temp_matrix_fixed)):
    if (i+1) % 6 == 3:
        heater_temp_matrix_fixed.append(temp_matrix_fixed[i])

print(len(time_matrix_fixed), len(heater_temp_matrix_fixed))

# 139

for line in data_yuzotuzdokuz:
    line = line.replace("\n", "")
    if line.count("Time = ") == 1:
        time_matrix_yuz.append(float(line[7:]))

    elif line.count("Min/max T:"):
        try:
            temp_matrix_yuz.append(float(line[-7:]))
        except:
            temp_matrix_yuz.append(float(line[line.rfind(" ")+1:]))

    elif line.count("ExecutionTime ="):
        clockTime_matrix_yuz.append(float(line[(line.rfind("=")) + 2:-2])/3600)


for i in range(len(temp_matrix_yuz)):
    if (i+1) % 6 == 3:
        heater_temp_matrix_yuz.append(temp_matrix_yuz[i])

print(len(time_matrix_yuz), len(clockTime_matrix_yuz))

# 1000

for line in data_bin:
    line = line.replace("\n", "")
    if line.count("Time = ") == 1:
        time_matrix_bin.append(float(line[7:]))

    elif line.count("Min/max T:"):
        try:
            temp_matrix_bin.append(float(line[-7:]))
        except:
            temp_matrix_bin.append(float(line[line.rfind(" ") +1:]))

    elif line.count("ExecutionTime ="):
        clockTime_matrix_bin.append(float(line[(line.rfind("=")) + 2:-2])/3600)


for i in range(len(temp_matrix_bin)):
    if (i+1) % 6 == 3:
        heater_temp_matrix_bin.append(temp_matrix_bin[i])

print(len(time_matrix_bin), len(clockTime_matrix_bin))

plt.figure(dpi=150)
plt.plot(time_matrix[:-1], heater_temp_matrix)
#plt.plot(time_matrix_fixed[:-1], heater_temp_matrix_fixed)
#plt.plot(time_matrix_bin[:], heater_temp_matrix_bin)
#plt.plot(time_matrix_yuz[:-1], heater_temp_matrix_yuz)
plt.xlabel("Time [s]")
plt.ylabel("Temp. [K]")
plt.title("CPU Temperature vs Time")
plt.legend(["zeroGradient"])
plt.grid(True)
plt.show()

plt.figure(dpi=150)
plt.plot(clockTime_matrix, time_matrix[:-1]) 
#plt.plot(clockTime_matrix_fixed, time_matrix_fixed[:-1])
#plt.plot(clockTime_matrix_bin, time_matrix_bin[:]) 
#plt.plot(clockTime_matrix_yuz, time_matrix_yuz[:-1])
plt.xlabel("Run Time [h]")
plt.ylabel("Simualtion Time [s]")
plt.title("Run Time vs Simulation Time")
plt.legend(["zeroGradient"])
plt.grid(True)
plt.show()


