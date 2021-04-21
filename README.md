# Cryptrack
Simple TUI crypto tracking tool with fuzzy search.

## Features:
  - Shows current price
  - Shows market cap
  - Fuzzy search for any currency

## Installation: 
Clone the repo and install the dependencies:
```sh
git clone https://github.com/Azarattum/Cryptrack.git
cd Cryptrack
pip install -r requirements.txt
```

Put your [api key](https://pro.coinmarketcap.com/pricing) in `config.py`:
```python
#Example of a key
API_KEY = "b2511a42-ffd3-410f-b2e9-a4170dcb830d"
```

## Usage:
Run the script
```sh
python cryptrack.py
```

Sample output:
```
 > bit
Token    Name             Market Cap (USD)       Price (USD)
-------  ---------------  ------------------  --------------
BTC      Bitcoin          1,036,628,289,878   55472.1
BCH      Bitcoin Cash     17,909,925,339        957.015
WBTC     Wrapped Bitcoin  8,553,019,789       55597.8
BSV      Bitcoin SV       5,685,954,839         303.88
BTT      BitTorrent       5,269,169,850           0.00798416
BTCB     Bitcoin BEP2     3,031,789,710       55529.3
BTG      Bitcoin Gold     1,649,286,995          94.17
BNB      Binance Coin     90,953,459,929        592.79
```