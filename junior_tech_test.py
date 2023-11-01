import csv


def read_csv_file(file_path):
    """
    Read a CSV file and return its content as a list of dictionaries.
    """

    with open(file_path, encoding='utf-8') as c:
        reader = csv.DictReader(c, delimiter=',')
        data = []
        for row in reader:
            data.append(row)
    return data

def get_unique_teams(data):
    """
    Return a set of unique team names from the provided data.
    """
    unique_teams = set() 

    for row in data:
        if 'team_name' in row and row['team_name'] is not None:
            unique_teams.add(row['team_name'])
    return unique_teams

def get_most_common_event_type(data):
    """
    Return the most common event type name from the provided data.
    """
    event_types = [row['event_type_name'] for row in data if 'event_type_name' in row and row['event_type_name'] is not None]
    if not event_types:
        return None
    return max(set(event_types), key=event_types.count)


def filter_by_team(data, team_name):
    """
    Filter the data by the provided team name and return the filtered data.
    """
    filtered_data = [row for row in data if 'team_name' in row and row['team_name'] == team_name and row['team_name'] is not None]
    return filtered_data



def count_event_type_by_team(data, team_name, event_type_name):
    """
    Count the number of events of a specific type for a given team.
    """
    count = sum(1 for row in data if row['team_name'] == team_name and row['event_type_name'] == event_type_name)
    return count


    
def average_pass_length_by_team(data, team_name):
    """
    Calculate the average pass length for the provided team to 1 decimal place.
    """
    pass_lengths = [float(row['pass_length']) for row in data if row['team_name'] == team_name and row['pass_length']]
    if not pass_lengths:
        return 0.0
    average_length = round(sum(pass_lengths) / len(pass_lengths), 1)
    return average_length




def filter_players_by_position(data, position_name):
    """
    Return a list of player names who play at the provided position.
    """
    players = {row['player_name'] for row in data if row['player_position_name'] == position_name}
    return players



def count_successful_passes(data):
    """
    Count the number of successful passes (not considering pass outcome).
    """
    successful_passes = 0  
    for i in range(len(data) - 1):
        current_event = data[i]
        next_event = data[i + 1]

        if current_event["event_type_name"] == "Pass" and next_event["event_type_name"] == "Ball Receipt*":
            successful_passes += 1

    return successful_passes

    # I can't figure this one out
    

def filter_by_period(data, period):
    """
    Return a list of events that occurred in the provided period (e.g., 1 or 2).
    """
    filtered_data = [row for row in data if row.get('period') == period]
    return filtered_data


def count_shots_by_player(data, player_name):
    """
    Count the number of shots taken by the provided player.
    """
    shots = 0
    index = set()  

    for row in data:
        if row["player_name"] == player_name and row["event_type_name"] == "Shot":
            if row["index"] not in index:
                index.add(row["index"])  
                shots += 1

    return shots
