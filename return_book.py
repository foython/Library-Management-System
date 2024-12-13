from update_lend import save_lends
from restore_books_file import read
from save_all_books import save_all_books
from validation import validate_return_book_name, validate_borrower_name_for_return


def return_book(all_books):
    file_name = 'lend_book.json'
    all_lends = read(file_name)
    if not all_lends:
        all_lends = []
        
    if all_books:
        book_name = validate_return_book_name(all_books)
        if book_name:
            for book in all_books:      
                if book_name in book.values():
                    borrower_name = validate_borrower_name_for_return(all_lends)
                    for item in all_lends:
                        if borrower_name in item.values():
                            all_lends.remove(item)
                            book['quantity'] += 1
                            save_lends(all_lends)
                            save_all_books(all_books)
                            print('Book return successfully')
                            break
                    else:
                        print("Borrower's name does not matched")
                        break
              
                            
        else:
            print('No book in library')
        
        