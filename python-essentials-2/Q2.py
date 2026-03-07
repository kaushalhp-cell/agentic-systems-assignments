class StudentScores:
    def __init__(self, scores):
        self.scores = scores

    def highest_last_two(self):
        try:
            # Get last two scores using negative indexing
            last_two = [self.scores[-2], self.scores[-1]]

            # Calculate highest score
            if self.scores[-2] - self.scores[-1] > 0:
                print("highest score among the last two : ", self.scores[-2])
            else:
                print("highest score among the last two : ", self.scores[-1])

        except IndexError:
            print("Not enough scores to check the highest value")


# Test Case - Valid list with 4 scores
scores = [45, 67, 89, 72]
student1 = StudentScores(scores)
student1.highest_last_two()
print()

# Test Case 2 - Empty list
scores = []
student2 = StudentScores(scores)
student2.highest_last_two()
print()
