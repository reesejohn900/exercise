class Library:

    def __init__(self,books,name):
        self.list_of_books=books
        self.library_name=name
        self.dict={}

    def display(self):
        for books in self.list_of_books:
            print(books)


    def add(self,book):
        self.list_of_books.append(book)
        print('book added')


    def return_book(self,book):
        self.dict.pop(book)
        print('book returned')


    def lend(self):
        d={}
        a=input('enter the book')
        b=self.list_of_books
        if a  in b:
            c=input('enter the name of the person')
            d[a]=c
            b.remove(a)

        elif a  in d:
            print('book is lended by :')
            print(d[a])

        else:
            print('book is not in the library')

        e=int(input('1:printing dictonary\n'))
        if e == 1:
            print(d)

        else:
            print('wrong choice')




if __name__ == '__main__':
    while True:
        q=int(input('press\n'
                    '1:display\n'
                    '2:add\n'
                    '3:return_book\n'
                    '4:lend\n'))

        all=Library(['In Search of Lost Time by Marcel Proust.','Lolita','War and Peace','Moby Dick','The Great Gatsby','Don Quixote'],'All Library')

        if q == 1:
            all.display()

        elif q == 2:
            book = input("enter the book to be added")
            all.add(book)

        elif q== 3:
            book = input("enter the book to be returned")
            all.return_book(book)

        elif q == 4:
            all.lend()

        else:
            print('wrong choice')
