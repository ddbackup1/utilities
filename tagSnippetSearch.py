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
            if file_extension == ".md":
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
    statep1 = False
    p1 = "```python"
    p2 = "```"
    tagmatchfiletotal = []
    linetotal = []
    tagmain = []
    value1 = "#c"
    fullfilenamehold = " "
    if value1 not in excludetag:
        tagmain.append(value1)
    for programName in allFilesMain:
        basefilename = os.path.basename(programName)
        fullfilename, file_extension = os.path.splitext(basefilename)
        index01 = 0
        with open(programName) as filei:
            line = filei.readline()
            tagfoundlistfile = []
            while line:
                tagmatchlist = []
                tagmatchlinetotal = []
                result = {}
                for tag in taglist2:
                    result[tag] = 0
                linelist = line.split()
                if "### 🟡" in line:
                    headerlevel3 = line
                for word in linelist:
                    if word[0:3] == "#c/":
                        if word not in tagmatchlinetotal:
                            tagmatchlinetotal.append(word)
                        for tag in taglist2:
                            if tag.lower() in word.lower():
                                result[tag] += 1
                                if word not in tagmatchlist:
                                    tagmatchlist.append(word)
                alltagsfound = True
                for tag in result:
                    if result[tag] == 0:
                        alltagsfound = False
                if alltagsfound:
                    if fullfilename != fullfilenamehold:
                        fileo.write("🔵" + fullfilename + "\n")
                        fullfilenamehold = fullfilename
                    fileo.write(headerlevel3)
                    fileo.write("🟢" + line)
                    if line not in linetotal:
                        linetotal.append(line)
                    for tag in tagmatchlinetotal:
                        if tag not in tagmatchfiletotal:
                            tagmatchfiletotal.append(tag)
                    fileo.write(" \n")
                line = filei.readline()

    fileo.write(f":--------------------------:\n")
    fileo.write(f": TOTAL TAGS MATCHED LIST  :\n")
    fileo.write(f":--------------------------:\n")
    for line in linetotal:
        fileo.write(f" {line}")
    fileo.write(f":--------------------------:\n")

    for tag in tagmatchfiletotal:
        fileo.write(f" {tag} \n")
    fileo.write(f":--------------------------:\n")

    fileo.write(f":--------------------:\n")
    fileo.write(f": TAGS LIST SEARCHED :\n")
    fileo.write(f":--------------------:\n")
    fileo.write(f":> ")
    for tag in taglist2:
        fileo.write(f"+ {tag} ")
    fileo.write(f" \n")
    fileo.write(f":--------------------:\n")

    print(" ")
    fileo.write(f":--------------------:\n")
    fileo.write(f": FILE LIST SEARCHED :\n")
    fileo.write(f":-------------------:\n")
    fileo.write(f": ")
    for tag in taglist1:
        fileo.write(f"+ {tag} ")
    fileo.write(f" \n")
    fileo.write(f":--------------------:\n")
    fileo.write(f" \n")


#
#
# Main:
#
#
# remember these are list terms need to be separated

curr_time = time.strftime("%H:%M:%S", time.localtime())
print("Current Time is :", curr_time)

taglist1 = []  # files
taglist2 = ["numpy", "array"]  # tags

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

dirName = "Z:\SharedA\Obsidian\CodeVault"
fileOutput = "Z:/SharedA/Repos/data/tagsnippet.txt"
programLocation = "Z:/SharedA/Repos/utilities/tagSnippetSearch.py"
# dirName = "Z:\SharedA\Obsidian\AlphaVault"

print("tagNameSearch version 001 Start")
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

print("------------------:")
print("Tag LIST SEARCHED:")
print("------------------:")
print(taglist2)
print("------------------:")
# fmt: off
fileo.write(f":-------------:\n")
# fmt: on
fileo.write(f": PROGRAM RUN : {programLocation} \n")
fileo.write(f":-------------------:\n")
fileo.write(f"Lines Match Summary :\n")
fileo.write(f":-------------------:\n")

allFilesMain = []
allFilesMain = getListOfFiles(dirName, taglist1, excludefile)
processFileMain(allFilesMain, taglist2, excludetag)

fileo.close()
print("------------------------------------- ")
print("tagNameSearch version 001 Termination")
print("Result File       : ", fileOutput)
# %%
