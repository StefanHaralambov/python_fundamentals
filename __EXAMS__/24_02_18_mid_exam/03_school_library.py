books = input().split("&")

command = input().split(" | ")

while command[0] != "Done":
    if command[0] == "Add Book":
        new_book = command[1]
        if new_book not in books:
            books.insert(0, new_book)
    if command[0] == "Take Book":
        remove_book = command[1]
        if remove_book in books:
            index_remove_book = books.index(remove_book)
            books.pop(index_remove_book)
    if command[0] == "Swap Books":
        book_1, book_2 = command[1], command[2]
        if book_1 in books and book_2 in books:
            index_book_1 = books.index(book_1)
            index_book_2 = books.index(book_2)
            books[index_book_2], books[index_book_1] = books[index_book_1], books[index_book_2]
    if command[0] == "Insert Book":
        insert_book = command[1]
        if insert_book not in books:
            books.append(insert_book)
    if command[0] == "Check Book":
        check_index = int(command[1])
        if check_index in range(len(books)):
            check_book = books[check_index]
            print(f"{check_book}")

    command = input().split(" | ")

print(*books, sep=", ")
