import argparse
from weather import get_weather


parser = argparse.ArgumentParser()

parser.add_argument('-c', '--city', metavar='city', required=True, help='the city to print weather of')
parser.add_argument('-a', '--appid', metavar='appid', required=True, help='the apy key to communicate with openweathermap api')

args = parser.parse_args()

print("Hello, Iguazio")

get_weather(args.city, args.appid)