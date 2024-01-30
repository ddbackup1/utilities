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
    tagfoundlisttotal = []
    filelist = []
    tagmain = []
    for i in range(0, 26):
        value1 = "#" + chr(97 + i)
        if value1 not in excludetag:
            tagmain.append(value1)
    for programName in allFilesMain:
        basefilename = os.path.basename(programName)
        fullfilename, file_extension = os.path.splitext(basefilename)
        index01 = 0
        with open(programName) as filei:
            line = filei.readline()
            result = {}
            tagfoundlistfile = []
            for tag in taglist2:
                result[tag] = 0
            while line:
                linelist = line.split()
                for word in linelist:
                    for tag in taglist2:
                        if tag[0:1] == "/":
                            tagl = len(tag) + 1
                            tagw = tag[1:tagl]
                        else:
                            tagw = tag
                        if tagw.lower() in word.lower():
                            if tag[0:1] == "/":
                                if word[0:1] == "#":
                                    result[tag] += 1
                            else:
                                result[tag] += 1
                for word in linelist:
                    for tag1 in tagmain:
                        if word[0:2] in tagmain:
                            if word not in tagfoundlistfile:
                                tagfoundlistfile.append(word)
                line = filei.readline()
        alltagsfound = True
        for tag in result:
            if result[tag] == 0:
                alltagsfound = False
        if alltagsfound:
            filelist.append(basefilename)
            fileo.write(f"{basefilename}\n")
            for tag in taglist2:
                fileo.write(f" :>{tag}:  ")
                if tag[0:1] == "/":
                    tagl = len(tag) + 1
                    tagw = tag[1:tagl]
                else:
                    tagw = tag
                for tag in tagfoundlistfile:
                    if tagw.lower() in tag.lower():
                        fileo.write(f"{tag} ")
                fileo.write(f" \n")
            fileo.write(f" \n")
            for tag in tagfoundlistfile:
                if tag not in tagfoundlisttotal:
                    tagfoundlisttotal.append(tag)

    fileo.write(f":--------------------------:\n")
    fileo.write(f": TOTAL TAGS MATCHED LIST  :\n")
    fileo.write(f":--------------------------:\n")
    for tag in taglist2:
        fileo.write(f"  + {tag}:>")
        if tag[0:1] == "/":
            tagl = len(tag) + 1
            tagw = tag[1:tagl]
        else:
            tagw = tag
        for tag in tagfoundlisttotal:
            if tagw.lower() in tag.lower():
                fileo.write(f" {tag} ")
        fileo.write(f" \n")
    fileo.write(f":--------------------------:\n")

    print(" ")
    fileo.write(f":--------------------:\n")
    fileo.write(f": FILE LIST SEARCHED :\n")
    fileo.write(f":--------------------:\n")
    fileo.write(f": ")
    for tag in taglist1:
        fileo.write(f"+ {tag} ")
    fileo.write(f" \n")
    fileo.write(f":--------------------:\n")
    for file1 in sorted(filelist):
        fileo.write(f" :> {file1}\n")
    fileo.write(f":--------------------:\n")
    fileo.write(f" \n")

    print("------------------:")
    print("TAGS LIST SEARCHED:")
    print("------------------:")
    print(taglist2)
    print("------------------:")

    fileo.write(f":--------------------:\n")
    fileo.write(f": TAGS LIST SEARCHED :\n")
    fileo.write(f":--------------------:\n")
    fileo.write(f":> ")
    for tag in taglist2:
        fileo.write(f"+ {tag} ")
    fileo.write(f" \n")
    fileo.write(f":--------------------:\n")

    for tag in sorted(tagfoundlisttotal):
        fileo.write(f"{tag}\n")


# Main:
# remember these are list terms need to be separated
taglist1 = []  # files
taglist2 = ["/SQL", "lam"]  # tags

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

dirName = "H:\Backup\Obsidian\CodeVault"
fileOutput = "Z:/SharedA/Repos/data/tagsearch.txt"
programLocation = "Z:/SharedA/Repos/utilities/tagNameSearch.py"
# dirName = "Z:\SharedA\Obsidian\AlphaVault"

curr_time = time.strftime("%H:%M:%S", time.localtime())
print("Current Time is :", curr_time)

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
# fmt: off
fileo.write(f":-------------:\n")
# fmt: on
fileo.write(f": PROGRAM RUN : {programLocation} \n")
fileo.write(f":-------------:\n")
fileo.write(f"File/Tag Match Summary: \n")
fileo.write(f" \n")
for tag in taglist1:
    fileo.write(f"{tag} + ")

allFilesMain = []
allFilesMain = getListOfFiles(dirName, taglist1, excludefile)
processFileMain(allFilesMain, taglist2, excludetag)

fileo.close()
print("------------------------------------- ")
print("tagNameSearch version 001 Termination")
print("Result File       : ", fileOutput)
# %%
