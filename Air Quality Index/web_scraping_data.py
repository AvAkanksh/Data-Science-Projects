import os
import time
import sys
import requests


def retrieve_html(starting_year=2013,ending_year=2020):
    for year in range(starting_year,ending_year+1):
        for month in range(1,13):
            if(month<10):
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month,year)
            else:
                url = 'https://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month,year)
            print(url)
            
            html_text = requests.get(url).text
            
            if not os.path.exists('Data/Html_data/{}'.format(year)):
                os.makedirs('Data/Html_data/{}'.format(year))
            with open('Data/Html_data/{}/{}.html'.format(year,month),'w') as output:
                output.write(html_text)
            
            sys.stdout.flush()

            
if __name__ == '__main__':
    retrieve_html(2013,2018)
    