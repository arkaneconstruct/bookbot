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
  #print(f"{num_words} words found in the book")
  char_count = get_num_chars(book_text)
  chars_dict = create_dict(char_count)

  print(f"--- Begin report of {book_path} ---")
  print(f"{num_words} words found in the document")
  print()
  for letter in chars_dict:
    if not letter["char"].isalpha():
      continue
    print(f"The '{letter['char']}' character was found {letter['num']} times")
  print("--- End report ---")

def get_num_words(text):
  words = text.split()
  return (len(words))

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_num_chars(text):
  chars = {}
  for c in text:
    lowered = c.lower() 
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1
  return chars

def sort_chars(char_count):
  return char_count["num"]

def create_dict(char_count):
    book_chars = []
    for letter in char_count:
      book_chars.append({"char":letter,"num":char_count[letter]})
    book_chars.sort(reverse=True, key=sort_chars)
    return book_chars
        
  


main()

