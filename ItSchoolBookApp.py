def add_book():
    print('Add a book option')


def list_book():
    print('List a book option')


def update_book():
    print('Update a book option')


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
