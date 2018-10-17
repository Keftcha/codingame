import datetime
from dateutil.relativedelta import relativedelta

begin = datetime.datetime.strptime(input(), "%d.%m.%Y")
end = datetime.datetime.strptime(input(), "%d.%m.%Y")

years = relativedelta(end, begin).years
months = relativedelta(end, begin).months % 12
days = str(end - begin)
days = days.split(", ")[0]

chaine = ""

if years:
    chaine += str(years) + " year" + ("s" if years != 1 else "") + ", "
if months:
    chaine += str(months) + " month" + ("s" if months != 1 else "") + ", "

if days == "0:00:00":
    days = "0 days"

print(chaine + "total " + days)
