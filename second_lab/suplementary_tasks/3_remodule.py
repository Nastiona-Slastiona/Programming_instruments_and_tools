import re 

#stroka = input()
stroka = 'drag23on@gmail.com'
result = re.findall(r'[\w\._]+@\w+\.\w{2,6}$', stroka) #e-mail validation
print(result)

chislo = 3421.0
result = re.findall(r'\d+\.(?:\d+)?$', str(chislo))# float validation
print(result)

URL = 'https://docs.python.org/3.8/library/re.html'
result = re.findall(r'^(?:https?:\/\/)?(?:[\w\.]+)\.(?:[a-z]{2,6}\.?)(?:\/[\w\.]*)*\/?$', URL) #URL validation
print(result)
