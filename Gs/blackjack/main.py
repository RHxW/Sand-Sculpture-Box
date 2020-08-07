import random
import time


def card_score(cards: list):
    if not cards:
        return [0]
    s = sum(cards)
    if s == 21:
        return [21]
    if 11 in cards:
        c = cards.count(11)
        s -= 10 * c
        ret = [s]
        for i in range(1, c + 1):
            # if s + 10*i > 21:
            #     continue
            ret.append(s + 10 * i)
        ret.sort()
        return ret
    return [s]


def main():
    print(
        "                       **********************************************************                                    ")
    print(
        "                                   Welcome to the game Casino - BLACK JACK !                                         ")
    print(
        "                       **********************************************************                                    ")
    ds = 0
    ps = 0
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 8
    random.shuffle(deck)
    while True:
        print("-" * 50)
        print("New Game:")
        print("\tTotal score: dealer-%d, player-%d" % (ds, ps))
        # deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        if len(deck) < 20:
            print("             === NEW DECK ===              ")
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 8
            random.shuffle(deck)
        d_cards = []
        p_cards = []
        # player init
        p_cards.append(deck.pop(0))
        p_cards.append(deck.pop(0))
        p_score = card_score(p_cards)
        print("Player's cards: ", p_cards, "\tplayer's score: %s" % str(p_score))
        if p_score[0] > 21:
            print("*************You are BUSTED !*************\n Dealer Wins !!")
            ds += 1
            k = int(input("1: Continue, 2: Quit"))
            if k == 1:
                continue
            else:
                exit(0)
        elif 21 in p_score:
            print("*************Black Jack !*************\n Player Wins !!")
            ps += 1
            k = int(input("1: Continue, 2: Quit"))
            if k == 1:
                continue
            else:
                exit(0)
        # if p_cards[0] == p_cards[1]:
        #     k = int(input("Do you want to split your cards? 1: Yes 2: No"))
        #     if k == 1:
        #         p_cards_1 = [p_cards[0]]
        #         p_cards_2 = [p_cards[1]]

        # dealer init
        d_cards.append(deck.pop(0))
        d_cards.append(deck.pop(0))
        d_cards_ = d_cards[1:]
        d_cards_.insert(0, "X")
        print("Dealer's cards: ", d_cards_)
        wining_flg = False
        while True:
            k = int(input("Choices: 1: Hit, 2: Stand, 3: Quit"))
            if k == 1:
                p_cards.append(deck.pop(0))
                p_score = card_score(p_cards)
                print("Player's cards: ", p_cards, "\tplayer's score: %s" % str(p_score))
                if p_score[0] > 21:
                    print("*************You are BUSTED !*************\n Dealer Wins !!")
                    wining_flg = True
                    ds += 1
                    k = int(input("1: Continue, 2: Quit"))
                    if k == 1:
                        break
                    else:
                        exit(0)
                elif 21 in p_score:
                    print("*************Black Jack !*************\n Player Wins !!")
                    wining_flg = True
                    ps += 1
                    k = int(input("1: Continue, 2: Quit"))
                    if k == 1:
                        break
                    else:
                        exit(0)
                else:
                    continue
            elif k == 2:
                break
            else:
                exit(0)
        if wining_flg is True:
            continue

        d_score = card_score(d_cards)
        print("Dealer's cards: ", d_cards, "\tdealer's score: %s" % str(d_score))
        if d_score[0] > 21:
            print("*************Dealer is BUSTED !*************\n Player Wins !!")
            ps += 1
        elif d_score[0] == 21:
            print("*************Black Jack !*************\n Dealer Wins !!")
            ds += 1
        else:
            d_s = d_score[0]
            for _ in d_score[1:]:
                if _ > d_s and _ <= 21:
                    d_s = _
            while d_s < 17:
                d_cards.append(deck.pop(0))
                d_score = card_score(d_cards)
                if d_score[0] >= 21:
                    d_s = d_score[0]
                else:
                    for _ in d_score:
                        if _ > d_s and _ <= 21:
                            d_s = _
                print(d_s)
                print("Dealer's cards: ", d_cards, "\tdealer's score: %s" % str(d_score))
                time.sleep(0.5)
            if d_score[0] > 21:
                print("*************Dealer is BUSTED !*************\n Player Wins !!")
                ps += 1
            elif 21 in d_score:
                print("*************Black Jack !*************\n Dealer Wins !!")
                ds += 1
            else:
                d_s = d_score[0]
                for _ in d_score[1:]:
                    if _ > d_s and _ <= 21:
                        d_s = _
                p_s = p_score[0]
                for _ in p_score[1:]:
                    if _ > p_s and _ <= 21:
                        p_s = _
                if d_s > p_s:
                    print("***********************Dealer Wins !!******************")
                    ds += 1
                elif d_s == p_s:
                    print("********************There is tie !!**************************")
                else:
                    print("***********************Player Wins !!******************")
                    ps += 1
        k = int(input("1: Continue, 2: Quit"))
        if k == 1:
            continue
        else:
            exit(0)


if __name__ == "__main__":
    main()
