# %%
import os
import time
from datetime import datetime


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
    global cntFileRead
    global cntFileBlocked
    global cntFileBlocked1
    global cntFileBlocked2
    global cntFileBlocked3
    global cntFileBlocked4
    global cntFileProcessed

    global clipTempList2
    global tempListT1
    global tempListJoin

    # documentation
    # if sql comment strip comment so processed like python
    # -- # modified to #
    #
    BlockTypeTid5 = "# ~~ "  # headers

    BlockTypeP3d5 = "# ++ "  # level 1
    BlockTypeP2d5 = "# +++"  # level 2
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

        # Specify the file path
        file_path = programName
        # Get the creation and modification datetime of the file
        stat_info = os.stat(file_path)
        creation_time = datetime.fromtimestamp(stat_info.st_ctime)
        modification_time = datetime.fromtimestamp(stat_info.st_mtime)
        if modification_time.month < 10:
            mod_month = "0" + str(modification_time.month)
        else:
            mod_month = str(modification_time.month)
        if modification_time.day < 10:
            mod_day = "0" + str(modification_time.day)
        else:
            mod_day = str(modification_time.day)
        if modification_time.hour < 10:
            mod_hour = "0" + str(modification_time.hour)
        else:
            mod_hour = str(modification_time.hour)
        if modification_time.minute < 10:
            mod_minute = "0" + str(modification_time.minute)
        else:
            mod_minute = str(modification_time.minute)
        if modification_time.second < 10:
            mod_second = "0" + str(modification_time.second)
        else:
            mod_second = str(modification_time.second)
        mod_date = (
            str(modification_time.year)
            + mod_month
            + mod_day
            + mod_hour
            + mod_minute
            + mod_second
        )

        cntFileRead += 1
        if updateMode == True:
            if checkModificationDate == True:
                if mod_date >= mod_date_last_checked:
                    print("allowed")
                    print("programName           = ", programName)
                    print("mod_date_last_checked = ", mod_date_last_checked)
                    print("mod_date program      = ", mod_date)
                else:
                    cntFileBlocked += 1
                    cntFileBlocked1 += 1
                    print("***********************")
                    print("***     BLOCKED 1   ***")
                    print("***********************")
                    continue
        else:
            cntFileBlocked += 1
            cntFileBlocked2 += 1
            print("***********************")
            print("***     BLOCKED 2   ***")
            print("***********************")
            continue

        blockCount = 0
        lineCount = 0
        tagHeaderFlag = False
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
                if line[0:4] == "-- #":
                    if line[3:8] in [
                        "# ~~ ",
                        "# ++ ",
                        "# +++",
                        "# == ",
                        "# %% ",
                        "# -- ",
                        "# ---",
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
                                "# ++ ",
                                "# +++",
                                "# == ",
                                "# %% ",
                                "# -- ",
                                "# ---",
                            ]:
                                line = line[3:].rstrip() + "\n"
                        if "# && " == line[0:5]:
                            if "Jupyter" in line:
                                # if "C:\\" in line or "H:\\" in line or "Z:\\" in line: debug
                                processMod = "Jupyter"
                                mainFileExtension = ".ipynb"
                                extname = ".ipynb"
            cntFileProcessed += 1
            if processMod == "Jupyter":
                # dirNameInputSplit = line[5:-1].split("\\") debug
                dirNameInputSplit = programName.split("\\")
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
                        "# ++ ",
                        "# +++",
                        "# == ",
                        "# %% ",
                        "# -- ",
                        "# ---",
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
            s1 = "\\"
            dirNameOutputFinal = s1.join(dirNameOutputbase)
            os.makedirs(dirNameOutputFinal, exist_ok=True)

            tempListT2 = dirNameOutputFinal.split("\\")

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
            clipTempList3 = "".join(clipTempList1)

            if extname == ".mdown":
                fileOutput = (
                    dirNameOutputFinal
                    + "/"
                    + clipTempList3
                    + "."
                    + fullfilename
                    + "."
                    + "mdown"
                    + ".md"
                )
                fullfilenametotal = clipTempList3 + "." + fullfilename
            else:
                fileOutput = (
                    dirNameOutputFinal
                    + "/"
                    + tempListT2[-1]
                    + "."
                    + fullfilename
                    + ".md"
                )
                fullfilenametotal = tempListT2[-1] + "." + fullfilename

            fileo = open(fileOutput, "w")
            fileo = open(fileOutput, "a")

            # replaced in vspath this originally
            clipOutputForwardList = clipOutputForward.split("/")

            tempListT1 = clipTempList2.split("/")
            tempListJoin = "".join(tempListT1)
            clipOutputFileTemp = clipOutputFile.replace(" ", "%20")
            fullfilenameTemp = fullfilename.replace(" ", "%20")
            clipOutputBackwardTemp = clipOutputBackward.replace(":", "")
            clipOutputBackwardTemp = clipOutputBackwardTemp.replace("\\", "/")

            fileo.write(f"---\n")
            fileo.write(f"filename: {fullfilename}\n")
            fileo.write(f"dirfolder:          {clipTempList2}\n")
            fileo.write(f"dirname:        {clipOutputBackwardTemp}\n")
            fileo.write(f"processMod:         {processMod}\n")
            fileo.write(
                f"dateMod:         {mod_date[:8]}.{mod_date[8:12]}.{mod_date[12:-1]}\n"
            )
            fileo.write(f"obsidianUIMode: preview\n")
            if processMod != "Jupyter":
                fileo.write(f"dirpath:          {clipOutputFileTemp}\n")
                fileo.write(
                    f"dirfilename:    {clipOutputFileTemp}/{fullfilenameTemp}{extname}\n"
                )
            if processMod == "Jupyter":
                clipInputList = programName.rstrip().split("\\")
                clipOutputForward = "/".join(clipInputList)
                clipOutputDouble = "\\\\".join(clipInputList)
                clipOutputFile = clipOutputForward.rstrip().split(":")
                driveLetter = "".join(clipOutputFile[0])
                clipOutputFile = (
                    "file:///" + driveLetter.lower() + "%3A" + clipOutputFile[1]
                )
                fileo.write(f"vsjupyterpy:     {clipOutputFile}\n")
                fileo.write(f"dirpath:          {clipOutputFileTemp}\n")
                clipOutputFileTemp = clipOutputFile.rstrip().split(".")
                clipOutputFileTemp[1] = ".ipynb"
                clipOutputFileTemp = "".join(clipOutputFileTemp)
                fileo.write(f"dirfilename:  {clipOutputFileTemp}\n")
            # insert frontmatter marking
            fileo.write(f"---\n")
            fileo.write(f"# 🔵Ptags:\n")
            canvasList = clipTempList2.split("/")
            canvasString = canvasList[-1]
            fileo.write(
                f"**vsext::** {extname} | **inputext::** {inputFileExtension} \
| **CodeVaultCode:** [[CodeVaultCode]] | **MyTags:** [[$MyTags]]\n"
            )
            tempListT1Temp = tempListT1[0].replace(" ", "")
            tempListJoinTemp = tempListJoin.replace(" ", "")
            fileo.write(
                f"**Odir:** [[{tempListJoinTemp}.dir]] \
| **Opage:** [[{fullfilenametotal}.page]] | **Ocanvas:** [[{canvasString}.canvas]]\n"
            )
            autoTagListTotal = []
            if extname in [".xlsx"]:
                print("***********************")
                print("***     BLOCKED 4   ***")
                print("***********************")
                tagHeaderFlag = True
                createTagHeader(fileo, fullfilename, extname, fullfilenametotal)
                cntFileBlocked4 += 1
                continue

            while line:
                if bool(line.strip()):  # block empty lines
                    linelist = line.split()

                    # write vstag as top line
                    if blockHeaderTid5 != line[0:5]:
                        if lineCount == 0:
                            tagHeaderFlag = True
                            createTagHeader(
                                fileo, fullfilename, extname, fullfilenametotal
                            )

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
                                fileo.write(f"vspriority:: {vspriority}\n")
                                fileo.write(f"vscomment::  *{line[7:].rstrip()}* \n")
                            else:
                                vspriority = ""
                                fileo.write(f"vspriority:: {vspriority}\n")
                                fileo.write(f"vscomment::  *{line[5:].rstrip()}* \n")
                            tagHeaderFlag = True
                            createTagHeader(
                                fileo, fullfilename, extname, fullfilenametotal
                            )
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
                    elif blockHeaderN3d5 in line:
                        if P1BlockModeOn:
                            fileo.write(f"{P2block}\n")
                            P1BlockModeOn = False
                        cPos = line.index(blockHeaderN3d5)
                        fileo.write("#### ✔" + line[cPos + 5 :].rstrip() + "\n")
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
                        # print error message for these
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
                                    tagtemp = "#b/" + tag.lower()
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
                else:
                    fileo.write(line.rstrip() + "\n")
                line = filei.readline()
                # if sql comment strip comment so processed like python mainline
                if line[0:4] == "-- #":
                    if line[3:8] in [
                        "# ~~ ",
                        "# ++ ",
                        "# +++",
                        "# == ",
                        "# %% ",
                        "# -- ",
                        "# ---",
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
        if tagHeaderFlag == False:
            tagHeaderFlag = True
            createTagHeader(fileo, fullfilename, extname, fullfilenametotal)

        fileo.close()


def createTagHeader(fileo, fullfilename, extname, fullfilenametotal):
    if extname == ".ipynb":
        typetag = "Jupyter"
    else:
        typetag = runMod
    tempListT1Temp = tempListT1[0].replace(" ", "")
    tempListJoinTemp = tempListJoin.replace(" ", "")
    clipTempList2temp = clipTempList2.replace("/", "")
    fileo.write(f"vsfolder::         *{clipTempList2}*\n")
    fileo.write(
        f"**OTypenotes:** [[a${typetag}]] **VSmdown:** [[{clipTempList2temp}.a$.mdown]]\n"
    )
    fileo.write(f"fbasetags::         #f/base/{tempListT1Temp}\n")
    fileo.write(f"fdirtags::          #f/dir/{tempListJoinTemp}\n")
    fileo.write(f"ftypetags::         #f/type/{typetag}\n")
    fileo.write(f"\n")
    fileo.write(f"## 🔵[[$MyTags#🔵TODO Open]]\n")
    fileo.write(f"```dataview\n")
    fileo.write(f"TASK\n")
    fileo.write(f"where file.name = this.file.name\n")
    fileo.write(f"WHERE !completed\n")
    fileo.write(f"```\n")
    # fileo.write(f"```dataviewjs\n")
    # fileo.write(
    #     f'const file = app.workspace.getActiveFile(); const tags = app.metadataCache.getFileCache(file)?.tags?.map(a => \n'
    # )
    # fileo.write(
    #     f'a.tag); if (tags) {{ const tagSet = new Set(tags); const tagArray = []; for (let tag of tagSet) {{ \n'
    # )
    # fileo.write(
    #     f'tagArray.push([tag, tags?.filter((b) => (b === tag))?.length]); }} dv.table(["Tag", "# of occurences"], \n'
    # )
    # fileo.write(
    #     f'tagArray); }} else {{ dv.span("No tags"); }} \n'
    # )

    # f'Where !contains(file.name,"@") and contains(file.tags,"c/") and contains(file.name, this.file.name)\n'
    fileo.write(f"```dataview\n")
    fileo.write(
        f'TABLE WITHOUT ID (tag + "(" + length(rows.file.link) + ")") AS VStags\n'
    )
    fileo.write(f'FROM -"Templates" and -"excalibrain" and -"_ZArchivedNotes"\n')
    fileo.write(
        f'Where !contains(file.name,"@") and contains(file.name, this.file.name)\n'
    )
    fileo.write(f"FLATTEN file.etags AS tag GROUP BY tag SORT VStags DESC\n")

    fullfilenametotallist = fullfilenametotal.split(".")
    fileo.write(f"```\n")
    fileo.write(f"# 🔵 {fullfilenametotallist[-1]}\n")
    fileo.write(f"___\n")


def mainline():
    global inputFileExtension
    global mainFileExtension
    if runMod == "Python":
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
    print("RunMod          :", runMod)
    print("================================== ")
    print("Input   Directory :", dirNameInput)
    print("Output  Directory :", dirNameOutput)
    print("Include File List :", includefile)
    print("Exclude File List :", excludefile)
    print("Include File Path :", includepath)
    print("Exclude File Path :", excludepath)
    print("autoTagListEntry  :", autoTagListEntry)
    print("runMod            :", runMod)
    print("inputFileExtension:", inputFileExtension)
    print("mainFileExtension :", mainFileExtension)

    print("==================:")
    print("FILE LIST SEARCHED:")
    print("==================:")
    print(includefile)
    print("==================:")

    allFilesMain = []
    allFilesMain = getListOfFiles(dirNameInput)

    processFileMain(allFilesMain)
    print(" ")
    print("formatpython version 002 Termination")


#
# Main:
#
now = datetime.now()
if now.month < 10:
    now_month = "0" + str(now.month)
else:
    now_month = str(now.month)
if now.day < 10:
    now_day = "0" + str(now.day)
else:
    now_day = str(now.day)
if now.hour < 10:
    now_hour = "0" + str(now.hour)
else:
    now_hour = str(now.hour)
if now.minute < 10:
    now_minute = "0" + str(now.minute)
else:
    now_minute = str(now.minute)
if now.second < 10:
    now_second = "0" + str(now.second)
else:
    now_second = str(now.second)

cntFileRead = 0
cntFileProcessed = 0
cntFileBlocked = 0
cntFileBlocked1 = 0
cntFileBlocked2 = 0
cntFileBlocked3 = 0
cntFileBlocked4 = 0

# initialization program
updateMode = True
checkModificationDate = False

# topPath = "2data"
# dirNameInputMain = "C:\\2data\\Python\\Projects"
# dirNameInputRoot = "C:\\2data"
# dirNameOutputMain = "H:\\Backup\\Obsidian\\CodeVault"

# topPath1 = "2data"
# dirNameInputMain1 = "C:\\2data"
# dirNameInputRoot1 = "C:\\2data"

topPath = "SharedA"
dirNameInputMain = "Z:\SharedA\Python\Projects"
dirNameInputRoot = "Z:\SharedA"
dirNameOutputMain = "H:\\Backup\\Obsidian\\CodeVault"

topPath1 = "SharedA"
dirNameInputMain1 = "Z:\SharedA"
dirNameInputRoot1 = "Z:\SharedA"

# -----------------------------

dirNameInput = dirNameInputMain
dirNameOutput = dirNameOutputMain

# main program
fileDateTime = dirNameOutput + "\\" + "Templates\\$modDateTime.md"
with open(fileDateTime, "r") as reader:
    mod_date_last_checked = reader.readline()

now_date = str(now.year) + now_month + now_day + now_hour + now_minute + now_second

file1 = open(fileDateTime, "w")
file1.write(now_date)
file1.close()

# main variables

includefilemain = []

includepathmain = [
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
]

excludefilemain = [
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
    "Repos",
]

excludepathmain = ["archive", "backup", "test"]

autoTagListEntrymain = [
    "argv",
    "csv",
    "dataframe",
    "derekbanas",
    "dictionary",
    "dictreader",
    "lambda",
    "numpy",
    "sql",
    "sqlite",
    "utf-8-sig",
    "xlwings",
]

curr_time = time.strftime("%H:%M:%S", time.localtime())
allFilesMain = []

# fmt: off

# ************************************************************
#   Main Execution
# ************************************************************

runMod = "Python"
dirNameInput = dirNameInputMain
dirNameOutput = dirNameOutputMain
autoTagListEntry = autoTagListEntrymain[:]
includefile = includefilemain[:]
includepath = includefilemain[:]
excludefile = excludefilemain[:]
excludepath = excludefilemain[:]
dirmodeSearch = "Projects"
dirmodePrint = "Projects"
mainline()

runMod = "md"
dirNameInput = dirNameInputMain
dirNameOutput = dirNameOutputMain
autoTagListEntry = autoTagListEntrymain[:]
includefile = includefilemain[:]
includepath = includefilemain[:]
excludefile = excludefilemain[:]
excludepath = excludefilemain[:]
dirmodeSearch = "Projects"
dirmodePrint = "Projects"
mainline()

runMod = "markdown"
dirNameInput = dirNameInputRoot1
dirNameOutput = dirNameOutputMain
autoTagListEntry = autoTagListEntrymain[:]
includefile = []
includepath = [topPath1]
excludefile = []
excludepath = ["Images", "InfoSelect", "Obsidian",
               "Typora",
               "Zotero","Repos"]
dirmodeSearch = topPath1
dirmodePrint = topPath1
mainline()

runMod = "mdown"
dirNameInput = dirNameInputMain
dirNameOutput = dirNameOutputMain
autoTagListEntry = autoTagListEntrymain[:]
includefile = includefilemain[:]
includepath = includefilemain[:]
excludefile = excludefilemain[:]
excludepath = excludefilemain[:]
dirmodeSearch = "Projects"
dirmodePrint = "Projects"
mainline()

runMod = "SQL"
dirNameInput = dirNameInputMain
dirNameOutput = dirNameOutputMain
autoTagListEntry = autoTagListEntrymain[:]
includefile = includefilemain[:]
includepath = includefilemain[:]
excludefile = excludefilemain[:]
excludepath = excludefilemain[:]
dirmodeSearch = "Projects"
dirmodePrint = "Projects"
mainline()

runMod = "txt"
dirNameInput = dirNameInputMain
dirNameOutput = dirNameOutputMain
autoTagListEntry = []
includefile = includefilemain[:]
includepath = includefilemain[:]
excludefile = excludefilemain[:]
excludepath = excludefilemain[:]
dirmodeSearch = "Projects"
dirmodePrint = "Projects"
mainline()

runMod = "ahk"
dirNameInput = dirNameInputMain
dirNameOutput = dirNameOutputMain
autoTagListEntry = []
includefile = includefilemain[:]
includepath = ["Python\\Projects"]
excludefile = excludefilemain[:]
excludepath = excludefilemain[:]
dirmodeSearch = "Projects"
dirmodePrint = "Projects"
mainline()

runMod = "data"
dirNameInput = dirNameInputMain
dirNameOutput = dirNameOutputMain
autoTagListEntry = []
includefile = includefilemain[:]
includepath = includefilemain[:]
excludefile = excludefilemain[:]
excludepath = excludefilemain[:]
dirmodeSearch = "Projects"
dirmodePrint = "Projects"
mainline()

runMod = "csv"
dirNameInput = dirNameInputMain
dirNameOutput = dirNameOutputMain
autoTagListEntry = []
includefile = includefilemain[:]
includepath = includefilemain[:]
excludefile = excludefilemain[:]
excludepath = excludefilemain[:]
dirmodeSearch = "Projects"
dirmodePrint = "Projects"
mainline()

runMod = "html"
dirNameInput = dirNameInputMain
dirNameOutput = dirNameOutputMain
autoTagListEntry = []
includefile = includefilemain[:]
includepath = includefilemain[:]
excludefile = excludefilemain[:]
excludepath = excludefilemain[:]
dirmodeSearch = "Projects"
dirmodePrint = "Projects"
mainline()

runMod = "htm"
dirNameInput = dirNameInputMain
dirNameOutput = dirNameOutputMain
autoTagListEntry = []
includefile = includefilemain[:]
includepath = includefilemain[:]
excludefile = excludefilemain[:]
excludepath = excludefilemain[:]
dirmodeSearch = "Projects"
dirmodePrint = "Projects"
mainline()

runMod = "xlsx"
dirNameInput = dirNameInputMain1
dirNameOutput = dirNameOutputMain
autoTagListEntry = [topPath1]
includefile = []
includepath = [topPath1]
excludefile = ["copy","backup"]
excludepath = ["archive", "backup", "test","Images", "InfoSelect", 
               "Obsidian","Typora","Zotero","ARFB",
               "z_python-for-excel",
               "Repos"]
dirmodeSearch = topPath1
dirmodePrint = topPath1
mainline()

# fmt: on

print("mod_date_last_checked       = ", mod_date_last_checked)
print("now_date                    = ", now_date)
print("updateMode                  = ", updateMode)
print("checkModificationDate       = ", checkModificationDate)
print("cntFileBlocked              = ", cntFileBlocked)
print("cntFileBlocked1 mod_date    = ", cntFileBlocked1)
print("cntFileBlocked2 updateMode  = ", cntFileBlocked2)
print("cntFileBlocked3 run/process = ", cntFileBlocked3)
print("cntFileBlocked4 xlsx        = ", cntFileBlocked4)
print("cntFileRead                 = ", cntFileRead)
print("cntFileProcessed            = ", cntFileProcessed)
