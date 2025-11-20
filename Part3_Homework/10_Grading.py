"""Simple grading system.

Takes a student's score as input and prints the corresponding letter
grade using the following scale:

90 or above: A
80-89: B
70-79: C
60-69: D
Below 60: F
"""

def get_letter_grade(score: float) -> str:
	if score >= 90:
		return "A"
	if score >= 80:
		return "B"
	if score >= 70:
		return "C"
	if score >= 60:
		return "D"
	return "F"


def main() -> None:
	try:
		raw = input("Enter student's score (0-100): ").strip()
		score = float(raw)
	except ValueError:
		print("Invalid input. Please enter a numeric score.")
		return

	if not (0 <= score <= 100):
		print("Score must be between 0 and 100.")
		return

	grade = get_letter_grade(score)
	print(f"Score: {score:g} -> Grade: {grade}")


if __name__ == "__main__":
	main()

