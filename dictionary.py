dictionary = {'Alice':69,'John':45,'Doe':89,'Dilleep':91,'Shyam':57,'Raju':77}
student_name = input("Enter the student's name:")
if student_name in dictionary:
    print(f"{student_name}'s mark's:{dictionary[student_name]}")
else:
    print("Student not found.")