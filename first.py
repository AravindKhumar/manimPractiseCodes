from manimlib.imports import *

class Shapes(Scene):
    def construct(self):
        text = TextMobject("Aravind Khumar A")
        circle = Circle()
        square = Square()
        line=Line(np.array([3,0,0]),np.array([5,0,0]))
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))

        self.play(Write(text), run_time = 4)
        self.wait(1)
        #self.remove(text)

        self.add(line)
        self.wait(1)
        self.remove(line)
        
        self.play(ShowCreation(square))

        self.play(FadeOut(circle))
        
        self.play(GrowFromCenter(square))
        
        self.play(Transform(square,triangle))
        
        self.wait(1)

"""
This class contains all the postions that can be included to move objects around the screen
1. Absolute Moving
2. Relative Moving

1.a. .to_edge(UP,DOWN,LEFT,RIGHT)
1.b. .to_corner(UL,UR,DL,DR)

2.a. .move_to(position)
2.b. .next_to(object,(UP,DOWN,RIGHT,LEFT),buff = )
2.c. .shift(UP,DOWN,LEFT,RIGHT)

.rotate(RADIANS , 45*DEGREES)

.flip(UP, LEFT)
"""
class positions(Scene):   
    def construct(self):
        object1 = Dot()
        object2 = Dot()
        #object.to_edge(UP)
        #object.to_edge(DOWN)
        #object.to_edge(RIGHT)
        #object.to_edge(LEFT)
        #object.to_edge(UR)
        #object.to_edge(UL)
        #object.to_edge(DR)
        object1.to_edge(DL,buff = 2)
        object2.to_corner(DOWN)
        self.add(object1)
        self.wait(1)
        self.remove(object1)
        self.wait(1)
        self.add(object2)
        self.wait(1)

class markingCoordinates(Scene):
    def construct(self):
        dot = Dot()
        text = TextMobject("(-2,2)")
        dot.move_to(np.array([-2,2,0]))
        text.next_to(dot,UP,buff = 0.01)
        self.add(dot)
        self.add(text)
        self.wait()
        text.shift(UP)
        self.add(text)  
        #self.wait()
        #text.rotate(PI/4, about_point = dot.get_center())
        #self.wait() 
        text.flip(RIGHT)
        self.add(text)
        self.wait()
        
"""
RENDERING SETTINGS:

-pl - low resolution 480p 15fps
-pm - Medium resolution 720p 30fps
-p  - High resolution 1080p 60fps

Modify the Height, Width of the video:

 -r Adjusts the height, width
-plr 1080,2468
-plm ____,____
-pr  ____,____

Modify the alpha level of the render:

-ptl
-ptm
-pt

Aplha modification with Height Adjustment
-ptlr
-ptmr
-ptr

To leave the progress bar completion on the screen itself:

-render settings  --leave_progress_bars

To modify the point at which the animation should start:

-render settings -n START, END+1 --leave_progress_bars

To change the output name of the video:

-render settings -o NAME
"""

"""
TEX OBJECTS:

Copy the text lines for a formula from a source and add r in front of the quotes to indicate that it is a raw string
or else change all \ to \\

Inorder to scale the appearance of the formula or text - use
TexMobject.scale(number)

"""

class formula(Scene):
    def construct(self):
        formula = TexMobject(r" Formula = \begin{bmatrix}1 & 2 & 3\\ 4 & 5 & 6\\ 7 & 8 & 9\end{bmatrix}")
        formula1 = TextMobject(r" Formula = $\displaystyle\begin{bmatrix}1 & 2 & 3\\ 4 & 5 & 6\\ 7 & 8 & 9\end{bmatrix}$")
        
        formula.to_edge(RIGHT, buff = 0)
        formula1.to_edge(LEFT, buff = 0)
        self.add(formula1)
        self.add(formula)
        self.wait(4)

class movingPoint(Scene):
    def construct(self):
        dot = Dot()
        for i in range(-4,5):
            dot.move_to(np.array([i,0,0]))
            point = TextMobject(str(dot.get_center()))
            self.add(dot)
            self.add(point.next_to(dot,UP,buff = 0.2))
            self.wait()
            self.remove(point)

