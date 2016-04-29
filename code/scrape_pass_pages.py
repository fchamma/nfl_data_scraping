__author__ = 'alexemorris'
import urllib2

for year in range(1998,2014):
    for week in range(1,18):
        for quarter in range(1,6):
            pass_url = 'http://www.pro-football-reference.com/play-index/play_finder.cgi?request=1&match=summary_all&search=&player_id=&year_min='+str(year)+'&year_max='+str(year)+'&team_id=&opp_id=&game_type=R&playoff_round=&game_num_min=0&game_num_max=99&week_num_min='+str(week)+'&week_num_max='+str(week)+'&quarter='+str(quarter)+'&tr_gtlt=lt&minutes=15&seconds=00&down=0&down=1&down=2&down=3&down=4&yds_to_go_min=&yds_to_go_max=&yg_gtlt=gt&yards=&is_first_down=-1&field_pos_min_field=team&field_pos_min=&field_pos_max_field=team&field_pos_max=&end_field_pos_min_field=team&end_field_pos_min=&end_field_pos_max_field=team&end_field_pos_max=&type=PASS&is_complete=-1&is_turnover=-1&turnover_type=interception&turnover_type=fumble&is_scoring=-1&score_type=touchdown&score_type=field_goal&score_type=safety&is_sack=0&include_kneels=-1&no_play=0&game_day_of_week=&game_location=&game_result=&margin_min=&margin_max=&order_by=yards&rush_direction=LE&rush_direction=LT&rush_direction=LG&rush_direction=M&rush_direction=RG&rush_direction=RT&rush_direction=RE&pass_location=SL&pass_location=SM&pass_location=SR&pass_location=DL&pass_location=DM&pass_location=DR'
            print pass_url
            request = urllib2.Request(pass_url)
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
            text_file = open("passes_y"+str(year)+"_q"+str(quarter)+"_w"+str(week)+".html", "w")
            text_file.write(page.read())
            text_file.close()





