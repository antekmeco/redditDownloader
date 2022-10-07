import json
import requests
import random
import os
import sys
import colorama
from pathlib import Path
from glob import glob
from urllib.parse import urlparse
max_number = 10000
try:
    subreddit = sys.argv[1]
    download_folder = subreddit
except IndexError:
    print(colorama.Fore.RED + "Specify subreddit!")
    print(colorama.Fore.YELLOW + "Usage: python3 redditDownloader.py [subreddit]"+ colorama.Style.RESET_ALL)
    raise SystemExit
     
if not os.path.isdir(download_folder):
    os.mkdir(download_folder)
while True:
    smiesznymeme = json.loads(json.dumps(requests.get(f"https://www.reddit.com/r/{subreddit}/random.json", headers={
                              'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}).json()))
    url = smiesznymeme[0]['data']['children'][0]['data']['url']
   # print(url)
    parsed = urlparse(url)
    # print(parsed)
    filename = parsed.path
    if 'i.redd.it' in url and not os.path.isfile(download_folder + filename):
        print(download_folder + filename)
        dst_filepath = Path(download_folder + filename)
        parent = dst_filepath.parent
        parent.mkdir(parents=True, exist_ok=True)
       # print(parent)
        r = requests.get(url, allow_redirects=True)
        open(dst_filepath, 'wb').write(r.content)
        print(len(glob(f"{download_folder}/*")))
