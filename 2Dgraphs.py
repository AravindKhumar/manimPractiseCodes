from manimlib.imports import *
import numpy as np

class twoDgraph(GraphScene):
	CONFIG = {
		"y_max"				: 50,
		"y_min"				: 0,
		"x_max"				: 10,
		"x_min"				: 0,
		"x_tick_frequency"	: 1,
		"y_tick_frequency"	: 10,
		"y_labeled_nums"	: range(0,50,10),
		"x_labeled_nums"	: list(np.arange(0,11,1)),
		"x_label_decimal"	: 1,
		"y_label_decimal"	: 1,
		"x_label_direction"	: DOWN,
		"y_label_direction"	: LEFT,
		#"graph_origin"		: np.array([0,0,0]),
		"axes_color"		: BLUE,		
	}

	def construct(self):
		self.setup_axes(animate = False)
		graph = self.get_graph(lambda x: (x**2)+2,
										color = GREEN,
										x_min = 0,
										x_max = 5
										)
		self.play(ShowCreation(graph), run_time = 2)
		self.wait(2)
		print(graph.points[0:5])

class twoDgraphUsingSetupMethod(GraphScene):
	CONFIG = {
		"y_max"				: 5,
		"y_min"				: 0,
		"x_max"				: 6,
		"x_min"				: -6,
		"y_tick_frequency"	: 0.5,
		"graph_origin"		: np.array([0,-3,0]),
		"axes_color"		: BLUE,
		"x_axis_label"		: "$t$",					
		"y_axis_label"		: "$f(t)$",
	}

	def construct(self):
		self.setup_axes()
		self.wait(2)

		graph = self.get_graph(lambda x : 2*np.exp(-x**2),
										 color = GREEN,)
		self.play(ShowCreation(graph), run_time = 2)
		self.wait(2)
		
	def setup_axes(self):
		GraphScene.setup_axes(self)
		self.x_axis.label_direction = DOWN
		self.y_axis_label_direction = LEFT

# These lines will add the numbers continuously to the number line
		self.x_axis.add_numbers(*range(-6,7,1))
		self.y_axis.add_numbers(*range(1,6,1))

# These ines will add selected points passed to the method only
		#self.y_axis.add_numbers(*[1,3,5,6])

		self.play(ShowCreation(self.x_axis))
		self.play(ShowCreation(self.y_axis))

class twoDgraphChangeLabelStyle(GraphScene):
	CONFIG = {
		"y_max"				: 5,
		"y_min"				: 0,
		"x_max"				: 6,
		"x_min"				: -6,
		"y_tick_frequency"	: 0.5,
		"graph_origin"		: np.array([0,-3,0]),
		"axes_color"		: BLUE,
	}

	def construct(self):
		self.setup_axes()
		self.wait(2)

		graph = self.get_graph(lambda x : 2*np.exp(-x**2),
										 color = GREEN,)
		self.play(ShowCreation(graph), run_time = 2)
		self.wait(2)
		
	def setup_axes(self):
		GraphScene.setup_axes(self)

		self.y_axis_label_direction = LEFT

		self.x_axis_labels = VGroup()
		self.dotXLabels = VGroup()

		xValArray = [-5.5,-4,-2.36,1.6,2.7,3.3,4,6]
		XTexArray = [*("%s" %i for i in xValArray)]
		#XTexArray[3] = "\\frac{8}{5}"
		tickLabels = zip(xValArray, XTexArray)

		for xVal, xTex in tickLabels:
			texObj = TexMobject(xTex).scale(0.6)
			dot = Dot()
			texObj.next_to(self.coords_to_point(xVal,0), DOWN)
			dot.move_to(self.coords_to_point(xVal,0))
			self.x_axis_labels.add(texObj)
			self.dotXLabels.add(dot)

		self.play(Write(self.x_axis_labels),
				  Write(self.dotXLabels),
				  Write(self.x_axis),
		          Write(self.y_axis),)

class twoDgraphLabelFormatting(GraphScene):
	CONFIG = {
		"y_max"				: 5,
		"y_min"				: 0,
		"x_max"				: 6,
		"x_min"				: -6,
		"x_tick_frequency"	: 0.5,
		"y_tick_frequency"	: 0.5,
		"graph_origin"		: np.array([0,-3,0]),
		"axes_color"		: BLUE,
	}

	def construct(self):
		self.setup_axes()
		self.wait(2)

		graph = self.get_graph(lambda x : 2*np.exp(-x**2),
										 color = GREEN,)
		self.play(ShowCreation(graph), run_time = 2)
		self.wait(2)
		
	def setup_axes(self):
		GraphScene.setup_axes(self)

		self.y_axis_label_direction = LEFT

		self.xLabelNumbers = VGroup()

		xValArray = np.arange(-6,6.5,0.5)
		XTexArray = [*("%.1f" %i for i in xValArray)]

		xTickLabels = zip(xValArray,XTexArray)

		for xVal, xTex in xTickLabels:
			texObj = TexMobject(xTex).scale(0.3)
			texObj.next_to(self.coords_to_point(xVal,0),DOWN*0.6)
			self.xLabelNumbers.add(texObj)

		self.play(
				Write(self.x_axis),
				Write(self.y_axis),
				Write(self.xLabelNumbers),
				)

