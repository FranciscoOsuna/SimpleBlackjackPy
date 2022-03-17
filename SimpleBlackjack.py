from random import sample
from os import system


def main():
    while True:
        system('cls')
        print('Uproszczona gra na podstawie BlackJack\n'
              'Twórca: Francisco Osuna')
        money = 1000
        while money > 0:
            print('-' * 30)
            print('Saldo: ' + str(money))
            deck = shuffle()
            print('wpisz ile chcesz postawić')
            placed = 0
            while not placed:
                try:
                    bet = int(input('> '))
                except ValueError:
                    print('wpisz liczbę')
                else:
                    if money >= bet > 0:
                        money -= bet
                        win = game(deck, bet)
                        if win == 'win':
                            money += 2 * bet
                        elif win == 'tie':
                            money += bet
                        placed = 1
                    else:
                        print('Nie możesz tyle postawić')

        print('Skończyły ci się pieniądze :c')
        print('[dowolny klawisz + Enter - zagraj jeszcze raz] [Enter - wyjdż]')
        if not input('> '):
            break


def draw_card(card):
    if len(card) == 2:
        return ('┌──────┐\n'
                '|      |\n'
                '|  {}  |\n'
                '|      |\n'
                '└──────┘'.format(card))
    else:
        return ('┌──────┐\n'
                '|      |\n'
                '| {}  |\n'
                '|      |\n'
                '└──────┘'.format(card))


def get_score(li):
    global cards
    out = 0
    for n in li:
        out += cards[n]
    return out


def shuffle():
    return sample(list(cards), 52)


def game(deck, bet):
    win = 0
    dealer = []
    player = []
    dealer.append(deck.pop())
    player.append(deck.pop())
    dealer.append(deck.pop())
    player.append(deck.pop())
    playing = 1
    while playing:
        player_score = get_score(player)
        dealer_score = get_score(dealer)
        system('cls')
        print('-' * 30)
        print('Stawka:' + str(bet))
        print('-' * 30)
        print('-----Karty Krupiera----')
        print(draw_card(dealer[0]))
        print(draw_card('??'))
        print('-' * 30)
        print('-----Karty Twoje----')
        n = 0
        for _ in player:
            print(draw_card(player[n]))
            n += 1
        print('-' * 30)
        print('Suma twoich kart: {}'.format(str(player_score)))
        print('-' * 30)
        if player_score > 21:
            print('Przegrałeś rundę :c')
            break
        print('[H/h - hit] [S/s - stand]')
        choice = 'f'
        while choice not in 'HhSs':
            choice = input('> ')
            if choice in 'Hh':
                player.append(deck.pop())
            elif choice in 'Ss':
                if dealer_score > 17 and player_score <= dealer_score:
                    dealer_score = get_score(dealer)
                    system('cls')
                    print('-' * 30)
                    print('Stawka:' + str(bet))
                    print('-' * 30)
                    print('-----Karty Krupiera----')
                    print(draw_card(dealer[0]))
                    print(draw_card('??'))
                    print('-----Karty Twoje----')
                    n = 0
                    for _ in player:
                        print(draw_card(player[n]))
                        n += 1
                    print('-' * 30)
                    n = 0
                    print('Suma twoich kart: {}'.format(str(player_score)))
                    print('-' * 30)
                    for _ in dealer:
                        print(draw_card(dealer[n]))
                        n += 1
                    print('-' * 30)
                    print('Suma kart dilera: {}'.format(str(dealer_score)))
                while dealer_score <= 17:
                    dealer.append(deck.pop())
                    dealer_score = get_score(dealer)
                    system('cls')
                    print('-' * 30)
                    print('Stawka:' + str(bet))
                    print('-' * 30)
                    print('-----Karty Krupiera----')
                    print(draw_card(dealer[0]))
                    print(draw_card('??'))
                    print('-' * 30)
                    print('-----Karty Twoje----')
                    n = 0
                    for _ in player:
                        print(draw_card(player[n]))
                        n += 1
                    print('-' * 30)
                    n = 0
                    print('Suma twoich kart: {}'.format(str(player_score)))
                    print('-' * 30)
                    for _ in dealer:
                        print(draw_card(dealer[n]))
                        n += 1
                    print('-' * 30)
                    print('Suma kart dilera: {}'.format(str(dealer_score)))
                if (dealer_score > 21) or (player_score > dealer_score):
                    print('Wygrałeś rundę')
                    return 'win'
                elif dealer_score == player_score:
                    print('Zremisowałeś rundę')
                    return 'tie'
                else:
                    print('Przegrałeś rundę')

                playing = 0


cards = {'1♣': 1, '2♣': 2, '3♣': 3, '4♣': 4, '5♣': 5, '6♣': 6, '7♣': 7,
         '8♣': 8, '9♣': 9, '10♣': 10, 'J♣': 10, 'K♣': 10, 'A♣': 1,
         '1♤': 1, '2♤': 2, '3♤': 3, '4♤': 4, '5♤': 5, '6♤': 6, '7♤': 7,
         '8♤': 8, '9♤': 9, '10♤': 10, 'J♤': 10, 'K♤': 10, 'A♤': 1,
         '1♥': 1, '2♥': 2, '3♥': 3, '4♥': 4, '5♥': 5, '6♥': 6, '7♥': 7,
         '8♥': 8, '9♥': 9, '10♥': 10, 'J♥': 10, 'K♥': 10, 'A♥': 1,
         '1♦': 1, '2♦': 2, '3♦': 3, '4♦': 4, '5♦': 5, '6♦': 6, '7♦': 7,
         '8♦': 8, '9♦': 9, '10♦': 10, 'J♦': 10, 'K♦': 10, 'A♦': 1}


main()
