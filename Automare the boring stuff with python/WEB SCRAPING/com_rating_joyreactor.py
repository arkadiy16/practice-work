import requests, bs4
import logging

logging.basicConfig(level=logging.WARNING, format=' %(asctime)s - %(levelname)s -  %(message)s')


def main(name):
    print('Searching...')
    data = []
    url = f'https://joyreactor.cc/user/{name}/comments'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    pages = int(soup.select_one('.pagination_expanded').select('a')[-1].get_text())
    logging.warning(pages)
    # Loop for every page.
    for page_num in range(2, 120):
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
            try:
                f.write(f'post:#{dat[0][6:]}, comment#{dat[1][7:]}, "{dat[2]}", rating:{dat[3]}\n')
            except TypeError:
                f.write('TextIOWrapper.write() takes no keyword arguments')


name = input()
main(name)
