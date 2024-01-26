# %%
print("formatjupyter version 001 Start")
print(" 2024-01-25 Update to process all level headers same")

programLocation = "Z:/SharedA/Repos/utilities/formatjupyter.py"
fileInput = "Z:/SharedA/Repos/data/jupinput.txt"
fileOutput = "Z:/SharedA/Repos/data/jupoutput.txt"

print("formatjupyter version 001 Start")
print("------------------------------- ")
print("Program Location  :", programLocation)
print("Input   File      :", fileInput)
print("Output  File      :", fileOutput)


# level indicates if python {p1} is written
level1 = True
level2 = True
level3 = True
level4 = True
level5 = True
level6 = True

# indcate last written was p1 or p2
statep1 = False
p1 = "```python"
p2 = "```"
index01 = 0

fileo = open(fileOutput, "w")
with open(fileInput) as filei:
    line = filei.readline()
    while line:
        if bool(line.strip()):  # block empty lines
            if "# %%" in line[0:4]:
                index01 += 1
            elif "#++ " in line[0:4]:
                if statep1:
                    fileo.write(f"{p2}\n")
                    statep1 = False
                fileo.write("# 🟪" + line[3:-1] + "\n")
            elif "# " in line[0:2]:
                if statep1:
                    fileo.write(f"{p2}\n")
                    statep1 = False
                fileo.write("## 🟡" + line[2:-1] + "\n")
                if level1:
                    fileo.write(f"[{index01}]\n")
                    fileo.write(f"{p1}\n")
                    statep1 = True
            elif "## " in line[0:3]:
                if statep1:
                    fileo.write(f"{p2}\n")
                    statep1 = False
                fileo.write("### ✔" + line[3:-1] + "\n")
                if level2:
                    fileo.write(f"[{index01}]\n")
                    fileo.write(f"{p1}\n")
                    statep1 = True
            elif "### " in line[0:4]:
                if statep1:
                    fileo.write(f"{p2}\n")
                    statep1 = False
                fileo.write("#### 🔸" + line[4:-1] + "\n")
                if level3:
                    fileo.write(f"[{index01}]\n")
                    fileo.write(f"{p1}\n")
                    statep1 = True
            elif "#### " in line[0:5]:
                if statep1:
                    fileo.write(f"{p2}\n")
                    statep1 = False
                fileo.write("##### 🔹" + line[5:-1] + "\n")
                if level4:
                    fileo.write(f"[{index01}]\n")
                    fileo.write(f"{p1}\n")
                    statep1 = True
            elif "##### " in line[0:6]:
                if statep1:
                    fileo.write(f"{p2}\n")
                    statep1 = False
                fileo.write("###### ✔" + line[6:-1] + "\n")
                if level5:
                    fileo.write(f"[{index01}]\n")
                    fileo.write(f"{p1}\n")
                    statep1 = True
            else:
                fileo.write(line)
        line = filei.readline()
fileo.write(f"[{index01}]\n")
if statep1:
    fileo.write(f"{p2}\n")
    statep1 = False
fileo.close()

print("formatjupyter version 001 End")

# %%
