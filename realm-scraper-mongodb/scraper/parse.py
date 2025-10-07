from bs4 import BeautifulSoup

"""
    Take the web page data (soup) and parse all the items from the page
"""

def parse_page(soupData):
    items: list[dict] = []
    soup = BeautifulSoup(soupData, "html.parser")
    tbodies = soup.find_all('tbody')
    print(soup.title.text) 

    for tbody in tbodies:

        # Only select tr tags that have children (skips empty ones)
        trs = [tag for tag in tbody.find_all('tr') if tag.find_all(True, recursive=False)]
        # print(trs)
        for tr in trs:
            # Reinitialize item each time
            item : dict = {
                "name": "",
                "imgSrc": "",
                "tier": "",        
            }

            tds = tr.find_all('td', limit=2)
            count: int = 0
            for td in tds:
                match count:
                    case 0:
                        img_tag  = td.find('img')
                        if img_tag:
                            item['imgSrc'] = img_tag.get('src')
                            item['name'] = img_tag.get('title')
                            count += 1
                    case _:
                        item['tier'] = td.get_text()
            print(item)
            if item['imgSrc'] and item['name'] and item['tier']:
                items.append(item)
        # print(tbody.text)
    return items
            

            
