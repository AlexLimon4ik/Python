import requests
from bs4 import BeautifulSoup

# URL головної сторінки
url = "https://books.toscrape.com/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Отримання всіх посилань на категорії
categories_list = []
for li_element in soup.select('div.side_categories ul.nav-list ul li'):
    a_element = li_element.find('a')
    category_link = "https://books.toscrape.com/" + a_element['href']
    categories_list.append(category_link)

# Функція для отримання назв книжок у категорії
def get_book_names(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    book_names = []
    for book_link in soup.select("article.product_pod h3 a"):
        book_name = book_link.get("title")
        book_names.append(book_name)

    next_page = soup.select_one('li.next a')
    if next_page:
        next_page_url = url.rsplit("/", 1)[0] + "/" + next_page["href"]
        book_names.extend(get_book_names(next_page_url))
    
    return book_names

# Збір книжок з усіх категорій
all_books = []
for category_link in categories_list:
    print(f"Збираю книжки з категорії: {category_link}")
    books = get_book_names(category_link)
    all_books.extend(books)

# Виведення всіх зібраних книжок
print("\nУсі зібрані книжки:")
for book in all_books:
    print(f"- {book}")