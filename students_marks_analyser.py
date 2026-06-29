import csv

def get_grades(average):
	if average >=90:
		return "A"
	elif average>=75:
		return "B"
	elif average >=60:
		return "C"
	else :
		return "Fail"


with open("students.csv",'r') as file:
	reader=csv.DictReader(file)
	students=list(reader)
for student in students:
	maths=int(student["Maths"])
	science=int(student["Science"])
	english=int(student["English"])

	average=(maths+science+english)/3

	student["Average"]= round(average,2)
	student["Grade"] = get_grades(average)

with open('result.csv','w',newline="") as outfile:

	fieldnames=[
        "Name",
        "Maths",
        "Science",
        "English",
        "Average",
        "Grade"
    ]

	writer =csv.DictWriter(outfile,fieldnames=fieldnames)

	writer.writeheader()

	writer.writerows(students)

print("Results are saved to result.csv")

for student in students :

    print(
    	student["Name"],
    	student["Maths"],
   		student["Science"],
   		student["English"],
   		student["Average"],
   		student["Grade"]
    		)

