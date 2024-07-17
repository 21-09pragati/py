import requests
r= requests.get('https://www.espncricinfo.com/')
print(r)
print(r.content)



response= requests.get ('https://www.espncricinfo.com/')

print(response.status_code)

#Authentication using Python Requests

print(response.headers)