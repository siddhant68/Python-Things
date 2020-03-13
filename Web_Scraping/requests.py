import requests

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.0535&lon=-118.2453#.Xk-9tcszbeQ')

#print(dir(page))
#print(help(page))

print(page.text)

# downloading an image

page = requests.get('https://www.101computing.net/wp/wp-content/uploads/python-logo-1.png')

print(page.status_code)

# status codes
# 200s are success 
# 300s are redirects
# 400s are client errors like permission denied
# 500s are server errors like site crashes

# It gives false for 400s and 500s otherwise true
print(page.ok)
with open('/home/sidhandsome/Coder_X/Python_Things/Requests/python.png', 'wb') as f:
    f.write(page.content)
# In-depth response information
print(page.headers)

payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)

print(r.text)

payload = {'username': 'sidhandsome', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)

print(r.url)
print(r.json())

r_dict = r.json()
print(r_dict['form'])










