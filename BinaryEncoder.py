"""BinaryUtility
    Creates a .dat file containing up to 8 semesters for one student
    Each semester contains up to 5 grades

    Takes in data as a Dict
    Line 1 is the name
    each subsequent line is a semester, 8 0s denote a new grade
"""
class BinaryUtility:

    def __init__(self, filename:str = "BinaryUtilOut.dat", datain:dict = None, studentname:str = None):
        self.filename = filename
        if datain is not None:
            self.data = datain
            if studentname is None:
                self.name = self.data["Name"]
            else:
                self.name = studentname
        else:
            self.data = {}
            self.data["Name"]:studentname
        self.binarydata = []
        self.builddata()
        

    def builddata(self):
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
            4 1s inbetween each grade

        Returns:
            str: The binary data for one semester
        """
        spacer = "1111"
        outstring = ""
        for number in semestergrades:
            outstring += format(number, "08b") +" "
        return outstring


    def printbinarydata(self)->None:
        for line in self.binarydata:
            print(line)
        print("\nbinarydata raw\n")
        print(self.binarydata)
        
    def loadsemesters(self):
        for key in self.data.keys():
            if key !="Name":
                self.binarydata.append(self.buildsemester(self.data[key]))

    def writeBinaryData(self):
        with open(self.filename, 'wb') as writer:
            for line in self.binarydata:
                linebyte = bytes(line, "utf-8")
                writer.write(linebyte)
                writer.write(bytes("\n", "utf-8"))


class BinaryRunner:
    def __init__(self):
        BU = BinaryUtility(datain=self.run())
        #BU.printbinarydata()
        BU.writeBinaryData()


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