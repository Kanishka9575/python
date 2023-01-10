import random
Toss_dict = {'O':"ODD",'E':"EVEN"}
user_count=0
comp_count=0
print("#### Let the toss begin ####")
user_toss = input("Choose ODD or EVEN: ")
if(user_toss == "ODD"):
  comp_toss = "EVEN"
else:
  comp_toss = "ODD"
Toss = random.choice(list(Toss_dict.keys()))
print("Toss: ",Toss_dict[Toss])
if(user_toss == Toss_dict[Toss]):
  print("HURRY!! YOU WON THE TOSS!")
else:
  print("COMPUTER WON THE TOSS!")
Game_dict = {'BAT': "Batting",'Ball': "Bowling"}
if(user_toss == Toss_dict[Toss]):
  user = input("Do you like to do Batting or Bowling ?? :")
  if(user == "Batting"):
    comp = "Bowling"
  else:
    comp = "Battting"
else:
  print("SORRY! YOU LOST THE TOSS!!")
  comp = random.choice(list(Game_dict.keys()))
  print("Computer has choosen :",Game_dict[comp])
  if(Game_dict[comp] == "Batting"):
    user = "Bowling"
  else:
    user = "Batting"
if(user == "Batting"):
  Game_score ={1:1 ,2:2,3:3,4:4,5:5,6:6}
  for i in range(0,6):
    user_score = int(input("Choose a number between 1-6: "))
    comp_score = random.choice(list(Game_score.keys()))
    print("You have choosen",user_score,"and computer has choosen",comp_score)
    if(user_score == comp_score):
      print("-- User Out--")
      break
    else:
         user_count = user_count + user_score
         comp_count = comp_count + comp_score
elif(user == "Bowling"):
  Game_score ={1:1 ,2:2,3:3,4:4,5:5,6:6}
  for i in range(0,6):
    user_score = int(input("Choose a number between 1-6: "))
    comp_score = random.choice(list(Game_score.keys()))
    print("Computer has choosen",comp_score,"and you have choosen",user_score)
    if(comp_score == user_score):
      print("-- Computer Out--")
      break
    else:
      user_count = user_count + user_score
      comp_count = comp_count + comp_score
elif(comp == "Bowling"):
  Game_score ={1:1 ,2:2,3:3,4:4,5:5,6:6}
  for i in range(0,6):
    user_score = int(input("Choose a number between 1-6: "))
    comp_score = random.choice(list(Game_score.keys()))
    print("You have choosen",user_score,"and computer has choosen",comp_score)
    if(user_score == comp_score):
      print("-- User Out--")
      break
    else:
      user_count = user_count + user_score
      comp_count = comp_count + comp_score
else:
  Game_score ={1:1 ,2:2,3:3,4:4,5:5,6:6}
  for i in range(0,6):
    user_score = int(input("Choose a number between 1-6: "))
    comp_score = random.choice(list(Game_score.keys()))
    print("Computer has choosen",comp_score,"and you have choosen",user_score)
    if(comp_score == user_score):
      print("-- Computer Out--")
      break
    else:
      user_count = user_count + user_score
      comp_count = comp_count + comp_score
print("User Score:",user_count,"and Computer Score:",comp_count)
if (user_count > comp_count):
  print("CONGRATULATIONS! YOU WON THE GAME!!")
elif(user_count == comp_count):
  print("OOPS! IT'S A TIE!!")
else:
  print("SORRY! YOU LOST THE GAME!!")