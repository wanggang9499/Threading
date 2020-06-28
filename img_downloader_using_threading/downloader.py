# encoding:utf-8

import requests
import time
import concurrent.futures

img_urls = ['https://images.unsplash.com/photo-1592999373293-c27500b8c293',
            'https://images.unsplash.com/photo-1593006082891-00053bcb17b3',
            'https://images.unsplash.com/photo-1592973675735-94df613e6b9f',
            'https://images.unsplash.com/photo-1582746019667-1cea6a77fc93',
            'https://images.unsplash.com/photo-1530912162784-514d437f58f7']

start_time = time.perf_counter()


def img_downloader(img_url):
    img_contents = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'

    with open(img_name, 'wb') as img_file:
        img_file.write(img_contents)
        print(f'{img_name}已经下载成功~...')


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(img_downloader, img_urls)
end_time = time.perf_counter()
print(f'整个项目花费的时间为{end_time - start_time}秒')
