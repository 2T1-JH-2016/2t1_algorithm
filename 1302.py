num = int(input())
book_list = dict()

for _ in range(0,num) : 
    book_name = input()
    if book_name not in book_list:
        book_list[book_name] = 1
    else : 
        book_list[book_name] += 1
book_list = dict(sorted(book_list.items()))
print(max(book_list,key=book_list.get))