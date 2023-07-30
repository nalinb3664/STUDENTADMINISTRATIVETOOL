import csv

def write_info_csv(info_list):
    with open('student_info.csv','w+',newline='') as csv_file:
        writer = csv.writer(csv_file)
    if csv_file.tell() == 0:
        writer.writeow(["NAME","AGE","CONTACT NO","EMAIL ID"])

        writer.writerow(info_list)

condition = True

while(condition):
    
   STUDENT_INFO= input("enter some student information in format (NAME,AGE,CONTACT NO,EMAIL ID):")
   print("entered information: " +STUDENT_INFO)

   STUDENT_INFO_list = STUDENT_INFO.split('')
   print("entered split up information is:" + str(STUDENT_INFO_list))
 
   print("\n the entered information is -\nNAME: {}\nAGE: {}\nCONTACT NO: {}\nEMAIL ID: {}".format(STUDENT_INFO_list[0],STUDENT_INFO_list[1],STUDENT_INFO_list[2],STUDENT_INFO_list[3]))
   choice_check = input("is the entered information correct?(yes/no):")
   write_info_csv(STUDENT_INFO_list)

condition_check = input("enter (yes/no)if you want to enter the student data")
if condition_check == "yes":
    condition = True
elif condition_check == "no":
    conditon = False
elif choice_check == "no":
    print("\nplease re enter the values!")