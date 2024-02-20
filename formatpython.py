# %%
import os
import time


# *****************************************************************************
# 2024-01-25 | First Version of program
# *****************************************************************************
def getListOfFiles(dirNameInput):
    the_path_list = []
    allFiles = []
    listOfFile = os.listdir(dirNameInput)
    for entry in listOfFile:
        fullPath = os.path.join(dirNameInput, entry)
        the_path_list.append(fullPath)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            filename, file_extension = os.path.splitext(entry)
            result = {}
            # tags are now a or condition comment out and condition
            # for includeName1 in includefile:
            #     result[includeName1] = 0
            validfilename = False
            if file_extension == inputFileExtension:
                # if includepath empty
                if not includepath:
                    validfilename = True
                else:
                    for includeName2 in includepath:
                        if includeName2.lower() in fullPath.lower():
                            validfilename = True
                if validfilename == True:
                    validfilename = False
                    # if includefile empty
                    if not includefile:
                        validfilename = True
                    else:
                        for includeName1 in includefile:
                            if includeName1.lower() in filename.lower():
                                validfilename = True
                        # tags are now a or condition comment out and condition
                        # result[includeName1] += 1
                        # allfileFound = True
                        # for tag in result:
                        #     if result[tag] == 0:
                        #         allfileFound = False
                if validfilename == True:
                    # if excludepath has entry
                    if excludepath:
                        for excludeName1 in excludepath:
                            if excludeName1.lower() in fullPath.lower():
                                validfilename = False
                if validfilename == True:
                    # if excludefile has entry
                    if excludefile:
                        for excludeName2 in excludefile:
                            if excludeName2 in filename:
                                validfilename = False
                if validfilename:
                    allFiles.append(fullPath)
    return allFiles


