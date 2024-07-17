print ("Hello Enreap")
print ("Hello Akash")
print ("Hello Dipak")



#Request library: Prasad


import requests

url = 'https://www.bvuniversity.edu.in/'

response = requests.get(url)

print(f"Status code: {response.status_code}")

print("Response content:")

print(response.text)

print(f"Status code: {response.status_code}")

print(response.headers)

if response:
    print("Success!")
else:
    raise Exception(f"Non-success status code: {response.status_code}")

#How to get response code by using if & else Request library: Prasad


if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Not Found.")


#How to get image from url by using Request library: Prasad


url = 'https://st5.depositphotos.com/1028436/68765/i/380/depositphotos_687655224-stock-photo-https-icon-mesh-isolated-tech.jpg'

response = requests.get(url)


if response.status_code == 200:
    
    image_data = response.content

    image_path = 'downloaded_image.jpg'

    with open(image_path, 'wb') as f:
        f.write(image_data)

    print(f"Image downloaded successfully and saved as {image_path}")
else:
    print(f"Error: {response.status_code}")



#How to get pdf from url by using Request library: Prasad

import requests

url = 'https://stc.aeplcdn.com/f/brochure/9/1290/x2w8sih.pdf'

response = requests.get(url)

if response.status_code == 200:
   
    with open('document.pdf', 'wb') as f:
        f.write(response.content)
    print("PDF downloaded successfully")
else:
    print(f"Failed to download PDF. Status code: {response.status_code}")
