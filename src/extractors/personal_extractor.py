import bs4

def html_findall(page):
    soup = bs4.BeautifulSoup(
                        page,
                        "html.parser"
                        )
    return soup.findAll

class PersonalDataExtractor:
    def __init__(self, html: str):
        self.__data = html

    def get_value(self, title, key):
        try:
            # Get all cards
            cards = html_findall(self.__data)('div', {'class': 'card'})

            # Get section with given title
            section = [*filter(
                lambda i: i.find('div', {'class': 'card-header'}).text == title,
                cards
            )][0]

            # Container containing rows
            container = section.find('div', {'class': 'container'})

            # Get rows inside this section
            for row in container.findAll('div', {'class': 'row'}):
                # Convert cells to iterator
                cells = iter(row.findAll('div'))
                for cell in cells:
                    # If cell has the key then 
                    # next cell is the value
                    if cell.text == key:
                        text = next(cells).text
                        return text if text else None

        except AttributeError:
            return None
