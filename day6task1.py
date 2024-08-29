class Book:
  total_book = 0
  def __init__(self, title, author):
    self.title = title
    self.author = author
    Book.total_book += 1

  def get_info(self):
    return (f'title: {self.title}, author: {self.author}')

book1 = Book('Mein Kampf', 'Adolf Hitler')
book2 = Book('The Communist Manifesto', 'Karl Marx')
book3 = Book('Grand Grimoire', 'Antonio del Rabina')

print(book1.get_info())
print(book2.get_info())
print(book3.get_info())


print(Book.total_book)
    
  