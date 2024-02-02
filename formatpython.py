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
    P1LastBlock = False
    headerWritten = False
    if mode == "Python":
        extname = ".py"
        P1block = "```python"
        P2block = "```"
        blockHeader = "# %%"
        blockHeaderSkip = "# --"
    elif mode == "Jupyter":
        extname = ".ipynb"
        P1block = "```python"
        P2block = "```"
        blockHeader = "# --"
        blockHeaderSkip = "# %%"
    elif mode == "SQL":
        extname = ".sql"
        P1block = "```sql"
        P2block = "```"
        blockHeader = "# %%"
        blockHeaderSkip = "# --"
    elif mode == "txt":
        extname = ".txt"
        P1block = "___"
        P2block = ""
        blockHeader = "# ~~"
        blockHeaderSkip = "# ~~"
    elif mode == "ahk":
        extname = ".ahk"
        P1block = "```c"
        P2block = "```"
        blockHeader = "# ~~"
        blockHeaderSkip = "# ~~"
    elif mode == "mdown":
        extname = ".mdown"
        P1block = "___"
        P2block = ""
        blockHeader = "# ~~"
        blockHeaderSkip = "# ~~"
    elif mode == "markdown":
        extname = ".markdown"
        P1block = "___"
        P2block = ""
        blockHeader = "# ~~"
        blockHeaderSkip = "# ~~"
    elif mode == "data":
        extname = ".data"
        P1block = "___"
        P2block = ""
        blockHeader = "# ~~"
        blockHeaderSkip = "# ~~"
    elif mode == "csv":
        extname = ".csv"
        P1block = "___"
        P2block = ""
        blockHeader = "# ~~"
        blockHeaderSkip = "# ~~"
    elif mode == "html":
        extname = ".html"
        P1block = "```python"
        P2block = "```"
        blockHeader = "# ~~"
        blockHeaderSkip = "# ~~"
    elif mode == "htm":
        extname = ".htm"
        P1block = "```python"
        P2block = "```"
        blockHeader = "# ~~"
        blockHeaderSkip = "# ~~"
    else:
        P1block = "```python"
        P2block = "```"
        extname = ".py"
        blockHeader = "# %%"
        blockHeaderSkip = "# --"

    for programName in allFilesMain:
        blockCount = 0
        P1Written = False
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
            if mode == "Jupyter" and blockHeaderSkip in line:
                line = filei.readline()
            dirNameOutputbase = [dirNameOutput]
            if "# ++ Z:\\" in line:
                dirNameInputSplit = line[5:-1].split("\\")
                dirname1 = dirNameInputSplit[-1]
                dirname2 = dirname1.split(sep=".")
                fullfilename = "".join(dirname2[0])
                dirNameInputSplit.pop()
                dirNameInput = "\\".join(dirNameInputSplit)
                line = filei.readline()
            else:
                dirNameInputSplit = dirNameInput.split("\\")

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
                f"vsext::              {extname[1:len(extname)]}   |   **mode::** {mode}    **inputext::** {inputFileExtension[1:len(inputFileExtension)]}   |   [[CodeVault Code]]\n"
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
                    linelist = line.split()
                    if "# comment: ".lower() == line[0:11].lower():
                        if blockCount == 0:
                            fileo.write(f"vscomment::   {line[11:len(line)]}\n")
                    elif "-- comment: ".lower() == line[0:12].lower():
                        if blockCount == 0:
                            fileo.write(f"vscomment::   {line[12:len(line)]}\n")
                    elif "# ++" in line[0:4]:
                        if P1LastBlock:
                            fileo.write(f"{P2block}\n")
                            P1LastBlock = False
                        # fmt: off
                        fileo.write("## 🟪" + line[5:len(line)])
                    # fmt: on
                    elif "# #c/" in line[0:5] or "#c/" in line[0:3]:
                        fileo.write(line.rstrip() + "\n")
                        if P1LastBlock:
                            fileo.write(f"{P2block}\n")
                            P1LastBlock = False
                        linelist = line.split()
                        for word in linelist:
                            if word not in autoTagListTotal:
                                if word[0:3] == "#c/":
                                    autoTagListTotal.append(word)
                        if len(autoTagListTotal) > 0:
                            autoTagListTotal.sort()
                            fileo.write(f"#c/tsx ")
                            for tag in autoTagListTotal:
                                fileo.write(f"{tag} ")
                            fileo.write(" \n")
                            autoTagListTotal = []
                    elif blockHeader in line[0:4]:
                        if bool(line[4 : len(line)].strip()):
                            if blockCount > 0:
                                if headerWritten == False:
                                    print(
                                        f"missing headerWritten for index: file=\
                                        {basefilename} index={blockCount} \nline={line}"
                                    )
                            blockCount += 1
                            if P1LastBlock:
                                fileo.write(f"{P2block}\n")
                                P1LastBlock = False
                            # if characters on this line write header
                            # fmt: off
                            fileo.write("### 🟡" + line[5:len(line)])
                            fileo.write(f"[{blockCount}]\n")
                            # fmt: on
                            headerWritten = True
                            if P1LastBlock == False:
                                P1Written = True
                                if blockCount == 0:
                                    fileo.write(f"___\n")
                                fileo.write(f"{P1block}\n")
                                P1LastBlock = True
                            # fmt: off
                            fileo.write("# " + line[5:len(line.strip())] + '\n')
                        else:
                            if P1Written == False:
                                P1Written = True
                                if blockCount == 0:
                                    fileo.write(f"___\n")
                                fileo.write(f"{P1block}\n")
                                P1LastBlock = True
                    # fmt: on
                    elif blockHeaderSkip in line[0:4]:
                        bsk = 0
                    else:
                        if (
                            line[0:3] == "#--"
                            or line[0:3] == "#++"
                            or line[0:3] == "#%%"
                        ):
                            print(
                                f"invalid control character \
                                    {basefilename} {line}, {blockCount}"
                            )
                        else:
                            if P1Written == False:
                                P1Written = True
                                if blockCount == 0:
                                    fileo.write(f"___\n")
                                fileo.write(f"{P1block}\n")
                                P1LastBlock = True
                            for tag in autoTagListEntry:
                                if tag.lower() in line.lower():
                                    tagtemp = "#c/" + tag.lower()
                                    if tagtemp not in autoTagListTotal:
                                        autoTagListTotal.append(tagtemp)
                            fileo.write(line.rstrip() + "\n")

                    if "#c/" in line:
                        if line[0:5] == "# #c/" or line[0:3] == "#c/":
                            bsk = 0
                        else:
                            print(
                                f"invalid tag character \
                                    {basefilename} {line}, {blockCount}"
                            )
                line = filei.readline()
        if P1LastBlock:
            fileo.write(f"{P2block}\n")
            P1LastBlock = False
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
        inputFileExtension = ".txt"
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
                    "argv","except","try",
]
# fmt: on

