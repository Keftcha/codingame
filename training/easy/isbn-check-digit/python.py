def parse_isbn(isbn):
    return [10 if elem == "X" else int(elem) for elem in isbn]
    

def valid_eh_isbn_10(isbn):
    tot = sum([isbn[idx] * multiplicator for idx, multiplicator in enumerate(range(10, 1, -1))])
    reminder = tot % 11
    last = (11 - reminder) if reminder != 0 else 0
    return last == isbn[-1]
        

def valid_eh_isbn_13(isbn):
    tot = sum([isbn[idx] * multiplicator for idx, multiplicator in enumerate([1, 3] * 6)])
    reminder = tot % 10
    last = (10 - reminder) if reminder != 0 else 0
    return last == isbn[-1]


isbns = [raw_input() for _ in range(int(input()))]

invalid_isbn = []
for isbn in isbns:
    if len(isbn) == 10:
        valid_eh = valid_eh_isbn_10
    elif len(isbn) == 13:
        valid_eh = valid_eh_isbn_13
    else:
        valid_eh = lambda arguments: False
    
    if not valid_eh(parse_isbn(isbn)):
        invalid_isbn.append(isbn)
    del isbn

print len(invalid_isbn), "invalid:"
for isbn in invalid_isbn:
    print isbn
