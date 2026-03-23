while True:
    subject1 = input("Subject 1 name: ")
    mark1 = int(input(f"{subject1} marks: "))
    subject2 = input("Subject 1 name: ")
    mark2 = int(input(f"{subject2} marks: "))
    subject3 = input("Subject 1 name: ")
    mark3 = int(input(f"{subject3} marks: "))
    if mark1 >= 35:
        print(f"{subject1}: Pass")
    else:
        print(f"{subject1}: Fail")
    if mark2 >= 35:
        print(f"{subject2}: Pass")
    else:
      print(f"{subject2}: Fail")
    if mark3 >= 35:
      print(f"{subject3}: Pass")
    else:
      print(f"{subject3}: Fail")
    avg=(mark1+mark2+mark3)/3
    if avg>=90:
        print("Your grade is A")
    elif 80 <= avg < 90 :
        print("Your grade is B")
    elif 70 <= avg < 80:
        print("Your grade is C")
    elif 60 <= avg < 70:
        print("Your grade is D")
    else:
        print("Your grade is F")
    if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
      print("You Pass")
    else:
      print("You Pass (Away)")
    again = input("Calculate again? (y/n): ")
    if again != 'y':
        break
