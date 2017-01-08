'''
Created on Jan 7, 2017

@author: rounsifr
'''

from lxml import html
import requests

def nextarrival(busstop):
    
    trio = 'Trio'
    copper = 'Copper'
    pierce = 'Pierce'
  
## TRIO STOP
    if busstop == trio:
        # get the page that is needed to scrape info
        page = requests.get('http://connect.ridetherapid.org/InfoPoint/Stops/Stop/9094')

        # must use page.content since html.fromstring expects bytes as an input
        tree = html.fromstring(page.content)
        time = tree.xpath('//div[@class="destination-cell"]/text()')
        return time

## COPPER        
    if busstop == copper:
        # get the page
        page = requests.get('http://connect.ridetherapid.org/InfoPoint/Stops/Stop/9105')
        
        # convert into tree for scraping
        tree = html.fromstring(page.content)
        time = tree.xpath('//div[@class="destination-cell"]/text()')
        return time

## PIERCE            
    if busstop == pierce:
        # get the page
        page = requests.get('http://connect.ridetherapid.org/InfoPoint/Stops/Stop/9105')
        
        # convert into tree for scraping
        tree = html.fromstring(page.content)
        time = tree.xpath('//div[@class="destination-cell"]/text()')
        return time
        
###### SCRAPE INFORMATION FROM WEBSITE ##########
# get the page that is needed to scrape info
#page = requests.get('http://connect.ridetherapid.org/InfoPoint/Stops/Stop/9108')
# must use page.content since html.fromstring expects bytes as an input
#tree = html.fromstring(page.content)
#nextstop = tree.xpath('//div[@class="destination-cell"]/text()')

####### TESTING PURPOSES ########
#nextarrival('Trio')
#nextarrival('Copper')
#nextarrival('Pierce')