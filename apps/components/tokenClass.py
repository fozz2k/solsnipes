class Token:
    def __init__(self, address, name, symbol, decimals, lastTradeUnixTime, liquidity, logoURI, mc, v24hChangePercent, v24hUSD):
        self.address = address
        self.name = name
        self.symbol = symbol
        self.decimals = decimals
        self.lastTradeUnixTime = lastTradeUnixTime
        self.liquidity = liquidity
        self.logoURI = logoURI
        self.mc = mc
        self.v24hChangePercent = v24hChangePercent
        self.v24hUSD = v24hUSD

    def __str__(self):
        return f"{self.name} ({self.symbol})"

    def __repr__(self):
        return f"{self.name} ({self.symbol})"