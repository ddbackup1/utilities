# %%
import os


# *****************************************************************************
# 2024-01-25 | First Version of program
# *****************************************************************************
def getListOfFiles(dirName, taglist1, excludefile):
    the_path_list = []
    allFiles = []
    listOfFile = os.listdir(dirName)
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        the_path_list.append(fullPath)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath, taglist1, excludefile)
        else:
            filename, file_extension = os.path.splitext(entry)
            result = {}
            for tag in taglist1:
                result[tag] = 0
            if file_extension == ".py":
                validfilename = True
                for exclude1 in excludefile:
                    if exclude1 in filename:
                        validfilename = False
                if validfilename:
                    for tag in taglist1:
                        if tag.lower() in filename.lower():
                            result[tag] += 1
                    alltagsfound = True
                    for tag in result:
                        if result[tag] == 0:
                            alltagsfound = False
                    if alltagsfound:
                        allFiles.append(fullPath)
    return allFiles


def processFileMain(allFilesMain, taglist2, excludetag):
    # level indicates if python {p1} is written
    level1 = True
    level2 = True
    level3 = True
    level4 = True
    level5 = True
    level6 = True

    # indcate last written was p1 or p2
    statep1 = False
    p1 = "```python"
    p2 = "```"
    index01 = 0
    firstP1 = True

    for programName in allFilesMain:
        basefilename = os.path.basename(programName)
        direname = os.path.dirname(programName)
        fullfilename, file_extension = os.path.splitext(basefilename)
        if firstP1:
            fileo.write("# 🟪" + dirName + "\n")
            firstP1 = False
        fileo.write("# 🟩" + fullfilename + "\n")
        with open(programName) as filei:
            line = filei.readline()
            while line:
                if bool(line.strip()):  # block empty lines
                    if "# %%" in line[0:4]:
                        index01 += 1
                    elif "# " in line[0:2]:
                        if statep1:
                            fileo.write(f"{p2}\n")
                            statep1 = False
                        fileo.write("## 🟡" + line[2:-1] + "\n")
                        if level1:
                            fileo.write(f"[{index01}]\n")
                            fileo.write(f"{p1}\n")
                            statep1 = True
                    elif "## " in line[0:3]:
                        print(f"Level2 Python p1 Flag = {level2}")
                        print("line2:> ", line.strip())
                        print("-----")
                        if statep1:
                            fileo.write(f"{p2}\n")
                            statep1 = False
                        fileo.write("### ✔" + line[3:-1] + "\n")
                        if level2:
                            fileo.write(f"[{index01}]\n")
                            fileo.write(f"{p1}\n")
                            statep1 = True
                    elif "### " in line[0:4]:
                        if statep1:
                            fileo.write(f"{p2}\n")
                            statep1 = False
                        fileo.write("#### 🔸" + line[4:-1] + "\n")
                        if level3:
                            fileo.write(f"[{index01}]\n")
                            fileo.write(f"{p1}\n")
                            statep1 = True
                    elif "#### " in line[0:5]:
                        if statep1:
                            fileo.write(f"{p2}\n")
                            statep1 = False
                        fileo.write("##### 🔹" + line[5:-1] + "\n")
                        if level4:
                            fileo.write(f"[{index01}]\n")
                            fileo.write(f"{p1}\n")
                            statep1 = True
                    elif "##### " in line[0:6]:
                        if statep1:
                            fileo.write(f"{p2}\n")
                            statep1 = False
                        fileo.write("###### ✔" + line[6:-1] + "\n")
                        if level5:
                            fileo.write(f"[{index01}]\n")
                            fileo.write(f"{p1}\n")
                            statep1 = True
                    else:
                        fileo.write(line)
                line = filei.readline()
        if statep1:
            fileo.write(f"{p2}\n")
            statep1 = False


# Main:
# remember these are list terms need to be separated
taglist1 = ["Ex"]  # files
taglist2 = []  # tags

excludefile = [
    "@",
    "$My",
    "2023-",
    "2022-",
    "2021-",
    "excalidraw",
    "excalibrain",
]
excludetag = ["#r"]

dirName = "Z:/SharedA/Python/Projects/PythonExercises"
fileOutput = "Z:/SharedA/Repos/data/totoutput.txt"
programLocation = "Z:/SharedA/Repos/Test/total01.py"
# dirName = "Z:\SharedA\Obsidian\AlphaVault"

print("total01 version 001 Start")
print("------------------------------- ")
print("Program Location  :", programLocation)
print("Input   Directory :", dirName)
print("Result  File      :", fileOutput)
print("Exclude File List :", excludefile)
print("Exclude Tag  List :", excludetag)

fileo = open(fileOutput, "w")
fileo = open(fileOutput, "a")


print("------------------:")
print("FILE LIST SEARCHED:")
print("------------------:")
print(taglist1)
print("------------------:")
# fmt: off
# fmt: on

allFilesMain = []
allFilesMain = getListOfFiles(dirName, taglist1, excludefile)
processFileMain(allFilesMain, taglist2, excludetag)

fileo.close()
print("------------------------------------- ")
print("total01 version 001 Termination")
print("Result File       : ", fileOutput)
# %%
