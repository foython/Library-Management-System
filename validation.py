
def validate_title():
    while True:
        try:
            user_input = input("Enter Book Title: ").strip()  # Remove extra whitespace
            
            if not user_input:
                raise ValueError('The book’s name cannot be empty.')
            return user_input
        
        except ValueError as e:
            print(f"Error: {e}")          


def validate_author():
    while True:
        try:
            user_input = input("Enter Author Name: ").strip()  # Remove extra whitespace
            
            if not user_input.replace(" ", "").isalpha():
                raise ValueError('The auther’s name must be a string and cannot be empty.')
            return user_input
        
        except ValueError as e:
            print(f"Error: {e}") 
            
            
def validate_year():
    while True:
        try:
            user_input = input("Enter Publishing Year : ").strip()
                      
            if not user_input.isnumeric():
                raise ValueError('The Publishing Year must be an integer and cannot be empty.')  
                      
            elif len(user_input) < 4:
                raise ValueError('Publishing Year should have four digit')
                                    
            return int(user_input)        
        
        except ValueError as e:
            print(f"Error: {e}")
     
            

def validate_price():
    while True:
        try:
            user_input = float(input("Enter Book Price: "))
                      
            if not user_input:
                raise ValueError('The book price must be an integer and cannot be empty.')
                                    
            return user_input        
        
        except ValueError as e:
            print(f"Error: {e}")
            
            
def validate_borrower_name():
    while True:
        try:
            user_input = input("Enter borrower's name  ").strip() # Remove extra whitespace
            
            if not user_input.replace(" ", "").isalpha():
                raise ValueError("The borrower's name must be a string and cannot be empty.")
            
            return user_input          
        
        except ValueError as e:
            print(f"Error: {e}")
            
            
def validate_borrower_name_for_return(all_lends):
    while True:
        try:
            user_input = input("Enter borrower's name  ").strip() # Remove extra whitespace
            
            if not user_input.replace(" ", "").isalpha():
                raise ValueError("The borrower's name must be a string and cannot be empty.")
            
            for item in all_lends:
                    if user_input in item.values():
                        return user_input
            else:
                raise ValueError('Nobody lended book by this name')
            
        
        except ValueError as e:
            print(f"Error: {e}") 
            
            
def validate_borrower_number():
    while True:
        try:
            user_input = input("Enter borrower's number ").strip()
                      
            if not user_input.isnumeric():
                raise ValueError("The borrower's number must be an integer and cannot be empty.")  
                      
            elif len(user_input) < 4:
                raise ValueError("Borrower's number should have five digit")
                                    
            return int(user_input)        
        
        except ValueError as e:
            print(f"Error: {e}")
            
            
def validate_lend_book_name(all_books):
    while True:
        try:
            user_input = input('Enter The name of book you want to lend ').strip()  # Remove extra whitespace
            
            if not user_input:
                raise ValueError("The book's name cannot be empty.")
            
            for book in all_books:      
                if user_input in book.values():
                    return user_input
            else:
                raise ValueError('Book not found in library')                  
            
        
        except ValueError as e:
            print(f"Error: {e}") 


def validate_return_book_name(all_books):
    while True:
        try:
            user_input = input('Enter The name of book you want to return ').strip()  # Remove extra whitespace
            
            if not user_input:
                raise ValueError('The book’s name cannot be empty.')
            
            for book in all_books:      
                if user_input in book.values():
                    return user_input
            else:
                raise ValueError('Book not found in library')
                    
        except ValueError as e:
            print(f"Error: {e}") 
            
            
  
