class TorKham:

	def __init__(self):
		self.words = []

	def restart(self):
		 ### Enter Your Code Here ###
		return "game restarted"

	def play(self, S):
		self.kham = S
		self.words = []
		for num in self.kham:
			list_1 = []
			list_1.append(str(num).split())
			if len(list_1[0]) == 2:
				if 'P' in list_1[0]:
					# lastword = self.words[-1]
					if len(self.words) > 0 and list_1[0][1].lower() in [word.lower() for word in self.words]:
						pass
					elif len(self.words) > 0 and self.words[-1][-2:].lower() != list_1[0][1][:2].lower():
						print("'" + list_1[0][1] + "'" + " -> ", end="")
						print("game over")
						break
					else:
						self.words.append(list_1[0][1])
					print("'" + list_1[0][1] + "'" + " -> ", end="")
					print(self.words)

				else:
					print(f"'{list_1[0][0]} {list_1[0][1]}'"" is Invalid Input !!!")
					break
			else:
				if 'R' in list_1[0]:
					self.words = []
					print(torkham.restart())
		return "game over"



torkham = TorKham()
print("*** TorKham HanSaa ***")
S = input("Enter Input : ").split(',')

 ### Enter Your Code Here ###
torkham.play(S)