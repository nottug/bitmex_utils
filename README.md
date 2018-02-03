# bitmex_utils 

Utility scripts for BitMEX Derivatives Exchange

## Liquidation Calculator

The code is a little bit buggy but the formulas were provided from BitMEX support. The prices are off usually off by less than a dollar, don't think this is resolvable.

### The formulas are:

#### Long:

```
Bankrupt = avg_entry_price / (1 + initial_margin)
Liquidation = bankrupt + (avg_entry_price * (maintenance_margin + funding_rate)
```

#### Short:

```
Bankrupt = avg_entry_price / (1 - initial_margin)
Liquidation = bankrupt - (avg_entry_price * (maintenance_margin - funding_rate)
```






#### For margin calculations:
```
initial_margin = (1 / leverage) - taker_fee - taker_fee
maintenance_margin = 0.05% * taker_fee
```
For XBTUSD the taker fee is 0.075%.


### Code 

```python
from liquidation import Liquidation
liq = Liquidation()

# Buy 1000 contracts at $10,0000 with 10x leverage
liq.calc_buy(10000, 1000, 10, 0.000375)

# Sell 1000 contracts at $10,0000 with 10x leverage
liq.calc_sell(10000, 1000, 10, 0.000375)
```

