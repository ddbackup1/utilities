# %%
import os
import time


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


def processFileMain(allFilesMain):
    # indcate last written was p1 or p2
    p1Open = False
    headerWritten = True
    p1 = "```python"
    p2 = "```"
    index01 = 0
    dirProcessed = []

    for programName in allFilesMain:
        basefilename = os.path.basename(programName)
        dirname = os.path.dirname(programName)
        fullfilename, file_extension = os.path.splitext(basefilename)
        if dirname in dirProcessed:
            fileo.write(f"## 🟩 {fullfilename} \n")
        else:
            fileo.write(f"# 🟪 {dirName} \n")
            fileo.write(f"## 🟩 {fullfilename} \n")
        dirProcessed = dirname
        with open(programName) as filei:
            line = filei.readline()
            while line:
                if bool(line.strip()):  # block empty lines
                    if bool(line.strip()):  # block empty lines
                        if "# ++" in line[0:4]:
                            if p1Open:
                                fileo.write(f"{p2}\n")
                                p1Open = False
                            fileo.write("## 🟪" + line[5:-1] + "\n")
                        elif "#c/" in line[0:3]:
                            if p1Open:
                                fileo.write(f"{p2}\n")
                                p1Open = False
                            fileo.write(line)
                        elif "# %%" in line[0:4]:
                            if not headerWritten:
                                print("missing headerWritten for index", index01)
                            headerWritten = False
                            index01 += 1
                            if p1Open:
                                fileo.write(f"{p2}\n")
                                p1Open = False
                            fileo.write(f"[{index01}]\n")
                            if bool(line[4:-1].strip()):
                                fileo.write("### 🟡" + line[5:-1] + "\n")
                                headerWritten = True
                            fileo.write(f"{p1}\n")
                            p1Open = True
                            fileo.write("# " + line[5:-1] + "\n")
                        else:
                            if (
                                line[0:3] == "#--"
                                or line[0:3] == "#++"
                                or line[0:3] == "#%%"
                            ):
                                print(f"invalid control character {line}, {index01}")
                        fileo.write(line)
                        if "#c/" in line:
                            print(f"invalid tag character {line}, {index01}")
                line = filei.readline()
        if p1Open:
            fileo.write(f"{p2}\n")
            p1Open = False


# Main:
# remember these are list terms need to be separated
taglist1 = ["IO"]  # files

excludefile = [
    "@",
    "$My",
    "2023-",
    "2022-",
    "2021-",
    "excalidraw",
    "excalibrain",
]
# dirName = "Z:/SharedA/Python/Projects/PythonExercises"
dirName = "Z:\SharedA\Python\Projects\CS50P\PythonIntro\Code"
fileOutput = "Z:/SharedA/Repos/data/pythonoutput.txt"
programLocation = "Z:/SharedA/Repos/Test/formatpython.py"
# dirName = "Z:\SharedA\Obsidian\AlphaVault"

curr_time = time.strftime("%H:%M:%S", time.localtime())
print("Current Time is :", curr_time)
print("formatpython version 001 Start")
print("------------------------------- ")
print("Program Location  :", programLocation)
print("Input   Directory :", dirName)
print("Result  File      :", fileOutput)
print("Taglist1- Files   :", taglist1)
print("Exclude File List :", excludefile)

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
processFileMain(allFilesMain)

fileo.close()
print("------------------------------------- ")
print("formatpython version 001 Termination")
print("Result File       : ", fileOutput)
# %%

# %%

# %%
