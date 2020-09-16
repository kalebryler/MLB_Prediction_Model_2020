########## ########## ########## ########## ########## ########## ########## ########## ########## ##########

###################
##### IMPORTS #####
###################

########## ########## ########## ########## ##########

### PDF ###
from fpdf import FPDF

### IMPORT / EXPORT ###
import os

########## ########## ########## ########## ##########

###################
##### PDF #####
###################

########## ########## ########## ########## ##########


def Title_Page(date):

    #### PAGE ORIENTATION ###

    pdf = FPDF(format = 'letter', unit = 'in')
    pdf.add_page()
    pdf.set_auto_page_break(auto = False, margin = 1)
    pdf.add_font('Proximan_Nova', '', '/Library/Fonts/Proxima Nova Regular.ttf', uni = True)
    pdf.add_font('Proximan_Nova_Bold', '', '/Library/Fonts/Proxima Nova Bold.ttf', uni = True)
    pdf.add_font('Proximan_Nova_Extra_Bold', '', '/Library/Fonts/Proxima Nova Extrabold.ttf', uni = True)

    page_width = pdf.w - (pdf.l_margin + pdf.r_margin)
    page_height = pdf.h - (pdf.t_margin + pdf.b_margin)

    #### TITLE PAGE ###

    pdf.set_font('Proximan_Nova_Extra_Bold', '', 50)
    pdf.set_xy(x = pdf.l_margin, y = pdf.t_margin + page_height / 2  - page_height / 8)

    pdf.cell(w = page_width, h = page_height / 8, txt = 'MLB Model', border = 0, ln = 1, align = 'C')

    pdf.set_font('Proximan_Nova', '', 40)
    date_model = date.split('-')[1] + '/' + date.split('-')[-1] + '/' + date.split('-')[0]

    pdf.cell(w = page_width, h = page_height / 8, txt = str(date_model), border = 0, ln = 2, align = 'C')

    return pdf


