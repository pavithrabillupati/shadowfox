# 1

def format_number(num, fmt):
    return format(num, fmt)

result = format_number(145, 'o')
print("Formatted result:", result)
print("Representation: Octal")
# 2

radius = 84
pi = 3.14

area = pi * radius * radius
print("Area of pond:", area)
water_per_sq_meter = 1.4
total_water = area * water_per_sq_meter

print("Total water (no decimal):", int(total_water))


# 3

distance = 490   
time_minutes = 7

time_seconds = time_minutes * 60

speed = distance / time_seconds

print("Speed (m/s, no decimal):", int(speed))