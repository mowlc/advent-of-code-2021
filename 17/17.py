data = open("data", "r").readline().split(": ")[1].split(", ")

x = data[0].split("=")[1].split("..")
y = data[1].split("=")[1].split("..")
x[0] = int(x[0])
x[1] = int(x[1])
y[0] = int(y[0])
y[1] = int(y[1])

y_vel_max = abs(min(y)) - 1
y_hei_max = (y_vel_max * (y_vel_max + 1)) / 2
print(y_hei_max)