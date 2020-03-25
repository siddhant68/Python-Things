from bs4 import BeautifulSoup as bs
import pandas as pd

with open('sample.xml', 'r') as f:
    content = f.readlines()
    content = ''.join(content)
    bs_content = bs(content, 'lxml')

#print(bs_content.text)
    
catalog = bs_content.find('book') # Gives First Book
catalog = bs_content.find('book', {'id': 'bk102'})
print(bs_content.find('book', {'id': 'bk102'}).title.get_text())

books = bs_content.find_all('book')

id_, author, title, genre, price, publish_date, description = [], [], [], [], [], [], []
for book in books:
    id_.append(book['id'])
    author.append(book.author.get_text())
    title.append(book.title.get_text())
    genre.append(book.genre.get_text())
    price.append(book.price.get_text())
    publish_date.append(book.publish_date.get_text())
    description.append(book.description.get_text())

books = pd.DataFrame({
            'id': id_,
            'author': author,
            'title': title,
            'genre': genre,
            'price': price,
            'publish_date': publish_date,
            'description': description
        })

books.to_csv('books.csv')
    
    