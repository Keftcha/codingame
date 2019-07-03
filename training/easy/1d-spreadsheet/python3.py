import operator

def operate(idx, sheet):
    if sheet[idx][0] == "VALUE":
        return sheet[idx][1]
    elif sheet[idx][0] == "ADD":
        function = operator.add
    elif sheet[idx][0] == "SUB":
        function = operator.sub
    elif sheet[idx][0] == "MULT":
        function = operator.mul
    
    return function(int(sheet[idx][1]), int(sheet[idx][2]))


def resolve(idx, sheet, results):
    # the first args is a reference
    if "$" in sheet[idx][1]:
        sheet[idx][1] = resolve(int(sheet[idx][1][1:]), sheet, results)
    # the second args is a reference
    if "$" in sheet[idx][2]:
        sheet[idx][2] = resolve(int(sheet[idx][2][1:]), sheet, results)
    
    results[idx] = str(operate(idx, sheet))
    
    return results[idx]
        

n = int(input())
spreadsheet = [input().split() for i in range(n)]
results = ["¤"] * n

while "¤" in results:
    resolve(results.index("¤"), spreadsheet, results)
    
[print(elem) for elem in results]
