lecturerTitle = input("Input Lecturer Title: ")
lecturerSurname = input("Input Lecturer Surname: ")
lecturerAddress = input("input Lecturer Address: ")

# Sender Details
senderName = input("input your name: ")
senderCountry = input("Input your Country:  ")


matlips = f" Dear {lecturerTitle} {lecturerSurname}, \n {lecturerAddress}. \n " \
          f" It is my pleasure to write you this letter, My name is {senderName} a citizen of {senderCountry}."

print(matlips)

