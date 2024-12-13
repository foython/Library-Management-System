# import json

# def restore_all_books(all_books):
#     with open("all_books.json", "r") as fp:
#         all_books = json.load(fp)
#     return all_books

import json

def read(file_name):
    try:
        with open(file_name, 'r+') as fp:          
            if fp:
                data = json.load(fp)
                if data:
                   return data                        
                   
    except FileNotFoundError:
        print('file dosnt exist')
       
        
    except json.JSONDecodeError:
        print('No data in file')