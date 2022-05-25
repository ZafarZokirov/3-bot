# class player:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def kimsan(self):
#         print(f"Mening ismim {self.name}.Yoshim {self.age}")
#     def update_age(self,new_age):
#         self.age=new_age
#     def update_name(self,new_name):
#         self.name=new_name
# Ronaldo=player("Cristiano Ronaldo",38)
# Sallah=player("Muhammad Sallah", 30)
# print(f"ismi: {Ronaldo.name},yoshi: {Ronaldo.age}")
# print(f"ismi: {Sallah.name},yoshi: {Sallah.age}")
# Ronaldo.update_age(18)
# Ronaldo.update_name("Messi")
# Ronaldo.kimsan()
# Sallah.kimsan()
# class Player:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def kimsan(self):
#         print(f"Mening ismim {self.name}. Yoshim {self.age}da")
#
#     def get_age(self):
#         return self.age
#
#     def get_name(self):
#         return self.name
#
#     def set_age(self, new_age):
#         self.age = new_age
#
#     def set_name(self, new_name):
#         self.name = new_name
#
#     def update_age(self):
#         self.age += 1
#
#     def get_player_info(self):
#         return f"O'yinchi:{self.name}, yoshi: {self.age}"
# class Team:
#     def __init__(self,name):
#         self.name=name
#         self.players_count=0
#         self.players=[]
#     def add_player(self,player):
#         self.players.append(player)
#         self.players_count += 1
#
#     def get_team_info(self):
#         print(f"Komanda nomi:{self.name} o'yinchilar nomi {self.players_count}")
#
#     def  get_players(self):
#         return [player.get_player_info() for player in self.players]
#
#
#
#
#
#
# player1=Player("Odil Ahmedov", 39)
# player2=Player("Eldor Sholmurodov", 29)
# player3=Player("Japarov Laban", 32)
#
# team1=Team("Roma")
# team1.get_team_info()
# team1.add_player(player3)
# team1.add_player(player2)
# team1.add_player(player1)
# team1.get_team_info()
# print(team1.get_players())
#




