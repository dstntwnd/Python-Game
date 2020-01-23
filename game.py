player = {'Name': 'Renalt', 'Attack': 20, 'Heal': 35, 'Health': 100}
monster = {'Name': 'Vilthreat', 'Attack': 25, 'Heal': 25, 'Health': 100}

import time
game_running = True

print('~~~' * 10)
print('What is your heros name? ')
player['Name'] = input().title()
time.sleep(.5)
print('')
time.sleep(.5)
print('Who is your rival? ')
monster['Name'] = input().title()
print('~~~' * 10)
time.sleep(1)
print('Let the battle...BEGIN')
time.sleep(1)
print('~~~' * 10)
print('')
print(player['Name'] + ':' + str(player['Health']))
print(monster['Name'] + ':' + str(monster['Health']))
print('')

while game_running == True:
    player_won = False
    monster_won = False

    print('')
    print('!! MAKE YOUR MOVE !!')
    print('1.) Attack')
    print('2.) Heal')

    player_choice = input('Input 1 or 2: ')

    # PLAYER

    if player_choice == '1':
        monster['Health'] = monster['Health'] - player['Attack']
        print('')
        time.sleep(.5)
        print('%s: %d' % (player['Name'], player['Health']))
        print('%s: %d' % (monster['Name'], monster['Health']))
        print(' ')
        time.sleep(1)
        if monster['Health'] <= 0:
            player_won = True

        elif monster['Health'] > 25:
            print('%s is making his move!' % (monster['Name']))
            print(' ')
            time.sleep(2)
            player['Health'] = player['Health'] - monster['Attack']
            print('')
            print('%s: %d' % (player['Name'], player['Health']))
            print('%s: %d' % (monster['Name'], monster['Health']))
            print(' ')
            time.sleep(2)
        elif monster['Health'] in range(16, 25):
            print('%s: This has gone on LONG ENOUGH, I will CRUSH YOU!!' % (monster['Name']))
            print(' ')
            time.sleep(3)
            print('%s is enraged!!  HE unleases a powerful attack!!' % (monster['Name']))
            time.sleep(3)
            player['Health'] = player['Health'] - monster['Attack'] * 2
            print('')
            print('%s: %d' % (player['Name'], player['Health']))
            print('%s: %d' % (monster['Name'], monster['Health']))
            print(' ')
            time.sleep(2)
            if player['Health'] <= 0:
                monster_won = True
        elif monster['Health'] <= 15:
            monster['Health'] = monster['Health'] + monster['Heal']
            print('')
            print('%s: %d' % (player['Name'], player['Health']))
            print('%s: %d' % (monster['Name'], monster['Health'])) 
            print(' ')
            time.sleep(2)
        
    elif player_choice == '2':
        player["Health"] = player['Health'] + player['Heal']
        print('')
        time.sleep(1)
        print('%s: %d' % (player['Name'], player['Health']))
        print('%s: %d' % (monster['Name'], monster['Health']))
        print(' ')
        time.sleep(2)
        if monster['Health'] > 25:
            print('%s is making his move!' % (monster['Name']))
            print(' ')
            time.sleep(2)
            player['Health'] = player['Health'] - monster['Attack']
            print('')
            print('%s: %d' % (player['Name'], player['Health']))
            print('%s: %d' % (monster['Name'], monster['Health']))
            print(' ')
            time.sleep(2)
            if player['Health'] <= 0:
                monster_won = True
        elif monster['Health'] in range(16, 25):
            print('%s: This has gone on LONG ENOUGH, I will CRUSH YOU!!' % (monster['Name']))
            print(' ')
            time.sleep(3)
            print('%s is enraged!!  HE unleases a powerful attack!!' % (monster['Name']))
            time.sleep(3)
            player['Health'] = player['Health'] - monster['Attack'] * 2
            print('')
            print('%s: %d' % (player['Name'], player['Health']))
            print('%s: %d' % (monster['Name'], monster['Health']))
            print(' ')
            time.sleep(2)
            if player['Health'] <= 0:
                monster_won = True
        elif monster['Health'] <= 15:
            monster['Health'] = monster['Health'] + monster['Heal']
            print('')
            print('%s: %d' % (player['Name'], player['Health']))
            print('%s: %d' % (monster['Name'], monster['Health'])) 
            print(' ')
            time.sleep(2)

    else:
        print('That is not an option')
        print(' ')
        time.sleep(2)

    # END OF GAME

    if monster_won == True:
        print('%s: Seeking a battle with me is no different that seeking death' % (monster['Name']))
        print(' ')
        time.sleep(4)
        print('You will get %s next time' % (monster['Name']))
        print(' ')
        time.sleep(3.5)
        game_running = False

    if player_won == True:
        print('%s: Lets be real %s...you never stood a chance' % (player['Name'], monster['Name']))
        print(' ')
        time.sleep(4)
        print('YOU WIN')
        print(' ')
        time.sleep(3.5)
        game_running = False
    else:
        game_running == True

#while game_running == False:
 #           print('Would you like test your strength against your rival again? ')
  #          time.sleep(1)
   #         player_restart = input('Yes or No: ')
    #        if player_restart == 'Yes' or 'yes':
     #           time.sleep(1)
      #          print('Get ready for another battle in...')
       #         print('3')
        #        time.sleep(1)
         #       print('2')
          #      time.sleep(1)
           #     print('1')
            #    time.sleep(1)
             #   game_running = True
            #elif player_restart == 'No' or 'no':
             #   time.sleep(1)
              #  print('Thank you for playing!  See you next time.')
               # time.sleep(2)
                #game_running = False
            #else:
             #   print('That is not an option.')