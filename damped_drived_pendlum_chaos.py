import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class damped_driven_pendlum():
	def __init__(self):
		#Some useful constants
		self.c = 0.05
		self.F = 0.3
		self.w = 0.7
		self.dt = 1e-4

		self.x = [1.5]
		self.v = [0.0]
		self.a = []
		self.t = [0.0]
		self.absTime = 0.0
		self.a.append(self.getA())


		self.pv = []
		self.px = [] 
		self.pcnt = 1

	def getX(self):
		x, v, a = self.x[-1], self.v[-1], self.a[-1]
		dt = self.dt
		return x + v*dt + 0.5*a*dt*dt

	def getV(self):
		v, a = self.v[-1], self.a[-1]
		dt = self.dt
		return v + a*dt

	def getA(self):
		x, v= self.x[-1], self.v[-1]
		c, F, w = self.c, self.F, self.w
		absTime = self.absTime
		return -c*v - np.sin(x) + F*np.cos(w*absTime)

	def update(self):
		self.absTime += self.dt
		
		self.a.append(self.getA())
		self.v.append(self.getV())
		self.x.append(self.getX())
		self.t.append(self.absTime)

		pass

	def simulator(self, iter_num):
		for i in range(iter_num):
			if(i % 50000 == 0):
				print(str(100*i//iter_num) + "% done")
			self.update()

			if(self.w*self.t[-1] > 2*np.pi*self.pcnt):
				self.pcnt += 1
				self.pv.append(self.v[-1])
				self.px.append(self.x[-1])


	def plot(self):
		mode = ["VT", "VX", "VX_P"]

		fig, ax = plt.subplots(7, 3)


		for i in range(7):
			self.__init__()
			self.F = 0.4 + 0.1*i
			print("[For condition : F = " + str(self.F) + "]")
			self.simulator(1000000)
			
			for j in range(3):
				if(mode[j] == "VX"):		
					ax[i, j].plot(self.x, self.v)
					ax[i, j].set_xlim(-np.pi, np.pi)
				elif(mode[j] == "VT"):
					ax[i, j].plot(self.t, self.v)
					ax[i, j].set_xlim(0, np.pi*20)
					#ax[i, j].set_ylim(-self.v[int(21*np.pi)],self.v[int(21*np.pi)])
				elif(mode[j] == "VX_P"):
					ax[i, j].plot(self.px, self.pv, "o")
					ax[i, j].set_xlim(-np.pi, np.pi)

			'''
			# Opposite Initial Condition
			self.__init__()
			self.F = -0.4 - 0.1*i
			self.x = [-1.0]
			self.v = [0.0]
			self.a = [self.getA()]
			print("[For condition : F = -" + str(self.F) + "]")
			self.simulator(1000000)

			for j in range(3):
				if(mode[j] == "VX"):		
					ax[i, j].plot(self.x, self.v)
					ax[i, j].set_xlim(-np.pi, np.pi)
			'''

		plt.show()


osc = damped_driven_pendlum()
osc.plot()


