import pandas as pd

def get_df(sheet_name: str)->pd.DataFrame:
    '''
        Load the wanted csv file

        Args:
            sheet_name (str): The name of the sheet to load
        
        Returns:
            The wanted dataframe
    '''
    data = pd.read_csv(f"./assets/data/EURO_2020_DATA_{sheet_name}.csv")
    if sheet_name == "Players_stats":
        data["FullName"] = data["PlayerName"] + " " + data["PlayerSurname"]
        data.drop(["PlayerName", "PlayerSurname"], axis=1, inplace=True)
        return data
    elif sheet_name == "Line-ups":
        data["FullName"] = data["OfficialName"] + " " + data["OfficialSurname"]
        data.drop(["OfficialName", "OfficialSurname"], axis=1, inplace=True)
        return data
    else:
        return data

def load_data()->pd.DataFrame:
    '''
        Load the csv files

        Returns:
            The 4 dataframes
    '''
    match_infos = get_df('Match_information')
    match_stats = get_df('Match_Stats')
    player_stats = get_df('Players_stats')
    line_ups = get_df('Line-ups')
    return match_infos, match_stats, player_stats, line_ups