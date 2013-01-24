#!/usr/bin/python
# training and testing data sets random generator
# Copyright (C) 2012-2013 Yuri Agafonov
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
from random import randint

class Instance(object):
	WEEKDAY = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
	OUTLOOK = ('Sunny', 'Overcast', 'Rain')
	WIND_DIRECTION = ('N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW')
	def __init__(self, training):
		random_item = lambda l:l[randint(0, len(l) - 1)]
		self.weekday = random_item(Instance.WEEKDAY)
		self.dayhour = float(randint(0, 23)) + float(randint(0, 59)) / 100.0
		self.outlook = random_item(Instance.OUTLOOK)
		self.temperature = float(randint(-30, 40))
		if self.dayhour <= 9.0 and self.temperature > 30.0:
			self.temperature = 20.0
		if self.temperature < 0.0 and self.outlook == 'Rain':
			self.outlook = 'Overcast'
		self.humidity = randint(0, 100)
		self.wind_direction = random_item(Instance.WIND_DIRECTION)
		self.wind_speed = float(randint(0, 100))
		self.training = training
		self.watch_anime = Instance.WatchAnime(self) if training else '?'
	
	def __str__(self):
		'''weekday,dayhour,outlook,temperature,humidity,wind_direction,wind_speed,watch_anime'''
		if self.training:
			return '%s,%0.2f,%s,%0.2f,%d,%s,%0.2f,%s' % (self.weekday,self.dayhour,self.outlook,self.temperature,self.humidity,self.wind_direction,self.wind_speed,'Yes' if self.watch_anime else 'No')
		else:
			return '%s,%0.2f,%s,%0.2f,%d,%s,%0.2f,?' % (self.weekday,self.dayhour,self.outlook,self.temperature,self.humidity,self.wind_direction,self.wind_speed)
	
	@staticmethod
	def WatchAnime(self):
		if self.temperature > 19.0:
			if self.dayhour <= 8.0:
				return True
		elif self.temperature < -10.0:
			if self.outlook == 'Sunny':
				return False
		if self.outlook == 'Rain' and self.weekday in ('Monday', 'Tuesday', 'Friday', 'Saturday'):
			return True
		return False

arff_header = '''@relation WhoIsWatchingAnime

@attribute weekday {Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday}
@attribute dayhour numeric
@attribute outlook {Sunny, Overcast, Rain}
@attribute temperature numeric
@attribute humidity numeric
@attribute windDirection {N, NNE, NE, ENE, E, ESE, SE, SSE, S, SSW, SW, WSW, W, WNW, NW, NNW}
@attribute windSpeed numeric
@attribute watchAnime {Yes, No}

@data
'''
def write(f, training, prediction):
	if training:
		f.write(arff_header)
		watch_anime = 0
		while watch_anime < 0xFF:
			i = Instance(True)
			watch_anime += i.watch_anime
			f.write('%s\n' % i)
	elif prediction:
		f.write(arff_header)
		for _ in xrange(0x100):
			f.write('%s\n' % Instance(True))
	else:
		for _ in xrange(0x100):
			f.write('%s\n' % Instance(False))

import sys
def main():
	if '-c' in sys.argv:
		sys.argv.remove('-c')
		assert len(sys.argv) > 2
		with open(sys.argv[1], 'rU') as finput:
			with open(sys.argv[2], 'w') as foutput:
				foutput.write(arff_header)
				for l in finput:
					foutput.write(l)
		return
	training = '-t' in sys.argv
	if training:
		sys.argv.remove('-t')
	prediction = '-p' in sys.argv
	if prediction:
		sys.argv.remove('-p')
	if len(sys.argv) > 1:
		with open(sys.argv[1], 'w') as f:
			write(f, training, prediction)
	else:
		write(sys.stdout, training, prediction)

if __name__ == '__main__':
	main()
