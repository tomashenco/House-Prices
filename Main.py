from WebSeeker import web_seeker
from WebSeeker import read_page

locations = ('Cambridge', 'York')

'''
('London', 'Canterbury', 'Newbury', 'Bristol', 'Exeter',
         'Ipswich', 'Cambridge', 'Northampton', 'Birmingham',
         'Boston', 'Sheffield', 'Manchester', 'Liverpool',
         'York', 'Lancaster', 'Middlesbrough', 'Carlisle', 'Newcastle')
'''

# web_seeker(locations)

link = 'http://www.rightmove.co.uk/new-homes-for-sale/property-43327825.html'
read_page(link)