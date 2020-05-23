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

class zoomInCamera(MovingCameraScene):
	def construct(self):

		eq1 = TexMobject(r"\nabla\textbf{u}").scale(2)
		sq = Square()

		group = VGroup(eq1,sq)
		group.arrange(RIGHT, buff = 5)

		self.play(Write(group))
		self.wait(2)

		self.camera_frame.save_state()

		self.play(

				self.camera_frame.set_width, eq1.get_width()*3,
				self.camera_frame.set_height, eq1.get_height()*2,
				self.camera_frame.move_to, eq1
				 )
		self.wait(2)
		self.play(Restore(self.camera_frame))
		self.wait(1)
		self.play(

				self.camera_frame.set_width, sq.get_width()*3,
				self.camera_frame.set_height, sq.get_height()*2,
				self.camera_frame.move_to, sq
				 )
		
		self.wait(2)

class drawingGraph(GraphScene,MovingCameraScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 5, 
        "x_tick_frequency" : 0.5, 
    }
    # Setup the scenes
    def setup(self):            
        MovingCameraScene.setup(self)
        GraphScene.setup(self)

    def construct(self):
        self.setup_axes(animate=True)

        self.wait(1)

        graph = self.get_graph(lambda x : x**2,  
                                    color = GREEN,
                                    x_min = 0, 
                                    x_max = 7
                                    )
        dot_at_start_graph=Dot().move_to(graph.points[0])
        dot_at_end_grap=Dot().move_to(graph.points[-1])

        self.add(graph,dot_at_end_grap,dot_at_start_graph)

        self.camera_frame.save_state()

        self.play(
            self.camera_frame.scale,.5,
            self.camera_frame.move_to,dot_at_start_graph
        )

        self.play(
            self.camera_frame.move_to,dot_at_end_grap
        )

        self.wait(2)

        self.play(
        	Restore(self.camera_frame)
        )

        self.wait(2)


class LinearTransformation(LinearTransformationScene):
	CONFIG = {
		"include_background_plane" : True,
		"include_foreground_plane" : True,
		"foreground_plane_kwargs" : {
			"x_radius" : FRAME_WIDTH,
			"y_radius" : FRAME_HEIGHT,
			"secondary_line_ratio" : 0,
		},
		"background_plane_kwargs" : {
			"color" : WHITE,
			"secondary_color" : RED,
			"axes_color" : RED,
			"stroke_width" : 7,
		},

		"show_coordinates" : False,
		"show_basis_vectors" : True,
		"basis_vector_stroke_width" : 6,
		"i_hat_color" : X_COLOR,
		"j_hat_color" : Y_COLOR,
		"leave_ghost_vectors" : 0, 
	}

	def construct(self):
		v1 = np.array([[1],[1]])
		mob = Circle()

		tfMatrix = np.array([[2,1],[-1,1]])
		self.add_transformable_mobject(mob)
		self.add_vector(v1)
		self.apply_matrix(tfMatrix)

		self.wait(2)

class removeAllObjectsInScene(Scene):
	def construct(self):

		self.add(
			VGroup(*[
				VGroup(*[
					Dot() for i in range(10)]
					  ).arrange(RIGHT) for k in range(10)]
				  ).arrange(DOWN)
				)
		self.play(*[FadeOut(mob) for mob in self.mobjects])
	#All objects on the screen are saved in self.mobjects
		self.wait(2)

