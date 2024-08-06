"""
def main():
  with open('books/frankenstein.txt') as f:
    file_contents = f.read()    
    words = file_contents.split()
    print(len(words))
    return

main()
"""

def main():
  book_path = "books/frankenstein.txt"
  book_text = get_book_text(book_path)
  num_words = get_num_words(book_text)
  print(f"{num_words} words found in the book")

def get_num_words(text):
  words = text.split()
  return (len(words))

def get_book_text(path):
  with open(path) as f:
    return f.read()
  
main()

