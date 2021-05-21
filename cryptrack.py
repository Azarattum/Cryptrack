import signal
import requests
from tabulate import tabulate
from config import API_KEY
from fuzzywuzzy.fuzz import partial_ratio
import curses
import re


def convert(data_point):
    return {
        "Token": data_point["symbol"],
        "Name": data_point["name"],
        "Market Cap (USD)": "{:,}".format(round(data_point["quote"]["USD"]["market_cap"])),
        "Price (USD)": data_point["quote"]["USD"]["price"]
    }


def fetch_data():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
        "X-CMC_PRO_API_KEY": API_KEY
    }

    data = requests.get(url, {
        "start": 1,
        "convert": "USD"
    }, headers=headers).json()

    if not "data" in data:
        return None

    return list(map(convert, data["data"]))


def render(screen, data, search=""):
    lines, _ = screen.getmaxyx()

    screen.erase()
    screen.addstr(" > {}".format(search))
    pos = screen.getyx()

    screen.addstr("\n")
    screen.addstr(tabulate(data[:lines-3], headers="keys"))

    screen.move(pos[0], pos[1])
    screen.refresh()


def interactive():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.addstr("Loading...")
    stdscr.refresh()

    data = fetch_data()
    found = data
    search = ""

    while 1:
        render(stdscr, found, search)
        c = chr(stdscr.getch())
        if c == "\x1b":
            break
        elif c == "\n":
            search = ""
        elif ord(c) == 127 or c == "\b":
            search = search[:-1]
        elif re.match("[A-Za-z0-9.]| ", c):
            search += c

        found = sorted(data, key=lambda x: partial_ratio(
            search.lower(), x["Name"].lower()), reverse=True)

    curses.endwin()


def signal_handler(signal, frame):
    curses.endwin()
    exit()


def main():
    signal.signal(signal.SIGINT, signal_handler)
    interactive()


if __name__ == "__main__":
    main()
