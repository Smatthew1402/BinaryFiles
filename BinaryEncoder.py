"""BinaryUtility
    Creates a .dat file containing up to 8 semesters for one student
    Each semester contains up to 5 grades

    Takes in data as a Dict
    Line 1 is the name
    each subsequent line is a semester, a space dentoes a new grade
"""
class BinaryUtility:
    def __init__(self, filenamein:str="BinaryUtilOut.dat"):
        #self.writer = self.Writer(filenamein)
        #self.reader = self.Reader(filenamein)
        pass

   

    class Reader:
        """Reads data from the file
        """
        
        def __init__(self, filenamein:str = "BinaryUtilOut.dat"):
            self.filename = filenamein
            self.lines = []
            self.studentdata = {}
            pass

        def read(self):
            self.studentdata["Name"]=self.translateName()

        
        def binarytoint(self, binary:list):
            count =7
            intout = 0
            for int in range(0,8):
                intout += (pow(2,count)*binary[int])
                count -=1
            return intout

        def readfile(self):
            with open(self.filename, "rb") as reader:
                for line in reader:
                    self.lines.append(line[0:-2])
            
        def printlines(self):
            for line in self.lines:
                print(line)
                print("\n")
        
        def translateName(self):
            letters = ""
            nameline = list(self.lines[0].decode())
            templist =[]
            for ch in nameline:
                if ch != " ":
                    num = int(ch)
                    templist.append(num)
                if ch == " ":
                    letters += (chr(self.binarytoint(templist)))
                    templist.clear()
            letters += (chr(self.binarytoint(templist)))
        
        def translateGrades():
            pass


    class Writer:
        """Writes data to the file 
        """
       
        def __init__(self, filenamein:str = "BinaryUtilOut.dat", datain:dict = None, studentname:str = None):
            self.filename = filenamein
            if datain is not None:
                self.data = datain
                if studentname is None:
                    self.name = self.data["Name"]
                else:
                    self.name = studentname
            else:
                self.data = {}
                self.data["Name"]:studentname
                self.name = studentname
            self.binarydata = []
            self.builddata()
            
        def addsemester(self, semestername:str, grades:list)->None:
            self.data[semestername]=grades

        def setname(self, studentname:str):
            self.data["Name"]=studentname
            self.name = studentname

        def builddata(self):
            """Filled the binarydata list
            """
            self.binarydata.append(self.buildname())
            self.loadsemesters()

        
        def buildname(self)->str:
            """builds the name line for the file

            Returns:
                str: the name of the file converted to binary
            """
            biname = ""
            bytearr = bytearray(self.name, "utf-8")
            bytelist = []
            for byte in bytearr:
                bytelist.append(format(byte, "08b")+" ")
            for str in bytelist:
                biname += str
            return biname

        def buildsemester(self, semestergrades:list)->str:
            """Builds a semester of data
                " " between each grade that semester

            Returns:
                str: The binary data for one semester in string form
            """
            outstring = ""
            for number in semestergrades:
                outstring += format(number, "08b") +" "
            return outstring


        def printbinarydata(self)->None:
            """Prints the data in binaryday two ways:
                Line-By-Line printing each line on its own line
                And wholesale, printing the default list.__repr__
            """
            for line in self.binarydata:
                print(line)
            print("\nbinarydata raw\n")
            print(self.binarydata)
            

        def loadsemesters(self):
            """Iterates through data's non-"Name" keys, sending the data associated with them into buildsemester
            """
            for key in self.data.keys():
                if key !="Name":
                    self.binarydata.append(self.buildsemester(self.data[key]))


        def writeBinaryData(self):
            """Writes the data from binarydata to filename
            """
            with open(self.filename, 'wb') as writer:
                for line in self.binarydata:
                    linebyte = bytes(line, "utf-8")
                    writer.write(linebyte)
                    writer.write(bytes("\n", "utf-8"))
                


class BinaryRunner:
    def __init__(self):
        BW = BinaryUtility.Writer(datain=self.run())
        #BW.printbinarydata()
        BW.writeBinaryData()
        BR = BinaryUtility.Reader()
        BR.readfile()
        BR.translateName()



    def run(self)->dict:
        semester1 = [90,90,90,90,90]
        semester2 = [91,91,91,91,91]
        semester3 = [92,92,92,92,92]
        semester4 = [93,93,93,93,93]
        semester5 = [94,94,94,94,94]
        semester6 = [95,95,95,95,95]
        semester7 = [96,96,96,96,96]
        semester8 = [97,97,97,97,97]
        studentdata = {"Name":"Teststudent"}
        studentdata["Semester1"]=semester1
        studentdata["Semester2"]=semester2
        studentdata["Semester3"]=semester3
        studentdata["Semester4"]=semester4
        studentdata["Semester5"]=semester5
        studentdata["Semester6"]=semester6
        studentdata["Semester7"]=semester7
        studentdata["Semester8"]=semester8
        return studentdata


if __name__ == "__main__":
    BR = BinaryRunner()
    