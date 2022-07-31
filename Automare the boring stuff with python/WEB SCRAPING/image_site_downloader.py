# Program for downloading photos from photo-sharing sites.


import bs4, requests, os
import logging

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s -  %(message)s')

def main(category, site='https://imgur.com', amount=10):
    os.makedirs(os.path.basename(site)[:-4], exist_ok=True)
    os.makedirs(f'{os.path.basename(site)[:-4]}/' + category, exist_ok=True)
    search = requests.get(site + '/search/score/all?q_type=jpg&q_all=' + category)
    search.raise_for_status()
    bs_search = bs4.BeautifulSoup(search.text, 'html.parser')
    search_list = bs_search.select('.post')
    if not search_list:
        print(f'Found 0 results for {category}')
        return None
    else:
        for image_post in search_list[:10]:
            img_url = site + image_post.select('.image-list-link')[0].get('href')
            logging.info(img_url)
            post = requests.get(img_url)
            bs_post = bs4.BeautifulSoup(post.text, 'html.parser')
            images = bs_post.select('.imageContainer zoomable')
            logging.warning(bs_post.prettify())
            for img_num, img in enumerate(images):
                logging.warning(img)

main('space')
