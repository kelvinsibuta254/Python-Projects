from book_class import Book

def main():
    #creating an instance
    my_book = Book("1984", "George Orwell", 1949)

    #Demonstrating the __str__ method
    print(my_book)# expected to use __str__

    #Demonstrating the __repr__ method
    print(repr(my_book)) #Expected to use __repr__

    #Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()
