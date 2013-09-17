import re
from re import sub
import time
import cookielib
from  cookielib import CookieJar
import urllib
from urllib import urlopen
import difflib
keyWord = 'syria'
def main():

	oldTwit = []
	newTwit = []
	while 1< 2:
		try:
			sourceCode = urllib.urlopen('https://twitter.com/search/realtime?q='+keyWord+'&src=hash').read()
			splitSource = re.findall(r'<p class="js-tweet-text tweet-text">(.*?)</p>',sourceCode)
			for item in splitSource:
				print ''
				print ''
				print ''
				print '______________________'
				aTweet = re.sub(r'<.*?>','',item)
				print aTweet
				newTwit.append(aTweet)
			comparison = difflib.SequenceMatcher(None,newTwit,oldTwit)
			howSim = comparison.ratio()
			print '##############'
			print howSim
			
			oldTwit = [None]
			for eachItem in newTwit:
				oldTwit.append(eachItem)
			newTwit =[None]
			
			time.sleep(50)
			
          	
            
	
		except Exception, e:
			print str(e)
			time.sleep(555)
		
main()