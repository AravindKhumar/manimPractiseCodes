from manimlib.imports import *
import numpy as np

class usingConfig(Scene):

	CONFIG = {

		"text1" : TexMobject("\\int_{a}^{b} f(x) = f(b) - f(a)"),
		"object1" : Circle().set_color(BLUE),
		"scaleFactor" : 4,
		"vector" : np.array([1,1,0])
	}
	def construct(self):

		self.play(Write(self.text1))
		self.wait()

		self.play(self.text1.scale, self.scaleFactor)
		self.wait()

		self.play(ReplacementTransform(self.text1, self.object1))
		self.wait()

		self.play(self.object1.shift, self.vector)

		self.wait

class reusingTheClassWithJustConfig(usingConfig):

	CONFIG = {
		"text1" : TexMobject("""\\begin{bmatrix}
								1 & 2\\\\
								3 & 4
								\\end{bmatrix}
							"""),
		"object1" : Square().set_color(RED),
		"scaleFactor" : 2,
		"vector" : np.array([-1,-1,0])
	}