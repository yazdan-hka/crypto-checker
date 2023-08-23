import winsound
from bs4 import BeautifulSoup
import requests
import datetime
import time


inputs = []


def keys():

    print('to close the program, type <exit>\n'
          'to go to the menu, type <menu>\n'
          'to see the keys, type <key>\n'
          'to read the words you entered, enter <inputs>\n')

    i = input('so, what are you about to do?\n>')

    input_checkup(i)


def input_checkup(inp):

    inputs.append(inp)

    if inp == 'inputs':

        for input1 in inputs:

            print(input1)

        i = input('anything else?\ny/n\n>')

        if i == 'y':
            start()

        elif i == 'n':

            input('come to see me again :)')
            exit()

        else:
            input_checkup(i)

    if inp == 'exit':
        exit()

    if inp == 'menu':
        start()

    if inp == 'key':
        keys()


def start():

    print('\nhello, user!\n')

    print('\nchoose what do you want to do:\n')

    i = input(f'1. check a crypto price\n'
              f'2. see the top growing currencies in the moment\n'
              f'3. set a price alert for the chosen crypto\n>')

    input_checkup(i)

    print('remember below keys:\n')
    print('to close the program, enter <exit>\n'
          'to go to the menu, enter <menu>\n'
          'to see the keys, enter <key>\n'
          'to read the words you entered, enter <inputs>\n')

    if i == '1':

        crypto_info(input('enter the crypto name:\n>'))

    elif i == '2':

        top_currencies()

    elif i == '3':

        price_alert()


def crypto_info(crp):

    input_checkup(crp)

    link = requests.get(f'https://www.coingecko.com/en/coins/{crp}')
    html = link.text
    soup = BeautifulSoup(html, 'lxml')

    price = soup.find('span', class_='no-wrap')
    highest = soup.find('div', class_="tw-text-gray-900 dark:tw-text-white tw-font-medium tw-col-span-1 tw-text-right")
    highest = highest.find('span', class_="no-wrap")
    lowest = soup.find('div', class_="tw-text-gray-900 dark:tw-text-white tw-font-medium tw-col-span-1")
    lowest = lowest.find('span', class_="no-wrap")

    if price is None:

        input('error! the crypto is not found or the name was incorrect. please hit enter and try again.')

        crypto_info(input('enter the crypto name:\n>'))

    elif lowest is None:

        input('error! the crypto is not found or the name was incorrect. please hit enter and try again.')

        crypto_info(input('enter the crypto name:\n>'))

    elif highest is None:

        input('error! the crypto is not found or the name was incorrect. please hit enter and try again.')

        crypto_info(input('enter the crypto name:\n>'))

    else:

        print(f'The price of {crp} in the moment is: {price.text}\n\n'
              f'the highest price of {crp} in last 24h is:______ {highest.text}\n'
              f'the lowest price of {crp} in last 24h is:_______ {lowest.text}\n')

    i = input('what else you wish to do?\nexit,menu,key,inputs\n>')

    input_checkup(i)


