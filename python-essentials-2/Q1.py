class StudentMarks:
    def __init__(self, marks):
        self.marks = marks

    def last_three_avg(self):
        try:
            # Get last three marks using negative indexing
            last_three = [self.marks[-3], self.marks[-2], self.marks[-1]]

            # Calculate average
            average = sum(last_three) / len(last_three)

            print(f"Average of last 3 marks is: {average}")

        except IndexError:
            print("Not enough marks to calculate average")


# Test Case 1 - Valid list with 5 marks
marks1 = [50, 60, 70, 80, 90]
student1 = StudentMarks(marks1)
student1.last_three_avg()
print()
# Output: Average of last 3 marks is: 80.0

# Test Case 2 - Valid list with 2 marks
marks2 = [80, 90]
student2 = StudentMarks(marks2)
student2.last_three_avg()
print()
# Output: Not enough marks to calculate average
