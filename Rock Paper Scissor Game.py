import random
print('ROCK PAPER SCISSOR GAME')

l = ['Rock', 'Paper', 'Scissor']

player=False

while player==False:
    comp=random.choice(l)
    play = input('Choose your option: Rock Paper Scissor ->  ')
    print('Player chose: ', play)
    print('Computer chose: ',comp)

    if comp==play:
        print('Match Drawn')
    else:
        if comp=='Rock':
            if play=='Paper':
                print('Player wins')
            else:
                print('Computer wins')
        elif comp=='Paper':
            if play=='Scissor':
                print('Player wins')
            else:
                print('Computer wins')
        elif comp=='Scissor':
            if play=='Rock':
                print('Player wins')
            else:
                print('Computer wins')
    
    ch=input('Do you wanna continue ? y/n ->')
    if ch=='n':
        player=True


            