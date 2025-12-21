import numpy
import pandas
import webbrowser
import requests

num_list = [1,2,3,4,5]
np_array = numpy.array(num_list)
print(len(np_array))
print(np_array)

url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

#for url in url_lists:
   #webbrowser.open_new_tab(url)
   
# important commands
# pip show pandas
# pip show --verbose pandas
# pip show packagename
# pip freeze
# pip install requests

# Reading data from a URL
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
print("getting the response from url: ", url)
response = requests.get(url)
print(response)

