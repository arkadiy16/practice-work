# This project used to collect all comments of a person from joyreactor.cc
# and sort them by rating, then this data will be write in new .txt file
# named <person_nicname_on_site>_comments_rating.txt in format: 
# post_num, comment_num, comment, comment_rating.

import requests, bs4
import logging

logging.basicConfig(level=logging.WARNING, format=' %(asctime)s - %(levelname)s -  %(message)s')


def main(name, pgs=None):
    """ Function for collecting data from site, sort them, and write in .txt file.
    
    Function will take string(name) and create new .txt file with data    
    """
    print('Searching...')
    data = []
    url = f'https://joyreactor.cc/user/{name}/comments'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    if not pgs:
        pgs = int(soup.select_one('.pagination_expanded').select('a')[-1].get_text())
    logging.warning(pgs)
    # Loop for every page.
    for page_num in range(2, pgs + 1):
        try:
            linkElems = soup.select('.txt')
            # Loop for every comment in page.
            for i in range(len(linkElems)):
                rat_url = linkElems[i].select_one('.comment_link').get('href').split('#')
                comment = linkElems[i].select_one('div').get_text()
                logging.info(rat_url)
                rat_req = requests.get('https://joyreactor.cc' + rat_url[0])
                rat_soup = bs4.BeautifulSoup(rat_req.text, 'html.parser')
                com = rat_soup.select_one(f'#{rat_url[1]}')
                logging.info(com)
                # Checking for comment exist.
                try:
                    com_rat = com.select_one('.comment_rating').get_text()
                except AttributeError:
                    com_rat = 0
                # Write comment info in list.
                data.append([rat_url[0], rat_url[1], comment, float(com_rat)])
            logging.warning(page_num)
            # Change page.
            url = 'https://joyreactor.cc/user/%D0%A7%D1%83%D0%B4%D0%BE%D0%9F%D1%91%D1%81/comments' + f'/{page_num}'
            res = requests.get(url)
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
        except:
            continue

    data.sort(key=lambda c: c[3], reverse=True)
    # Write comment info in file.
    with open(f'{name}_comments_rating.txt', 'w') as f:
        for dat in data:
            f.write(f'post:#{dat[0][6:]}, comment#{dat[1][7:]}, "{dat[2]}", rating:{dat[3]}\n')



name = input()
main(name)