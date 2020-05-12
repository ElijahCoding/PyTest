import os
import requests
from download_util import download_file

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOADS_DIR = os.path.join(BASE_DIR, 'downloads')
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

downloaded_img_path = os.path.join(DOWNLOADS_DIR, 'test.jpg')
url = "https://q-cf.bstatic.com/images/hotel/max1024x768/211/211636126.jpg"

# a smallish item
r = requests.get(url, stream=True)
r.raise_for_status() # 200
with open(downloaded_img_path, 'wb') as f:
    f.write(r.content)

download_file(url, DOWNLOADS_DIR)