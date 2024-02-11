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
    BlockTypeTid5  = '# ~~ '
    BlockTypeH1d5  = '# +++'
    BlockTypeH2d5  = '# ++ '
    BlockTypeEqu5  = '# == '
    BlockTypePer4  = "# %%"
    BlockTypeNeg5  = "# -- "
    if runMod == "Python":
        extname = ".py"
        P1block = "```python"
        P2block = "```"
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderH1d5 = BlockTypeH1d5
        blockHeaderH2d5 = BlockTypeH2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPer4 = BlockTypePer4
        blockHeaderNeg5 = BlockTypeNeg5
    elif runMod == "Jupyter":
        extname = ".ipynb"
        P1block = "```python"
        P2block = "```"
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderH1d5 = BlockTypeH1d5
        blockHeaderH2d5 = BlockTypeH2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPer4 = BlockTypePer4
        blockHeaderNeg5 = BlockTypeNeg5
    elif runMod == "SQL":
        extname = ".sql"
        P1block = "```sql"
        P2block = "```"
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderH1d5 = BlockTypeH1d5
        blockHeaderH2d5 = BlockTypeH2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPer4 = BlockTypePer4
        blockHeaderNeg5 = BlockTypeTid5
    elif runMod == "txt":
        extname = ".txt"
        P1block = "___"
        P2block = ""
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderH1d5 = BlockTypeH1d5
        blockHeaderH2d5 = BlockTypeH2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPer4 = BlockTypePer4
        blockHeaderNeg5 = BlockTypeTid5
    elif runMod == "ahk":
        extname = ".ahk"
        P1block = "```c"
        P2block = "```"
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderH1d5 = BlockTypeH1d5
        blockHeaderH2d5 = BlockTypeH2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPer4 = BlockTypePer4
        blockHeaderNeg5 = BlockTypeTid5
    elif runMod == "mdown":
        extname = ".mdown"
        P1block = ""
        P2block = ""
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderH1d5 = BlockTypeH1d5
        blockHeaderH2d5 = BlockTypeH2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPer4 = BlockTypePer4
        blockHeaderNeg5 = BlockTypeTid5
    elif runMod == "markdown":
        extname = ".markdown"
        P1block = ""
        P2block = ""
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderH1d5 = BlockTypeH1d5
        blockHeaderH2d5 = BlockTypeH2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPer4 = BlockTypePer4
        blockHeaderNeg5 = BlockTypeTid5
    elif runMod == "data":
        extname = ".data"
        P1block = ""
        P2block = ""
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderH1d5 = BlockTypeH1d5
        blockHeaderH2d5 = BlockTypeH2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPer4 = BlockTypePer4
        blockHeaderNeg5 = BlockTypeTid5
    elif runMod == "csv":
        extname = ".csv"
        P1block = ""
        P2block = ""
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderH1d5 = BlockTypeH1d5
        blockHeaderH2d5 = BlockTypeH2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPer4 = BlockTypePer4
        blockHeaderNeg5 = BlockTypeTid5
    elif runMod == "html":
        extname = ".html"
        P1block = "```python"
        P2block = "```"
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderH1d5 = BlockTypeH1d5
        blockHeaderH2d5 = BlockTypeH2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPer4 = BlockTypePer4
        blockHeaderNeg5 = BlockTypeTid5
    elif runMod == "htm":
        extname = ".htm"
        P1block = "```python"
        P2block = "```"
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderH1d5 = BlockTypeH1d5
        blockHeaderH2d5 = BlockTypeH2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPer4 = BlockTypePer4
        blockHeaderNeg5 = BlockTypeTid5
    else:
        P1block = "```python"
        P2block = "```"
        extname = ".py"
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderH1d5 = BlockTypeH1d5
        blockHeaderH2d5 = BlockTypeH2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPer4 = BlockTypePer4
        blockHeaderNeg5 = BlockTypeNeg5

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
            if extname in [".py",".ipynb"]:
                processMod = "Python"
                extname = ".py"
            else:
                processMod = runMod
            line = filei.readline()
            if blockHeaderPer4 == line[0:4]:
                line = filei.readline()
                if blockHeaderTid5 == line[0:5]:
                    if ("C:\\" in line or "H:\\" in line or "Z:\\" in line):
                        processMod = "Jupyter"
                        extname = ".ipynb"

            if runMod != processMod:
                continue

            if processMod == "Jupyter": 
                dirNameInputSplit = line[5:-1].split("\\")
                dirname1 = dirNameInputSplit[-1]
                dirname2 = dirname1.split(sep=".")
                fullfilename = "".join(dirname2[0])
                dirNameInputSplit.pop()
                dirNameInput = "\\".join(dirNameInputSplit)
                line = filei.readline()
            else:
                dirNameInputSplit = dirNameInput.split("\\")

            dirNameOutputbase = [dirNameOutput]
            clipInputList = dirNameInput.rstrip().split("\\")
            if processMod == "Jupyter":
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
            # append method build output directory changed
            appendFlag = False
            for dirnodes in dirNameInputSplit:
                if dirnodes == "Projects":
                    appendFlag = True
                if appendFlag == True:
                    dirNameOutputbase.append(dirnodes)
            # for dirnodes in dirNameInputSplit:
            #     # if dirnodes not in ["Z:", "SharedA", "Python"]:
            #     if dirnodes not in ["Z:", "SharedA", "C:", "Users", "DDD2", "Documents", "Python", "2data"]:
            #         dirNameOutputbase.append(dirnodes)

            s1 = "\\"
            dirNameOutputFinal = s1.join(dirNameOutputbase)
            os.makedirs(dirNameOutputFinal, exist_ok=True)

            fileOutput = dirNameOutputFinal + "/" + fullfilename + ".md"
            fileo = open(fileOutput, "w")
            fileo = open(fileOutput, "a")

            clipTempList = clipOutputForward.rstrip().split("/")
            i = 0
            clipTempList1 = []
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
                f"vsext::              {extname}   |  **inputext::** {inputFileExtension}   |   [[CodeVault Code]]\n"
            )
            fileo.write(f"runMod::         {runMod}\n")
            fileo.write(f"vsfilename::     {clipOutputFile}/{fullfilename}{extname}\n")
            if processMod == "Jupyter":
                clipInputList = programName.rstrip().split("\\")
                clipOutputForward = "/".join(clipInputList)
                clipOutputDouble = "\\\\".join(clipInputList)
                clipOutputFile = clipOutputForward.rstrip().split(":")
                driveLetter = "".join(clipOutputFile[0])
                clipOutputFile = (
                    "file:///" + driveLetter.lower() + "%3A" + clipOutputFile[1]
                )
                fileo.write(f"jupyterpy::       {clipOutputFile}\n")
                clipOutputFileTemp = clipOutputFile.rstrip().split(".")
                clipOutputFileTemp[1] = ".ipynb"
                clipOutputFileTemp = "".join(clipOutputFileTemp)
                fileo.write(f"jupytermain::   {clipOutputFileTemp}\n")
            fileo.write(f"vssearch::        {clipOutputBackward}\n")

            autoTagListTotal = []
            while line:
                if bool(line.strip()):  # block empty lines
                    linelist = line.split()

                    # write vstag as top line
                    if lineCount == 0:
                        fileo.write("vstags::          `=this.file.tags`\n")
                        fileo.write("___\n")

                    # check if sql comment
                    if "-- com ".lower() == line[0:7].lower(): 
                        if lineCount == 0:
                            if line[7:8] in ['!', '?', '$']:
                                vspriority = line[7:8]
                            else:
                                vspriority = ""
                            fileo.write(f"vscomment::  {line[7:]}")
                            fileo.write(f"vspriority:: {vspriority}\n")
                            fileo.write(f"___\n")
                    # check if python / sql tag
                    elif line[0:3] == '#c/' or line [0:6] == '-- #c/':
                        # write cooment line if in code block
                        if P1BlockModeOn:
                            fileo.write(line.rstrip() + "\n")
                        if P1BlockModeOn:
                            fileo.write(f"{P2block}\n")
                            P1BlockModeOn = False
                        for word in linelist:
                            if word not in autoTagListTotal:
                                if "#c/" in word:
                                    autoTagListTotal.append(word)
                        if len(autoTagListTotal) > 0:
                            autoTagListTotal.sort()
                            for tag in autoTagListTotal:
                                fileo.write(f"{tag} ")
                            fileo.write(" \n")
                            autoTagListTotal = []
                    elif blockHeaderTid5 == line[0:5]:
                        if lineCount == 0:
                            if line[5:6] in ['!', '?', '$']:
                                vspriority = line[5:6]
                            else:
                                vspriority = ""
                            fileo.write(f"vscomment::  {line[5:]}")
                            fileo.write(f"vspriority:: {vspriority}\n")
                            fileo.write(f"___\n")
                    elif blockHeaderH1d5 == line[0:5]:
                        if P1BlockModeOn:
                            fileo.write(f"{P2block}\n")
                            P1BlockModeOn = False
                        fileo.write("# 🟩" + line[5:].rstrip() + "\n")
                    elif blockHeaderH2d5 == line[0:5]:
                        if P1BlockModeOn:
                            fileo.write(f"{P2block}\n")
                            P1BlockModeOn = False
                        fileo.write("## 🟪" + line[5:].rstrip() + "\n")
                    elif blockHeaderEqu5 == line[0:5]:
                        if P1BlockModeOn:
                            fileo.write(f"{P2block}\n")
                            P1BlockModeOn = False
                        fileo.write(line[5:].rstrip() + "\n")
                    elif blockHeaderPer4 == line[0:4] or \
                         blockHeaderNeg5 == line[0:5]:
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
                        ):
                            print(
                                f"invalid OTHER format found on line \
                                    {basefilename} {line}, {blockCount}"
                            )
                        if P1BlockModeOn == False:
                            fileo.write(f"{P1block}\n")
                            P1BlockModeOn = True
                        fileo.write(line.rstrip() + "\n")

                        # exclude comment lines from auto tagging
                        if line.strip()[0] not in ["'", "\"", "#"]:
                            for tag in autoTagListEntry:
                                if tag.lower() in line.lower():
                                    tagtemp = "#c/i/" + tag.lower()
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
                lineCount += 1
        if P1BlockModeOn:
            fileo.write(f"{P2block}\n")
            P1BlockModeOn = False
        if len(autoTagListTotal) > 0:
            autoTagListTotal.sort()
            for tag in autoTagListTotal:
                fileo.write(f"{tag} ")
            fileo.write(" \n")
            autoTagListTotal = []
        fileo.close()


