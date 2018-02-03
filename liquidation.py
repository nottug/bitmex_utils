

class Liquidation(object):

	def __init__(self):
		self.avg_entry = 0
		self.qty = 0
		self.maker_fee = -0.00025
		self.taker_fee = 0.00075
		self.maintenance_margin = 0.005 - self.taker_fee


	def _initial_margin(self, lev):

		return (1 / lev) - self.taker_fee * 2


	def calc_buy(self, entry, qty, lev, funding_rate, new=True):

		if new:
			self.avg_entry = entry
			self.qty = qty
		else:
			ratios = [(qty / (self.qty + qty)), (self.qty / (self.qty + qty))]
			self.avg_entry = ((entry * ratios[0]) + (self.avg_entry * ratios[1]))
			self.qty += qty

		bankrupt = (self.avg_entry / (1 + self._initial_margin(lev)))
		liq = bankrupt + (self.avg_entry * (self.maintenance_margin + funding_rate))

		return liq


	def calc_sell(self, entry, qty, lev, funding_rate, new=True):

		if new:
			self.avg_entry = entry
			self.qty = qty
		else:
			ratios = [abs((qty / (self.qty + qty))), abs((self.qty / (self.qty + qty)))]
			print(sum(ratios))
			self.avg_entry = (entry * ratios[0]) + (self.avg_entry * ratios[1])
			self.qty += qty

		bankrupt = (self.avg_entry / (1 - self._initial_margin(lev)))
		liq = bankrupt - (self.avg_entry * (self.maintenance_margin - funding_rate))

		return liq


