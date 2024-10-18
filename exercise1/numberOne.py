# The volume of a sphere with radius r is (4/3)* pie * r**2. 
# What is the volume of the sphere with radius 5. 
# Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places

import math

def calculate_sphere_volume(radius):
    """Calculate the volume of a sphere given its radius."""
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

def main():
    try:
        # Get the radius from the user
        radius = float(input("Enter the radius of the sphere: "))
        

        volume = calculate_sphere_volume(radius)
        
      
        print(f"The volume of the sphere with radius {radius} is: {volume:.2f} cubic units")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value for the radius.")

if __name__ == "__main__":
    main()