def mainline():
    global inputFileExtension
    global mainFileExtension
    if runMod == "Jupyter":
        inputFileExtension = ".py"
        mainFileExtension = ".ipynb"
    elif runMod == "Python":
        inputFileExtension = ".py"
        mainFileExtension = ".py"
    elif runMod == "SQL":
        inputFileExtension = ".sql"
        mainFileExtension = ".sql"
    elif runMod == "txt":
        inputFileExtension = ".txt"
        mainFileExtension = ".txt"
    elif runMod == "ahk":
        inputFileExtension = ".ahk"
        mainFileExtension = ".ahk"
    elif runMod == "mdown":
        inputFileExtension = ".mdown"
        mainFileExtension = ".mdown"
    elif runMod == "markdown":
        inputFileExtension = ".markdown"
        mainFileExtension = ".markdwon"
    elif runMod == "data":
        inputFileExtension = ".data"
        mainFileExtension = ".data"
    elif runMod == "csv":
        inputFileExtension = ".csv"
        mainFileExtension = ".csv"
    elif runMod == "html":
        inputFileExtension = ".html"
        mainFileExtension = ".html"
    elif runMod == "htm":
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
    print("runMod            :", runMod)
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
autoTagListEntry = ["dictionary","dictreader","sql","sqlite","argv","dataframe",
                    "derekbanas"
]
# fmt: on

