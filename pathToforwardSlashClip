# %%
import pyperclip
import time

# read clipboard
clipInput = pyperclip.paste()

# split escape character required on back slash
clipInputList = clipInput.rstrip().split("\\")

# join list back into string
clipOutputForward = "/".join(clipInputList)
clipOutputDouble = "\\\\".join(clipInputList)
clipOutputFile = clipOutputForward.rstrip().split(":")
driveLetter = "".join(clipOutputFile[0])
clipOutputFile = "file:///" + driveLetter.lower() + "%3A" + clipOutputFile[1]

print("Path Conversion Results")
print("------------------------------------------------")
print(f"clip..> {clipInput}")
print(f"path..> {clipOutputForward}")
print(f"file..> {clipOutputFile}")
print(f"double> {clipOutputDouble}")
print("------------------------------------------------")

# write clipboard
pyperclip.copy(clipOutputDouble)
time.sleep(1)
pyperclip.copy(clipOutputFile)
time.sleep(1)
pyperclip.copy(clipOutputForward)


# %%

# Z:/SharedA/Python/Projects/CS50P_/Python_/Data_/students.csv

# Z:\SharedA\Python\Projects\CS50P_\Python_\Data_\names.txt

# Z:/SharedA/Python/Projects/CS50P_/Python_/Data_/names.txt
