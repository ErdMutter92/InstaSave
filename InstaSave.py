import urllib2, sys

def downloadPhoto(url):
    
    website = urllib2.urlopen(url)
    website = website.read()
    
    website = website.split('<meta property="og:image" content="')
    photo = website[1].split('" />')
    

    photo_name = photo[0].split('/')
    photo_file = urllib2.urlopen(photo[0])

    with open(photo_name[-1], 'wb') as output:
        output.write(photo_file.read())

    print "Downloaded 1 Photo: ", photo_name[-1]

downloadPhoto(sys.argv[-1])