curr_time = time.strftime("%H:%M:%S", time.localtime())
allFilesMain = []

# ************************************************************
#   Remote
# ************************************************************
# runMod = "Python"
# dirNameInput = "C:\\2data\\Python\\Projects"
# dirNameOutput = "H:\\Backup\\Obsidian\\CodeVault"
# programLocation = "H:/SharedA/Repos/Utilities/formatpython.py"
# taglist1 = [""]  # files
# mainline()

# runMod = "Jupyter"
# dirNameInput = "C:\\2data\\Python\\Projects"
# dirNameOutput = "H:\\Backup\\Obsidian\\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# taglist1 = [""]  # files
# mainline()

# ************************************************************
#   Main
# ************************************************************
runMod = "Python"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatjupyter.py"
taglist1 = [""]  # files
mainline()

runMod = "Jupyter"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatjupyter.py"
taglist1 = [""]  # files
mainline()

runMod = "SQL"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = [""]  # files
mainline()

runMod = "txt"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = [""]  # files
mainline()

runMod = "ahk"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = [""]  # files
mainline()

runMod = "mdown"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = [""]  # files
mainline()

runMod = "markdown"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = [""]  # files
mainline()

runMod = "data"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = [""]  # files
mainline()

runMod = "csv"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = [""]  # files
mainline()

runMod = "html"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = [""]  # files
mainline()

runMod = "htm"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = [""]  # files
mainline()