class circlePointMarking(Scene):
    def construct(self):
        dot = Dot()
        n = 8
        prevPoint = np.array([2,0,0])
        dot.move_to(prevPoint)
        self.add(dot)
        for i in range(1,n+1):
            dot.rotate(2*PI/n,about_point = np.array([0,0,0]))
            currentPoint = dot.get_center()
            l = Line(prevPoint,currentPoint)
            prevPoint = currentPoint
            self.add(dot)
            self.add(l)
            self.wait(0.5)            

"""
object.set_color() - sets the colour to the object
within () there should be hex value of the coour or names for which have to be defined in the 
constants.py in manim folder
"""

class formulaCrossing(Scene):
    def construct(self):
        formula = TexMobject("\\int_a^b{f(x)}","=","{f(b) - f(a)}")
        cross = Cross(formula[2])
        cross.set_stroke(RED, 6)
        self.play(Write(formula))
        self.wait(2)
        self.play(ShowCreation(cross))
        self.wait(2)

class transformationClass(Scene):
    def construct(self):
        text1 = TextMobject("Hello World")
        text2 = TextMobject("Hehee World")

        self.play(Write(text1))
        self.wait()
        self.play(Transform(text1, text2))
        self.wait()

class integralAnimation(Scene):
    def construct(self):
        formula = TexMobject("\\int",     #0
                                "_{a}",  #1
                                "^{b}",  #2
                                "f(",    #3
                                "x",     #4
                                ")",     #5
                                "dx = ",  #6
                                "f(",    #7
                                "b",     #8
                                ")",     #9
                                "-",     #10
                                "f(",    #11
                                "a",     #12
                                ")")     #13
        self.play(Write(formula[0:7]))
        self.wait(1)
        self.play(
                    Transform(formula[3].copy(),formula[7]),
                    Transform(formula[3].copy(),formula[11]),
                    Write(formula[9]),
                    Write(formula[13]),
                    Write(formula[10]),
                    Transform(formula[1].copy(),formula[8]),
                    Transform(formula[2].copy(),formula[12])
                )
        self.wait(1)
        
'''Some Tranformations in animation'''

'''This class contains the braces that can be put to show grouping in screens'''
class braces(Scene):
    def construct(self):
        text = TexMobject("\\frac{d}{dx} f(x).g(x) = ",
                          "f(x) \\frac{d}{dx}g(x)",
                          "+",
                          "g(x) \\frac{d}{dx}f(x)"
            )
        self.play(Write(text))
        self.wait(2)

        brace1 = Brace(text[1],UP,buff = SMALL_BUFF)
        brace1text = brace1.get_text("$f.g'$")
        brace2 = Brace(text[3],UP,buff = SMALL_BUFF)
        brace2text = brace2.get_text("$g.f'$")

        self.play(
                GrowFromCenter(brace1),
                FadeIn(brace1text),
            )
        self.wait(2)

        self.play(
                ReplacementTransform(brace1.copy(), brace2),   # Remove copy() and the braces and text will move
                ReplacementTransform(brace1text.copy(), brace2text),
            )
        self.wait(2)
'''This Class is used to draw rectangle boxes to highlight the things in screen'''
class rectBox(Scene):
    def construct(self):
        text = TexMobject("\\frac{d}{dx} f(x).g(x) = ",
                          "f(x) \\frac{d}{dx}g(x)",
                          "+",
                          "g(x) \\frac{d}{dx}f(x)"
            )
        self.play(Write(text))
        self.wait(2)

        rect1 = SurroundingRectangle(text[1],buff = SMALL_BUFF)
        rect2 = SurroundingRectangle(text[3],buff = SMALL_BUFF)

        rect1text = TexMobject("f.g'")
        rect1text.next_to(rect1,UP, buff = SMALL_BUFF)
        rect2text = TexMobject("g.f'")
        rect2text.next_to(rect2,UP, buff = SMALL_BUFF)

        
        self.play(
                ShowCreation(rect1),
                Write(rect1text),
            )
        self.wait(2)
        self.remove(rect1text)
        self.play(
                ReplacementTransform(rect1, rect2),
                path_arc = np.pi
                )
        self.play(Write(rect2text))
        self.wait(2)
