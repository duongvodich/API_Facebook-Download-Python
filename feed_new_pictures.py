from lib2to3.refactor import get_all_fix_names
from requests import session

s=session()
access_token='Token_Facebook_Fulll'
id_group = "gentle.fanpage"
get_api='?fields=feed.limit(100){full_picture}'
json_data= s.get('https://graph.facebook.com/' + id_group + get_api + '&access_token=' + access_token)

# print(json_data.json()['feed']['data'][0]['full_picture'])

number=0
for x in json_data.json ()['feed']['data']:
    number+=1
    if 'full_picture' in x:
        img_url=x['full_picture']
        img_data=s.get(img_url).content
        with open('C:\\Users\Administrator\\Documents\\Python_auto\\Img_gentle\\image_name'+str(number)+'.jpg', 'wb') as handler:
            handler.write(img_data)

