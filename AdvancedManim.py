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

class changeBackgroundColor(Scene):
	CONFIG = {
		"camera_config":{"background_color":WHITE},
		"text1" : TexMobject(r"\frac{dy}{dx} \Bigr|_{y=2}").scale(3).set_color(BLACK),	
	}
	def construct(self):
		self.play(Write(self.text1))
		self.wait(2)

class arrangeAndGroupObjects(Scene):
	def construct(self):

		eq1 = TexMobject("2x + 3y = 6")
		eq2 = TexMobject("1x + 6y = 3")

		group = VGroup(eq1,eq2)

		group.arrange(RIGHT, buff = 0.4)

		self.add(group)	
		self.wait(2)

		self.play(group.arrange, DOWN, {"aligned_edge" : LEFT, "buff" : 0.5})
		self.wait(1)