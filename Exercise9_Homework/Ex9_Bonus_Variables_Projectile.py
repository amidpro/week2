import math

# import math modulus - built-in math functions

# At a barrel height of 1m, after a horizontal distance of 0.5m, an elevation of 80 degr ees, and an initial velocity of 44 m/s, what is the height of the projectile?

# original variables used - refactored to make more sense

# yo = 1
# x = 0.5
# theta = 80*(math.pi/180)
# vo = 44
# g = 9.81

yo_height_of_the_barrel_meters = 1
x_the_horizontal_distance_travelled = 0.5
theta_elevation_angle_in_radians = 80*(math.pi/180)
vo_the_initial_velocity_ms = 44
g_acceleration_due_to_gravity = 9.81

# - gx**2/2(44 math.cos math.theta)**2 - using math methods to calulate
# print((yo + (x*math.tan(theta))) - (((g*x)**2) / (2 * ((vo * math.cos(theta))**2)))) - original calculation


# detailed calulation:
print((yo_height_of_the_barrel_meters + (x_the_horizontal_distance_travelled*math.tan(theta_elevation_angle_in_radians))) - (((g_acceleration_due_to_gravity*x_the_horizontal_distance_travelled)**2) / (2 * ((vo_the_initial_velocity_ms * math.cos(theta_elevation_angle_in_radians))**2))))