curr_time = time.strftime("%H:%M:%S", time.localtime())
allFilesMain = []

mode = "Python"
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = ["IOand"]  # files
mainline()

mode = "Jupyter"
dirNameInput = "Z:\SharedA\Python\Projects\Data\jupyter"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatjupyter.py"
taglist1 = ["jupfile"]  # files
mainline()

# mode = "SQL"
# dirNameInput = "Z:\SharedA\Python\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# taglist1 = [""]  # files
# mainline()

# mode = "txt"
# dirNameInput = "Z:\SharedA\Python\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# taglist1 = ["mbox, name"]  # files
# mainline()

# mode = "ahk"
# dirNameInput = "Z:\SharedA\Python\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# taglist1 = [""]  # files
# mainline()

# mode = "mdown"
# dirNameInput = "Z:\SharedA\Python\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# taglist1 = [""]  # files
# mainline()

# mode = "markdown"
# dirNameInput = "Z:\SharedA\Python\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# taglist1 = [""]  # files
# mainline()

# mode = "data"
# dirNameInput = "Z:\SharedA\Python\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# taglist1 = [""]  # files
# mainline()

# mode = "csv"
# dirNameInput = "Z:\SharedA\Python\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# taglist1 = [""]  # files
# mainline()

# mode = "html"
# dirNameInput = "Z:\SharedA\Python\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# taglist1 = [""]  # files
# mainline()

# mode = "htm"
# dirNameInput = "Z:\SharedA\Python\Projects"
# dirNameOutput = "H:\Backup\Obsidian\CodeVault"
# programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
# taglist1 = [""]  # files
# mainline()
