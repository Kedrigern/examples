from bs4 import BeautifulSoup, ResultSet
import pandas as pd
import requests

def prepare_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def extract_categories(soup: BeautifulSoup) -> list[tuple[str,str,str]]:
    """Example for cattegory
    <aside class="sidebar col-sm-4 col-md-3">
        <div class="side_categories">
            <ul class="nav nav-list">
                <li>
                    <a href="catalogue/category/books_1/index.html">
                    Books
                    </a>
            <ul>                     
    """

    links: list[tuple[str,str,str]] = []
    # for link in soup.select('div.side_categories a:not(:first-child)'):
    for link in soup.find('div', class_='side_categories').find_all('a')[1:]:
        href = link['href']
        text = link.text.strip()
        category_id = href.split('/')[3]
        links.append((category_id, text, href))

    return links

def extract_books_on_title(soup: BeautifulSoup) -> list:
    """
     <section>
        <div class="alert alert-warning" role="alert"><strong>Warning!</strong> This is a demo website for web scraping purposes. Prices and ratings here were randomly assigned and have no real meaning.</div>
            <div>
                <ol class="row">
                    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
                        <article class="product_pod">
        
                        <div class="image_container">                    
                            <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>        
                        </div>
                        <p class="star-rating Three">
                            <i class="icon-star"></i>
                            <i class="icon-star"></i>
                            <i class="icon-star"></i>
                            <i class="icon-star"></i>
                            <i class="icon-star"></i>
                        </p>
                        <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
                        <div class="product_price">
                            <p class="price_color">£51.77</p>
                            <p class="instock availability">
                                <i class="icon-ok"></i>In stock
                            </p>        
                            <form>
                                <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
                            </form>
                        </div>
                        </article>
    </li>"""
    books: list = []
    for book_html in soup.select('article.product_pod'):
        book_data = {}

        image_container = book_html.find('div', class_='image_container')
        if image_container:
            image_link = image_container.find('a')
        if image_link:
            book_data['image_url'] = image_link['href']

        title_link = book_html.find('h3').find('a')
        if title_link:
            book_data['title'] = title_link.text.strip()

        price_element = book_html.find('p', class_='price_color')
        if price_element:
            book_data['price'] = price_element.text.strip()

        if book_data:
            books.append(book_data)

    return books


def main():
    soup = prepare_soup('http://books.toscrape.com/')
    cats = extract_categories(soup)
    # print(cats)
    books = extract_books_on_title(soup)
    print(books)

if __name__ == '__main__':
    main()