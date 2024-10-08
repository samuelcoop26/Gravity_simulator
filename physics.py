import numpy as np

#Helper Functions:
def magnitude(arr):
	return np.sqrt(pow(arr[0],2) + pow(arr[1],2) + pow(arr[2],2))

def unit_vector(arr):
	mag=magnitude(arr)
	return np.array([
			[
				arr[0] / mag,
				arr[1] / mag,
				arr[2] / mag,
			]
	])

class Physics:
	def __init__(self):
		self.body_pos_array=np.array([]).reshape((0,3))
		self.body_list = None

	def define_bodies(self, body_list):
		self.body_list = [np.array([i,body]) for i, body in enumerate(body_list)]

	def force(self):
		distances=[]
		forces=[]
		Fnet=[]


		for current_body in self.body_list:
			temp = np.array([]).reshape((0, 3))
			for other_body in self.body_list:
				temp = np.append(
				temp,
				(current_body[1].position - other_body[1].position) * np.array([[-1, -1, 1]]),
				axis=0
				)
			distances.append(temp)
			temp = np.array([]).reshape((0, 3))


		for current_body in self.body_list:
			temp = np.array([]).reshape((0, 3))
			for other_body in self.body_list:
				if magnitude(distances[current_body[0]][other_body[0]]) != 0:
					force = 6.67 * pow(10, -11) * current_body[1].mass * other_body[1].mass * (
						#multiply magnitude by 0.25 to magnify effect:
						1 / pow(magnitude(distances[current_body[0]][other_body[0]]) * 0.25, 2))
					force = force * unit_vector(distances[current_body[0]][other_body[0]])
					temp = np.append(
						temp,
						force * np.array([[1, 1, 1]]),
						axis=0
					)
				else:
					temp=np.append(
						temp,
						np.array([[0.0,0.0,0.0]]),
						axis=0
					)
			forces.append(temp)
			temp = np.array([]).reshape((0,3))

		for obj in forces:

			Fnet.append(obj.sum(axis=0))

		return Fnet
