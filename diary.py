from datetime import date

while True:

	print("Menu")
	print('1.Make entry')
	print('2.View entries')
	print('3.Exit')

	choice=input("Enter choice")
	if choice=="1":

		Entry=input("How was your day?")

		today= date.today()

		with open('Diary.txt','a') as f:
			f.write(f"Date: {today}\n")
			f.write(f"Entry: {Entry}\n")
			f.write("-------------------\n")
			3


	elif choice=="2":
		try:

			with open('Diary.txt','r') as f:
				print(f.read(),end=" ")
		except FileNotFoundError:
	   		print("No entries yet. Start writing!")

	elif choice=="3":
		print("exiting Diary entry app....")
		break

	else:
		print("Wrong input")

