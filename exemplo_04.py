import requests 

URL = "https://api.nasa.gov/planetary/apod?api_key=API_NASA"

response = requests.get(URL)

image_path = response.json()['url']

image_data = requests.get(image_path).content

if response.status_code == 200:
    with open("imagem_download.jpg", 'wb') as file:
        file.write(image_data)
else:
    print(f"Erro ao baixar a imagem. Código de status HTTP: {response.status_code}")
