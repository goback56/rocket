import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rocket Simulation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load rocket image
rocket = pygame.image.load('falcon9.png')  # Ensure you have a falcon9.png file
rocket = pygame.transform.scale(rocket, (50, 100))  # Resize if necessary

# Set up the rocket position
rocket_x = width // 2 - 25  # Center horizontally
rocket_y = height - 120      # Start near the bottom

# Rocket movement speed and physics parameters
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

mass = initial_mass
displacement = 0
velocity = 0
time = 0

def find_velocity(t):
    global displacement
    global velocity
    global mass
    if displacement < 11000:
        air_density = 1.225 * ((288.15 - 0.00065 * displacement) / 288.15) ** (g / (0.0065 * 287) - 1)
    else:
        air_density = 0
    
    drag_force = 0.5 * u_drag * air_density * cross_sectional_area * velocity ** 2

    weight = mass * g

    if displacement < 72500:
        net_force = thrust - drag_force - weight
    else:
        net_force = thrust_vacuum - drag_force - weight
    
    acceleration = net_force / mass
    velocity += acceleration * time_step
    displacement += velocity * time_step
    return velocity / 100 ## to slow it down

# Main game loop
running = True
while running:
    screen.fill(BLACK)  # Clear the screen
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Move the rocket upwards
    velocity = find_velocity(time)
    rocket_y -= velocity * time_step  # Update rocket position
    time += time_step  # Increment time

    if rocket_y < -100:  # Reset position if it goes off screen
        rocket_y = height - 120
        displacement = 0  # Reset displacement if desired

    # Draw the rocket
    screen.blit(rocket, (rocket_x, rocket_y))
    
    # Update the display
    pygame.display.flip()
    
