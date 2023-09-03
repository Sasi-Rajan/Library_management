class Library():
    def __init__(self,list):
        self.books_list=list
        self.available_books_list=list[:]
        self.books_lent={}

    def display_available_books(self):
        for book in self.available_books_list:
            print(book)
    def display_all_books(self):
        for book in self.books_list:
            print(book)
    def borrow_book(self,name,bk_name):
        if bk_name not in self.books_list:
            print("Incorrect book name. Please check book list")
            return
        if bk_name in self.available_books_list:
            self.books_lent.update({bk_name:name})
            self.available_books_list.remove(bk_name)
            print("You can now take the book")
        else:
            print("The book is already taken by "+ self.books_lent[bk_name])

    def return_book(self,bk_name):
        del self.books_lent[bk_name]
        self.available_books_list.append(bk_name)



if __name__=="__main__":
    lib = Library(["Thermodyanics","HMT","Automobile","OOP in C"])
    print("Welcome to library. Enter an option")
    while True:
        print("1.Display available books\n2.Display all books\n3.Borrow a book\n4.Return a book\n5.Exit")
        user_choice=int(input("Enter your choice "))
        if user_choice==1:
            lib.display_available_books()
        elif user_choice==2:
            lib.display_all_books()
        elif user_choice==3:
            name=input("Enter user name")
            bk_name=input("Enter book name")
            lib.borrow_book(name,bk_name)
        elif user_choice==4:
            bk_name=input("Enter the book name")
            lib.return_book(bk_name)
        elif user_choice == 5:
            break
        else:
            print("Invalid choice")


