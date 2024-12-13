from datetime import datetime, timedelta
from update_lend import save_lends
from restore_books_file import read
from save_all_books import save_all_books
from validation import validate_borrower_name, validate_borrower_number, validate_lend_book_name



def lend_book(all_books):
    file_name = 'lend_book.json'
    all_lends = read(file_name)
    if not all_lends:
            all_lends = []
        
    book_name = validate_lend_book_name(all_books)
    
    for book in all_books:      
        if book_name in book.values():
            if book['quantity'] > 0:
                book['quantity'] -= 1               
                borrower_name = validate_borrower_name()
                borrower_number = validate_borrower_number()
                current_date = str(datetime.today() + timedelta(days=10))
                
                lend = {
                    'borrower_name' : borrower_name,
                    'borrower_number' : borrower_number,
                    'book_title' : book_name,                
                    'return_date' : current_date             
                }
                
                
                all_lends.append(lend)
                save_lends(all_lends)
                save_all_books(all_books)                
                print('Data added succesfully')
            else: 
                print("There are not enough books available to lend.")
                break
    