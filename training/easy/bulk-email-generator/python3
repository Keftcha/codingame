import sys

email = "\n".join([input() for _ in range(int(input()))])

print(email, file=sys.stderr)

nb_choice = 0
# while there is choice
while ")" in email:
    # the interval where the propositions or a choice are
    deb_choice, end_choice = email.index("("), email.index(")")
    # get a list of choice 
    choices = email[deb_choice+1:end_choice].split("|")
    # choose the choise
    choice = choices[nb_choice%len(choices)]
    nb_choice += 1
    
    # replace the propositions by the choice
    email = email.replace(email[deb_choice:end_choice+1], choice, 1)
    
print(email)
