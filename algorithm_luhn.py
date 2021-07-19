
def luhn(card_num):
    empty_list = []
    for i in range(len(card_num)):
        if i%2==0:
            num = int(card_num[i])
            if num*2<=9:
                empty_list.append(num * 2)
            else:
                num = num * 2
                empty_list.append(num // 10 + num % 10)
        else:
            num = int(card_num[i])
            empty_list.append(num)
    if sum(empty_list)%10==0:
        print("Yeeees! Your card number is valid!")
    else:
        print("Sorry, the card number you entered is invalid")

card = input("Enter your card number: ")
luhn(card)