def Matchup_Page(game, model_dictionary, zone_model_dictionary, comparison_model_dictionary, momentum_model_dictionary, pdf):

    #### PAGE ORIENTATION ###

    pdf.add_page()
    pdf.set_auto_page_break(auto = False, margin = 1)
    pdf.add_font('Proximan_Nova', '', '/Library/Fonts/Proxima Nova Regular.ttf', uni = True)
    pdf.add_font('Proximan_Nova_Bold', '', '/Library/Fonts/Proxima Nova Bold.ttf', uni = True)
    pdf.add_font('Proximan_Nova_Extra_Bold', '', '/Library/Fonts/Proxima Nova Extrabold.ttf', uni = True)

    path = os.path.dirname(os.path.dirname(__file__))
    root_path = path.split('MLB Model')[0]

    page_width = pdf.w - (pdf.l_margin + pdf.r_margin)
    page_height = pdf.h - (pdf.t_margin + pdf.b_margin)

    team_matchup_height = page_height / 15
    team_matchup_width = page_width

    time_height = page_height / 100
    time_width = page_width

    pitcher_matchup_height = page_height / 15
    pitcher_matchup_width = page_width

    boxscore_height = page_height * 2 / 25
    boxscore_width = page_width

    lineup_height = page_height * 7 / 25
    lineup_width = page_width / 2 - pdf.l_margin / 2

    boxscore_away_set_x = pdf.l_margin
    boxscore_home_set_x = lineup_width + 2 * pdf.l_margin

    model_height = page_height / 30
    model_width = page_width / 3 - pdf.l_margin / 3

    output_height = page_height / 15
    output_width = page_width

    boxscore_title_height = boxscore_height / 4
    boxscore_row_height = boxscore_height / 2
    boxscore_team_width = boxscore_width / 5 - boxscore_row_height
    boxscore_team_icon_width = boxscore_row_height
    boxscore_first_5_width = boxscore_width / 5
    boxscore_last_4_width = boxscore_width / 5
    boxscore_runs_width = boxscore_width / 5
    boxscore_hits_width = boxscore_width / 5

    lineup_team_name_height = page_height / 30
    lineup_team_name_width = lineup_width

    lineup_title_height = lineup_height / 10
    lineup_row_height = lineup_height / 10
    lineup_batter_width = lineup_width * 7 / 20
    lineup_stats_width = lineup_width * 13 / 80

    starting_pitcher_title_height = lineup_height / 10
    starting_pitcher_height = lineup_height / 10
    starting_pitcher_width = lineup_width * 7 / 20
    starting_pitcher_stats_width = lineup_width * 13 / 80

    bullpen_title_height = lineup_height / 10
    bullpen_row_height = lineup_height / 10
    bullpen_pitcher_width = lineup_width * 7 / 20
    bullpen_stats_width = lineup_width * 13 / 80

    model_winner_width = model_width * 2 / 5
    model_confidence_width = model_width * 3 / 5

    winner_width = output_width / 2
    confidence_width = output_width / 2

    team_names = {
                    'ARI': 'Arizona Diamondbacks'   ,
                    'ATL': 'Atlanta Braves'         ,
                    'BAL': 'Baltimore Orioles'      ,
                    'BOS': 'Boston Red Sox'         ,
                    'CHC': 'Chicago Cubs'           ,
                    'CIN': 'Cincinnati Reds'        ,
                    'CLE': 'Cleveland Indians'      ,
                    'COL': 'Colorado Rockies'       ,
                    'CWS': 'Chicago White Sox'      ,
                    'DET': 'Detroit Tigers'         ,
                    'HOU': 'Houston Astros'         ,
                    'KC': 'Kansas City Royals'      ,
                    'LAA': 'Los Angeles Angels'     ,
                    'LAD': 'Los Angeles Dodgers'    ,
                    'MIA': 'Miami Marlins'          ,
                    'MIL': 'Milwaukee Brewers'      ,
                    'MIN': 'Minnesota Twins'        ,
                    'NYM': 'New York Mets'          ,
                    'NYY': 'New York Yankees'       ,
                    'OAK': 'Oakland Athletics'      ,
                    'PHI': 'Philadelphia Phillies'  ,
                    'PIT': 'Pittsburgh Pirates'     ,
                    'SD': 'San Diego Padres'        ,
                    'SEA': 'Seattle Mariners'       ,
                    'SF': 'San Francisco Giants'    ,
                    'STL': 'St. Louis Cardinals'    ,
                    'TB': 'Tampa Bay Rays'          ,
                    'TEX': 'Texas Rangers'          ,
                    'TOR': 'Toronto Blue Jays'      ,
                    'WSH': 'Washington Nationals'
                            }

    team_nicknames = {
                        'ARI': 'Diamondbacks'   ,
                        'ATL': 'Braves'         ,
                        'BAL': 'Orioles'        ,
                        'BOS': 'Red Sox'        ,
                        'CHC': 'Cubs'           ,
                        'CIN': 'Reds'           ,
                        'CLE': 'Indians'        ,
                        'COL': 'Rockies'        ,
                        'CWS': 'White Sox'      ,
                        'DET': 'Tigers'         ,
                        'HOU': 'Astros'         ,
                        'KC': 'Royals'          ,
                        'LAA': 'Angels'         ,
                        'LAD': 'Dodgers'        ,
                        'MIA': 'Marlins'        ,
                        'MIL': 'Brewers'        ,
                        'MIN': 'Twins'          ,
                        'NYM': 'Mets'           ,
                        'NYY': 'Yankees'        ,
                        'OAK': 'Athletics'      ,
                        'PHI': 'Phillies'       ,
                        'PIT': 'Pirates'        ,
                        'SD': 'Padres'          ,
                        'SEA': 'Mariners'       ,
                        'SF': 'Giants'          ,
                        'STL': 'Cardinals'      ,
                        'TB': 'Rays'            ,
                        'TEX': 'Rangers'        ,
                        'TOR': 'Blue Jays'      ,
                        'WSH': 'Nationals'
                                }

    ##### TITLE #####

    ### TEAM MATCHUP ###

    pdf.set_font('Proximan_Nova_Extra_Bold', '', 25)
    pdf.set_xy(x = pdf.l_margin, y = pdf.t_margin)

    pdf.cell(w = team_matchup_width, h = team_matchup_height, txt = team_names[str(game).split(' @ ')[0]] + ' @ ' + team_names[str(game).split(' @ ')[1]], border = 0, ln = 1, align = 'C')

    ### TIME ###

    pdf.set_font('Proximan_Nova_Bold', '', 15)
    pdf.set_xy(x = pdf.l_margin, y = pdf.t_margin + team_matchup_height)

    pdf.cell(w = time_width, h = time_height, txt = str(momentum_model_dictionary['Time']) + ' PT', border = 0, ln = 1, align = 'C')

    ### PITCHER MATCHUP ###

    pdf.set_font('Proximan_Nova', '', 20)
    pdf.set_xy(x = pdf.l_margin, y = pdf.t_margin + team_matchup_height + time_height)

    pdf.cell(w = pitcher_matchup_width, h = pitcher_matchup_height, txt = str(list(model_dictionary['Away']['Pitching'])[0]) + ' vs. ' + str(list(model_dictionary['Home']['Pitching'])[0]), border = 0, ln = 1, align = 'C')

    ##### BOXSCORE #####

    ### BOXSCORE TITLE ###

    pdf.set_font('Proximan_Nova', '', 15)
    pdf.set_xy(x = pdf.l_margin + boxscore_team_icon_width + boxscore_team_width, y = pdf.t_margin + team_matchup_height + time_height + pitcher_matchup_height)

    boxscore_title_set_y = pdf.t_margin + team_matchup_height + time_height + pitcher_matchup_height

    pdf.cell(w = boxscore_first_5_width, h = boxscore_title_height, txt = 'First 5', border = 0, ln = 1, align = 'C')
    pdf.set_xy(x = pdf.l_margin + boxscore_team_icon_width + boxscore_team_width + boxscore_first_5_width, y = boxscore_title_set_y)

    pdf.cell(w = boxscore_last_4_width, h = boxscore_title_height, txt = 'Last 4', border = 0, ln = 1, align = 'C')
    pdf.set_xy(x = pdf.l_margin + boxscore_team_icon_width + boxscore_team_width + boxscore_first_5_width + boxscore_last_4_width, y = boxscore_title_set_y)

    pdf.cell(w = boxscore_runs_width, h = boxscore_title_height, txt = 'Runs', border = 0, ln = 1, align = 'C')
    pdf.set_xy(x = pdf.l_margin + boxscore_team_icon_width + boxscore_team_width + boxscore_first_5_width + boxscore_last_4_width + boxscore_runs_width, y = boxscore_title_set_y)

    pdf.cell(w = boxscore_hits_width, h = boxscore_title_height, txt = 'Hits', border = 0, ln = 1, align = 'C')

    ### BOXSCORE ###

    pdf.set_font('Proximan_Nova_Bold', '', 15)
    pdf.set_xy(x = pdf.l_margin, y = boxscore_title_set_y + boxscore_title_height)

    boxscore_away_set_y = boxscore_title_set_y + boxscore_title_height
    boxscore_home_set_y = boxscore_away_set_y + boxscore_row_height

    pdf.image(root_path + '/MLB Model/Miscellaneous/Team Icons/' + str(game).split(' @ ')[0] + '.png', h = boxscore_row_height * 0.8, x = pdf.l_margin + boxscore_row_height * 0.1, y = boxscore_away_set_y + boxscore_row_height * 0.1)
    pdf.cell(w = boxscore_team_icon_width, h = boxscore_row_height, border = 'LTB', ln = 1, align = 'C')
    pdf.set_xy(x = pdf.l_margin + boxscore_team_icon_width, y = boxscore_away_set_y)

    pdf.cell(w = boxscore_team_width, h = boxscore_row_height, txt = str(game).split(' @ ')[0], border = 'RTB', ln = 1, align = 'C')
    pdf.set_xy(x = pdf.l_margin + boxscore_team_icon_width + boxscore_team_width, y = boxscore_away_set_y)

    pdf.cell(w = boxscore_first_5_width, h = boxscore_row_height, txt = str( '%.2f' % round(model_dictionary['Totals']['Away First 5'], 2)), border = 1, ln = 1, align = 'C')
    pdf.set_xy(x = pdf.l_margin + boxscore_team_icon_width + boxscore_team_width + boxscore_first_5_width, y = boxscore_away_set_y)

    pdf.cell(w = boxscore_last_4_width, h = boxscore_row_height, txt = str( '%.2f' % round(model_dictionary['Totals']['Away Last 4'], 2)), border = 1, ln = 1, align = 'C')
    pdf.set_xy(x = pdf.l_margin + boxscore_team_icon_width + boxscore_team_width + boxscore_first_5_width + boxscore_last_4_width, y = boxscore_away_set_y)

    pdf.cell(w = boxscore_runs_width, h = boxscore_row_height, txt = str( '%.2f' % round(model_dictionary['Totals']['Away Runs'], 2)), border = 1, ln = 1, align = 'C')
    pdf.set_xy(x = pdf.l_margin + boxscore_team_icon_width + boxscore_team_width + boxscore_first_5_width + boxscore_last_4_width + boxscore_runs_width, y = boxscore_away_set_y)

    pdf.cell(w = boxscore_hits_width, h = boxscore_row_height, txt = str( '%.2f' % round(model_dictionary['Totals']['Away Hits'], 2)), border = 1, ln = 1, align = 'C')
    pdf.set_xy(x = pdf.l_margin, y = boxscore_home_set_y)

    pdf.image(root_path + '/MLB Model/Miscellaneous/Team Icons/' + str(game).split(' @ ')[1] + '.png', h = boxscore_row_height * 0.8, x = pdf.l_margin + boxscore_row_height * 0.1, y = boxscore_home_set_y + boxscore_row_height * 0.1)
    pdf.cell(w = boxscore_team_icon_width, h = boxscore_row_height, border = 'LTB', ln = 1, align = 'C')
    pdf.set_xy(x = pdf.l_margin + boxscore_team_icon_width, y = boxscore_home_set_y)

    pdf.cell(w = boxscore_team_width, h = boxscore_row_height, txt = str(game).split(' @ ')[1], border = 'RTB', ln = 1, align = 'C')
    pdf.set_xy(x = pdf.l_margin + boxscore_team_icon_width + boxscore_team_width, y = boxscore_home_set_y)

    pdf.cell(w = boxscore_first_5_width, h = boxscore_row_height, txt = str( '%.2f' % round(model_dictionary['Totals']['Home First 5'], 2)), border = 1, ln = 1, align = 'C')
    pdf.set_xy(x = pdf.l_margin + boxscore_team_icon_width + boxscore_team_width + boxscore_first_5_width, y = boxscore_home_set_y)

    pdf.cell(w = boxscore_last_4_width, h = boxscore_row_height, txt = str( '%.2f' % round(model_dictionary['Totals']['Home Last 4'], 2)), border = 1, ln = 1, align = 'C')
    pdf.set_xy(x = pdf.l_margin + boxscore_team_icon_width + boxscore_team_width + boxscore_first_5_width + boxscore_last_4_width, y = boxscore_home_set_y)

    pdf.cell(w = boxscore_runs_width, h = boxscore_row_height, txt = str( '%.2f' % round(model_dictionary['Totals']['Home Runs'], 2)), border = 1, ln = 1, align = 'C')
    pdf.set_xy(x = pdf.l_margin + boxscore_team_icon_width + boxscore_team_width + boxscore_first_5_width + boxscore_last_4_width + boxscore_runs_width, y = boxscore_home_set_y)

    pdf.cell(w = boxscore_hits_width, h = boxscore_row_height, txt = str( '%.2f' % round(model_dictionary['Totals']['Home Hits'], 2)), border = 1, ln = 1, align = 'C')

    ##### AWAY BOXSCORE #####

    ### AWAY TEAM NAME ###

    pdf.set_font('Proximan_Nova', '', 20)
    pdf.set_xy(x = boxscore_away_set_x, y = boxscore_home_set_y + boxscore_row_height + lineup_team_name_height / 2)

    pdf.cell(w = lineup_team_name_width, h = lineup_team_name_height, txt = team_nicknames[str(game).split(' @ ')[0]], border = 0, ln = 1, align = 'C')

    #### AWAY LINEUP TITLE ###

    pdf.set_font('Proximan_Nova_Bold', '', 15)
    pdf.set_xy(x = boxscore_away_set_x, y = boxscore_home_set_y + boxscore_row_height + lineup_team_name_height / 2 + lineup_team_name_height)

    lineup_title_set_y = boxscore_home_set_y + boxscore_row_height + lineup_team_name_height / 2 + lineup_team_name_height

    pdf.cell(w = lineup_batter_width, h = lineup_title_height, txt = 'Batter', border = 'LTB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_away_set_x + lineup_batter_width, y = lineup_title_set_y)

    pdf.cell(w = lineup_stats_width, h = lineup_title_height, txt = 'wOBA', border = 'TB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_away_set_x + lineup_batter_width + lineup_stats_width, y = lineup_title_set_y)

    pdf.cell(w = lineup_stats_width, h = lineup_title_height, txt = 'Z', border = 'TB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_away_set_x + lineup_batter_width + lineup_stats_width + lineup_stats_width, y = lineup_title_set_y)

    pdf.cell(w = lineup_stats_width, h = lineup_title_height, txt = 'C', border = 'TB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_away_set_x + lineup_batter_width + lineup_stats_width + lineup_stats_width + lineup_stats_width, y = lineup_title_set_y)

    pdf.cell(w = lineup_stats_width, h = lineup_title_height, txt = 'M', border = 'RTB', ln = 1, align = 'C')

    #### AWAY LINEUP ROWS ###

    pdf.set_font('Proximan_Nova', '', 12)
    pdf.set_xy(x = boxscore_away_set_x, y = lineup_title_set_y + lineup_title_height)

    lineup_row_1_set_y = lineup_title_set_y + lineup_title_height
    lineup_row_2_set_y = lineup_row_1_set_y + lineup_title_height
    lineup_row_3_set_y = lineup_row_2_set_y + lineup_title_height
    lineup_row_4_set_y = lineup_row_3_set_y + lineup_title_height
    lineup_row_5_set_y = lineup_row_4_set_y + lineup_title_height
    lineup_row_6_set_y = lineup_row_5_set_y + lineup_title_height
    lineup_row_7_set_y = lineup_row_6_set_y + lineup_title_height
    lineup_row_8_set_y = lineup_row_7_set_y + lineup_title_height
    lineup_row_9_set_y = lineup_row_8_set_y + lineup_title_height

    lineup_row_set_y = {
                            '0': lineup_row_1_set_y ,
                            '1': lineup_row_2_set_y ,
                            '2': lineup_row_3_set_y ,
                            '3': lineup_row_4_set_y ,
                            '4': lineup_row_5_set_y ,
                            '5': lineup_row_6_set_y ,
                            '6': lineup_row_7_set_y ,
                            '7': lineup_row_8_set_y ,
                            '8': lineup_row_9_set_y
                                    }

    for i in range(9):

        pdf.set_xy(x = boxscore_away_set_x, y = lineup_row_set_y[str(i)])

        pdf.cell(w = lineup_batter_width, h = lineup_row_height, txt = str(list(model_dictionary['Away']['Lineup'])[i])[0] + '.' + str(list(model_dictionary['Away']['Lineup'])[i]).split(list(model_dictionary['Away']['Lineup'])[i].split(' ')[0])[1], border = 'LB', ln = 1, align = 'C')
        pdf.set_xy(x = boxscore_away_set_x + lineup_batter_width, y = lineup_row_set_y[str(i)])

        pdf.cell(w = lineup_stats_width, h = lineup_row_height, txt = str('%.3f' % round(model_dictionary['Away']['Lineup'][list(model_dictionary['Away']['Lineup'])[i]]['wOBA'], 3))[1:], border = 'B', ln = 1, align = 'C')
        pdf.set_xy(x = boxscore_away_set_x + lineup_batter_width + lineup_stats_width, y = lineup_row_set_y[str(i)])

        pdf.cell(w = lineup_stats_width, h = lineup_row_height, txt = str('%.3f' % round(zone_model_dictionary['Away']['Lineup'][list(zone_model_dictionary['Away']['Lineup'])[i]]['wOBA'], 3))[1:], border = 'B', ln = 1, align = 'C')
        pdf.set_xy(x = boxscore_away_set_x + lineup_batter_width + lineup_stats_width + lineup_stats_width, y = lineup_row_set_y[str(i)])

        pdf.cell(w = lineup_stats_width, h = lineup_row_height, txt = str('%.3f' % round(comparison_model_dictionary['Away']['Lineup'][list(comparison_model_dictionary['Away']['Lineup'])[i]]['wOBA'], 3))[1:], border = 'B', ln = 1, align = 'C')
        pdf.set_xy(x = boxscore_away_set_x + lineup_batter_width + lineup_stats_width + lineup_stats_width + lineup_stats_width, y = lineup_row_set_y[str(i)])

        pdf.cell(w = lineup_stats_width, h = lineup_row_height, txt = str('%.3f' % round(momentum_model_dictionary['Away']['Lineup'][list(momentum_model_dictionary['Away']['Lineup'])[i]]['wOBA'], 3))[1:], border = 'RB', ln = 1, align = 'C')

    #### AWAY STARTING PITCHER TITLE ###

    pdf.set_font('Proximan_Nova_Bold', '', 15)
    pdf.set_xy(x = boxscore_away_set_x, y = lineup_row_9_set_y + lineup_row_height + starting_pitcher_title_height)

    starting_pitcher_title_set_y = lineup_row_9_set_y + lineup_row_height + starting_pitcher_title_height

    pdf.cell(w = starting_pitcher_width, h = starting_pitcher_title_height, txt = 'Starter', border = 'LTB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_away_set_x + starting_pitcher_width, y = starting_pitcher_title_set_y)

    pdf.cell(w = starting_pitcher_stats_width, h = starting_pitcher_title_height, txt = 'wERA', border = 'TB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_away_set_x + starting_pitcher_width + starting_pitcher_stats_width, y = starting_pitcher_title_set_y)

    pdf.cell(w = starting_pitcher_stats_width, h = starting_pitcher_title_height, txt = 'Z', border = 'TB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_away_set_x + starting_pitcher_width + starting_pitcher_stats_width + starting_pitcher_stats_width, y = starting_pitcher_title_set_y)

    pdf.cell(w = starting_pitcher_stats_width, h = starting_pitcher_title_height, txt = 'C', border = 'TB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_away_set_x + starting_pitcher_width + starting_pitcher_stats_width + starting_pitcher_stats_width + starting_pitcher_stats_width, y = starting_pitcher_title_set_y)

    pdf.cell(w = starting_pitcher_stats_width, h = starting_pitcher_title_height, txt = 'M', border = 'RTB', ln = 1, align = 'C')

    #### AWAY STARTING PITCHER ###

    pdf.set_font('Proximan_Nova', '', 12)
    pdf.set_xy(x = boxscore_away_set_x, y = starting_pitcher_title_set_y + starting_pitcher_title_height)

    starting_pitcher_set_y = starting_pitcher_title_set_y + starting_pitcher_title_height

    pdf.cell(w = starting_pitcher_width, h = starting_pitcher_height, txt = str(list(model_dictionary['Away']['Pitching'])[0])[0] + '.' + str(list(model_dictionary['Away']['Pitching'])[0]).split(list(model_dictionary['Away']['Pitching'])[0].split(' ')[0])[1], border = 'LB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_away_set_x + starting_pitcher_width, y = starting_pitcher_set_y)

    pdf.cell(w = starting_pitcher_stats_width, h = starting_pitcher_height, txt = str('%.2f' % round(model_dictionary['Away']['Pitching'][list(model_dictionary['Away']['Pitching'])[0]]['wERA'], 2)), border = 'B', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_away_set_x + starting_pitcher_width + starting_pitcher_stats_width, y = starting_pitcher_set_y)

    pdf.cell(w = starting_pitcher_stats_width, h = starting_pitcher_height, txt = str('%.2f' % round(zone_model_dictionary['Away']['Pitching'][list(zone_model_dictionary['Away']['Pitching'])[0]]['wERA'], 2)), border = 'B', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_away_set_x + starting_pitcher_width + starting_pitcher_stats_width + starting_pitcher_stats_width, y = starting_pitcher_set_y)

    pdf.cell(w = starting_pitcher_stats_width, h = starting_pitcher_height, txt = str('%.2f' % round(comparison_model_dictionary['Away']['Pitching'][list(comparison_model_dictionary['Away']['Pitching'])[0]]['wERA'], 2)), border = 'B', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_away_set_x + starting_pitcher_width + starting_pitcher_stats_width + starting_pitcher_stats_width + starting_pitcher_stats_width, y = starting_pitcher_set_y)

    pdf.cell(w = starting_pitcher_stats_width, h = starting_pitcher_height, txt = str('%.2f' % round(momentum_model_dictionary['Away']['Pitching'][list(momentum_model_dictionary['Away']['Pitching'])[0]]['wERA'], 2)), border = 'RB', ln = 1, align = 'C')

    #### AWAY BULLPEN TITLE ###

    pdf.set_font('Proximan_Nova_Bold', '', 15)
    pdf.set_xy(x = boxscore_away_set_x, y = starting_pitcher_set_y + starting_pitcher_height + bullpen_title_height)

    bullpen_title_set_y = starting_pitcher_set_y + starting_pitcher_height + bullpen_title_height

    pdf.cell(w = bullpen_pitcher_width, h = bullpen_title_height, txt = 'Reliever', border = 'LTB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_away_set_x + bullpen_pitcher_width, y = bullpen_title_set_y)

    pdf.cell(w = bullpen_stats_width, h = bullpen_title_height, txt = 'wERA', border = 'TB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_away_set_x + bullpen_pitcher_width + bullpen_stats_width, y = bullpen_title_set_y)

    pdf.cell(w = bullpen_stats_width, h = bullpen_title_height, txt = 'Z', border = 'TB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_away_set_x + bullpen_pitcher_width + bullpen_stats_width + bullpen_stats_width, y = bullpen_title_set_y)

    pdf.cell(w = bullpen_stats_width, h = bullpen_title_height, txt = 'C', border = 'TB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_away_set_x + bullpen_pitcher_width + bullpen_stats_width + bullpen_stats_width + bullpen_stats_width, y = bullpen_title_set_y)

    pdf.cell(w = bullpen_stats_width, h = bullpen_title_height, txt = 'M', border = 'RTB', ln = 1, align = 'C')

    #### AWAY BULLPEN ###

    pdf.set_font('Proximan_Nova', '', 12)
    pdf.set_xy(x = boxscore_away_set_x, y = bullpen_title_set_y + bullpen_title_height)

    bullpen_row_1_set_y = bullpen_title_set_y + bullpen_row_height
    bullpen_row_2_set_y = bullpen_row_1_set_y + bullpen_row_height
    bullpen_row_3_set_y = bullpen_row_2_set_y + bullpen_row_height
    bullpen_row_4_set_y = bullpen_row_3_set_y + bullpen_row_height
    bullpen_row_5_set_y = bullpen_row_4_set_y + bullpen_row_height
    bullpen_row_6_set_y = bullpen_row_5_set_y + bullpen_row_height
    bullpen_row_7_set_y = bullpen_row_6_set_y + bullpen_row_height

    bullpen_row_set_y = {
                            '1': bullpen_row_1_set_y    ,
                            '2': bullpen_row_2_set_y    ,
                            '3': bullpen_row_3_set_y    ,
                            '4': bullpen_row_4_set_y    ,
                            '5': bullpen_row_5_set_y    ,
                            '6': bullpen_row_6_set_y    ,
                            '7': bullpen_row_7_set_y
                                    }

    for i in range(1, len(list(model_dictionary['Away']['Pitching']))):

        pdf.set_xy(x = boxscore_away_set_x, y = bullpen_row_set_y[str(i)])

        pdf.cell(w = bullpen_pitcher_width, h = bullpen_row_height, txt = str(list(model_dictionary['Away']['Pitching'])[i])[0] + '.' + str(list(model_dictionary['Away']['Pitching'])[i]).split(list(model_dictionary['Away']['Pitching'])[i].split(' ')[0])[1], border = 'LB', ln = 1, align = 'C')
        pdf.set_xy(x = boxscore_away_set_x + bullpen_pitcher_width, y = bullpen_row_set_y[str(i)])

        pdf.cell(w = bullpen_stats_width, h = bullpen_row_height, txt = str('%.2f' % round(model_dictionary['Away']['Pitching'][list(model_dictionary['Away']['Pitching'])[i]]['wERA'], 2)), border = 'B', ln = 1, align = 'C')
        pdf.set_xy(x = boxscore_away_set_x + bullpen_pitcher_width + bullpen_stats_width, y = bullpen_row_set_y[str(i)])

        pdf.cell(w = bullpen_stats_width, h = bullpen_row_height, txt = str('%.2f' % round(zone_model_dictionary['Away']['Pitching'][list(zone_model_dictionary['Away']['Pitching'])[i]]['wERA'], 2)), border = 'B', ln = 1, align = 'C')
        pdf.set_xy(x = boxscore_away_set_x + bullpen_pitcher_width + bullpen_stats_width + bullpen_stats_width, y = bullpen_row_set_y[str(i)])

        pdf.cell(w = bullpen_stats_width, h = bullpen_row_height, txt = str('%.2f' % round(comparison_model_dictionary['Away']['Pitching'][list(comparison_model_dictionary['Away']['Pitching'])[i]]['wERA'], 2)), border = 'B', ln = 1, align = 'C')
        pdf.set_xy(x = boxscore_away_set_x + bullpen_pitcher_width + bullpen_stats_width + bullpen_stats_width + bullpen_stats_width, y = bullpen_row_set_y[str(i)])

        pdf.cell(w = bullpen_stats_width, h = bullpen_row_height, txt = str('%.2f' % round(momentum_model_dictionary['Away']['Pitching'][list(momentum_model_dictionary['Away']['Pitching'])[i]]['wERA'], 2)), border = 'RB', ln = 1, align = 'C')

    ##### HOME BOXSCORE #####

    ### HOME TEAM NAME ###

    pdf.set_font('Proximan_Nova', '', 20)
    pdf.set_xy(x = boxscore_home_set_x, y = boxscore_home_set_y + boxscore_row_height + lineup_team_name_height / 2)

    pdf.cell(w = lineup_team_name_width, h = lineup_team_name_height, txt = team_nicknames[str(game).split(' @ ')[1]], border = 0, ln = 1, align = 'C')

    #### HOME LINEUP TITLE ###

    pdf.set_font('Proximan_Nova_Bold', '', 15)
    pdf.set_xy(x = boxscore_home_set_x, y = boxscore_home_set_y + boxscore_row_height + lineup_team_name_height / 2 + lineup_team_name_height)

    lineup_title_set_y = boxscore_home_set_y + boxscore_row_height + lineup_team_name_height / 2 + lineup_team_name_height

    pdf.cell(w = lineup_batter_width, h = lineup_title_height, txt = 'Batter', border = 'LTB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_home_set_x + lineup_batter_width, y = lineup_title_set_y)

    pdf.cell(w = lineup_stats_width, h = lineup_title_height, txt = 'wOBA', border = 'TB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_home_set_x + lineup_batter_width + lineup_stats_width, y = lineup_title_set_y)

    pdf.cell(w = lineup_stats_width, h = lineup_title_height, txt = 'Z', border = 'TB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_home_set_x + lineup_batter_width + lineup_stats_width + lineup_stats_width, y = lineup_title_set_y)

    pdf.cell(w = lineup_stats_width, h = lineup_title_height, txt = 'C', border = 'TB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_home_set_x + lineup_batter_width + lineup_stats_width + lineup_stats_width + lineup_stats_width, y = lineup_title_set_y)

    pdf.cell(w = lineup_stats_width, h = lineup_title_height, txt = 'M', border = 'RTB', ln = 1, align = 'C')

    #### HOME LINEUP ROWS ###

    pdf.set_font('Proximan_Nova', '', 12)
    pdf.set_xy(x = boxscore_home_set_x, y = lineup_title_set_y + lineup_title_height)

    lineup_row_1_set_y = lineup_title_set_y + lineup_title_height
    lineup_row_2_set_y = lineup_row_1_set_y + lineup_title_height
    lineup_row_3_set_y = lineup_row_2_set_y + lineup_title_height
    lineup_row_4_set_y = lineup_row_3_set_y + lineup_title_height
    lineup_row_5_set_y = lineup_row_4_set_y + lineup_title_height
    lineup_row_6_set_y = lineup_row_5_set_y + lineup_title_height
    lineup_row_7_set_y = lineup_row_6_set_y + lineup_title_height
    lineup_row_8_set_y = lineup_row_7_set_y + lineup_title_height
    lineup_row_9_set_y = lineup_row_8_set_y + lineup_title_height

    lineup_row_set_y = {
                            '0': lineup_row_1_set_y ,
                            '1': lineup_row_2_set_y ,
                            '2': lineup_row_3_set_y ,
                            '3': lineup_row_4_set_y ,
                            '4': lineup_row_5_set_y ,
                            '5': lineup_row_6_set_y ,
                            '6': lineup_row_7_set_y ,
                            '7': lineup_row_8_set_y ,
                            '8': lineup_row_9_set_y
                                    }

    for i in range(9):

        pdf.set_xy(x = boxscore_home_set_x, y = lineup_row_set_y[str(i)])

        pdf.cell(w = lineup_batter_width, h = lineup_row_height, txt = str(list(model_dictionary['Home']['Lineup'])[i])[0] + '.' + str(list(model_dictionary['Home']['Lineup'])[i]).split(list(model_dictionary['Home']['Lineup'])[i].split(' ')[0])[1], border = 'LB', ln = 1, align = 'C')
        pdf.set_xy(x = boxscore_home_set_x + lineup_batter_width, y = lineup_row_set_y[str(i)])

        pdf.cell(w = lineup_stats_width, h = lineup_row_height, txt = str('%.3f' % round(model_dictionary['Home']['Lineup'][list(model_dictionary['Home']['Lineup'])[i]]['wOBA'], 3))[1:], border = 'B', ln = 1, align = 'C')
        pdf.set_xy(x = boxscore_home_set_x + lineup_batter_width + lineup_stats_width, y = lineup_row_set_y[str(i)])

        pdf.cell(w = lineup_stats_width, h = lineup_row_height, txt = str('%.3f' % round(zone_model_dictionary['Home']['Lineup'][list(zone_model_dictionary['Home']['Lineup'])[i]]['wOBA'], 3))[1:], border = 'B', ln = 1, align = 'C')
        pdf.set_xy(x = boxscore_home_set_x + lineup_batter_width + lineup_stats_width + lineup_stats_width, y = lineup_row_set_y[str(i)])

        pdf.cell(w = lineup_stats_width, h = lineup_row_height, txt = str('%.3f' % round(comparison_model_dictionary['Home']['Lineup'][list(comparison_model_dictionary['Home']['Lineup'])[i]]['wOBA'], 3))[1:], border = 'B', ln = 1, align = 'C')
        pdf.set_xy(x = boxscore_home_set_x + lineup_batter_width + lineup_stats_width + lineup_stats_width + lineup_stats_width, y = lineup_row_set_y[str(i)])

        pdf.cell(w = lineup_stats_width, h = lineup_row_height, txt = str('%.3f' % round(momentum_model_dictionary['Home']['Lineup'][list(momentum_model_dictionary['Home']['Lineup'])[i]]['wOBA'], 3))[1:], border = 'RB', ln = 1, align = 'C')

    #### HOME STARTING PITCHER TITLE ###

    pdf.set_font('Proximan_Nova_Bold', '', 15)
    pdf.set_xy(x = boxscore_home_set_x, y = lineup_row_9_set_y + lineup_row_height + starting_pitcher_title_height)

    starting_pitcher_title_set_y = lineup_row_9_set_y + lineup_row_height + starting_pitcher_title_height

    pdf.cell(w = starting_pitcher_width, h = starting_pitcher_title_height, txt = 'Starter', border = 'LTB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_home_set_x + starting_pitcher_width, y = starting_pitcher_title_set_y)

    pdf.cell(w = starting_pitcher_stats_width, h = starting_pitcher_title_height, txt = 'wERA', border = 'TB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_home_set_x + starting_pitcher_width + starting_pitcher_stats_width, y = starting_pitcher_title_set_y)

    pdf.cell(w = starting_pitcher_stats_width, h = starting_pitcher_title_height, txt = 'Z', border = 'TB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_home_set_x + starting_pitcher_width + starting_pitcher_stats_width + starting_pitcher_stats_width, y = starting_pitcher_title_set_y)

    pdf.cell(w = starting_pitcher_stats_width, h = starting_pitcher_title_height, txt = 'C', border = 'TB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_home_set_x + starting_pitcher_width + starting_pitcher_stats_width + starting_pitcher_stats_width + starting_pitcher_stats_width, y = starting_pitcher_title_set_y)

    pdf.cell(w = starting_pitcher_stats_width, h = starting_pitcher_title_height, txt = 'M', border = 'RTB', ln = 1, align = 'C')

    #### HOME STARTING PITCHER ###

    pdf.set_font('Proximan_Nova', '', 12)
    pdf.set_xy(x = boxscore_home_set_x, y = starting_pitcher_title_set_y + starting_pitcher_title_height)

    starting_pitcher_set_y = starting_pitcher_title_set_y + starting_pitcher_title_height

    pdf.cell(w = starting_pitcher_width, h = starting_pitcher_height, txt = str(list(model_dictionary['Home']['Pitching'])[0])[0] + '.' + str(list(model_dictionary['Home']['Pitching'])[0]).split(list(model_dictionary['Home']['Pitching'])[0].split(' ')[0])[1], border = 'LB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_home_set_x + starting_pitcher_width, y = starting_pitcher_set_y)

    pdf.cell(w = starting_pitcher_stats_width, h = starting_pitcher_height, txt = str('%.2f' % round(model_dictionary['Home']['Pitching'][list(model_dictionary['Home']['Pitching'])[0]]['wERA'], 2)), border = 'B', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_home_set_x + starting_pitcher_width + starting_pitcher_stats_width, y = starting_pitcher_set_y)

    pdf.cell(w = starting_pitcher_stats_width, h = starting_pitcher_height, txt = str('%.2f' % round(zone_model_dictionary['Home']['Pitching'][list(zone_model_dictionary['Home']['Pitching'])[0]]['wERA'], 2)), border = 'B', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_home_set_x + starting_pitcher_width + starting_pitcher_stats_width + starting_pitcher_stats_width, y = starting_pitcher_set_y)

    pdf.cell(w = starting_pitcher_stats_width, h = starting_pitcher_height, txt = str('%.2f' % round(comparison_model_dictionary['Home']['Pitching'][list(comparison_model_dictionary['Home']['Pitching'])[0]]['wERA'], 2)), border = 'B', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_home_set_x + starting_pitcher_width + starting_pitcher_stats_width + starting_pitcher_stats_width + starting_pitcher_stats_width, y = starting_pitcher_set_y)

    pdf.cell(w = starting_pitcher_stats_width, h = starting_pitcher_height, txt = str('%.2f' % round(momentum_model_dictionary['Home']['Pitching'][list(momentum_model_dictionary['Home']['Pitching'])[0]]['wERA'], 2)), border = 'RB', ln = 1, align = 'C')

    #### HOME BULLPEN TITLE ###

    pdf.set_font('Proximan_Nova_Bold', '', 15)
    pdf.set_xy(x = boxscore_home_set_x, y = starting_pitcher_set_y + starting_pitcher_height + bullpen_title_height)

    bullpen_title_set_y = starting_pitcher_set_y + starting_pitcher_height + bullpen_title_height

    pdf.cell(w = bullpen_pitcher_width, h = bullpen_title_height, txt = 'Reliever', border = 'LTB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_home_set_x + bullpen_pitcher_width, y = bullpen_title_set_y)

    pdf.cell(w = bullpen_stats_width, h = bullpen_title_height, txt = 'wERA', border = 'TB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_home_set_x + bullpen_pitcher_width + bullpen_stats_width, y = bullpen_title_set_y)

    pdf.cell(w = bullpen_stats_width, h = bullpen_title_height, txt = 'Z', border = 'TB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_home_set_x + bullpen_pitcher_width + bullpen_stats_width + bullpen_stats_width, y = bullpen_title_set_y)

    pdf.cell(w = bullpen_stats_width, h = bullpen_title_height, txt = 'C', border = 'TB', ln = 1, align = 'C')
    pdf.set_xy(x = boxscore_home_set_x + bullpen_pitcher_width + bullpen_stats_width + bullpen_stats_width + bullpen_stats_width, y = bullpen_title_set_y)

    pdf.cell(w = bullpen_stats_width, h = bullpen_title_height, txt = 'M', border = 'RTB', ln = 1, align = 'C')

    #### HOME BULLPEN ###

    pdf.set_font('Proximan_Nova', '', 12)
    pdf.set_xy(x = boxscore_home_set_x, y = bullpen_title_set_y + bullpen_title_height)

    bullpen_row_1_set_y = bullpen_title_set_y + bullpen_row_height
    bullpen_row_2_set_y = bullpen_row_1_set_y + bullpen_row_height
    bullpen_row_3_set_y = bullpen_row_2_set_y + bullpen_row_height
    bullpen_row_4_set_y = bullpen_row_3_set_y + bullpen_row_height
    bullpen_row_5_set_y = bullpen_row_4_set_y + bullpen_row_height
    bullpen_row_6_set_y = bullpen_row_5_set_y + bullpen_row_height
    bullpen_row_7_set_y = bullpen_row_6_set_y + bullpen_row_height

    bullpen_row_set_y = {
                            '1': bullpen_row_1_set_y    ,
                            '2': bullpen_row_2_set_y    ,
                            '3': bullpen_row_3_set_y    ,
                            '4': bullpen_row_4_set_y    ,
                            '5': bullpen_row_5_set_y    ,
                            '6': bullpen_row_6_set_y    ,
                            '7': bullpen_row_7_set_y
                                    }

    for i in range(1, len(list(model_dictionary['Home']['Pitching']))):

        pdf.set_xy(x = boxscore_home_set_x, y = bullpen_row_set_y[str(i)])

        pdf.cell(w = bullpen_pitcher_width, h = bullpen_row_height, txt = str(list(model_dictionary['Home']['Pitching'])[i])[0] + '.' + str(list(model_dictionary['Home']['Pitching'])[i]).split(list(model_dictionary['Home']['Pitching'])[i].split(' ')[0])[1], border = 'LB', ln = 1, align = 'C')
        pdf.set_xy(x = boxscore_home_set_x + bullpen_pitcher_width, y = bullpen_row_set_y[str(i)])

        pdf.cell(w = bullpen_stats_width, h = bullpen_row_height, txt = str('%.2f' % round(model_dictionary['Home']['Pitching'][list(model_dictionary['Home']['Pitching'])[i]]['wERA'], 2)), border = 'B', ln = 1, align = 'C')
        pdf.set_xy(x = boxscore_home_set_x + bullpen_pitcher_width + bullpen_stats_width, y = bullpen_row_set_y[str(i)])

        pdf.cell(w = bullpen_stats_width, h = bullpen_row_height, txt = str('%.2f' % round(zone_model_dictionary['Home']['Pitching'][list(zone_model_dictionary['Home']['Pitching'])[i]]['wERA'], 2)), border = 'B', ln = 1, align = 'C')
        pdf.set_xy(x = boxscore_home_set_x + bullpen_pitcher_width + bullpen_stats_width + bullpen_stats_width, y = bullpen_row_set_y[str(i)])

        pdf.cell(w = bullpen_stats_width, h = bullpen_row_height, txt = str('%.2f' % round(comparison_model_dictionary['Home']['Pitching'][list(comparison_model_dictionary['Home']['Pitching'])[i]]['wERA'], 2)), border = 'B', ln = 1, align = 'C')
        pdf.set_xy(x = boxscore_home_set_x + bullpen_pitcher_width + bullpen_stats_width + bullpen_stats_width + bullpen_stats_width, y = bullpen_row_set_y[str(i)])

        pdf.cell(w = bullpen_stats_width, h = bullpen_row_height, txt = str('%.2f' % round(momentum_model_dictionary['Home']['Pitching'][list(momentum_model_dictionary['Home']['Pitching'])[i]]['wERA'], 2)), border = 'RB', ln = 1, align = 'C')

    ##### OUTPUT #####

    ### ZONE MODEL TITLE ###

    pdf.set_font('Proximan_Nova_Bold', '', 20)
    pdf.set_xy(x = pdf.l_margin, y = bullpen_row_7_set_y + bullpen_row_height + model_height / 2)

    pdf.cell(w = model_width, h = model_height, txt = 'Zone', border = 0, ln = 1, align = 'C')

    ### ZONE MODEL OUTPUT ###

    pdf.set_font('Proximan_Nova', '', 12)
    pdf.set_xy(x = pdf.l_margin, y = bullpen_row_7_set_y + bullpen_row_height + model_height / 2 + model_height)

    zone_model_set_x = pdf.l_margin
    zone_model_set_y = bullpen_row_7_set_y + bullpen_row_height + model_height / 2 + model_height

    pdf.cell(w = model_width, h = model_height, txt = 'Winner: ' + str(zone_model_dictionary['Winner']) + '  ' + 'Confidence: ' + str((round(zone_model_dictionary['Winner Confidence'] * 100, 1))) + '%', border = 0, ln = 1, align = 'C')
    pdf.set_xy(x = pdf.l_margin, y = zone_model_set_y + model_height)

    pdf.cell(w = model_width, h = model_height / 3, txt = 'Total: ' + str( '%.2f' % round(zone_model_dictionary['Total'], 2)), border = 0, ln = 1, align = 'C')

    #### COMPARISON MODEL TITLE ###

    pdf.set_font('Proximan_Nova_Bold', '', 20)
    pdf.set_xy(x = zone_model_set_x + model_winner_width + model_confidence_width + pdf.l_margin / 2, y = bullpen_row_7_set_y + bullpen_row_height + model_height / 2)

    pdf.cell(w = model_width, h = model_height, txt = 'Comparison', border = 0, ln = 1, align = 'C')

    #### CONPARISON MODEL OUTPUT ###

    pdf.set_font('Proximan_Nova', '', 12)
    pdf.set_xy(x = zone_model_set_x + model_winner_width + model_confidence_width + pdf.l_margin / 2, y = bullpen_row_7_set_y + bullpen_row_height + model_height / 2 + model_height)

    comparison_model_set_x = zone_model_set_x + model_winner_width + model_confidence_width + pdf.l_margin / 2
    comparison_model_set_y = bullpen_row_7_set_y + bullpen_row_height + model_height / 2 + model_height

    pdf.cell(w = model_width, h = model_height, txt = 'Winner: ' + str(comparison_model_dictionary['Winner']) + '  ' + 'Confidence: ' + str((round(comparison_model_dictionary['Winner Confidence'] * 100, 1))) + '%', border = 0, ln = 1, align = 'C')
    pdf.set_xy(x = comparison_model_set_x, y = comparison_model_set_y + model_height)

    pdf.cell(w = model_width, h = model_height / 3, txt = 'Total: ' + str( '%.2f' % round(comparison_model_dictionary['Total'], 2)), border = 0, ln = 1, align = 'C')

    ### MOMENTUM MODEL TITLE ###

    pdf.set_font('Proximan_Nova_Bold', '', 20)
    pdf.set_xy(x = comparison_model_set_x + model_winner_width + model_confidence_width + pdf.l_margin / 2, y = bullpen_row_7_set_y + bullpen_row_height + model_height / 2)

    pdf.cell(w = model_width, h = model_height, txt = 'Momentum', border = 0, ln = 1, align = 'C')

    ### MOMENTUM MODEL OUTPUT ###

    pdf.set_font('Proximan_Nova', '', 12)
    pdf.set_xy(x = comparison_model_set_x + model_winner_width + model_confidence_width + pdf.l_margin / 2, y = bullpen_row_7_set_y + bullpen_row_height + model_height / 2 + model_height)

    momentum_model_set_x = comparison_model_set_x + model_winner_width + model_confidence_width + pdf.l_margin / 2
    momentum_model_set_y = bullpen_row_7_set_y + bullpen_row_height + model_height / 2 + model_height

    pdf.cell(w = model_width, h = model_height, txt = 'Winner: ' + str(momentum_model_dictionary['Winner']) + '  ' + 'Confidence: ' + str((round(momentum_model_dictionary['Winner Confidence'] * 100, 1))) + '%', border = 0, ln = 1, align = 'C')
    pdf.set_xy(x = momentum_model_set_x, y = momentum_model_set_y + model_height)

    pdf.cell(w = model_width, h = model_height / 3, txt = 'Total: ' + str( '%.2f' % round(momentum_model_dictionary['Total'], 2)), border = 0, ln = 1, align = 'C')

    ### OUTPUT ###

    pdf.set_font('Proximan_Nova_Extra_Bold', '', 25)
    pdf.set_xy(x = pdf.l_margin, y = momentum_model_set_y + model_height + output_height / 4)

    winner_set_x = pdf.l_margin
    winner_set_y = momentum_model_set_y + model_height + output_height / 4

    pdf.cell(w = page_width, h = output_height, txt = '      Winner: ' + str(model_dictionary['Winner']) + '        ' + 'Confidence: ' + str((round(model_dictionary['Winner Confidence'] * 100, 1))) + '%', border = 0, ln = 1, align = 'C')
    pdf.set_xy(x = winner_set_x + winner_width, y = winner_set_y)

    return pdf

 ########## ########## ########## ########## ##########










 ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########