def top_currencies():

    did = input("enter the number of coins you wish to see\n>")

    input_checkup(did)

    bib = 0
    arz_names = ['none']

    print('please wait!\ncollecting information...\n')

    link_info = requests.get('https://www.coingecko.com/').text
    soup = BeautifulSoup(link_info, 'lxml')

    print('a little more...')

    radif_ha = soup.find_all('tr')

    for radif in radif_ha:

        num = radif.find('td', class_="table-number tw-text-left text-xs cg-sticky-co"
                                      "l cg-sticky-second-col tw-max-w-14 lg:tw-w-14")
        name = radif.find('a', class_="tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between")
        short_name = radif.find('a', class_="d-lg-none font-bold tw-w-12")
        price = radif.find('span', class_="no-wrap")
        change_24h = radif.find('span', class_="text-danger")

        if change_24h is None:
            change_24h = radif.find('span', class_="text-green")

        if num is None:

            pass
            print("#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_")

        elif name is None:

            print('error! this currency have false information [name]. go on on the list:\n'
                  'or you can check link below for more information')

            bib = bib + 1

        elif short_name is None:

            print('error! this currency have false information [short_name]. go on on the list:\n'
                  'or you can check link below for more information')

            bib = bib + 1

        elif price is None:

            print('error! this currency have false information [price]. go on on the list:\n'
                  'or you can check link below for more information')

            bib = bib + 1

        elif change_24h is None:

            print('error! this currency have false information [price]. go on on the list:\n'
                  'or you can check link below for more information')

            bib = bib + 1

        else:

            num = num.text.strip()
            name = name.text.strip()
            short_name = short_name.text.strip()
            price = price.text.strip()
            change_24h = change_24h.text.strip()

            while len(name) <= 25:
                name = name + "_"

            while len(short_name) <= 5:
                short_name = short_name + "_"

            while len(num) <= 3:
                num = num + "_"

            while len(price) <= 15:
                price = price + "_"

            print(f'{num}{name} {short_name}  {price} last 24h change: {change_24h}')

            bib = bib + 1

            name = name.replace('_', '')
            name = name.replace(' ', '-')
            name = name.lower()

            arz_names.append(name)

            if int(did) <= bib:
                break

    suggestion = input('would you like to check more info on a specific currency?\ny/n\n>')

    input_checkup(suggestion)

    if suggestion == 'y':

        index_arz_names = input('enter the number of it:\n>')
        input_checkup(index_arz_names)
        crypto_info(arz_names[int(index_arz_names)])

    elif suggestion == 'n':

        i = input('ok, feel free to close me ;)')

        input_checkup(i)


def price_alert():

    crp_name = input('enter the name of currency:\n>')

    input_checkup(crp_name)

    print('collecting information...')

    link = requests.get(f'https://www.coingecko.com/en/coins/{crp_name}')
    html = link.text
    soup = BeautifulSoup(html, 'lxml')

    price = soup.find('span', class_='no-wrap')

    if price is None:

        i = input('error! the crypto is not found or the name was incorrect. please hit enter and try again.')

        input_checkup(i)

        price_alert()

    start_price = price.text

    print(f'the price of {crp_name} is: {price.text}\n')

    set_price = input('enter the warn price:\n>')

    input_checkup(set_price)

    price = price.text.replace('$', '').replace(',', '')
    price = float(price)
    set_price = float(set_price)
    alert = False
    tries = 0
    wait = 50
    start_time = datetime.datetime.now()

    if set_price < price:

        print(f'recheck every {wait} seconds.')

        while alert is False:

            link = requests.get(f'https://www.coingecko.com/en/coins/{crp_name}')
            html = link.text
            soup = BeautifulSoup(html, 'lxml')

            time.sleep(wait)

            price = soup.find('span', class_='no-wrap')

            if price is None:

                i = input('error! the crypto is not found or the name was incorrect. please hit enter and try again.')

                input_checkup(i)

                price_alert()

            price = price.text.replace('$', '').replace(',', '')

            price = float(price)
            set_price = float(set_price)

            if price <= set_price:

                alert = True

            tries = tries + 1
            space_between = price - set_price

            print(f'try: {tries}, price: {price}, space between: {space_between}')

    elif set_price > price:

        print(f'recheck every {wait} seconds.')

        while alert is False:

            link = requests.get(f'https://www.coingecko.com/en/coins/{crp_name}')
            html = link.text
            soup = BeautifulSoup(html, 'lxml')

            time.sleep(wait)

            price = soup.find('span', class_='no-wrap')

            if price is None:

                i = input('error! the crypto is not found or the name was incorrect. please hit enter and try again.')

                input_checkup(i)

                price_alert()

            price = price.text.replace('$', '').replace(',', '')

            price = float(price)
            set_price = float(set_price)

            if price >= set_price:

                alert = True

            tries = tries + 1
            space_between = set_price - price

            print(f'try: {tries}, price: {price}, space between: {space_between}')

        if alert is True:

            alert_time = datetime.datetime.now()

            with open(f'alert/{crp_name}_{tries}th.txt', 'w') as f:

                f.write(f'checking started at: {start_time}\n'
                        f'the price was {start_price}\n\n'
                        f'the {crp_name}, reached or go over {set_price} in value of<{price}>, at {alert_time}'
                        f'\nyour inputs were: {inputs}'
                        f'\n\nhope you noticed in time!\n\n'
                        f'<3')

            ol = 9999
            el = 9999
            snd = ol * el
            i = '1'

            while i == '1':

                winsound.Beep(10000, snd)

