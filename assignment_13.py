calculate_grade = int(input("Enter your numerical grade from 0 to 100: "))

match calculate_grade:

   case calculate_grade if 90 <= calculate_grade <= 100:
      print("Grade: A")
   case calculate_grade if 80 <= calculate_grade < 90:
      print("Grade: B")
   case calculate_grade if 70 <= calculate_grade < 80:
      print("Grade: C")
   case calculate_grade if 60 <= calculate_grade < 70:
      print("Grade: D")
   case calculate_grade if 0<= calculate_grade < 60:
      print("Grade: F")   
   case _:
      print("Enter numerical grade from 0 to 100 only!")