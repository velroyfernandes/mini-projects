import pyshorteners
link = input("enter your link")
shortener=pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print( x)