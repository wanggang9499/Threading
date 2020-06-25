# encoding:utf-8

import requests
import time

img_urls = ['https://unsplash.com/photos/T6R85k-AUBc',
            'https://unsplash.com/photos/m0BHTN-srjc',
            'https://unsplash.com/photos/T6R85k-AUBc',
            'https://unsplash.com/photos/A_RXuJWAvmk',
            'https://unsplash.com/photos/uoSEDUu8F-I',
            'https://unsplash.com/photos/ydivV0igJOE']

start_time = time.perf_counter()

for img_url in img_urls:
    img_contents = requests.get(img_url).content
    img_name = img_url.split('/')[4]
    img_name = f'{img_name}.jpg'

    with open(img_name, 'wb') as img_file:
        img_file.write(img_contents)
        print(f'{img_name}已经下载成功~...')

end_time = time.perf_counter()
print(f'整个项目花费的时间为{end_time-start_time}秒')