# pattern_drawing.py

size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop to handle rows
while row < size:
    # Inner loop to handle columns (printing a row of asterisks)
    for col in range(size):
        print("*", end="") 
    print()  
    row += 1  
