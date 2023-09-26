#winner = the key assigned to highest points in player_points{}
for key, value in player_points.items():
    if value == max(player_points.values()):
        winner = key
print(f"{winner} wins with {max(player_points.values())}!")