''' Draws arrows from one point to another '''
class arrowShow1(Scene):
    def construct(self):

        step1 = TextMobject("Step 1")
        step2 = TextMobject("Step 2")
        arrow = Arrow(LEFT, RIGHT)

        step1.move_to(LEFT*2)
        arrow.next_to(step1, RIGHT, buff = SMALL_BUFF)
        step2.next_to(arrow, RIGHT, buff = SMALL_BUFF)

        self.play(Write(step1))
        self.play(GrowArrow(arrow))
        self.play(Write(step2))

        self.wait(2)

class arrowShow2(Scene):
    def construct(self):

        step1 = TextMobject("Step 1")
        step2 = TextMobject("Step 2")

        step1.to_corner(DL)
        step2.to_corner(UR)

        arrow1 = Arrow(step1.get_right(), step2.get_left(), buff = SMALL_BUFF).set_color(RED)
        arrow2 = Arrow(step1.get_top(), step2.get_bottom(), buff = SMALL_BUFF).set_color(BLUE)

        self.play(Write(step1))
        self.play(GrowArrow(arrow1))
        self.play(GrowArrow(arrow2))
        self.play(Write(step2))

        self.wait(2)
''' Draws lines from one point to another '''
class lineShow(Scene):
    def construct(self):

        step1 = TextMobject("Step 1")
        step2 = TextMobject("Step 2")

        step1.to_corner(DL)
        step2.to_corner(UR)

        arrow1 = Line(step1.get_right(), step2.get_left(), buff = SMALL_BUFF).set_color(RED)
        arrow2 = Line(step1.get_top(), step2.get_bottom(), buff = SMALL_BUFF).set_color(BLUE)

        self.play(Write(step1))
        self.play(ShowCreation(arrow1))
        self.play(ShowCreation(arrow2))
        self.play(Write(step2))

        self.wait(2)

class dashedlineShow(Scene):
    def construct(self):

        step1 = TextMobject("Step 1")
        step2 = TextMobject("Step 2")

        step1.to_corner(DL)
        step2.to_corner(UR)

        arrow1 = DashedLine(step1.get_right(), step2.get_left(), buff = SMALL_BUFF).set_color(RED)
        arrow2 = DashedLine(step1.get_top(), step2.get_bottom(), buff = SMALL_BUFF).set_color(BLUE)

        self.play(Write(step1))
        self.play(ShowCreation(arrow1))
        self.play(ShowCreation(arrow2))
        self.play(Write(step2))

        self.wait(2)
''' This class shows that without using transform the object can be shifted by diretions'''
class ShiftObjectInPlay(Scene):
    def construct(self):

        step1 = TextMobject("Step 1")
        step2 = TextMobject("Step 2")

        step1.to_corner(DL)
        step2.to_corner(UR)

        arrow1 = DashedLine(step1.get_right(), step2.get_left(), buff = SMALL_BUFF).set_color(RED)
        
        self.play(Write(step1))
        self.play(ShowCreation(arrow1))
        self.play(Write(step2))

        self.wait(2)

        self.play(step2.next_to, step2, LEFT)

        self.wait(1)

class anotherLineAnimation(Scene):
    def construct(self):
        step1 = TexMobject("Step 1").to_corner(DL)
        step2 = TexMobject("Step 2").to_corner(UR)
        step3 = TexMobject("Step 2").next_to(step2, LEFT*1.3)

        arrow = Arrow(step1.get_right(), step2.get_bottom(), buff = SMALL_BUFF).set_color(BLUE)
        arrow_dup = Arrow(step1.get_right(), step3.get_bottom(), buff = SMALL_BUFF).set_color(RED)
        
        self.play(Write(step1), Write(step2))
        self.wait(1)

        self.play(GrowArrow(arrow))

        self.play(ReplacementTransform(step2, step3),
                  ReplacementTransform(arrow, arrow_dup))
        self.wait(2)




