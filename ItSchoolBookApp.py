def add_book():
    book_name = input('Insert a book name -> ')
    book_author = input("Insert book's author -> ")
    import csv  # importing csv lib
    with open('BooksDB.csv', mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=[
            'BookName', 'AuthorName', 'SharedWith', 'IsRed'
        ])
        writer.writerow({'BookName': book_name,
                         'AuthorName': book_author,
                         'SharedWith': 'None',
                         'IsRed': False})
    print('Book was added successfully')


def list_book():
    import csv
    with open('BooksDB.csv', mode='r')as file:
        rows = csv.DictReader(file, fieldnames=('BookName', 'AuthorName', 'SharedWith', 'IsRed'))  # prelucram datele din DB in randuri
        for row in rows:
            print(f"Book name is: {row.get('BookName')},written by {row.get('AuthorName')}, shared with {row.get('SharedWith')}, red {row.get('IsRed')}")


def update_book():
    book_name = input('Enter book name:')
    book_red = input('Have you red the book?(Y/N)')
    if book_red == 'Y':
        book_red = True
    else:
        book_red = False
    import csv
    rows = []
    with open('BooksDB.csv', mode='r') as file:
        rows = list(csv.DictReader(file, fieldnames=['BookName', 'AuthorName', 'SharedWith', 'IsRed']))
        for row in rows:
            if row.get('BookName') == book_name:
                row['IsRed'] = book_red
                break
    with open('BooksDB.csv', mode='w') as file:
        csv_writer = csv.DictWriter(file, fieldnames=[
            'BookName', 'AuthorName', 'SharedWith', 'IsRed'
        ])
        csv_writer.writerow({'BookName': row.get('book_name'),
                         'AuthorName': row.get('book_author'),
                         'SharedWith': row.get('SharedWith'),
                         'IsRed': book_red})
        print('Book was updated successfully')




def share_book():
    title = input("What book are you looking for today? --> ")
    list_of_books = []
    shared_with = "None"
    import csv
    with open("BooksDB.csv", mode="r") as file:
        list_of_books = csv.DictReader(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRead"])
        for book in list_of_books:
            if book.get("BookTitle") != title:
                add = input('''This book is not in our list.
    Would you like to add this book? Y/N --> ''')
                if add == "Y":
                    add_book()
                else:
                    print("Good bye!")
            else:
                shared_with = input(f"Who would you like to share {title} with? --> ")
                with open("BooksDB.csv", mode="w") as file:
                    writer = csv.DictWriter(file, fieldnames=["BookTitle", "BookAuthor", "SharedWith", "IsRed"])
                    writer.writerow({"BookTitle": book.get("BookTitle"), "BookAuthor": book.get("BookAuthor"),
                                     "SharedWith": shared_with, "IsRed": book.get("IsRed")})
                print(f"{title} is now shared with {shared_with}")


#  Main menu for user

print('\tBooks Menu')
print('1 : Add a book')
print('2 : List books')
print('3 : Update books')
print('4 : Share books')
user_option = int(input('Choose an option -> '))

if user_option == 1:
    add_book()
elif user_option == 2:
    list_book()
elif user_option == 3:
    update_book()
elif user_option == 4:
    share_book()
else:
    print('Invalid option.')
