from datetime import datetime
from pathlib import Path

""" Coin to sell """
COIN = 'SUI'

MIN_PRICE: float = 3
"""MIN_PRICE is a treshold value, if the best bid will be above, then the script will place a limit order with the last buy bid price"""
list_time = datetime(year=2023, month=5, day=3, hour=15, minute=0, second=10)

COEFFICIENT: float = 1 
""" This coeffiecient will be used to multiply the best bid price.

Use <1 to place an order in advance with a higher price, 
use >1 to place an order with a lower price than a best buy bid,
use 1 to place an order with the best buy bid price.

If 
MIN_PRICE set as 1 USD
The KuCoin best buy bid is 1 USD
Coefficient set as 1
= script will place a sell order

If 
MIN_PRICE set as 1 USD
The KuCoin best buy bid is 1 USD
Coefficient set as 1.1
= script will not place a sell order, because of the target price is 1.1 now with this multiplicator"""


correction = 0

""" time.is - website to watch time
If they lag behind = minus (how far behind) 
If they're in a hurry = (how much hurry) """

list_time = list_time.timestamp() + correction
project_root = Path(__file__).parent
