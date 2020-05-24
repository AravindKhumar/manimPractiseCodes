from manimlib.imports import *
import numpy as np

class cameraPosition(ThreeDScene):
	def construct(self):
		axes = ThreeDAxes()
		circle = Circle()

		# phi and theta are same as values in Sperical Coordinates
		# distance parameter denotes the distance of the camera from the object
		# gamma parameter rotates the present axes + object to the said angle

		self.set_camera_orientation(phi = 70*DEGREES, theta = 45*DEGREES, distance = 6, gamma = -30*DEGREES)
		self.play(ShowCreation(circle), ShowCreation(axes))
		self.wait(2)

class moveCameraAnimation(ThreeDScene):
	def construct(self):

		axes = ThreeDAxes()
		circle = Circle()

		self.play(ShowCreation(axes), ShowCreation(circle))
		self.move_camera(theta = -45*DEGREES, phi = 80*DEGREES, run_time = 4)
		self.wait()

class ambientCameraRotation(ThreeDScene):
	def construct(self):

		axes = ThreeDAxes()
		circle = Circle()

		self.set_camera_orientation(theta = -45*DEGREES, phi = 80*DEGREES)
		self.play(ShowCreation(axes), ShowCreation(circle))
		self.begin_ambient_camera_rotation(rate = 0.1)
		self.wait(5)
		self.stop_ambient_camera_rotation()
		self.wait()

class parametricEquationGraphing(ThreeDScene):
	def construct(self):

		axes = ThreeDAxes()

		obj1 = ParametricFunction(
					lambda u : np.array([
							np.sin(u),
							np.cos(u),
							u/2
						]), t_max = TAU,t_min = -TAU, color = RED, 
				)

		self.add(axes)

		self.set_camera_orientation(theta = 45*DEGREES, phi = 80*DEGREES)
		self.begin_ambient_camera_rotation(rate = 0.2)

		self.play(ShowCreation(obj1), run_time = 3)
		self.wait(2)

		self.stop_ambient_camera_rotation()
		self.wait()

class parametricEquationTransformation(ThreeDScene):
	def construct(self):

		axes = ThreeDAxes()

		obj1 = ParametricFunction(
					lambda u : np.array([
							np.sin(u),
							np.cos(u),
							u/2
						]), t_max = TAU,t_min = -TAU, color = RED, 
				)

		obj2 = ParametricFunction(
					lambda u : np.array([
							np.sin(u),
							np.cos(u),
							u
						]), t_max = TAU,t_min = -TAU, color = YELLOW, 
				)
		self.add(axes)

# Overlapping of curve surface over the axes in correct form
		obj1.set_shade_in_3d(True)
		obj2.set_shade_in_3d(True)
		
		self.set_camera_orientation(theta = 45*DEGREES, phi = 80*DEGREES)
		self.begin_ambient_camera_rotation(rate = 0.2)

		self.play(ShowCreation(obj1))
		self.wait()

		self.play(Transform(obj1, obj2), rate_func = there_and_back, run_time = 4)

		self.stop_ambient_camera_rotation()
		self.wait()


class surfaceGraphing(ThreeDScene):
	def construct(self):

		axes = ThreeDAxes()

		torus = ParametricSurface(
				lambda u,v: np.array([
						np.sin(TAU*u)*(3.6+np.cos(TAU*v)),
						np.cos(TAU*u)*(3.6+np.cos(TAU*v)),
						np.sin(TAU*v)
					]),
				resolution = (6,32)).fade(0.5)

		self.add(axes)
		self.set_camera_orientation(theta = 45*DEGREES, phi = 70*DEGREES)
		self.begin_ambient_camera_rotation(rate = 0.1)

		self.play(Write(torus), run_time = 2)
		self.wait(4)
		self.stop_ambient_camera_rotation()
		self.wait()