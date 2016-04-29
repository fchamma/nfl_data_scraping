__author__ = 'alexemorris'
import sys
import urllib2
from bs4 import BeautifulSoup
import re
import csv
import lxml

for year in range(1998,2015):
    for week in range(1,18):
        for quarter in range(1,6):
            goal_url = 'http://www.pro-football-reference.com/play-index/play_finder.cgi?request=1&match=summary_all&search=&player_id=&year_min='+str(year)+'&year_max='+str(year)+'&team_id=&opp_id=&game_type=R&playoff_round=&game_num_min=0&game_num_max=99&week_num_min='+str(week)+'&week_num_max='+str(week)+'&quarter='+str(quarter)+'&tr_gtlt=lt&minutes=15&seconds=00&down=0&down=1&down=2&down=3&down=4&yds_to_go_min=&yds_to_go_max=&yg_gtlt=gt&yards=&is_first_down=-1&field_pos_min_field=team&field_pos_min=&field_pos_max_field=team&field_pos_max=&end_field_pos_min_field=team&end_field_pos_min=&end_field_pos_max_field=team&end_field_pos_max=&type=FG&is_complete=-1&is_turnover=-1&turnover_type=interception&turnover_type=fumble&is_scoring=-1&score_type=touchdown&score_type=field_goal&score_type=safety&is_sack=-1&include_kneels=-1&no_play=0&game_day_of_week=&game_location=&game_result=&margin_min=&margin_max=&order_by=yards&rush_direction=LE&rush_direction=LT&rush_direction=LG&rush_direction=M&rush_direction=RG&rush_direction=RT&rush_direction=RE&pass_location=SL&pass_location=SM&pass_location=SR&pass_location=DL&pass_location=DM&pass_location=DR'
            request = urllib2.Request(goal_url)
            try:
                page = urllib2.urlopen(request)
            except urllib2.URLError, e:
                if hasattr(e, 'reason'):
                    print 'Failed to reach url'
                    print 'Reason: ', e.reason
                    break
                elif hasattr(e, 'code'):
                    if e.code == 404:  # page not found
                        print 'Error: ', e.code
                        break
            print year, week, quarter
            text_file = open("goal_y"+str(year)+"_q"+str(quarter)+"_w"+str(week)+".html", "w")
            text_file.write(page.read())
            text_file.close()



def scrapePassData(urls):

    id, date, off_team, def_team, quarter, time, down, togo, location, home_score, away_score, passer, receiver, complete, yds, epb, epa = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
    i = 0
    for scrape_number, url in enumerate(urls):
        print str(scrape_number/float(len(urls)) * 100) + '%'

        request = urllib2.Request(url)

        try:
            page = urllib2.urlopen(request)
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'Failed to reach url'
                print 'Reason: ', e.reason
                sys.exit()
            elif hasattr(e, 'code'):
                if e.code == 404:  # page not found
                    print 'Error: ', e.code
                    sys.exit()

        football_data = BeautifulSoup(page.read(), 'lxml')
        rows = football_data.find(id="div_").find_all('tr')


        f = open("passes.csv", "a")
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
                    passer = items[9].find_all('a')[0].string
                else:
                    passer = 'NULL'

                if len(items[9].find_all('a')) > 1:
                    receiver = items[9].find_all('a')[1].string
                else:
                    receiver = 'NULL'

                if re.search(r'incomplete',str(items[9])):
                    complete = 0
                else:
                    complete = 1

                if items[10].string:
                    yds = items[10].string
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

                writer.writerow([id, date, off_team, def_team, quarter, time, down, togo, location_side, yard_line, home_score, away_score, passer, receiver, complete, yds, epb, epa])
        f.close()

#scrapePassData(urls)
