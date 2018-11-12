ponctuation = [",", "."]

intext = raw_input().lower()
# is the last character is a dot ?
point = True if intext[-1] == "." else False

# remove excessive space
intext = " ".join(intext.split())
for p in ponctuation:
    # remove space before ponctuation
    intext = intext.replace(" " + p, p)
    # remove space after ponctiation
    intext = intext.replace(p + " ", p)
    # put space after ponctuation
    intext = intext.replace(p, p + " ")

# put lettres before dot in upper case
intext = list(intext)
for idx, elem in enumerate(intext):
    if idx == 0 or (idx > 0 and intext[idx-2] == "."):
        intext[idx] = elem.upper()
intext = "".join(intext)

# remove multiple ponctiation
for p in ponctuation:
    intext = intext.split(p+ " ")
    intext = [elem for elem in intext if elem != ""]
    intext = (p+" ").join(intext)

# strip to remove the last white space and we add the last point if there was here
print("".join(intext).strip() + ("." if point else ""))
