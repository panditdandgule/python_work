from studinfo import Student


class StudentImpl:
    filename='studinfo.txt'

    def add_student_info(self,studdetails):
        try:
            studInfo=str(studdetails.studId)+"\t\t"+studdetails.studName+"\t\t"+str(studdetails.studAge)+"\t\t"+studdetails.studAdr+"\n"
            with open(self.filename,'w') as f:
                f.writelines(studInfo)
                print("Data written successfully to the file..")
        except:
            print("There was an error while adding data to the file..")

    def read_student_info(self):
        try:
            studList=[]
            with open(self.filename,'r') as f:
                alllines=f.readlines() #reading all lines.
                #print(alllines)
                alllines=[line.strip() for line in alllines] #removing  new lines.
                #print(alllines)
                for word in alllines:
                    words=word.split("\t\t")#splitting \t\t
                    studList.append(Student(sid=words[0],sname=words[1],sage=words[2],sadr=word[3]))
            print("Student List: ",studList)

        except:
            print("There was an error while reading data..")