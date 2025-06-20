import requests
import shutil
import json
class llamadasininternet():
    def primer_request():
        url = 'https://jcw87.github.io/c2-sans-fight/'
        r = requests.get('https://jcw87.github.io/c2-sans-fight/')
        print(r)
        print(r.content)
        print(r.status_code)

    def imagen(self,url,file_name):
        
        res = requests.get(url,stream=True)
        if 200==res.status_code:
            with open(file_name,'wb')as f:
                shutil.copyfileobj(res.raw,f)
            print('imagen descargada correctamente')
        else:
             print('no se encontro la imagen')


    def clima(self,api_key,city):


       
        base_url = 'https//api.openweathermap.org/daba/2.5/weather?'
        params = {'q':city,'appid':api_key,'units':'metric'}
        
        try:
            r = requests.get(base_url, params=params)
            r.raise_for_status()
            weather_data = r.json()
        
            if 200==weather_data['cod']:
                print(f'el clima en{weather_data['name']}:')
                print(f'descripcion{weather_data['weather'][0]['description']}')
                print(f'temperatura{weather_data['main']['temp']}°c')
                print(f'humedad{weather_data['main']['Humidity']}%')
                print(f'viento{weather_data['wind']['speed']}m/s')
            else:
                print(f'Error{weather_data['message']}')
        
        except:
        
            print ('Error')

req = llamadasininternet()
req.imagen(url, 'yes i am.png')
api_key = '69ec8ca2037d63a120d31c59efd0f604'
city='Zapopan'
url = 'https://jojo.fandom.com/wiki/Muhammad_Avdol?file=YESIAM%21.png'