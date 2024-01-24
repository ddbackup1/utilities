# %%
print("formatjupyter version 001a Start")
fileo = open("Z:/SharedA/Repos/data/jupoutput.txt", "w")
firstwrite = True
p1 = "```python"
p2 = "```"
index01 = 0

with open("Z:/SharedA/Repos/data/jupinput.txt") as filei:
    line = filei.readline()
    while line:
        if bool(line.strip()):  # block empty lines
            if "# %%" in line:
                b = 0
            elif "# " in line[0:2]:
                print("#  heading error line dropped")
                print("line:> ", line.strip())
                print("-----")
            elif "## " in line[0:3]:
                print("## heading error line dropped")
                print("line:> ", line.strip())
                print("-----")
            elif "### " in line[0:4]:
                index01 += 1
                if firstwrite:
                    firstwrite = False
                    fileo.write("### ✔" + line[4:-1] + "\n")
                    fileo.write(f"[{index01}]\n")
                    fileo.write(f"{p1}\n")
                else:
                    fileo.write(f"{p2}\n")
                    fileo.write("### ✔" + line[4:-1] + "\n")
                    fileo.write(f"[{index01}]\n")
                    fileo.write(f"{p1}\n")
            else:
                fileo.write(line)
        line = filei.readline()
fileo.write(f"[{index01}]\n")
fileo.write(f"{p2}\n")
fileo.close()
print("formatjupyter version 001a End")

# %%
