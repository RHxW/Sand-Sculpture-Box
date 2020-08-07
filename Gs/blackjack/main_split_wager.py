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
    w_level = int(input("wager level: "))
    tokens = int(input("your tokens: "))
    while True:
        if tokens <= 0:
            print("YOU ARE BROKEN!")
            exit(0)
        tokens -= w_level
        print("-" * 50)
        print("New Game:")
        print("\tTotal score: dealer-%d, player-%d" % (ds, ps))
        print("\tPlayer token: %d" % tokens)
        # deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        if len(deck) < 20:
            print("             === NEW DECK ===              ")
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 8
        random.shuffle(deck)
        d_cards = []
        p_cards = [[]]
        # player init
        p_cards[0].append(deck.pop(0))
        p_cards[0].append(deck.pop(0))
        hands_count = 1
        # split
        print("Player's cards: ", p_cards[0], "\tplayer's score: %s" % str(card_score(p_cards[0])))
        if p_cards[0][0] == p_cards[0][1]:
            if tokens >= w_level:
                k = int(input("Do you want to split your cards? 1: Yes, 2: No"))
                if k == 1:
                    print("Cards splited!")
                    hands_count += 1
                    tokens -= w_level
                    p_cards.append([p_cards[0].pop(0)])
                    p_cards[0].append(deck.pop(0))
                    p_cards[1].append(deck.pop(0))

        # p_stat: list -1: busted, 0: neutral, 1: black jack
        if len(p_cards) > 1:
            p_score = []
            p_stat = [0 for _ in range(len(p_cards))]
            for i in range(len(p_cards)):
                p_score.append(card_score(p_cards[i]))
                print("Player's cards_%d: " % (i + 1), p_cards[i], "\tplayer's score_%d: %s" % (i + 1, str(p_score[i])))
                if p_score[i][0] > 21:
                    print("******Player's card %d Busted !******" % (i+1))
                    p_stat[i] = -1
                    ds += 1
                elif 21 in p_score[i]:
                    print("******Player's card %d Black Jack !******" % (i + 1))
                    tokens += w_level * 2
                    p_stat[i] = 1
                    ps += 1
            # if 0 not in p_stat:
            #     k = int(input("1: Continue, 2: Quit"))
            #     if k == 1:
            #         continue
            #     else:
            #         exit(0)
        else:
            p_stat = [0]
            p_score = [card_score(p_cards[0])]
            # print("Player's cards: ", p_cards[0], "\tplayer's score: %s" % str(p_score[0]))
            if p_score[0][0] > 21:
                print("*************You are BUSTED !*************\n Dealer Wins !!")
                p_stat[0] = -1
                ds += 1
                # k = int(input("1: Continue, 2: Quit"))
                # if k == 1:
                #     continue
                # else:
                #     exit(0)
            elif 21 in p_score[0]:
                print("*************Black Jack !*************\n Player Wins !!")
                tokens += w_level * 2
                p_stat[0] = 1
                ps += 1
        if 0 not in p_stat:
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

        restart = False
        for i in range(len(p_cards)):
            if p_stat[i] == -1:
                print("Player's cards_%d: " % (i + 1), p_cards[i], "\tplayer's score_%d: %s" % (i + 1, str(p_score[i])), "  BUSTED!")
                continue
            elif p_stat[i] == 1:
                print("Player's cards_%d: " % (i + 1), p_cards[i],
                      "\tplayer's score_%d: %s" % (i + 1, str(p_score[i])), "  Black Jack!")
                continue

            print("Player's cards_%d: " % (i + 1), p_cards[i], "\tplayer's score_%d: %s" % (i + 1, str(p_score[i])))
            while True:
                k = int(input("Choices: 1: Hit, 2: Stand, 3: Quit"))
                if k == 1:
                    p_cards[i].append(deck.pop(0))
                    p_score[i] = card_score(p_cards[i])
                    print("Player's cards_%d: " % (i + 1), p_cards[i],
                          "\tplayer's score_%d: %s" % (i + 1, str(p_score[i])))
                    if p_score[i][0] > 21:
                        if len(p_cards) > 1:
                            print("******Player's card %d Busted !******" % (i + 1))
                        else:
                            print("*************You are BUSTED !*************\n Dealer Wins !!")
                        p_stat[i] = -1
                        ds += 1
                        break
                        # k = int(input("1: Continue, 2: Quit"))
                        # if k == 1:
                        #     break
                        # else:
                        #     exit(0)
                    elif 21 in p_score[i]:
                        if len(p_cards) > 1:
                            print("******Player's card %d Black Jack !******" % (i + 1))
                        else:
                            print("*************Black Jack !*************\n Player Wins !!")
                        tokens += w_level * 2
                        p_stat[i] = 1
                        ps += 1
                        break
                        # k = int(input("1: Continue, 2: Quit"))
                        # if k == 1:
                        #     break
                        # else:
                        #     exit(0)
                    else:
                        continue

                elif k == 2:
                    break
                else:
                    exit(0)
            if 0 not in p_stat:  # TODO Quit?
                k = int(input("1: Continue, 2: Quit"))
                if k == 1:
                    restart = True
                    break
                else:
                    exit(0)
        if restart:
            continue

        print("+++++++++++++++Results+++++++++++++++")
        d_score = card_score(d_cards)
        print("Dealer's cards: ", d_cards, "\tdealer's score: %s" % str(d_score))
        if d_score[0] > 21:
            print("*************Dealer is BUSTED !*************\n Player Wins !!")
            tokens += w_level * hands_count
            ps += 1
        elif d_score[0] == 21:
            print("*************Black Jack !*************\n Dealer Wins !!")
            ds += 1
        else:
            d_score_ = []
            for _ in d_score:
                if _ <= 21:
                    d_score_.append(_)
            d_score_.sort()
            while d_score_ and d_score_[-1] < 17:
                d_cards.append(deck.pop(0))
                d_score = card_score(d_cards)
                d_score_ = []
                for _ in d_score:
                    if _ <= 21:
                        d_score_.append(_)
                d_score_.sort()
                print("Dealer's cards: ", d_cards, "\tdealer's score: %s" % str(d_score))
                time.sleep(0.5)
            if d_score[0] > 21:
                print("*************Dealer is BUSTED !*************\n Player Wins !!")
                tokens += w_level * hands_count * 2
                ps += max(p_stat.count(0), 1)
            elif 21 in d_score:
                print("*************Black Jack !*************\n Dealer Wins !!")
                ds += 1
            else:
                d_s = d_score[0]
                for _ in d_score[1:]:
                    if _ > d_s and _ <= 21:
                        d_s = _
                for i in range(len(p_cards)):
                    if p_stat[i] == -1:
                        print("Player's cards_%d: " % (i + 1), p_cards[i],
                              "\tplayer's score_%d: %s" % (i + 1, str(p_score[i])), "  BUSTED!")
                        continue
                    elif p_stat[i] == 1:
                        print("Player's cards_%d: " % (i + 1), p_cards[i],
                              "\tplayer's score_%d: %s" % (i + 1, str(p_score[i])), "  Black Jack!")
                        continue
                    else:
                        print("Player's cards_%d: " % (i + 1), p_cards[i],
                              "\tplayer's score_%d: %s" % (i + 1, str(p_score[i])))


                    p_s = p_score[i][0]
                    for _ in p_score[i][1:]:
                        if _ > p_s and _ <= 21:
                            p_s = _
                    if d_s > p_s:
                        print("***********************Dealer Wins !!******************")
                        ds += 1
                    elif d_s == p_s:
                        print("********************There is tie !!**************************")
                        tokens += w_level
                    else:
                        print("***********************Player Wins !!******************")
                        tokens += w_level * hands_count * 2
                        ps += 1
        k = int(input("1: Continue, 2: Quit"))
        if k == 1:
            continue
        else:
            exit(0)


if __name__ == "__main__":
    main()
