import string as str_import

with open("normalVersion.txt") as file_in:
    normalLines = []
    for line in file_in:
        #Removes any trailing numbers and dots representing versions
        string = line.replace(".", "").rstrip(str_import.digits).replace(" -> ","->")

        # removes extra white space and splits string based on spaces
        array = " ".join(string.split()).split(" ")
     #   print(array)
        if len(array) > 5 and (array[5]!="." and array[5]!=".."):
            normalLines.append(array)

with open("TestieVersion.txt") as file_in2:
    testieLines = []
    for line in file_in2:
        # Removes any trailing numbers and dots representing versions
        string = line.replace(".", "").rstrip(str_import.digits).replace(" -> ","->")

        # removes extra white space and splits string based on spaces
        array = " ".join(string.split()).split(" ")
        if len(array) > 5:
            testieLines.append(array)
found = False
notFound = []
for testLine in testieLines:
    for normalLine in normalLines:
        if len(normalLine) > 8 and len(testLine) > 8 and normalLine[8] == testLine[8]:
            found = True
            if normalLine[0] != testLine[0] or normalLine[2] != testLine[2] or normalLine[3] != testLine[3]:
                normalLineString = "".join(str(e) for e in normalLine)
                testLineString = "".join(str(e) for e in testLine)
                print("Reg = " + normalLineString + "    Wrong = " + testLineString)
    if found == False:
        notFound.append(testLine)
    found = False
print("Not Found Lines in TestieVersion.txt:")
for notFoundElem in notFound:
    print("".join(str(e) for e in notFoundElem))





