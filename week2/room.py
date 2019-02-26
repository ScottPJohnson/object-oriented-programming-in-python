class Room():

	def __init__(self):
		self.name = None
		self.description = None

	def set_description(self, room_description):
		self.description = room_description

	def get_description(self):
		return self.description

	def set_name(self, room_name):
		self.name = room_name

	def get_name(self):
		return self.name

	def describe(self):
		print(self.name)
		print(self.description)