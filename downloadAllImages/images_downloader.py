# app download all Images from a URL with Python
import requests
import bs4
import pathlib


def get_img_links(url='https://en.wikipedia.org/wiki/Tomato'):
    """
    Function to get all image links from given url
    :param url:
    :return: list of image links
    """
    source = requests.get(url)
    bsoup = bs4.BeautifulSoup(source.text, 'html.parser')
    result = list()
    img_links = bsoup.find_all('img')
    for img in img_links:
        if 'en.wikipedia.org' in url and 'upload.wikimedia.org' in img['src']:
            result.append(f'https:{img['src']}')
        elif 'books.toscrape.com' in url:
            result.append(f'https://books.toscrape.com/{img['src']}')
        elif 'en.wikipedia.org' not in url and 'books.toscrape.com' not in url:
            result.append(f'{url}{img['src']}')
    return result


def download_images(img_links):
    """
    Function to download images from given image links.
    Images will be downloaded in a created folder
    :param img_links: list of image links
    :return:
    """
    # create folder
    img_folder = pathlib.Path('downloaded_images')

    try:
        img_folder.mkdir()
    except FileExistsError:
        print('Downloaded_images folder already exists')
    else:
        print('Downloaded_images folder created')

    # download images
    for img in img_links:
        # create name fo file
        file_name = pathlib.Path(img).parts[-1]
        save_path = img_folder / file_name
        # get image source
        data_img = requests.get(img).content

        with open(save_path, 'wb') as f:
            f.write(data_img)
        print(f'Downloaded: {save_path}')
