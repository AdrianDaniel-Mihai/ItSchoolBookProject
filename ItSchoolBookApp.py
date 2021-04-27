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
    with open('BooksDB.csv', mode='a') as file:
        rows = list(csv.DictReader(file))
        for row in rows:
            if row.get('BookName') == book_name:
                row['IsRed'] = book_red
                csv_writer = csv.DictWriter(file, fieldnames=[
            'BookName', 'AuthorName', 'SharedWith', 'IsRed'
        ])
                csv_writer.writerow(row)
                break
        print('Book was updated successfully')




def share_book():
    print('Share a book option')


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
