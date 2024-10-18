def calculate_triangle_area(base, height):
    """Calculate the area of a triangle given the base and height."""
    return 0.5 * base * height

def main():
    try:
        
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        
       
        area = calculate_triangle_area(base, height)
        
       
        print(f"The area of the triangle with base {base} and height {height} is: {area:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for base and height.")

if __name__ == "__main__":
    main()
