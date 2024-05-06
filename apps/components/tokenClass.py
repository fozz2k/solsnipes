# Base token class for filter.py
class Token:
    def __init__(self, name, symbol, liquidity, mc, v24hChangePercent, v24hUSD):
        self.name = name
        self.symbol = symbol
        self.liquidity = liquidity
        self.mc = mc
        self.v24hChangePercent = v24hChangePercent
        self.v24hUSD = v24hUSD
class FullToken(Token):
    def __init__(self, address, decimals, lastTradeUnixTime, logoURI, name, symbol, mc, liquidity, v24hChangePercent, v24hUSD):
        # Initialize attributes specific to FullToken
        self.address = address
        self.decimals = decimals
        self.lastTradeUnixTime = lastTradeUnixTime
        self.logoURI = logoURI
        
        # Call the __init__ of the base class (Token) to initialize common attributes
        super().__init__(name, symbol, mc, liquidity, v24hChangePercent, v24hUSD)

    def __str__(self):
        return f"{self.name} ({self.symbol}) - Address: {self.address}"

    def __repr__(self):
        return f"{self.name} ({self.symbol}) - Address: {self.address}"
    
class CoinrankingToken:
    def __init__(self, name, symbol, price, market_cap, change, volume, tier, uuid):
        self.name = name
        self.symbol = symbol
        self.price = price
        self.market_cap = market_cap
        self.change = change
        self.volume = volume
        self.tier = tier
        self.uuid = uuid