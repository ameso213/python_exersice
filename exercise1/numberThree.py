def get_grade(score):
    """Determine the grade based on the score."""
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 50 <= score < 60:
        return 'E'
    else:
        return 'Fail'

def main():
    # Get user input for the score
    try:
        score = float(input("Enter the score (0-100): "))
        
        if score < 0 or score > 100:
            print("Please enter a valid score between 0 and 100.")
        else:
            grade = get_grade(score)
            print(f"The grade for a score of {score} is: {grade}")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