def processFileMain(allFilesMain):
    # indicate last written was P1block or P2block
    # P1BlockModeOn = False
    # headerWritten = False
    # (# == - [ ]) checkbox    (#c/) anywhere in line tag
    BlockTypeTid5 = "# ~~ "  # headers
    BlockTypeP3d5 = "# +++"  # level 1
    BlockTypeP2d5 = "# ++ "  # level 2
    BlockTypePec4 = "# %%"  # level 3
    BlockTypeN2d5 = "# -- "  # level 3
    BlockTypeN3d5 = "# ---"  # level 4
    BlockTypeEqu5 = "# == "  # remove
    if runMod == "Python":
        extname = ".py"
        P1block = "```python"
        P2block = "```"
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderP3d5 = BlockTypeP3d5
        blockHeaderP2d5 = BlockTypeP2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPec4 = BlockTypePec4
        blockHeaderN2d5 = BlockTypeN2d5
        blockHeaderN3d5 = BlockTypeN3d5
    elif runMod == "Jupyter":
        extname = ".ipynb"
        P1block = "```python"
        P2block = "```"
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderP3d5 = BlockTypeP3d5
        blockHeaderP2d5 = BlockTypeP2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPec4 = BlockTypePec4
        blockHeaderN2d5 = BlockTypeN2d5
        blockHeaderN3d5 = BlockTypeN3d5
    elif runMod == "SQL":
        extname = ".sql"
        P1block = "```sql"
        P2block = "```"
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderP3d5 = BlockTypeP3d5
        blockHeaderP2d5 = BlockTypeP2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPec4 = BlockTypePec4
        blockHeaderN2d5 = BlockTypeN2d5
        blockHeaderN3d5 = BlockTypeN3d5
    elif runMod == "txt":
        extname = ".txt"
        P1block = ""
        P2block = ""
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderP3d5 = BlockTypeP3d5
        blockHeaderP2d5 = BlockTypeP2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPec4 = BlockTypePec4
        blockHeaderN2d5 = BlockTypeN2d5
        blockHeaderN3d5 = BlockTypeN3d5
    elif runMod == "ahk":
        extname = ".ahk"
        P1block = "```c"
        P2block = "```"
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderP3d5 = BlockTypeP3d5
        blockHeaderP2d5 = BlockTypeP2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPec4 = BlockTypePec4
        blockHeaderN2d5 = BlockTypeN2d5
        blockHeaderN3d5 = BlockTypeN3d5
    elif runMod == "mdown":
        extname = ".mdown"
        P1block = ""
        P2block = ""
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderP3d5 = BlockTypeP3d5
        blockHeaderP2d5 = BlockTypeP2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPec4 = BlockTypePec4
        blockHeaderN2d5 = BlockTypeN2d5
        blockHeaderN3d5 = BlockTypeN3d5
    elif runMod == "markdown":
        extname = ".markdown"
        P1block = ""
        P2block = ""
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderP3d5 = BlockTypeP3d5
        blockHeaderP2d5 = BlockTypeP2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPec4 = BlockTypePec4
        blockHeaderN2d5 = BlockTypeN2d5
        blockHeaderN3d5 = BlockTypeN3d5
    elif runMod == "md":
        extname = ".md"
        P1block = ""
        P2block = ""
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderP3d5 = BlockTypeP3d5
        blockHeaderP2d5 = BlockTypeP2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPec4 = BlockTypePec4
        blockHeaderN2d5 = BlockTypeN2d5
        blockHeaderN3d5 = BlockTypeN3d5
    elif runMod == "data":
        extname = ".data"
        P1block = ""
        P2block = ""
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderP3d5 = BlockTypeP3d5
        blockHeaderP2d5 = BlockTypeP2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPec4 = BlockTypePec4
        blockHeaderN2d5 = BlockTypeN2d5
        blockHeaderN3d5 = BlockTypeN3d5
    elif runMod == "csv":
        extname = ".csv"
        P1block = ""
        P2block = ""
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderP3d5 = BlockTypeP3d5
        blockHeaderP2d5 = BlockTypeP2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPec4 = BlockTypePec4
        blockHeaderN2d5 = BlockTypeN2d5
        blockHeaderN3d5 = BlockTypeN3d5
    elif runMod == "html":
        extname = ".html"
        P1block = "```python"
        P2block = "```"
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderP3d5 = BlockTypeP3d5
        blockHeaderP2d5 = BlockTypeP2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPec4 = BlockTypePec4
        blockHeaderN2d5 = BlockTypeN2d5
        blockHeaderN3d5 = BlockTypeN3d5
    elif runMod == "htm":
        extname = ".htm"
        P1block = "```python"
        P2block = "```"
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderP3d5 = BlockTypeP3d5
        blockHeaderP2d5 = BlockTypeP2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPec4 = BlockTypePec4
        blockHeaderN2d5 = BlockTypeN2d5
        blockHeaderN3d5 = BlockTypeN3d5
    elif runMod == "xlsx":
        extname = ".xlsx"
        P1block = "```python"
        P2block = "```"
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderP3d5 = BlockTypeP3d5
        blockHeaderP2d5 = BlockTypeP2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPec4 = BlockTypePec4
        blockHeaderN2d5 = BlockTypeN2d5
        blockHeaderN3d5 = BlockTypeN3d5
    else:
        P1block = "```python"
        P2block = "```"
        extname = ".py"
        blockHeaderTid5 = BlockTypeTid5
        blockHeaderP3d5 = BlockTypeP3d5
        blockHeaderP2d5 = BlockTypeP2d5
        blockHeaderEqu5 = BlockTypeEqu5
        blockHeaderPec4 = BlockTypePec4
        blockHeaderN2d5 = BlockTypeN2d5
        blockHeaderN3d5 = BlockTypeN3d5

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
            # may not need .ipynb for now leaving 2024-02-13
            if extname in [".py", ".ipynb"]:
                processMod = "Python"
                extname = ".py"
            else:
                processMod = runMod
            if extname not in [".xlsx"]:
                line = filei.readline()
                # if sql comment strip comment so processed like python
                # if sql comment check further
                if line[0:4] == "-- #":
                    if line[3:8] in [
                        "# ~~ ",
                        "# +++",
                        "# ++ ",
                        "# == ",
                        "# %% ",
                        "# -- ",
                    ]:
                        line = line[3:].rstrip() + "\n"
                if blockHeaderPec4 == line[0:4]:
                    # if nothing on line read next
                    if bool(line[5:].strip()):
                        bsk = 0
                    else:
                        line = filei.readline()
                        # if sql comment strip comment so processed like python
                        if line[0:4] == "-- #":
                            if line[3:8] in [
                                "# ~~ ",
                                "# +++",
                                "# ++ ",
                                "# == ",
                                "# %% ",
                                "# -- ",
                            ]:
                                line = line[3:].rstrip() + "\n"
                        if blockHeaderTid5 == line[0:5]:
                            if "C:\\" in line or "H:\\" in line or "Z:\\" in line:
                                processMod = "Jupyter"
                                extname = ".ipynb"
                # block runMod Jupyter python from being processed runMod Python
                #       only time these two cannot match
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
                # if sql comment strip comment so processed like python
                if line[0:4] == "-- #":
                    if line[3:8] in [
                        "# ~~ ",
                        "# +++",
                        "# ++ ",
                        "# == ",
                        "# %% ",
                        "# -- ",
                    ]:
                        line = line[3:].rstrip() + "\n"
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
                if dirnodes == dirmodeSearch:
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
            clipTempList1 = []
            appendFlag = False
            for dirnodes in clipTempList:
                # this check is reversed to block main dir from being appended
                if appendFlag == True:
                    clipTempList1.append(dirnodes)
                if dirnodes == dirmodePrint:
                    appendFlag = True
            clipTempList2 = "/".join(clipTempList1)

            fileo.write(f"# 🟩 {fullfilename}\n")
            fileo.write(f"vspath::           {clipOutputForward}\n")
            fileo.write(f"explorerpath:: {clipOutputFile}\n")
            fileo.write(f"vsfolder::         {clipTempList2}\n")
            fileo.write(
                f"vsext::              {extname}   |  **inputext::** {inputFileExtension}   |   [[CodeVault Code]]  |  [[$MyTags]]\n"
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
            if extname in [".xlsx"]:
                continue

            while line:
                if bool(line.strip()):  # block empty lines
                    linelist = line.split()

                    # write vstag as top line
                    if lineCount == 0:
                        fileo.write("vstags::          `=this.file.tags`\n")
                        fileo.write("___\n")

                    # check if python / sql tag
                    if "#c/" in line:
                        # write comment line if in code block and code block being used
                        if P1block != "":
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
                        # process comments
                        if lineCount == 0:
                            if line[5:6] in ["!", "?", "$"]:
                                vspriority = line[5:6]
                            else:
                                vspriority = ""
                            fileo.write(f"vscomment::  {line[5:]}")
                            fileo.write(f"vspriority:: {vspriority}\n")
                            fileo.write(f"___\n")
                    elif blockHeaderP3d5 == line[0:5]:
                        if P1BlockModeOn:
                            fileo.write(f"{P2block}\n")
                            P1BlockModeOn = False
                        fileo.write("# 🟩" + line[5:].rstrip() + "\n")
                    elif blockHeaderP2d5 == line[0:5]:
                        if P1BlockModeOn:
                            fileo.write(f"{P2block}\n")
                            P1BlockModeOn = False
                        fileo.write("## 🟪" + line[5:].rstrip() + "\n")
                    elif blockHeaderN3d5 == line[0:5]:
                        if P1BlockModeOn:
                            fileo.write(f"{P2block}\n")
                            P1BlockModeOn = False
                        fileo.write("#### 🟠" + line[5:].rstrip() + "\n")
                    elif blockHeaderEqu5 == line[0:5]:
                        if P1BlockModeOn:
                            fileo.write(f"{P2block}\n")
                            P1BlockModeOn = False
                        fileo.write(line[5:].rstrip() + "\n")
                    elif blockHeaderPec4 == line[0:4] or blockHeaderN2d5 == line[0:5]:
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
                        if line.strip()[0] not in ["'", '"', "#"]:
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
                if line[0:4] == "-- #":
                    if line[3:8] in [
                        "# ~~ ",
                        "# +++",
                        "# ++ ",
                        "# == ",
                        "# %% ",
                        "# -- ",
                    ]:
                        line = line[3:].rstrip() + "\n"
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
        mainFileExtension = ".markdown"
    elif runMod == "md":
        inputFileExtension = ".md"
        mainFileExtension = ".md"
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
    elif runMod == "xlsx":
        inputFileExtension = ".xlsx"
        mainFileExtension = ".xlsx"
    else:
        inputFileExtension = ".zzz"
        mainFileExtension = ".zzz"

    print("Current Time is :", curr_time)
    print("formatpython version 002 Start")
    print("------------------------------- ")
    print("Program Location  :", programLocation)
    print("Input   Directory :", dirNameInput)
    print("Output  Direcotry :", dirNameOutput)
    print("Include File List :", includefile)
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
    print(includefile)
    print("------------------:")

    allFilesMain = []
    allFilesMain = getListOfFiles(dirNameInput)

    processFileMain(allFilesMain)
    print("------------------------------------- ")
    print("formatpython version 002 Termination")


#
# Main:
#
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
includefile = []

excludepath = ["archive", "backup", "test"]

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

autoTagListEntry = [
    "dictionary",
    "dictreader",
    "sql",
    "sqlite",
    "argv",
    "dataframe",
    "derekbanas",
]

curr_time = time.strftime("%H:%M:%S", time.localtime())
allFilesMain = []

# fmt: off
# ************************************************************
#   Remote
# ************************************************************
# runMod = "Python"
# includepath = ["Projects","PythonExercises"]
# includefile = ["Exercise0"]
# excludepath = ["archive", "backup", "test"]
# excludefile = []
# dirmodeSearch = "Projects"
# dirmodePrint = "Projects"
# dirNameInput = "C:\\2data\\Python\\Projects"
# dirNameOutput = "H:\\Backup\\Obsidian\\CodeVault"
# programLocation = "H:/SharedA/Repos/Utilities/formatpython.py"
# mainline()

# runMod = "Jupyter"
# includepath = ["Projects"]
# includefile = []
# excludepath = ["archive", "backup", "test"]
# excludefile = []
# dirmodeSearch = "Projects"
# dirmodePrint = "Projects"
# dirNameInput = "C:\\2data\\Python\\Projects"
# dirNameOutput = "H:\\Backup\\Obsidian\\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# mainline()

# runMod = "markdown"
# includepath = []
# includefile = []
# excludepath = ["Images", "InfoSelect", "Obsidian","Python","Typora","Zotero"]
# excludefile = []
# dirmodeSearch = "2data"
# dirmodePrint = "2data"
# dirNameInput = "C:\\2data"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# mainline()

# runMod = "xlsx"
# includepath = []
# includefile = []
# excludepath = ["Images", "InfoSelect", "Obsidian","Typora","Zotero","ARFB","Retirement","Python"]
# excludefile = []
# dirmodeSearch = "2data"
# dirmodePrint = "2data"
# dirNameInput = "C:\\2data"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# mainline()

# runMod = "xlsx"
# includepath = []
# includefile = []
# excludepath = ["z_python-for-excel"]
# excludefile = []
# dirmodeSearch = "Projects"
# dirmodePrint = "Projects"
# dirNameInput = "C:\\2data\\Python\\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# mainline()

# ************************************************************
#   Main Execution
# ************************************************************
includepath = ["PythonforExcel","PythonExercises","SQLite", "CS50P","Repos"]
includepath = ["PythonforExcel","PythonExercises","SQLite", "CS50P","Repos"]
includefile = []
excludepath = ["archive", "backup", "test"]
excludefile = ["copy","backup"]
autoTagListEntry = ["dictionary","dictreader","sql","sqlite","argv","dataframe",
"derekbanas"]

runMod = "Python"
includefile = ["Exercise0"]
dirmodeSearch = "Projects"
dirmodePrint = "Projects"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatjupyter.py"
mainline()

runMod = "Jupyter"
includefile = []
dirmodeSearch = "Projects"
dirmodePrint = "Projects"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatjupyter.py"
mainline()

includepath = ["SharedA"]
includefile = []
excludepath = ["Images", "InfoSelect", "Obsidian","Python","Typora","Zotero"]
excludefile = []
runMod = "markdown"
dirmodeSearch = "SharedA"
dirmodePrint = "SharedA"
dirNameInput = "Z:\SharedA"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
includefile = []  # files
mainline()

# ************************************************************
#   Other
# ************************************************************
# runMod = "SQL"
# includefile = []
# dirmodeSearch = "Projects"
# dirmodePrint = "Projects"
# dirNameInput = "Z:\SharedA\Python\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# mainline()

# runMod = "txt"
# includefile = []
# dirmodeSearch = "Projects"
# dirmodePrint = "Projects"
# dirNameInput = "Z:\SharedA\Python\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# mainline()

# runMod = "ahk"
# includefile = []
# dirmodeSearch = "Projects"
# dirmodePrint = "Projects"
# dirNameInput = "Z:\SharedA\Python\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# mainline()

# runMod = "mdown"
# includefile = []
# dirmodeSearch = "Projects"
# dirmodePrint = "Projects"
# dirNameInput = "Z:\SharedA\Python\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# mainline()

# runMod = "data"
# includefile = []
# dirmodeSearch = "Projects"
# dirmodePrint = "Projects"
# dirNameInput = "Z:\SharedA\Python\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# mainline()

# runMod = "csv"
# includefile = []
# dirmodeSearch = "Projects"
# dirmodePrint = "Projects"
# dirNameInput = "Z:\SharedA\Python\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# mainline()

# runMod = "html"
# includefile = []
# dirmodeSearch = "Projects"
# dirmodePrint = "Projects"
# dirNameInput = "Z:\SharedA\Python\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# includefile = []  # files
# mainline()

# runMod = "htm"
# includefile = []
# dirmodeSearch = "Projects"
# dirmodePrint = "Projects"
# dirNameInput = "Z:\SharedA\Python\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# mainline()

# ************************************************************
#   Miscellaneous
# ************************************************************
# runMod = "xlsx"
# includepath = []
# includefile = []
# excludepath = ["Images", "InfoSelect", "Obsidian","Typora","Zotero","ARFB","Retirement","Python"]
# excludefile = []
# dirmodeSearch = "SharedA"
# dirmodePrint = "Z:"
# dirNameInput = "Z:\SharedA"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# mainline()

# runMod = "xlsx"
# includepath = []
# includefile = []
# excludepath = ["z_python-for-excel"]
# excludefile = []
# dirmodeSearch = "Projects"
# dirmodePrint = "Projects"
# dirNameInput = "Z:\SharedA\Python\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# mainline()

# fmt: on

mainline()
# %%
