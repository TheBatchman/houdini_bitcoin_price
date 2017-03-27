import requests, time
from datetime import timedelta, date

# YYYY-MM-DD
start_date = date(2013, 12, 25)
end_date = date.today()

date_from = start_date.isoformat()
date_to = end_date.isoformat()

# Today
#date_to = time.strftime("%Y-%m-%d")

dates = []
prices = []

#HTTPS does not work!
url = "http://api.coindesk.com/v1/bpi/historical/close.json?start=%s&end=%s" % (date_from, date_to)
req = requests.get(url, headers={'Accept': 'application/json'})
data = req.json()

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

for single_date in daterange(start_date, end_date):

    date = single_date.strftime("%Y-%m-%d")

    dates.append(date)
    prices.append(data['bpi'][date])

    print "%s: %s" % (date, data['bpi'][date])

print len(dates)

geo = hou.pwd().geometry()
#price_attr = geo.addAttrib(hou.attribType.Point, "price", 0)
spacing = 2

for number, date in enumerate(dates):
    point = geo.createPoint()    
    bottom = ( prices[number] - min(prices) )
    point.setPosition((0, bottom, -number * spacing))
    #point.setAttribValue(price_attr, prices[number])
