class Student:
    def __init__(self, name, favorite_subject):
        self.name = name
        self.favorite_subjects = favorite_subject
        self.subjects = {"Math":[], "Arts":[], "Language":[]}
        """Used to initialize the Student."""
    def input_grade(self, subject, score):
            self.subjects[subject].append(score)
            """Used to input the grade per each subject."""
    def __str__(self):
        Str = (f"{self.name}'s grades are:\n")
        subj = self.subjects.keys()
        for key in subj:
            Str += (f"{key}: {self.subjects[key]}\n")
        Str += f"{self.name}'s favorite subject is {self.favorite_subjects}."
        return Str
        """Used to print the scores for all of the subjects."""
    def get_average(self, subject):
        x = 0
        for score in self.subjects[subject]: 
            x += score
        return int(x/len(self.subjects[subject]))
        """Used to return the average score of a certain subjec inputted."""
    def change_favorite_subjects(self, new_favorite_subject):
        self.favorite_subjects = new_favorite_subject
        """Used to change the favorite subject of the student."""
    def __eq__(self, other):
        """Used to compare favorite subject average scores with ==."""
        return self.get_average(self.favorite_subjects) == other.get_average(other.favorite_subjects)
        
    def __ne__(self, other):
        """Used to compare favorite subject average scores with !=."""
        return self.get_average(self.favorite_subjects) != other.get_average(other.favorite_subjects)
        
    def __lt__(self, other):
        """Used to compare favorite subject average scores with <."""
        return self.get_average(self.favorite_subjects) < other.get_average(other.favorite_subjects)
        
    def __gt__(self, other):
        """Used to compare favorite subject average scores with ==."""
        return self.get_average(self.favorite_subjects) > other.get_average(other.favorite_subjects)
        
    def __ge__(self, other):
        """Used to compare favorite subject average scores with >."""
        return self.get_average(self.favorite_subjects) >= other.get_average(other.favorite_subjects)
    
    def __le__(self, other):
        """Used to compare favorite subject average scores with <=."""
        return self.get_average(self.favorite_subjects) <= other.get_average(other.favorite_subjects)

Student1 = Student("Josh", "Math")
Student1.input_grade("Math", 5)
Student1.input_grade("Arts", 200)
Student1.input_grade("Language", 3)
print(Student1)
Student1.input_grade("Math", 10)
Student1.input_grade("Math", 10)
print(Student1)
print(Student1.get_average("Math"))
    
Student2 = Student("Bumgyu", "Arts")
Student2.input_grade("Math", 0)
Student2.input_grade("Arts", 0)
Student2.input_grade("Language", 0)
print(Student2)
Student2.input_grade("Math", 0)
Student2.input_grade("Math", 0)
print(Student2)

print(Student1 > Student2)
print(Student1 >= Student2)
print(Student1 == Student2)
print(Student1 < Student2)
print(Student1 <= Student2)
print(Student1 != Student2)
