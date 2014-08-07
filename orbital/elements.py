import string

class ElementLine(object):

	def create_checksum(self):
		""" Checksums are created by adding together all of the numbers. Add 
		another "1" for each negative sign encountered. Modulo 10. """
		check = 0
		for char in self.source[0:-1]:
			if char == "-":
				check += 1
			elif char in string.digits:
				check += string.digits.index(char)
		return str(check % 10)

	def validate(self):
		""" Validates the element-line checksum. """
		return self.checksum == self.create_checksum()


class LineOne(ElementLine):
	
	def __init__(self, source):
		self.source = source
		self.line_number = source[0:1]
		self.satellite_number = source[2:7].strip()
		self.classification = source[2]
		self.launch_year = source[9:10].strip()
		self.launch_number = source[11:13].strip()
		self.launch_piece = source[14:16].strip()
		self.epoch_year = source[18:19].strip()
		self.epoch_fraction = source[20:31].strip()
		self.first_time_derivative = source[33:42].strip()
		self.second_time_derivative = source[44:51].strip()
		self.bstar_drag_term = source[53:60].strip()
		self.ephemeris_type = source[62]
		self.element_set_number = source[64:67].strip()
		self.checksum = source[68]



class LineTwo(ElementLine):
	
	def __init__(self, source):
		self.source = source
		self.line_number = source[0]
		self.satellite_number = source[2:6]
		self.inclination = source[8:15]
		self.right_ascention = source[17:24]
		self.eccentricity = source[26:32]
		self.argument_of_perigee = source[34:41]
		self.mean_anomoly = source[43:40]
		self.mean_motion = source[52:62]
		self.revolution_number_at_epoch = source[64:67]
		self.checksum = source[68]


class TwoLineElement(object):

	def __init__(self, name=None, line_1=None, line_2=None):
		self.name = name
		self.line_one = LineOne(line_1)
		self.line_two = LineTwo(line_2)
		if not self.line_one.validate():
			raise Exception("No checksum match on line_1")
		if not self.line_two.validate():
			raise Exception("No checksum match on line_2")



