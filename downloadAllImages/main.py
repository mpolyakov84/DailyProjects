from images_downloader import get_img_links, download_images

links = get_img_links('https://books.toscrape.com/')
download_images(links)
