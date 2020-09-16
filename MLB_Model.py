########## ########## ########## ########## ########## ########## ########## ########## ########## ##########

###################
##### IMPORTS #####
###################

########## ########## ########## ########## ##########

### DATA ###
import numpy as np

### IMPORT / EXPORT ###
import json
import sys
import os

### PATHS ###
path = os.path.dirname(os.path.dirname(__file__))
root_path = path.split('MLB Model')[0]

sys.path.append(root_path + '/MLB Model')
sys.path.append(root_path + '/MLB Model/Zone Model/Code')
sys.path.append(root_path + '/MLB Model/Comparison Model/Code')
sys.path.append(root_path + '/MLB Model/Momentum Model/Code')
sys.path.append(root_path + '/MLB Model/Miscellaneous')

### MODEL FILES ###
import Zone_Model
import Comparison_Model
import Momentum_Model
import MLB_Model_Output
import Starting_Lineups

########## ########## ########## ########## ##########

#####################
##### MLB MODEL #####
#####################

########## ########## ########## ########## ##########

def get_Game_Info(date):

	game_info = Starting_Lineups.get_Game_Info(date)
	bullpen = Starting_Lineups.get_Bullpen()

	for game in game_info:

		game_info[game]['Home Bullpen'] = bullpen[game_info[game]['Home Team'][0]]
		game_info[game]['Away Bullpen'] = bullpen[game_info[game]['Away Team'][0]]

	return game_info


def normalize_Model(data):

	target_wOBA = 0.3
	target_wERA = 5
	target_Total = 8.5
	target_Hits = 7

	totals = []
	team_totals = []

	first_5_totals = []
	first_5_team_totals = []

	last_4_totals = []
	last_4_team_totals = []

	team_hits = []

	wOBAs = []
	wERAs = []

	for game in data:

		totals.append(data[game]['Total'])
		team_totals.append(data[game]['Away Runs'])
		team_totals.append(data[game]['Home Runs'])

		first_5_totals.append(data[game]['Total First 5'])
		first_5_team_totals.append(data[game]['Away First 5'])
		first_5_team_totals.append(data[game]['Home First 5'])

		last_4_totals.append(data[game]['Total Last 4'])
		last_4_team_totals.append(data[game]['Away Last 4'])
		last_4_team_totals.append(data[game]['Home Last 4'])

		team_hits.append(data[game]['Away Hits'])
		team_hits.append(data[game]['Home Hits'])

		for batter in data[game]['Away']['Lineup']:
			wOBAs.append(data[game]['Away']['Lineup'][batter]['wOBA'])

		for batter in data[game]['Home']['Lineup']:
			wOBAs.append(data[game]['Home']['Lineup'][batter]['wOBA'])

		for pitcher in data[game]['Away']['Pitching']:
			wERAs.append(data[game]['Away']['Pitching'][pitcher]['wERA'])

		for pitcher in data[game]['Home']['Pitching']:
			wERAs.append(data[game]['Home']['Pitching'][pitcher]['wERA'])

	totals_multiplier = 1 / np.mean(totals) * target_Total
	team_totals_multiplier = 1 / np.mean(team_totals) * target_Total / 2

	first_5_totals_multiplier = 1/ np.mean(first_5_totals) * target_Total * 5 / 9
	first_5_team_totals_multiplier = 1 / np.mean(first_5_team_totals) * target_Total * 5 / 18

	last_4_totals_multiplier = 1 / np.mean(last_4_totals) * target_Total * 4 / 9
	last_4_team_totals_multiplier = 1 / np.mean(last_4_team_totals) * target_Total * 4 / 18

	team_hits_multiplier = 1 / np.mean(team_hits) * target_Hits

	wOBAs_multiplier = 1 / np.mean(wOBAs) * target_wOBA
	wERAs_multiplier = 1 / np.mean(wERAs) * target_wERA

	for game in data:

		data[game]['Total'] *= totals_multiplier
		data[game]['Away Runs'] *= team_totals_multiplier
		data[game]['Home Runs'] *= team_totals_multiplier

		data[game]['Total First 5'] *= first_5_totals_multiplier
		data[game]['Away First 5'] *= first_5_team_totals_multiplier
		data[game]['Home First 5'] *= first_5_team_totals_multiplier

		data[game]['Total Last 4'] *= last_4_totals_multiplier
		data[game]['Away Last 4'] *= last_4_team_totals_multiplier
		data[game]['Home Last 4'] *= last_4_team_totals_multiplier

		data[game]['Away Hits'] *= team_hits_multiplier
		data[game]['Home Hits'] *= team_hits_multiplier

		for batter in data[game]['Away']['Lineup']:
			data[game]['Away']['Lineup'][batter]['wOBA'] *= wOBAs_multiplier

		for batter in data[game]['Home']['Lineup']:
			data[game]['Home']['Lineup'][batter]['wOBA'] *= wOBAs_multiplier

		for pitcher in data[game]['Away']['Pitching']:
			data[game]['Away']['Pitching'][pitcher]['wERA'] *= wERAs_multiplier

		for pitcher in data[game]['Home']['Pitching']:
			data[game]['Home']['Pitching'][pitcher]['wERA'] *= wERAs_multiplier

	return data


