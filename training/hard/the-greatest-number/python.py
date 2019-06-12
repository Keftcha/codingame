n = int(raw_input())
nb = raw_input().split()
digits = [d for d in nb if d.isdigit()]

# make the number
if all([d == "0" for d in digits]):    # only 0
    digits = ["0"]
elif "-" in nb:    # negative number
    digits.sort()
    if "." in nb:
        digits.insert(1, ".")
    digits.insert(0, "-")
else:    # psitive number
    digits.sort(reverse=True)
    if "." in nb:
        # remove useless 0
        if digits[-1] == "0":
            del digits[-1]
        else:
            digits.insert(-1, ".")

print "".join(digits)
