# 2. Design a Grade System based on student marks.
# 	○ Collect marks from user.
# 	○ Print Grade based on the below hierarchy
# 		§ 90 & above: Grade A
# 		§ 70 & above: Grade B
# 		§ 60 & above: Grade C
# 		§ Less than 60: Grade D
mark = input('Enter your marks:')
while(mark !='e' and mark !='E'): 
    mark = int(mark)   
    if (mark >= 0 and mark <= 100):
        if mark >= 90:
            print("Grade A")
        elif mark >= 70:
            print("Grade B")
        elif mark >= 60:
            print("Grade C")
        else:
            print("Grade D")
        break
    else:
        print('Invalid input. Valid Mark range: 0-100')
        print("Please retry with valid mark!--OR-- Press E for exit")
        mark = input()
    







    
