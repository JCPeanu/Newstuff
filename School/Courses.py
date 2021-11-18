classes = {'Language Arts': 'Mrs. Slabbert', 'Math': "Ms. Chang", "AP Physics 1": 'Mr. Fernanandez', 'Applied Chemistry': "Mr. Long", "Research" : "Mr. pinzon","Python": "Mr. Pinzon", "AP Computer Science" : "Mr. Pinzon", "CRW10": "Mr. Cochrane", "World History 10": "Mr. Robus"}
lst = list(classes.keys())
print("The subjects I'm seeing this year are: ", end = "")
[print(lst[i] + ", ", end = "") for i in range(len(lst) - 1)]
print(lst[-1])
c = input("Which course do you want to know who the teacher is? ")
print("The teacher is {}.".format(classes.get(c)))