class Problem:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def solution(self, algo):
        algo()

    def __str__(self) -> str:
        return f"\nProblem: {self.title}\n{'-' * 50}\n{self.description}{'=' * 50}\nEND OF PROBLEM"
