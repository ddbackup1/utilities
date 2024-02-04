# %%
import os
import time


# *****************************************************************************
# 2024-01-25 | First Version of program
# *****************************************************************************
def getListOfFiles(dirNameInput, taglist1, excludefile, includepath, excludepath):
    the_path_list = []
    allFiles = []
    listOfFile = os.listdir(dirNameInput)
    for entry in listOfFile:
        fullPath = os.path.join(dirNameInput, entry)
        the_path_list.append(fullPath)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(
                fullPath, taglist1, excludefile, includepath, excludepath
            )
        else:
            filename, file_extension = os.path.splitext(entry)
            result = {}
            for tag in taglist1:
                result[tag] = 0
            if file_extension == inputFileExtension:
                validfilename = False
                for include1 in includepath:
                    if include1.lower() in fullPath.lower():
                        validfilename = True
                for exclude2 in excludepath:
                    if exclude2.lower() in fullPath.lower():
                        validfilename = False
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
    # indicate last written was P1block or P2block
    # P1BlockModeOn = False
    # headerWritten = False
    BlockTypePer4  = "# %%"
    BlockTypeNeg4  = "# --"
    BlockTypePos4  = '# ++'
    BlockTypeTid4  = '# ~~'
    BlockTypeEqu5  = '# == '
    if mode == "Python":
        extname = ".py"
        P1block = "```python"
        P2block = "```"
        blockHeaderPer4 = BlockTypePer4
        blockHeaderNeg4 = BlockTypeNeg4
        blockHeaderPos4 = BlockTypePos4
        blockHeaderEqu5 = BlockTypeEqu5
    elif mode == "Jupyter":
        extname = ".ipynb"
        P1block = "```python"
        P2block = "```"
        blockHeaderPer4 = BlockTypePer4
        blockHeaderNeg4 = BlockTypeNeg4
        blockHeaderPos4 = BlockTypePos4
        blockHeaderEqu5 = BlockTypeEqu5
    elif mode == "SQL":
        extname = ".sql"
        P1block = "```sql"
        P2block = "```"
        blockHeaderPer4 = BlockTypePer4
        blockHeaderNeg4 = BlockTypeTid4
        blockHeaderPos4 = BlockTypePos4
        blockHeaderEqu5 = BlockTypeEqu5
    elif mode == "txt":
        extname = ".txt"
        P1block = "___"
        P2block = ""
        blockHeaderPer4 = BlockTypeTid4
        blockHeaderNeg4 = BlockTypeTid4
        blockHeaderPos4 = BlockTypePos4
        blockHeaderEqu5 = BlockTypeEqu5
    elif mode == "ahk":
        extname = ".ahk"
        P1block = "```c"
        P2block = "```"
        blockHeaderPer4 = BlockTypeTid4
        blockHeaderNeg4 = BlockTypeTid4
        blockHeaderPos4 = BlockTypePos4
        blockHeaderEqu5 = BlockTypeEqu5
    elif mode == "mdown":
        extname = ".mdown"
        P1block = ""
        P2block = ""
        blockHeaderPer4 = BlockTypeTid4
        blockHeaderNeg4 = BlockTypeTid4
        blockHeaderPos4 = BlockTypePos4
        blockHeaderEqu5 = BlockTypeEqu5
    elif mode == "markdown":
        extname = ".markdown"
        P1block = ""
        P2block = ""
        blockHeaderPer4 = BlockTypeTid4
        blockHeaderNeg4 = BlockTypeTid4
        blockHeaderPos4 = BlockTypePos4
        blockHeaderEqu5 = BlockTypeEqu5
    elif mode == "data":
        extname = ".data"
        P1block = ""
        P2block = ""
        blockHeaderPer4 = BlockTypeTid4
        blockHeaderNeg4 = BlockTypeTid4
        blockHeaderPos4 = BlockTypePos4
        blockHeaderEqu5 = BlockTypeEqu5
    elif mode == "csv":
        extname = ".csv"
        P1block = ""
        P2block = ""
        blockHeaderPer4 = BlockTypeTid4
        blockHeaderNeg4 = BlockTypeTid4
        blockHeaderPos4 = BlockTypePos4
        blockHeaderEqu5 = BlockTypeEqu5
    elif mode == "html":
        extname = ".html"
        P1block = "```python"
        P2block = "```"
        blockHeaderPer4 = BlockTypeTid4
        blockHeaderNeg4 = BlockTypeTid4
        blockHeaderPos4 = BlockTypePos4
        blockHeaderEqu5 = BlockTypeEqu5
    elif mode == "htm":
        extname = ".htm"
        P1block = "```python"
        P2block = "```"
        blockHeaderPer4 = BlockTypeTid4
        blockHeaderNeg4 = BlockTypeTid4
        blockHeaderPos4 = BlockTypePos4
        blockHeaderEqu5 = BlockTypeEqu5
    else:
        P1block = "```python"
        P2block = "```"
        extname = ".py"
        blockHeaderPer4 = BlockTypePer4
        blockHeaderNeg4 = BlockTypeNeg4
        blockHeaderPos4 = BlockTypePos4
        blockHeaderEqu5 = BlockTypeEqu5

    for programName in allFilesMain:
        blockCount = 0
        lineCount = 0
        P1BlockModeOn = False
        headerWritten = False
        basefilename = os.path.basename(programName)
        dirNameInput = os.path.dirname(programName)
        fullfilename, file_extension = os.path.splitext(basefilename)
        print("programName =", programName)
        print("basefilename=", basefilename)
        print("dirNameInput=", dirNameInput)
        print("fullfilename=", fullfilename)

        with open(programName) as filei:
            line = filei.readline()
            # read extra line for jupyter files
            if mode == "Jupyter": 
                if blockHeaderPer4 in line:
                    line = filei.readline()
                    if (blockHeaderPos4 == line[0:4]) and \
                       ("# ++ Z:\\" in line or "# ++ C:\\" in line):
                        dirNameInputSplit = line[5:-1].split("\\")
                        dirname1 = dirNameInputSplit[-1]
                        dirname2 = dirname1.split(sep=".")
                        fullfilename = "".join(dirname2[0])
                        dirNameInputSplit.pop()
                        dirNameInput = "\\".join(dirNameInputSplit)
                        line = filei.readline()
                    else:
                        print ("Invalid header line for Jupyter file")
                        continue
                else:
                    print ("Invalid header line for Jupyter file")
                    continue
            else:
                dirNameInputSplit = dirNameInput.split("\\")

            dirNameOutputbase = [dirNameOutput]
            clipInputList = dirNameInput.rstrip().split("\\")
            if mode == "Jupyter":
                clipOutputBackward = (
                    "\\".join(clipInputList) + "\\" + fullfilename + mainFileExtension
                )
            else:
                clipOutputBackward = "\\".join(clipInputList) + "\\" + basefilename

            clipOutputForward = "/".join(clipInputList)
            clipOutputDouble = "\\\\".join(clipInputList)
            clipOutputFile = clipOutputForward.rstrip().split(":")
            driveLetter = "".join(clipOutputFile[0])
            clipOutputFile = (
                "file:///" + driveLetter.lower() + "%3A" + clipOutputFile[1]
            )
            print("clipOutputFile", clipOutputFile)

            for dirnodes in dirNameInputSplit:
                if dirnodes not in ["Z:", "SharedA", "Python"]:
                    dirNameOutputbase.append(dirnodes)

            s1 = "\\"
            dirNameOutputFinal = s1.join(dirNameOutputbase)
            print(f"dirNameOutputFinal = {dirNameOutputFinal}")
            os.makedirs(dirNameOutputFinal, exist_ok=True)

            fileOutput = dirNameOutputFinal + "/" + fullfilename + ".md"
            print("fileoutput = ", fileOutput)
            fileo = open(fileOutput, "w")
            fileo = open(fileOutput, "a")

            clipTempList = clipOutputForward.rstrip().split("/")
            i = 0
            clipTempList1 = []
            print(clipTempList)
            for clip in clipTempList:
                if i >= 4 and i <= 10:
                    if extname not in clip:
                        clipTempList1.append(clip)
                i += 1
            clipTempList2 = "/".join(clipTempList1)

            fileo.write(f"# 🟩 {fullfilename}\n")
            fileo.write(f"vspath::           {clipOutputForward}\n")
            fileo.write(f"vsfolder::         {clipTempList2}\n")
            fileo.write(
                f"vsext::              {extname}   |   **mode::** {mode}    **inputext::**\
 {inputFileExtension}   |\   [[CodeVault Code]]\n"
            )
            fileo.write(f"vsfilename::     {clipOutputFile}/{fullfilename}{extname}\n")
            if mode == "Jupyter":
                clipInputList = programName.rstrip().split("\\")
                clipOutputForward = "/".join(clipInputList)
                clipOutputDouble = "\\\\".join(clipInputList)
                clipOutputFile = clipOutputForward.rstrip().split(":")
                driveLetter = "".join(clipOutputFile[0])
                clipOutputFile = (
                    "file:///" + driveLetter.lower() + "%3A" + clipOutputFile[1]
                )
                fileo.write(f"vsjupyter::       {clipOutputFile}\n")
            fileo.write(f"vssearch::        {clipOutputBackward}\n")

            autoTagListTotal = []
            while line:
                if bool(line.strip()):  # block empty lines
                    lineCount += 1
                    linelist = line.split()

                    if lineCount == 1:
                        fileo.write("vstags:: `=this.file.tags`\n")
                        fileo.write("___\n")

                    if "# comment: ".lower() == line[0:11].lower() and  lineCount == 1:
                            fileo.write(f"vscomment::  {line[11:]} \n")
                    elif "-- comment: ".lower() == line[0:12].lower() and lineCount == 1:
                            fileo.write(f"vscomment::  {line[12:]} \n")
                    elif blockHeaderPos4 in line[0:4]:
                        if P1BlockModeOn:
                            fileo.write(f"{P2block}\n")
                            P1BlockModeOn = False
                        fileo.write("## 🟪" + line[5:])
                    elif "# #c/" in line[0:5] or "#c/" in line[0:3]:
                        fileo.write(line.rstrip() + "\n")
                        if P1BlockModeOn:
                            fileo.write(f"{P2block}\n")
                            P1BlockModeOn = False
                        for word in linelist:
                            if word not in autoTagListTotal:
                                if word[0:3] == "#c/":
                                    autoTagListTotal.append(word)
                        if len(autoTagListTotal) > 0:
                            autoTagListTotal.sort()
                            for tag in autoTagListTotal:
                                fileo.write(f"{tag} ")
                            fileo.write(" \n")
                            autoTagListTotal = []
                    elif blockHeaderEqu5 in line[0:5]:
                        if P1BlockModeOn:
                            fileo.write(f"{P2block}\n")
                            P1BlockModeOn = False
                        fileo.write(line[5:].rstrip() + "\n")
                    elif blockHeaderPer4 in line[0:4] or \
                         blockHeaderNeg4 in line[0:4]:
                        if bool(line[5:].strip()):
                            if len(autoTagListTotal) > 0:
                                if P1BlockModeOn:
                                    fileo.write(f"{P2block}\n")
                                    P1BlockModeOn = False
                                autoTagListTotal.sort()
                                for tag in autoTagListTotal:
                                    fileo.write(f"{tag} ")
                                    fileo.write(" \n")
                                autoTagListTotal = []
                            if blockCount > 0:
                                if headerWritten == False:
                                    print(
                                        f"missing headerWritten for index: file=\
                                        {basefilename} index={blockCount} \nline={line}"
                                    )
                            blockCount += 1
                            if P1BlockModeOn:
                                fileo.write(f"{P2block}\n")
                                P1BlockModeOn = False
                            fileo.write("### 🟡" + line[5:])
                            fileo.write(f"[{blockCount}]\n")
                            headerWritten = True
                    else:
                        if (
                            line[0:3] == "#--"
                            or line[0:3] == "#++"
                            or line[0:3] == "#%%"
                            or 'comment' in line
                        ):
                            print(
                                f"invalid OTHER format found on line \
                                    {basefilename} {line}, {blockCount}"
                            )
                        if P1BlockModeOn == False:
                            fileo.write(f"{P1block}\n")
                            P1BlockModeOn = True
                        fileo.write(line.rstrip() + "\n")

                        for tag in autoTagListEntry:
                            if tag.lower() in line.lower():
                                tagtemp = "#c/" + tag.lower()
                                if tagtemp not in autoTagListTotal:
                                    autoTagListTotal.append(tagtemp)

                    if "#c/" in line:
                        if line[0:5] == "# #c/" or line[0:3] == "#c/":
                            bsk = 0
                        else:
                            print(
                                f"invalid TAG format found on line \
                                    {basefilename} {line}, {blockCount}"
                            )
                line = filei.readline()
        if P1BlockModeOn:
            fileo.write(f"{P2block}\n")
            P1BlockModeOn = False
        if len(autoTagListTotal) > 0:
            autoTagListTotal.sort()
            fileo.write(f"#c/tsx ")
            for tag in autoTagListTotal:
                fileo.write(f"{tag} ")
            fileo.write(" \n")
            autoTagListTotal = []
        fileo.close()


