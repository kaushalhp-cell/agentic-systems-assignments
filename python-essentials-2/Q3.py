class StudentPerformance:
    def __init__(self, scores):
        self.scores = scores

    def score_difference(self):
        try:
            # Calculate score difference
            print("Difference between last & first scores is : ",
                  self.scores[-1]-self.scores[0])

        except IndexError:
            print("No scores available to calculate difference")


# Test Case 1 - Valid list with 4 scores
scores = [55, 65, 75, 85]
student1 = StudentPerformance(scores)
student1.score_difference()
print()

# Test Case 2 - Empty list
scores = []
student2 = StudentPerformance(scores)
student2.score_difference()
print()
