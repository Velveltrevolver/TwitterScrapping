import re
from re import sub
import time
import cookielib
from  cookielib import CookieJar
import urllib
from urllib import urlopen

keyWord = 'kathmandu'
def main():
	try:
	    sourceCode = urllib.urlopen('https://twitter.com/search/realtime?q='+keyWord+'&src=hash').read()
	    splitSource = re.findall(r'<p class="js-tweet-text tweet-text">(.*?)</p>',sourceCode)
			   
	    for item in splitSource:
			print ''
			print ''
			print ''
			print '______________________'
			print re.sub(r'<.*?>','',item)
				
          	
            
	
	except Exception, e:
		print str(e)
		time.sleep(555)
		
main()