def mainline():
    global inputFileExtension
    global mainFileExtension
    if mode == "Jupyter":
        inputFileExtension = ".py"
        mainFileExtension = ".ipynb"
    elif mode == "Python":
        inputFileExtension = ".py"
        mainFileExtension = ".py"
    elif mode == "SQL":
        inputFileExtension = ".sql"
        mainFileExtension = ".sql"
    elif mode == "txt":
        inputFileExtension = ".txt"
        mainFileExtension = ".txt"
    elif mode == "ahk":
        inputFileExtension = ".ahk"
        mainFileExtension = ".ahk"
    elif mode == "mdown":
        inputFileExtension = ".mdown"
        mainFileExtension = ".mdown"
    elif mode == "markdown":
        inputFileExtension = ".markdown"
        mainFileExtension = ".markdwon"
    elif mode == "data":
        inputFileExtension = ".data"
        mainFileExtension = ".data"
    elif mode == "csv":
        inputFileExtension = ".csv"
        mainFileExtension = ".csv"
    elif mode == "html":
        inputFileExtension = ".html"
        mainFileExtension = ".html"
    elif mode == "htm":
        inputFileExtension = ".htm"
        mainFileExtension = ".htm"
    else:
        inputFileExtension = ".zzz"
        mainFileExtension = ".zzz"

    print("Current Time is :", curr_time)
    print("formatpython version 002 Start")
    print("------------------------------- ")
    print("Program Location  :", programLocation)
    print("Input   Directory :", dirNameInput)
    print("Output  Direcotry :", dirNameOutput)
    print("Include File List :", taglist1)
    print("Exclude File List :", excludefile)
    print("Include File Path :", includepath)
    print("Exclude File Path :", excludepath)
    print("autoTagListEntry  :", autoTagListEntry)
    print("mode              :", mode)
    print("inputFileExtension:", inputFileExtension)
    print("mainFileExtension :", mainFileExtension)

    print("------------------:")
    print("FILE LIST SEARCHED:")
    print("------------------:")
    print(taglist1)
    print("------------------:")

    allFilesMain = []
    allFilesMain = getListOfFiles(
        dirNameInput, taglist1, excludefile, includepath, excludepath
    )

    processFileMain(allFilesMain)
    print("------------------------------------- ")
    print("formatpython version 002 Termination")


