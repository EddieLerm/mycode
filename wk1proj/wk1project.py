#!/usr/bin/env python3

print('***THE CALL***')

a = ''
p = print

p('\nIts 1955, your 18 and a highly valued future football college prospect')
p('Your are the QB of your team, its the championship game with the score 14 to 17')
p('your team coming up short, your team has possesion of the ball on the 35 with 15 seconds left')
p('\n1.Its 5 and 3rd Your coach says to run slants for the quick pass and first down')
p('2.Your recievers have been out running the defense all day you think you can go for the long pass \nand touhdown')
p('3.Your RB is confident and says can get the first and more and is requesting the ball')
while a == '' :

    a = input('What do you do? Enter Number(enter q to quit): ')

    if a == str(1) :
        p('\nYour pass to your reciever, catching the ball and making a break for the touchdown')
        p('diving in and scoring gaining the win for your team!')

    elif a == str(2) :
        p('\nYour recievers go deep but can not get open, there is a gap in the line and you make a')
        p('break for it. Running all the way to touchdown scoring and winning the game.')

    elif a == str(3) :
        p('\nYour RB runs the ball, punching through the center breaking two tackles only')
        p('to come up short and time expiring losing the game.')

    elif a == 'q':
        p('\nQuitter')

    else:
        p('Please enter a number:')