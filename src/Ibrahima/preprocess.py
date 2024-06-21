def preprocess(players_stats):
    players_stats = players_stats[["FullName", "StatsID", "StatsName", "Value"]]
    players_stats = players_stats.query("StatsID == 17")
    
    tackles_stats = players_stats.groupby('FullName')['Value'].sum().reset_index()
    
    tackles_stats['Value'] = tackles_stats['Value'].astype('int')
    
    return tackles_stats.nlargest(15, 'Value')