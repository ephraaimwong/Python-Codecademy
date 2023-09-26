'''
Game of scrabble of up to 6 players
5 turns each, in order of players
Show scores at the end, highest score wins

'''
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {key : value for key, value in zip(letters, points)}
#this blank entry will allow for loop to score spaces
letters_to_points[" "] = 0

def score_word(word):
    point_total = 0
    for i in word.upper():
        #.get(i) from dict with scrabble scores, returns 0 if theres no match
        letters_to_points.get(i, 0)
        po  int_total += letters_to_points[i]
    return point_total

def play_word(playernum, word):
    player_wordhistory[playernum].append(word)
            
num_of_players = []
player_names = []
#Creating of player numbers up to input number of players
for i in range(int(input("Please Enter No. of Players(Up to 6): "))):
    #(i+1) so player number starts from value "1" instead of "0".
    num_of_players.append(i+1)
#Assigning names according to player number
for i in num_of_players:
    player_names.append(input(f"Enter name for player {i}:"))
player_playernum ={key:value for key, value in zip(player_names, num_of_players)}
print(player_playernum)

#players' wordhistory
player_wordhistory = {}
#Creating empty lists for each player to store their wordhistory
for i in player_playernum.keys():
    player_wordhistory[i] = []

#appending their words into individual lists
turn = 1
while turn <= 5:
    print(f"Turn {turn}.")
    for i in player_playernum.keys():
        player_wordhistory[i].append(input("Enter word: "))
    turn += 1

#players' scores
player_points = {}
#Joining the wordhistory of each player into 1 string, fed through score_word() to get score
for i in player_wordhistory.keys():
    player_points[i] = score_word(("".join(player_wordhistory[i])))


#Gets winner from player_points{} based on highest points
for key, value in player_points.items():
    #winner = the key assigned to highest points in player_points{}
    if value == max(player_points.values()):
        winner = key
print(f"{winner} wins with {max(player_points.values())}!")
    



