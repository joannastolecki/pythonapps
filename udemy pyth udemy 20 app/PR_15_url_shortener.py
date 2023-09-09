import pyshorteners


url = input('Enter url:\n')
print("url after shortening: \n",pyshorteners.Shortener().tinyurl.short(url))