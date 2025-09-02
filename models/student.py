class Student:
    def __init__(self, id: str, name: str, dept: str, scores=None):
        self.id = id
        self.name = name
        self.dept = dept
        self.scores = scores if scores is not None else {}

    def add_score(self, subject: str, marks: float):
        self.scores[subject] = marks

    def get_average_score(self) -> float:
        if not self.scores:
            return 0.0
        return sum(self.scores.values()) / len(self.scores)

    def __str__(self):
        if self.scores:
            avg_score = self.get_average_score()
            score_info = f"Average Score: {avg_score:.2f}"
        else:
            score_info = "No scores added yet."

        return (f"Student ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Department: {self.dept}\n"
                f"{score_info}")


class GraduateStudent(Student):
    def __init__(self, id: str, name: str, dept: str, thesis_title: str):
        super().__init__(id, name, dept)
        self.thesis_title = thesis_title

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nThesis Title: {self.thesis_title}"
