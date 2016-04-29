__author__ = 'alexemorris'
import glob
from bs4 import BeautifulSoup
import lxml
import csv
files = glob.glob("field_goal_data/*.html")
import re
def scrapePassData(files):

    i = 0

    for scrape_number, html_file in enumerate(files):
        print str(scrape_number/float(len(files)) * 100) + '%'
        page = open(html_file, 'r').read()

        football_data = BeautifulSoup(page, 'lxml')

        try:
            rows = football_data.find(id="div_").find_all('tr')
        except AttributeError, e:
            print e

        f = open("fieldgoals.csv", "a")
        writer = csv.writer(f)


        for row in rows:
            items = row.find_all('td')
            if len(items) == 14:
                i += 1
                id = i

                if items[0].string:
                    date = items[0].string
                else:
                    date = 'NULL'

                if items[1].string:
                    off_team = items[1].string
                else:
                    off_team = 'NULL'

                if items[2].string:
                    def_team = items[2].string
                else:
                    def_team = 'NULL'

                if items[3].string:
                    quarter = items[3].string
                else:
                    quarter = 'NULL'

                if items[4].string:
                    time = '00:' + items[4].string
                else:
                    time = 'NULL'

                if items[5].string:
                    down = items[5].string
                else:
                    down = 'NULL'

                if items[6].string:
                    togo = items[6].string
                else:
                    togo = 'NULL'

                if items[7].string:
                    location_side = re.search(r'([\w]+)',items[7].string).group(0)
                else:
                    location_side = 'NULL'

                if items[7].string:
                    yard_line = re.search(r'([\d]+)',items[7].string).group(0)
                else:
                    yard_line = 'NULL'

                if re.search(r'([\d]+)\-',items[8].string) and re.search(r'\-([\d]+)',items[8].string):
                    home_score = re.search(r'([\d]+)\-',items[8].string).group(1)
                    away_score = re.search(r'\-([\d]+)',items[8].string).group(1)
                else:
                    home_score, away_score = 'NULL', 'NULL'

                if len(items[9].find_all('a')) > 0:
                    kicker = items[9].find_all('a')[0].string
                else:
                    kicker = 'NULL'

                if re.search(r'no good',str(items[9])):
                    outcome = 0
                else:
                    outcome = 1

                if re.search(r'[\d]+', items[9].get_text()):
                    yds = re.search(r'([\d]+)', items[9].get_text()).group(1)
                else:
                    yds = 'NULL'

                if items[11].string:
                    epb = items[11].string
                else:
                    epb = 'NULL'

                if items[12].string:
                    epa = items[12].string
                else:
                    epa = 'NULL'

                writer.writerow([id, date, off_team, def_team, quarter, time, down, togo, location_side, yard_line, home_score, away_score, kicker, outcome, yds, epb, epa])
        f.close()

scrapePassData(files)