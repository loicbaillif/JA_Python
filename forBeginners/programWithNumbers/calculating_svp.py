# Program with Numbers - Calculating S V P #
# Ask the user about parameters of a rectangular parallelepiped 
# (3 integers representing the length, width, and height) and print the sum 
# of edge lengths, its total surface area, and the volume, one answer per line.

length = int(input())
width = int(input())
height = int(input())

sum_edge_lengths = 4 * (length + width + height)
surface = 2 * (length * width + width * height + length * height)
volume = length * width * height

print(sum_edge_lengths)
print(surface)
print(volume)