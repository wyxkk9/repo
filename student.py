class Student:
    def __init__(self, name, age, group_count, average_score):
        self.name = name
        self.age = age
        self.group_count = group_count
        self.average_score = average_score

    def display_info(self):
        return f"name: {self.name}, age: {self.age}"

    def scholarship_amount(self):
        if self.average_score == 5:
            return 6000
        elif self.average_score < 5:
            return 4000
        else:
            return 0

    def compare_scholarship(self, other):
        if self.scholarship_amount() > other.scholarship_amount():
            return f"{self.name} > {other.name}"
        elif self.scholarship_amount() < other.scholarship_amount():
            return f"{self.name} < {other.name}"
        else:
            return f"{self.name} = {other.name} "


class Graduate(Student):
    def __init__(self, name, age, group_count, average_score, thesis_title):
        super().__init__(name, age, group_count, average_score)
        self.thesis_title = thesis_title

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, title: {self.thesis_title}"

    def scholarship_amount(self):
        if self.average_score == 5:
            return 8000
        elif self.average_score < 5:
            return 6000
        else:
            return 0


# test
student1 = Student("zhang", 20, 3, 5)
student2 = Student("li", 21, 2, 4.5)
graduate1 = Graduate("wang", 24, 1, 5, "Machine Learning Research")
graduate2 = Graduate("zhao", 25, 1, 4, "Deep Learning Applications")

# information
print(student1.display_info())
print(graduate1.display_info())

# scholarship
print(f"{student1.name} стипендия: {student1.scholarship_amount()} рублей")
print(f"{graduate1.name} стипендия: {graduate1.scholarship_amount()} рублей")

# compare
print(student1.compare_scholarship(student2))
print(graduate1.compare_scholarship(graduate2))