class graphingSineWave(GraphScene,MovingCameraScene):
	CONFIG = {
		"x_max"				: 2*PI,
		"x_min"				: -2*PI,
		"y_max"				: 1,
		"y_min"				: -1,
		"x_tick_frequency"	: PI/2,
		"y_tick_frequency"	: 1,
		"axes_color"		: BLUE,
		"graph_origin"		: ORIGIN,
		"x_axis_label"		: None,
		"y_axis_label"		: None,
	}

	def setup(self):
		GraphScene.setup(self)
		MovingCameraScene.setup(self)

	def construct(self):
		self.setup_axes()
		self.wait()
		graph = self.get_graph(lambda x: np.sin(x), color = GREEN, x_max = PI, x_min = -PI)

		self.play(ShowCreation(graph), run_time = 2)
		self.wait(1)

		# self.camera_frame.save_state()

		# self.play(
		# 		self.camera_frame.scale, .2,
		# 		self.camera_frame.move_to, ORIGIN
		# 		)
		# self.wait(2)

		# self.play(
		# 		Restore(self.camera_frame)
		# 		)
		# self.wait()

	def setup_axes(self):
		GraphScene.setup_axes(self)

		yAxisLabel = TexMobject("\\sin\\theta")
		xAxisLabel = TexMobject("\\theta")
		xAxisLabel.next_to(self.x_axis, RIGHT)
		yAxisLabel.next_to(self.y_axis, UP)

		self.x_axis.set_color(YELLOW)
		self.y_axis.set_color(RED)

		self.y_axis.label_direction =  LEFT
		self.y_axis.add_numbers(*[-1,1])

		xValArray = np.arange(-2*PI, 5*PI/2, PI/2)
		xTexArray = [
					"{-2}\\pi",
					"-\\frac{3\\pi}{2}",
					"-\\pi",
					"-\\frac{\\pi}{2}",
					" ",
					"\\frac{\\pi}{2}",
					"\\pi",
					"\\frac{3\\pi}{2}",
					"{2}\\pi",
					]
		xTickLabels = zip(xValArray,xTexArray)
		self.xLabelNumbers = VGroup()
		for xVal, xTex in xTickLabels:
			texObj = TexMobject(xTex).scale(0.7)
			if(xVal == PI or xVal == -PI):
				texObj.next_to(self.coords_to_point(xVal,0),DOWN*1.4)
			else:
				texObj.next_to(self.coords_to_point(xVal,0),DOWN*0.7)
			self.xLabelNumbers.add(texObj)

		self.play(
				*[Write(obj) for obj in 
					[
					self.x_axis,
					self.y_axis,
					self.xLabelNumbers,
					xAxisLabel,
					yAxisLabel
					]
				]
			)

class plotSinCos(graphingSineWave):

	def construct(self):
		graphingSineWave.setup_axes(self)

		plotSin = self.get_graph(lambda x : np.sin(x), 
													 color = GREEN, 
													 x_min = -3*PI/2,
													 x_max = 3*PI/2
								)

		plotCos = self.get_graph(lambda x : np.cos(x), 
													 color = GREY, 
													 x_min = -3*PI/2,
													 x_max = 3*PI/2
								)
		for i in [plotSin, plotCos]:
			self.play(ShowCreation(i), run_time = 2)

		self.wait()

class extendTheWidthOfAxis(GraphScene):
	CONFIG = {
		"y_min"					:-8,
		"y_max"					:8,
		"x_min"					:-8,
		"x_max"					:8,
		"graph_origin"			:ORIGIN,
		"x_tick_frequency"		:1,
		"y_tick_frequency"		:1,
		"x_axis_label"			:"$x$",
		"y_axis_label"			:"$f(x)$",
		"axes_color"			:BLUE,
		"x_labeled_nums"		:np.arange(-8,9,1),
		"y_labeled_nums"		:np.arange(-8,9,1),
		"x_label_direction"		:DOWN,
		"y_label_direction"		:RIGHT, 
		"x_axis_width"			:13.5,
		"y_axis_height"			:6.5,
	}

	def construct(self):
		self.setup_axes(animate = True)
		graph = self.get_graph(lambda x: x, color = GREEN, x_min = -8, x_max = 8)

		self.play(ShowCreation(graph), run_time = 4)
		self.wait(2)