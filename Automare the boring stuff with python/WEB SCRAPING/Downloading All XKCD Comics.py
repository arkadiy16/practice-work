# What's program does:
# 1) Loads the XKCD home page.
# 2) Saves the comic image on that page.
# 3) Follows the Previous Comic link.
# 4) Repears until it reaches the first comic.
# Program will do the following:
# 1) Download pages with the requests module.
# 2) Find the URL of the comic image for a page using BeautifulSoup.
# 3) Download and save the comic image to the hard drive with iter_content().
# 4) Find the URL of the Previous Comic link, and repeat.

import requests, os, bs4

url = 'https://xkcd.com/10'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    # Download the page.
    page = requests.get(url)
    page.raise_for_status()
    page_bs = bs4.BeautifulSoup(page.text, 'html.parser')
    # Find the URL of the comic image.
    comic_elem = page_bs.select('#comic img')
    if not comic_elem:
        print('Could not find comic image')
    else:
        comic_url = 'https:' + comic_elem[0].get('src')
        # Download the image.
        print(f'downloading comic {comic_url}')
        res = requests.get(comic_url)
        res.raise_for_status()
        # Save the image to ./xkcd.
        with open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb') as comic_file:
            for chunk in res.iter_content(100000):
                comic_file.write(chunk)
    # Get the Prev button's url.
    prev_link = page_bs.select('a[rel="prev"]')[0].get('href')
    url = 'https://xkcd.com' + prev_link

print('Done.')
