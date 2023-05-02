# SUI KuCoin Seller Script by [nftscripts]( https://github.com/nftscripts "nftscripts"), ReadMe by VikVM
![](https://play-lh.googleusercontent.com/ovFbGElmfBf5gqcNhKLDkNIMMf_54hJ02G6lNTQFYsmK4rqwBjKrbl24RiAPOLiVkdk) ![](https://www.block-chain24.com/sites/default/files/crypto/sui_sui_coin_icon_256x256.svg)
![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/KUCOIN.svg/1200px-KUCOIN.svg.png)
------------

## This Python script will place a sell limit order for a target price as soon the best buy bid is reached the target price against USDT.

Supports proxy
> Readme By Https://Github.Com/Vikvm, more alpha at Russian here: Https://T.Me/Degenovosti, script is safe for use, verified by me

## Script Launch:
### 1) Download the repo and unpack it

------------


### 2) Configure accounts.json 
Fill in the accounts.json file with your creditentials

#### Name 
Up to you for your understanding

#### API Key
Get it here https://www.kucoin.com/account/api

#### API Secret
Generated when the API Key is created

#### API Passphrase
Refers to the one you used to create the KuCoin API.

#### Proxy
Use it if you want

#### Multiaccount Feature
If you have more than 1 account, then add the following for each account 

```
{
      "name": "",
      "api_key": "",
      "api_secret": "",
      "api_passphrase": "",
      "proxy": null
    }
   ````
    
#### Example code for 2 accounts:
```
{
  "accounts": [
    {
      "name": "",
      "api_key": "",
      "api_secret": "",
      "api_passphrase": "",
      "proxy": null
    },
    {
      "name": "",
      "api_key": "",
      "api_secret": "",
      "api_passphrase": "",
      "proxy": null
    }
  ]
}
````

------------


### 3) Configure config.py
Edit config.py to set the order placement time and a minimal price.
Script will check what is the best bid to buy and if the best bid is higher than a setted minimal price then script will place a sell order

#### MIN PRICE
Treshold price to place an order, price per base currency e.g. 0.01 (USDT)

#### COEFFICIENT
Edit if you want to place an order in advance or after the best bid is higher than a MIN PRICE

#### CorrectionCorrection
Use it if the time is lagging

------------


#### 4) Run The Script In Advance Before A Sale

------------


#### 5) Good luck KINGS

![](https://www.nicepng.com/png/full/831-8318812_view-samegoogleiqdbsaucenao-based-pepe-in-a-tuxedo.png)
