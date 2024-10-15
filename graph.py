import numpy as np
import matplotlib.pyplot as plt

# Parameters
g = 9.81
thrust = 7607000
thrust_vacuum = 1020000
cross_sectional_area = 7.62
mass_flow_rate = 230
u_drag = 0.335
initial_air_density = 1.225
initial_mass = 250000
time_step = 1
total_time = 180
altitude_vacuum = 100000
sealevel_temp = 288.15
temp_laps_rate = 0.0065

# Set up
time_values = []
velocity_values = []
acceleration_values = []
displacement_values = []

mass = initial_mass
displacement = 0
velocity = 0
time = 0

# Rocket movement displacement, velocity, and acceleration
while time < total_time:
    # air density depending on displacement
    if displacement < 11000:
        air_density = initial_air_density * ((sealevel_temp - temp_laps_rate * displacement) / sealevel_temp) ** (g /(temp_laps_rate * 287) - 1)
    else:
        air_density = 0
    
    drag_force = 0.5 * u_drag * air_density *cross_sectional_area* velocity ** 2

    weight = mass * g
    
    # net force depending on displacement
    if displacement < 72500:
        net_force = thrust - drag_force - weight
    else:
        net_force = thrust_vacuum - drag_force - weight

    # variables
    acceleration = net_force / mass
    velocity += acceleration * time_step
    displacement += velocity * time_step

    time_values.append(time)
    displacement_values.append(displacement)
    velocity_values.append(velocity)
    acceleration_values.append(acceleration)

    time += time_step

time_values = np.array(time_values)
displacement_values = np.array(displacement_values)
velocity_values = np.array(velocity_values)
acceleration_values = np.array(acceleration_values)

plt.figure(figsize=(15, 10))

# displacement graph
plt.subplot(3, 1, 1)
plt.plot(time_values, displacement_values / 1000, label='Displacement (km)')
plt.title('Displacement of Falcon 9 Rocket')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (km)')
plt.grid()
plt.legend()

# velocity graph
plt.subplot(3, 1, 2)
plt.plot(time_values, velocity_values, label='Velocity (m/s)', color='orange')
plt.title('Velocity of Falcon 9 Rocket')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.grid()
plt.legend()

# acceleration graph
plt.subplot(3, 1, 3)
plt.plot(time_values, acceleration_values, label='Acceleration (m/s²)', color='green')
plt.title('Acceleration of Falcon 9 Rocket')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s²)')
plt.grid()
plt.legend()

# show graph
plt.tight_layout()
plt.show()
