# %%
import os
import time


# *****************************************************************************
# 2024-01-25 | First Version of program
# *****************************************************************************
def getListOfFiles(dirNameInput, taglist1, excludefile):
    the_path_list = []
    allFiles = []
    listOfFile = os.listdir(dirNameInput)
    for entry in listOfFile:
        fullPath = os.path.join(dirNameInput, entry)
        the_path_list.append(fullPath)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath, taglist1, excludefile)
        else:
            filename, file_extension = os.path.splitext(entry)
            result = {}
            for tag in taglist1:
                result[tag] = 0
            if file_extension == inputFileExtension:
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
    # indcate last written was P1block or P2block
    P1LastBlock = False
    headerWritten = False
    P1block = "```python"
    P2block = "```"

    for programName in allFilesMain:
        blockCount = 0
        P1Written = False
        alphaNumericProcessed = False
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
            if inputFileExtension == ".txt":
                line = filei.readline()
            dirNameOutputbase = [dirNameOutput]
            if "# ++ Z:\\" in line:
                dirNameInputSplit = line[5:-1].split("\\")
                dirname1 = dirNameInputSplit[-1]
                dirname2 = dirname1.split(sep=".")
                fullfilename = "".join(dirname2[0])
                dirNameInputSplit.pop()
                extname = ".ipynb"
                dirNameInput = "\\".join(dirNameInputSplit)
                blockHeader = "# --"
                blockHeaderSkip = "# %%"
                line = filei.readline()
                filequalifier = " Jupyter"
            else:
                dirNameInputSplit = dirNameInput.split("\\")
                extname = ".py"
                blockHeader = "# %%"
                blockHeaderSkip = "# --"
                filequalifier = ""

            clipInputList = dirNameInput.rstrip().split("\\")
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
            fileo.write(f"# 🟩 {fullfilename}{filequalifier}\n")
            fileo.write(f"- {clipOutputForward}\n")
            fileo.write(f"- {clipOutputFile}/{fullfilename}{extname}\n")
            autoTagListTotal = []
            while line:
                if bool(line.strip()):  # block empty lines
                    linelist = line.split()

                    if "# ++" in line[0:4]:
                        if P1LastBlock:
                            fileo.write(f"{P2block}\n")
                            P1LastBlock = False
                        # fmt: off
                        fileo.write("## 🟪" + line[5:len(line)])
                    # fmt: on
                    elif "# #c/" in line[0:5] or "#c/" in line[0:3]:
                        fileo.write(line)
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
                                fileo.write(f"{P1block}\n")
                                P1LastBlock = True
                            # fmt: off
                            fileo.write("# " + line[5:len(line.strip())] + '\n')
                        else:
                            if P1Written == False:
                                P1Written = True
                                fileo.write(f"{P1block}\n")
                                P1LastBlock = True
                            # if P1LastBlock:
                            #     if alphaNumericProcessed:
                            #         fileo.write(f"{P2block}\n")
                            #         P1LastBlock = False
                            # if len(autoTagListTotal) > 0:
                            #     autoTagListTotal.sort()
                            #     fileo.write(f"#c/tsx ")
                            #     for tag in autoTagListTotal:
                            #         fileo.write(f"{tag} ")
                            #     fileo.write(" \n")
                            #     autoTagListTotal = []
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
                            if alphaNumericProcessed == False:
                                if (line[0:1].isalnum()) or (line[0:1] in ['"']):
                                    alphaNumericProcessed = True
                                    if P1Written == False:
                                        P1Written = True
                                        fileo.write(f"{P1block}\n")
                                        P1LastBlock = True
                            for tag in autoTagListEntry:
                                if tag.lower() in line.lower():
                                    tagtemp = "#c/" + tag.lower()
                                    if tagtemp not in autoTagListTotal:
                                        autoTagListTotal.append(tagtemp)
                            fileo.write(line)

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


# Main:
# remember these are list terms need to be separated
curr_time = time.strftime("%H:%M:%S", time.localtime())
dirNameInput = "Z:\SharedA\Python\Projects"
dirNameOutput = "H:\Backup\Obsidian\CodeVault"
programLocation = "Z:/SharedA/Repos/Utilities/formatpython.py"
taglist1 = []  # files
if "jupinput" in taglist1:
    inputFileExtension = ".txt"
else:
    inputFileExtension = ".py"

excludefile = [
    "@",
    "$My",
    "2023-",
    "2022-",
    "2021-",
    "excalidraw",
    "excalibrain",
]
# fmt: off
autoTagListEntry = ["dictionary","dictreader","sql","sqlite","select","insert","fetchone",
                    "argv","except","try",
]
# fmt: on


# autoTagListEntry = [
#     "order",
#     "distinct",
# ]


print("Current Time is :", curr_time)
print("formatpython version 001 Start")
print("------------------------------- ")
print("Program Location  :", programLocation)
print("Input   Directory :", dirNameInput)
print("Output  Direcotry :", dirNameOutput)
print("Taglist1- Files   :", taglist1)
print("Exclude File List :", excludefile)
print("autoTagListEntry  :", autoTagListEntry)


print("------------------:")
print("FILE LIST SEARCHED:")
print("------------------:")
print(taglist1)
print("------------------:")
# fmt: off
# fmt: on

allFilesMain = []
allFilesMain = getListOfFiles(dirNameInput, taglist1, excludefile)

processFileMain(allFilesMain)
print("------------------------------------- ")
print("formatpython version 001 Termination")
