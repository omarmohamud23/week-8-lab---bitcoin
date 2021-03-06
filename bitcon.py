import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def main():
    bitcoin = get_bitcoins()
    bitcoin_rate = convert_bitcoins_to_dollars(bitcoin)
    display_results(bitcoin, bitcoin_rate)


def get_bitcoins():
    while True:
        try:
            dollars = float(input('Enter the number of coins: '))
            if dollars >= 0:
                return dollars
            else:
                print(' Please enter a number greater than 0')
        except ValueError:
            print('Enter a valid number.')


def convert__from_bitcoins_to_dollars(coins):
    exchange_rate = requests_rate(coins)
    bitcoin = math_conversion(coins, exchange_rate)
    return bitcoin


def requests_rate(rate):
    try:
        response = requests.get(url)
        data = response.json()
        dollars_exchange_rate = data['bpi']['USD']['rate_float']
        return(dollars_exchange_rate)
    except Exception as e:
        print(f'Error making request', e)


def math_conversion(coins, bitcoin_rate):
    return coins * bitcoin_rate



def display_results(bitcoin, bitcoin_rate):
    print(f'{bitcoin} bitcoins is equal to ${bitcoin_rate:.2f}')




if __name__ == '__main__':
    main()