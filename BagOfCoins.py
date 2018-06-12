from __future__ import division

class FlipPredictor(object):
	
	def __init__(self,coins):
		self.coins = coins
		n = len(coins)
		self.probs = [1/n]*n

	def PHeads(self):
		return sum(eachHeads*eachCoin for eachHeads,eachCoin in zip(self.probs,self.coins))

	def update(self,result):
		probHeads = self.PHeads()
		if result == 'H':
			self.probs = [eachHeads*eachCoin/probHeads for eachHeads,eachCoin in zip(self.probs,self.coins)]
		elif result == 'T':
			self.probs = [(1-eachHeads)*eachCoin/(1-probHeads) for eachHeads,eachCoin in zip(self.probs,self.coins)]

def test(coins,flips):
	f=FlipPredictor(coins)
	guesses = []
	for flip in flips:
		f.update(flip)
		guesses.append(f.PHeads())
	return guesses

n = int(input('Enter The Number of Coins: '))
print test([float(input('Enter Probability for Coin ' + str(i+1) + ': ')) for i in range(0,n)],str(input('Enter Flips: ')))