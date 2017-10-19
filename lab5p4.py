def main():
    inputString = str(input("Enter your Blackjack hand: "))
    blackJackScore(inputString)

def blackJackScore(iS):
    aces = 0
    score = 0
    for x in range(len(iS)):
        if (iS[x] == "A"):
            score += 11
            aces += 1
        elif (iS[x] in "TJQK"):
            score += 10
        else:
            score += int(iS[x])
    while score > 21 and aces > 0:
        aces -= 1
        score -= 10
    if score > 21:
        print("Bust!")
    else:
        print("Your hand value is: ", score)

main()
