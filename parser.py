import requests
import time
import csv

def take_1000_posts():


    token = 'cb634836cb634836cb634836bfcb1664b6ccb63cb63483694a3977e3b752bce531986e1'
    version = '5.126'
    domain = 'cutthecraptv'
    count = 100
    offset = 0
    all_posts = []


    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get', params = {
        'domain':domain,
        'access_token':token,
        'v':version,
        'count':count,
        'offset':offset
        })

        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
        time.sleep(0.5)

    return all_posts



def file_writer(data):
    with open('cutthecraptv.csv','w', encoding = 'utf8') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('likes','body','url'))
        for post in data:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                pass

            a_pen.writerow((post['likes']['count'],post['text'],img_url))


all_posts = take_1000_posts()
file_writer(all_posts) 


