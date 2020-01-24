from random import randint
import time
def monster_attack():
    return randint(monster['Min_attack'], monster['Max_attack'])
def player_attack():
    return randint(player['Min_attack'], player['Max_attack'])
def monster_heal():
    return randint(monster['Min_heal'], monster['Max_heal'])
def player_heal():
    return randint(player['Min_heal'], player['Max_heal'])
def player_spec_atk():
    return randint(player['Min_special_attack'], player['Max_special_attack'])
def player_spec_heal():
    return randint(player['Min_special_heal'], player['Max_special_heal'])
def monster_spec_atk():
    return randint(monster['Min_special_attack'], monster['Max_special_attack'])

game_running = True

player = {'Name': 'Renalt', 'Min_attack': 20, 'Max_attack': 40, 'Min_special_attack': 0, 'Max_special_attack': 60, 'Min_heal': 35, 'Max_heal': 50, 'Min_special_heal': 10, 'Max_special_heal': 80, 'Health': 100}
monster = {'Name': 'Vilthreat', 'Min_attack': 20, 'Max_attack': 45, 'Min_special_attack': 15, 'Max_special_attack': 70, 'Min_heal': 20, 'Max_heal': 45, 'Health': 100}

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
    print('~~~' * 10)
    print('!! MAKE YOUR MOVE !!')
    print('~~~' * 10)
    print('1.) Attack (20-40)')
    print('2.) Heal (35-50)')
    print('3.) Special Attack (0-60)')
    print('4.) Special Heal (10-80)')

    player_choice = input('Input: ')

    # PLAYER

    if player_choice == '1':
        monster['Health'] = monster['Health'] - player_attack()
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
            player['Health'] = player['Health'] - monster_attack()
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
            player['Health'] = player['Health'] - monster_spec_atk()
            print('')
            print('%s: %d' % (player['Name'], player['Health']))
            print('%s: %d' % (monster['Name'], monster['Health']))
            print(' ')
            time.sleep(2)
            if player['Health'] <= 0:
                monster_won = True
        elif monster['Health'] <= 15:
            print('%s: You hold more power than I had thought.  It does not matter though, you are not the only being with magic.' % (monster['Name']))
            print('')
            time.sleep(1)
            print('(%s is healing)' % (monster['Name']))
            time.sleep(1.5)
            monster['Health'] = monster['Health'] + monster_heal()
            print('')
            print('%s: %d' % (player['Name'], player['Health']))
            print('%s: %d' % (monster['Name'], monster['Health'])) 
            print(' ')
            time.sleep(2)
        
    elif player_choice == '2':
        player["Health"] = player['Health'] + player_heal()
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
            player['Health'] = player['Health'] - monster_attack()
            print('')
            print('%s: %d' % (player['Name'], player['Health']))
            print('%s: %d' % (monster['Name'], monster['Health']))
            print(' ')
            time.sleep(2)
            if player['Health'] <= 0:
                monster_won = True
        elif monster['Health'] in range(16, 25):
            print('%s: Your healing magic cannot save you %s.  Today, you entered your last battle.' % (monster['Name'], player['Name']))
            print(' ')
            time.sleep(3)
            player['Health'] = player['Health'] - monster_attack()
            print('')
            print('%s: %d' % (player['Name'], player['Health']))
            print('%s: %d' % (monster['Name'], monster['Health']))
            print(' ')
            time.sleep(2)
            if player['Health'] <= 0:
                monster_won = True
        elif monster['Health'] <= 15:
            print('%s: You hold more power than I had thought.  It does not matter though, you are not the only being with magic.' % (monster['Name']))
            print('')
            time.sleep(1)
            print('(%s is healing)' % (monster['Name']))
            time.sleep(1.5)
            monster['Health'] = monster['Health'] + monster_heal()
            print('')
            print('%s: %d' % (player['Name'], player['Health']))
            print('%s: %d' % (monster['Name'], monster['Health'])) 
            print(' ')
            time.sleep(2)
    
    elif player_choice == '3':
        print('')
        print('%s: Its risky, but I cant let him defeat me!!' % (player['Name']))
        print('')
        time.sleep(1)
        print('(%s goes in for a DEVESTATING ATTACK)' % player['Name'])
        print('')
        time.sleep(2)
        monster['Health'] = monster['Health'] - player_spec_atk()
        print('')
        print('%s: %d' % (player['Name'], player['Health']))
        print('%s: %d' % (monster['Name'], monster['Health']))
        print(' ')
        time.sleep(1)
        if player_spec_atk() == 0:
            print('(The attack missed %s)' % (monster['Name']))
        elif player_spec_atk() in range(50, 61):
            print('(%s UNLEASHED A CRITICAL HIT)' % (player['Name']))
            if monster['Health'] <= 0:
                player_won = True
            
        if monster['Health'] > 25:
            print('%s is making his move!' % (monster['Name']))
            print(' ')
            time.sleep(2)
            player['Health'] = player['Health'] - monster_attack()
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
            player['Health'] = player['Health'] - monster['Special_attack']
            print('')
            print('%s: %d' % (player['Name'], player['Health']))
            print('%s: %d' % (monster['Name'], monster['Health']))
            print(' ')
            time.sleep(2)
            if player['Health'] <= 0:
                monster_won = True
        elif monster['Health'] <= 15:
            print('%s: You hold more power than I had thought.  It does not matter though, you are not the only being with magic.' % (monster['Name']))
            print('')
            time.sleep(1)
            print('(%s is healing)' % (monster['Name']))
            time.sleep(1.5)
            monster['Health'] = monster['Health'] + monster_heal()
            print('')
            print('%s: %d' % (player['Name'], player['Health']))
            print('%s: %d' % (monster['Name'], monster['Health'])) 
            print(' ')
            time.sleep(2)

    elif player_choice == '4':
        print('%s: %s is more powerful than I thought, I need to risk using this unstable magic if I am going to defeat him.' % (player['Name'], monster['Name']))
        print('')
        time.sleep(2)
        player['Health'] = player['Health'] + player_spec_heal()
        print('%s: %d' % (player['Name'], player['Health']))
        print('%s: %d' % (monster['Name'], monster['Health']))
        print('')
        if player_spec_heal() in range(0, 15):
            print('%s: I was hoping for more, but this will have to work.' % (player['Name']))
        elif player_spec_heal() in range(59, 81):
            print('%s: IT WORKED!!  I FEEL RENEWED!!' % player['Name'])
        if monster['Health'] > 25:
            print('%s: Do you really think your magic will save you!!' % (monster['Name']))
            print(' ')
            time.sleep(2)
            player['Health'] = player['Health'] - monster_spec_atk()
            print('')
            print('%s: %d' % (player['Name'], player['Health']))
            print('%s: %d' % (monster['Name'], monster['Health']))
            print(' ')
            time.sleep(2)
            if player['Health'] <= 0:
                monster_won = True
        elif monster['Health'] in range(16, 25):
            print('%s: Your healing magic cannot save you %s.  Today, you entered your last battle.' % (monster['Name'], player['Name']))
            print(' ')
            time.sleep(3)
            player['Health'] = player['Health'] - monster_attack()
            print('')
            print('%s: %d' % (player['Name'], player['Health']))
            print('%s: %d' % (monster['Name'], monster['Health']))
            print(' ')
            time.sleep(2)
            if player['Health'] <= 0:
                monster_won = True
        elif monster['Health'] <= 15:
            print('%s: You hold more power than I had thought.  It does not matter though, you are not the only being with magic.' % (monster['Name']))
            print('')
            time.sleep(1)
            print('(%s is healing)' % (monster['Name']))
            time.sleep(1.5)
            monster['Health'] = monster['Health'] + monster_heal()
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