import urllib2, sys

def downloadPhoto(url):

    photo_url = url.split('/')
    
    if len(photo_url[-1]) == 10:
        if len(photo_url[-2]) == 1:
            if photo_url[-3] == 'instagram.com':
    
                website = urllib2.urlopen(url)
                website = website.read()
    
                website = website.split('<meta property="og:image" content="')
                photo = website[1].split('" />')
    
    
                photo_name = photo[0].split('/')
                photo_file = urllib2.urlopen(photo[0])
        
                with open(photo_name[-1], 'wb') as output:
                    output.write(photo_file.read())

                print "Downloaded 1 Photo: ", photo_name[-1]
            else:
                print "Invalid URL:", url
        else:
            print "Invalid URL:", url
    else:
        print "Invalid URL:", url

downloadPhoto(sys.argv[-1])