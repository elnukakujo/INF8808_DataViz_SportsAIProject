def preprocess(players_stats):
    players_stats = players_stats[["FullName", "StatsID", "StatsName", "Value"]]
    players_stats = players_stats.query("StatsID == 17")
    players_stats['Value'] = players_stats['Value'].astype('int')
    
    tackles_stats = players_stats.groupby('FullName')['Value'].sum().reset_index()    
    
    return tackles_stats.nlargest(15, 'Value')