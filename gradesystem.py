def main():
    # Input
    exam_score = float(input("Enter your Exam Score: "))

    if exam_score >= 70:
        print(f"{exam_score} is a Grade A")
    elif exam_score >= 60:
        print(f"{exam_score} is a Grade B")
    elif exam_score >= 50:
        print(f"{exam_score} is a Grade C")
    elif exam_score >= 40:
        print(f"{exam_score} is a Grade D")
    else:
        print(f"{exam_score} is a Grade F")

if __name__ == "__main__":
    main()