def MLB_Model(date, num_sims):

	weights_total = [1.5, 1.5, 1]
	weights_batter = [1, 1, 1]
	weights_pitcher = [2, 2, 1]

	game_info = get_Game_Info(date)

	try:

		previous_dict = json.load(open(root_path + '/MLB Model/MLB Model Output/TXT/' + date + '.TXT', 'r'))

		previous_model = previous_dict['Overall Model']
		previous_zone_model = previous_dict['Zone Model']
		previous_comparison_model = previous_dict['Comparison Model']
		previous_momentum_model = previous_dict['Momentum Model']

		new_game_info = {}

		for game in game_info:

			game_name = game_info[game]['Away Team'][0] + ' @ ' + game_info[game]['Home Team'][0] + game_info['Game Number']

			if game_name not in previous_model.keys():
				new_game_info[game] = game_info[game]

	except:

		previous_model = {}
		previous_zone_model = {}
		previous_comparison_model = {}
		previous_momentum_model = {}

		new_game_info = game_info

	zone_model = Zone_Model.Zone_Model(date, num_sims, new_game_info)
	comparison_model = Comparison_Model.Comparison_Model(date, num_sims, new_game_info)
	momentum_model = Momentum_Model.Momentum_Model(date, num_sims, new_game_info)

	zone_model = normalize_Model(zone_model)
	comparison_model = normalize_Model(comparison_model)
	momentum_model = normalize_Model(momentum_model)

	model = {}

	for game in zone_model:

		away_team_name = game.split(' @ ')[0]
		home_team_name = game.split(' @ ')[1]

		model[game] = {}

		model[game]['Away'] = {}
		model[game]['Home'] = {}

		model[game]['Totals'] = {}

		model[game]['Away']['Lineup'] = {}
		model[game]['Home']['Lineup'] = {}

		model[game]['Away']['Pitching'] = {}
		model[game]['Home']['Pitching'] = {}

		model[game]['Totals']['Total'] = np.average([zone_model[game]['Total'], comparison_model[game]['Total'], momentum_model[game]['Total']], weights = weights_total)

		model[game]['Totals']['Away Runs'] = np.average([zone_model[game]['Away Runs'], comparison_model[game]['Away Runs'], momentum_model[game]['Away Runs']], weights = weights_total)
		model[game]['Totals']['Home Runs'] = np.average([zone_model[game]['Home Runs'], comparison_model[game]['Home Runs'], momentum_model[game]['Home Runs']], weights = weights_total)

		model[game]['Totals']['Total First 5'] = np.average([zone_model[game]['Total First 5'], comparison_model[game]['Total First 5'], momentum_model[game]['Total First 5']], weights = weights_total)

		model[game]['Totals']['Away First 5'] = np.average([zone_model[game]['Away First 5'], comparison_model[game]['Away First 5'], momentum_model[game]['Away First 5']], weights = weights_total)
		model[game]['Totals']['Home First 5'] = np.average([zone_model[game]['Home First 5'], comparison_model[game]['Home First 5'], momentum_model[game]['Home First 5']], weights = weights_total)

		model[game]['Totals']['Total Last 4'] = np.average([zone_model[game]['Total Last 4'], comparison_model[game]['Total Last 4'], momentum_model[game]['Total Last 4']], weights = weights_total)

		model[game]['Totals']['Away Last 4'] = np.average([zone_model[game]['Away Last 4'], comparison_model[game]['Away Last 4'], momentum_model[game]['Away Last 4']], weights = weights_total)
		model[game]['Totals']['Home Last 4'] = np.average([zone_model[game]['Home Last 4'], comparison_model[game]['Home Last 4'], momentum_model[game]['Home Last 4']], weights = weights_total)

		model[game]['Totals']['Away Hits'] = np.average([zone_model[game]['Away Hits'], comparison_model[game]['Away Hits'], momentum_model[game]['Away Hits']], weights = weights_total)
		model[game]['Totals']['Home Hits'] = np.average([zone_model[game]['Home Hits'], comparison_model[game]['Home Hits'], momentum_model[game]['Home Hits']], weights = weights_total)

		for batter in [x for x in zone_model[game]['Away']['Lineup'] if x in comparison_model[game]['Away']['Lineup']]:

			model[game]['Away']['Lineup'][batter] = {}

			model[game]['Away']['Lineup'][batter]['PA'] = np.average([zone_model[game]['Away']['Lineup'][batter]['PA'], comparison_model[game]['Away']['Lineup'][batter]['PA'], momentum_model[game]['Away']['Lineup'][batter]['PA']], weights = weights_batter)
			model[game]['Away']['Lineup'][batter]['1B'] = np.average([zone_model[game]['Away']['Lineup'][batter]['1B'], comparison_model[game]['Away']['Lineup'][batter]['1B'], momentum_model[game]['Away']['Lineup'][batter]['1B']], weights = weights_batter)
			model[game]['Away']['Lineup'][batter]['2B'] = np.average([zone_model[game]['Away']['Lineup'][batter]['2B'], comparison_model[game]['Away']['Lineup'][batter]['2B'], momentum_model[game]['Away']['Lineup'][batter]['2B']], weights = weights_batter)
			model[game]['Away']['Lineup'][batter]['3B'] = np.average([zone_model[game]['Away']['Lineup'][batter]['3B'], comparison_model[game]['Away']['Lineup'][batter]['3B'], momentum_model[game]['Away']['Lineup'][batter]['3B']], weights = weights_batter)
			model[game]['Away']['Lineup'][batter]['HR'] = np.average([zone_model[game]['Away']['Lineup'][batter]['HR'], comparison_model[game]['Away']['Lineup'][batter]['HR'], momentum_model[game]['Away']['Lineup'][batter]['HR']], weights = weights_batter)
			model[game]['Away']['Lineup'][batter]['BB'] = np.average([zone_model[game]['Away']['Lineup'][batter]['BB'], comparison_model[game]['Away']['Lineup'][batter]['BB'], momentum_model[game]['Away']['Lineup'][batter]['BB']], weights = weights_batter)
			model[game]['Away']['Lineup'][batter]['SO'] = np.average([zone_model[game]['Away']['Lineup'][batter]['SO'], comparison_model[game]['Away']['Lineup'][batter]['SO'], momentum_model[game]['Away']['Lineup'][batter]['SO']], weights = weights_batter)
			model[game]['Away']['Lineup'][batter]['OUT-SOFT'] = np.average([zone_model[game]['Away']['Lineup'][batter]['OUT-SOFT'], comparison_model[game]['Away']['Lineup'][batter]['OUT-SOFT'], momentum_model[game]['Away']['Lineup'][batter]['OUT-SOFT']], weights = weights_batter)
			model[game]['Away']['Lineup'][batter]['OUT-HARD'] = np.average([zone_model[game]['Away']['Lineup'][batter]['OUT-HARD'], comparison_model[game]['Away']['Lineup'][batter]['OUT-HARD'], momentum_model[game]['Away']['Lineup'][batter]['OUT-HARD']], weights = weights_batter)

			model[game]['Away']['Lineup'][batter]['wOBA'] = np.average([zone_model[game]['Away']['Lineup'][batter]['wOBA'], comparison_model[game]['Away']['Lineup'][batter]['wOBA'], momentum_model[game]['Away']['Lineup'][batter]['wOBA']], weights = weights_batter)

		for batter in [x for x in zone_model[game]['Home']['Lineup'] if x in comparison_model[game]['Home']['Lineup'] and x in zone_model[game]['Home']['Lineup']]:

			model[game]['Home']['Lineup'][batter] = {}

			model[game]['Home']['Lineup'][batter]['PA'] = np.average([zone_model[game]['Home']['Lineup'][batter]['PA'], comparison_model[game]['Home']['Lineup'][batter]['PA'], momentum_model[game]['Home']['Lineup'][batter]['PA']], weights = weights_batter)
			model[game]['Home']['Lineup'][batter]['1B'] = np.average([zone_model[game]['Home']['Lineup'][batter]['1B'], comparison_model[game]['Home']['Lineup'][batter]['1B'], momentum_model[game]['Home']['Lineup'][batter]['1B']], weights = weights_batter)
			model[game]['Home']['Lineup'][batter]['2B'] = np.average([zone_model[game]['Home']['Lineup'][batter]['2B'], comparison_model[game]['Home']['Lineup'][batter]['2B'], momentum_model[game]['Home']['Lineup'][batter]['2B']], weights = weights_batter)
			model[game]['Home']['Lineup'][batter]['3B'] = np.average([zone_model[game]['Home']['Lineup'][batter]['3B'], comparison_model[game]['Home']['Lineup'][batter]['3B'], momentum_model[game]['Home']['Lineup'][batter]['3B']], weights = weights_batter)
			model[game]['Home']['Lineup'][batter]['HR'] = np.average([zone_model[game]['Home']['Lineup'][batter]['HR'], comparison_model[game]['Home']['Lineup'][batter]['HR'], momentum_model[game]['Home']['Lineup'][batter]['HR']], weights = weights_batter)
			model[game]['Home']['Lineup'][batter]['BB'] = np.average([zone_model[game]['Home']['Lineup'][batter]['BB'], comparison_model[game]['Home']['Lineup'][batter]['BB'], momentum_model[game]['Home']['Lineup'][batter]['BB']], weights = weights_batter)
			model[game]['Home']['Lineup'][batter]['SO'] = np.average([zone_model[game]['Home']['Lineup'][batter]['SO'], comparison_model[game]['Home']['Lineup'][batter]['SO'], momentum_model[game]['Home']['Lineup'][batter]['SO']], weights = weights_batter)
			model[game]['Home']['Lineup'][batter]['OUT-SOFT'] = np.average([zone_model[game]['Home']['Lineup'][batter]['OUT-SOFT'], comparison_model[game]['Home']['Lineup'][batter]['OUT-SOFT'], momentum_model[game]['Home']['Lineup'][batter]['OUT-SOFT']], weights = weights_batter)
			model[game]['Home']['Lineup'][batter]['OUT-HARD'] = np.average([zone_model[game]['Home']['Lineup'][batter]['OUT-HARD'], comparison_model[game]['Home']['Lineup'][batter]['OUT-HARD'], momentum_model[game]['Home']['Lineup'][batter]['OUT-HARD']], weights = weights_batter)

			model[game]['Home']['Lineup'][batter]['wOBA'] = np.average([zone_model[game]['Home']['Lineup'][batter]['wOBA'], comparison_model[game]['Home']['Lineup'][batter]['wOBA'], momentum_model[game]['Home']['Lineup'][batter]['wOBA']], weights = weights_batter)

		for pitcher in [x for x in zone_model[game]['Away']['Pitching'] if x in comparison_model[game]['Away']['Pitching'] and x in momentum_model[game]['Away']['Pitching']]:

			model[game]['Away']['Pitching'][pitcher] = {}

			model[game]['Away']['Pitching'][pitcher]['Innings'] = np.average([zone_model[game]['Away']['Pitching'][pitcher]['Innings'], comparison_model[game]['Away']['Pitching'][pitcher]['Innings'], momentum_model[game]['Away']['Pitching'][pitcher]['Innings']], weights = weights_pitcher)
			model[game]['Away']['Pitching'][pitcher]['Runs'] = np.average([zone_model[game]['Away']['Pitching'][pitcher]['Runs'], comparison_model[game]['Away']['Pitching'][pitcher]['Runs'], momentum_model[game]['Away']['Pitching'][pitcher]['Runs']], weights = weights_pitcher)
			model[game]['Away']['Pitching'][pitcher]['Hits'] = np.average([zone_model[game]['Away']['Pitching'][pitcher]['Hits'], comparison_model[game]['Away']['Pitching'][pitcher]['Hits'], momentum_model[game]['Away']['Pitching'][pitcher]['Hits']], weights = weights_pitcher)

			model[game]['Away']['Pitching'][pitcher]['wERA'] = np.average([zone_model[game]['Away']['Pitching'][pitcher]['wERA'], comparison_model[game]['Away']['Pitching'][pitcher]['wERA'], momentum_model[game]['Away']['Pitching'][pitcher]['wERA']], weights = weights_pitcher)

		for pitcher in [x for x in zone_model[game]['Home']['Pitching'] if x in comparison_model[game]['Home']['Pitching'] and x in zone_model[game]['Home']['Pitching']]:

			model[game]['Home']['Pitching'][pitcher] = {}

			model[game]['Home']['Pitching'][pitcher]['Innings'] = np.average([zone_model[game]['Home']['Pitching'][pitcher]['Innings'], comparison_model[game]['Home']['Pitching'][pitcher]['Innings'], momentum_model[game]['Home']['Pitching'][pitcher]['Innings']], weights = weights_pitcher)
			model[game]['Home']['Pitching'][pitcher]['Runs'] = np.average([zone_model[game]['Home']['Pitching'][pitcher]['Runs'], comparison_model[game]['Home']['Pitching'][pitcher]['Runs'], momentum_model[game]['Home']['Pitching'][pitcher]['Runs']], weights = weights_pitcher)
			model[game]['Home']['Pitching'][pitcher]['Hits'] = np.average([zone_model[game]['Home']['Pitching'][pitcher]['Hits'], comparison_model[game]['Home']['Pitching'][pitcher]['Hits'], momentum_model[game]['Home']['Pitching'][pitcher]['Hits']], weights = weights_pitcher)

			model[game]['Home']['Pitching'][pitcher]['wERA'] = np.average([zone_model[game]['Home']['Pitching'][pitcher]['wERA'], comparison_model[game]['Home']['Pitching'][pitcher]['wERA'], momentum_model[game]['Home']['Pitching'][pitcher]['wERA']], weights = weights_pitcher)


		if zone_model[game]['Winner'] == away_team_name:

			zone_away_team_wins = zone_model[game]['Winner Confidence']
			zone_home_team_wins = 1 - zone_away_team_wins

		else:

			zone_home_team_wins = zone_model[game]['Winner Confidence']
			zone_away_team_wins = 1 - zone_home_team_wins

		if comparison_model[game]['Winner'] == away_team_name:

			comparison_away_team_wins = comparison_model[game]['Winner Confidence']
			comparison_home_team_wins = 1 - comparison_away_team_wins

		else:

			comparison_home_team_wins = comparison_model[game]['Winner Confidence']
			comparison_away_team_wins = 1 - comparison_home_team_wins

		if momentum_model[game]['Winner'] == away_team_name:

			momentum_away_team_wins = momentum_model[game]['Winner Confidence']
			momentum_home_team_wins = 1 - momentum_away_team_wins

		else:

			momentum_home_team_wins = momentum_model[game]['Winner Confidence']
			momentum_away_team_wins = 1 - momentum_home_team_wins

		away_team_wins = np.average([zone_away_team_wins, comparison_away_team_wins, momentum_away_team_wins], weights = weights_total)
		home_team_wins = np.average([zone_home_team_wins, comparison_home_team_wins, momentum_home_team_wins], weights = weights_total)

		if away_team_wins > home_team_wins:

			model[game]['Winner'] = away_team_name
			model[game]['Winner Confidence'] = away_team_wins

		else:

			model[game]['Winner'] = home_team_name
			model[game]['Winner Confidence'] = home_team_wins


	model = {**previous_model, **model}
	zone_model = {**previous_zone_model, **zone_model}
	comparison_model = {**previous_comparison_model, **comparison_model}
	momentum_model = {**previous_momentum_model, **momentum_model}

	d = {}
	d['Overall Model'] = model
	d['Zone Model'] = zone_model
	d['Comparison Model'] = comparison_model
	d['Momentum Model'] = momentum_model

	with open(root_path + '/MLB Model/MLB Model Output/TXT/' + date + '.TXT', 'w') as file:
		file.write(json.dumps(d))

	return model, zone_model, comparison_model, momentum_model


def write_MLB_Model_PDF(date, num_sims):

	model, zone_model, comparison_model, momentum_model = MLB_Model(date, num_sims)

	games = sorted(zone_model.items(), key = lambda x: x[1]['Time'])

	games = [x[0] for x in games]

	pdf = MLB_Model_Output.Title_Page(date)

	for game in games:

		pdf = MLB_Model_Output.Matchup_Page(game, model[game], zone_model[game], comparison_model[game], momentum_model[game], pdf)

	pdf.output(root_path + '/MLB Model/MLB Model Output/PDF/' + date + '.pdf')

########## ########## ########## ########## ##########

write_MLB_Model_PDF('2020-09-15', 250)








########## ########## ########## ########## ########## ########## ########## ########## ########## ##########
