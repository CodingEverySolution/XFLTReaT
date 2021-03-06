# MIT License

# Copyright (c) 2017 Balazs Bucsay

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# this file is placeholder, most probably the structure of the checks will
# change. So do not count on this file please.

import sys

if "checks.py" in sys.argv[0]:
	print("[-] Instead of poking around just try: python xfltreat.py --help")
	sys.exit(-1)

import struct
import random

class Checks():
	def __init__(self):
		return

	# generating challenge and saving the solution in the return values
	def check_default_generate_challenge(self):
		number1 = random.randint(0, 4294967295)
		number2 = random.randint(0, 4294967295)
		number3 = number1 ^ number2

		return (struct.pack(">II", number1, number2), struct.pack(">I", number3))

	# calculate result for challenge
	def check_default_calculate_challenge(self, challenge):
		numbers = struct.unpack(">II", challenge)
		return struct.pack(">I", numbers[0] ^ numbers[1])