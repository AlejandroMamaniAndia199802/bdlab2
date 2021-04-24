
# Ejercicio 1
# import pandas as pd

# data=pd.read_csv("WorldCupMatches.csv")
# solution1 = data.query("HomeTeamName=='Ecuador'")
# print (solution1)

# Ejercicio 2
# import pandas as pd

# data=pd.read_csv("WorldCupMatches.csv")
# solution2 = data.query("(HomeTeamName=='Brazil'|HomeTeamName=='Argentina') & (AwayTeamName=='Brazil'|AwayTeamName=='Argentina')")
# print(solution2)

#Ejercicio 3
#import pandas as pd
#data=pd.read_csv("WorldCups.csv")

#solution3_1 = data.query("Year=='2010'")
#print(solution3_1)

#data_matchid=pd.read_csv("WorldCupMatches.csv")
#solution3_2=data_matchid.query("Year=='2010'& Stage=='Final'")
#print(solution3_2)

#match_id = 300061509

#data_players=pd.read_csv("WorldCupPlayers.csv")
#solution3_3=data_players.query("(MatchID=='300061509'& TeamInitials=='ESP') & Line=='S' ")
#print(solution3_3)

#Ejercicio 4
import pandas as pd
data=pd.read_csv("WorldCupPlayers.csv")

solution4_1 = data.query("PlayerName=='RONALDINHO'")
#print(solution4_1)

# 43950010 
# 43950026
# 43950041
# 43950054
# 43950057
# 43950062
# 43950064
# 97410011
# 97410027
# 97410043
# 97410055
# 97410060  


data_matches=pd.read_csv("WorldCupMatches.csv")

#& (MatchID=='43950026')& (MatchID=='43950041')& (MatchID=='43950054')& (MatchID=='43950057')& (MatchID=='43950062')& (MatchID=='43950064')& (MatchID=='97410011')& (MatchID=='97410027')& (MatchID=='97410043')& (MatchID=='97410055')& (MatchID=='97410060')
solution4_2 = data_matches.query(" (MatchID=='43950010'| MatchID=='43950026'|MatchID=='43950041'|MatchID=='43950054'|MatchID=='43950057'| MatchID=='43950062'|MatchID=='43950064'| MatchID=='97410011'| MatchID=='97410027'| MatchID=='97410043'|MatchID=='97410055'|MatchID=='97410060')")
print(solution4_2)