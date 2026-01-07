def main():
    due = 50
    change = 0
    accepted_coins = [25,10,5]
    while due>0:
        print(f"Amount Due: {due}")
        coin = int(input("Insert Coin: "))
        if(coin not in accepted_coins):
            continue
        else:
            due -= coin
            if(due<0):
                change+=-due

    print(f"Change Owed: {change}")

main()