#
# Main:
#
excludefile = [
    "@",
    "$My",
    "2023-",
    "2022-",
    "2021-",
    "excalidraw",
    "excalibrain",
    "obsidian0",
    "copy",
    "backup",
]

includepath = [
    "CrashBook",
    "CrashCourse",
    "Jupyter",
    "LearnProg",
    "Obsidian",
    "PythonforEverybody",
    "PythonforExcel",
    "PythonExercises",
    "SQLite",
    "CS50P",
    "AutoHotKey",
    "Data",
    "Repos",
]
excludepath = [
    "archive",
    "backup",
    "test",
]
# fmt: off
autoTagListEntry = ["dictionary","dictreader","sql","sqlite","select","insert","fetchone",
                    "argv","except","try","dataframe","derekbanas"
]
# fmt: on

curr_time = time.strftime("%H:%M:%S", time.localtime())
allFilesMain = []

mode = "Python"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = ["program"]  # files
mainline()

mode = "Jupyter"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatjupyter.py"
taglist1 = [""]  # files
mainline()

mode = "SQL"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = [""]  # files
mainline()

mode = "txt"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = ["mbox, name"]  # files
mainline()

mode = "ahk"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = [""]  # files
mainline()

mode = "mdown"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = [""]  # files
mainline()

mode = "markdown"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = [""]  # files
mainline()

mode = "data"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = [""]  # files
mainline()

mode = "csv"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = [""]  # files
mainline()

mode = "html"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = [""]  # files
mainline()

mode = "htm"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = [""]  # files
mainline()

# %%
