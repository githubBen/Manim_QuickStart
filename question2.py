from manim import *
from common_utils import *

class Question2Scene1(Scene):
    def construct(self):
        utils = Utils(self)
        question2 = utils.create_underline_text("2.Manim包含哪些对象？")
        self.play(AddTextLetterByLetter(question2[0]))
        self.play(Create(question2[1]))
        self.play(question2.animate.scale(0.75).move_to(UP * 3.5))

        rect_scenes = utils.create_rect_group("Scenes", width=1.5, height= 4.5).shift(LEFT*3)
        self.play(GrowFromCenter(rect_scenes))

        rect_mobjects = utils.create_rect_group("Mobjects", width=1.5, height= 4.5)
        self.play(GrowFromCenter(rect_mobjects))

        rect_aimations = utils.create_rect_group("Aimations", width=1.5, height= 4.5).shift(RIGHT*3)
        self.play(GrowFromCenter(rect_aimations))

        rect_Manim = utils.create_rect_group("Manim", width = 1.5, height = 0.5).shift(LEFT*6)

        self.play(Rotate(rect_scenes[0], angle=PI/2),
                  Rotate(rect_mobjects[0], angle=PI/2),
                  Rotate(rect_aimations[0], angle=PI/2),)

        self.play(rect_scenes[0].animate.scale(SCALE_VALUE),
                  rect_mobjects[0].animate.scale(SCALE_VALUE),
                  rect_aimations[0].animate.scale(SCALE_VALUE))
        
        self.play(GrowFromEdge(rect_Manim, UL),
                  rect_scenes.animate.next_to(rect_Manim, UR+RIGHT),
                  rect_mobjects.animate.next_to(rect_Manim, 2*RIGHT),
                  rect_aimations.animate.next_to(rect_Manim, DR+RIGHT))

        rect_scene = utils.create_rect_group("Scene").shift(RIGHT)
        self.play(FadeIn(rect_scene))
        self.play(rect_scene[0].animate.scale(SCALE_VALUE), run_time = 0.5)
        self.play(rect_scene.animate.next_to(rect_scenes, UR+RIGHT), run_time = 0.5)

        rect_zoomed_scene = utils.create_rect_group("ZoomedScene").shift(RIGHT)
        utils.show_group(rect_zoomed_scene)
        self.play(rect_zoomed_scene.animate.next_to(rect_scenes, 2*RIGHT), run_time = 0.5)

        line1 = Line(rect_Manim.get_right(), rect_scenes.get_left(), color=LIGHTER_GRAY)
        self.play(Create(line1),
                  Create(Line(rect_Manim.get_right(), rect_mobjects.get_left(), color=LIGHTER_GRAY)),
                  Create(Line(rect_Manim.get_right(), rect_aimations.get_left(), color=LIGHTER_GRAY)))

        line2 = Line(rect_scenes.get_right(), rect_scene.get_left(), color=LIGHTER_GRAY)
        self.play(Create(line2),
                  Create(Line(rect_scenes.get_right(), rect_zoomed_scene.get_left(), color=LIGHTER_GRAY)), run_time=0.5)

        self.play(ShowPassingFlash(rect_Manim[0].copy().set_color(ORANGE), time_width=1))

        utils.play_move_along(line1, ORANGE)
        self.play(ShowPassingFlash(rect_scenes[0].copy().set_color(ORANGE), time_width=1))
        utils.play_move_along(line2, ORANGE)
        self.play(ShowPassingFlash(rect_scene[0].copy().set_color(ORANGE), time_width=1))

        all_mobjects = Group(*self.mobjects) 
        all_mobjects.remove(question2).remove(rect_mobjects) 
        self.play(FadeOut(all_mobjects),
                  rect_mobjects.animate.shift(2*LEFT)) 
        print(rect_mobjects.get_center())
    

class Question2Scene2(Scene):
    def construct(self):
        utils = Utils(self)
        question2 = utils.create_underline_text("2.Manim包含哪些对象？")
        question2.scale(0.75).move_to(UP * 3.5)
        self.add(question2)

        rect_mobjects = utils.create_rect_group("Mobjects", width=4.5, height= 1.5).move_to([-5.9625, 0., -0.125 ])
        rect_mobjects[0].scale(SCALE_VALUE)
        self.add(rect_mobjects)

        rect_annularSector = utils.create_rect_group("AnnularSector").shift(RIGHT)
        utils.show_group(rect_annularSector)
        annularSector = AnnularSector(inner_radius=1, outer_radius=1.5, angle=PI, fill_opacity=0.25, color=BLUE).move_to(8 * RIGHT)
        utils.move_group(rect_annularSector)
        self.play(annularSector.animate.move_to(4 * RIGHT))
        self.wait(0.75)
        self.play(FadeOut(annularSector), rect_annularSector.animate.next_to(rect_mobjects, UR + 7*UP), run_time = 0.5)

        rect_annulus = utils.create_rect_group("Annulus").shift(RIGHT)
        utils.show_group_no_text_scale(rect_annulus)
        annulus = Annulus(inner_radius=0.3, outer_radius=0.6, color=RED).shift(8 * RIGHT)
        utils.move_group(rect_annulus)
        self.play(annulus.animate.shift(4 * LEFT))
        self.wait(0.75)
        self.play(FadeOut(annulus), rect_annulus.animate.next_to(rect_annularSector, DOWN), run_time = 0.5)

        rect_arc = utils.create_rect_group("Arc").shift(RIGHT)
        utils.show_group_no_text_scale(rect_arc)
        arc = Arc(angle=PI).shift(8 * RIGHT)
        utils.move_group(rect_arc)
        self.play(arc.animate.shift(4 * LEFT))
        self.wait(0.75)
        self.play(FadeOut(arc), rect_arc.animate.next_to(rect_annulus, DOWN), run_time = 0.5)

        rect_arcBetweenPoints = utils.create_rect_group("ArcBetweenPoints").shift(RIGHT)
        utils.show_group(rect_arcBetweenPoints)
        arcBetweenPoints = ArcBetweenPoints(start=2 * RIGHT, end=2 * UP, stroke_color=YELLOW).shift(4 * RIGHT + DOWN)
        utils.move_group(rect_arcBetweenPoints)
        self.play(Create(arcBetweenPoints))
        self.wait(0.75)
        self.play(FadeOut(arcBetweenPoints), rect_arcBetweenPoints.animate.next_to(rect_arc, DOWN), run_time = 0.5)

        rect_circle = utils.create_rect_group("Circle").shift(RIGHT)
        self.play(FadeIn(rect_circle))
        utils.create_target(rect_circle, rect_arcBetweenPoints)
        self.play(MoveToTarget(rect_circle), run_time = 0.5)

        rect_dot = utils.create_rect_group("Dot").shift(RIGHT)
        self.play(FadeIn(rect_dot))
        utils.create_target(rect_dot, rect_circle)
        self.play(MoveToTarget(rect_dot), run_time = 0.5)

        rect_Ellipse = utils.create_rect_group("Ellipse").shift(RIGHT)
        self.play(FadeIn(rect_Ellipse))
        utils.create_target(rect_Ellipse, rect_dot)
        self.play(MoveToTarget(rect_Ellipse), run_time = 0.5)

        rect_LabeledDot = utils.create_rect_group("LabeledDot").shift(RIGHT)
        utils.show_group_no_text_scale(rect_LabeledDot)
        labeledDot = LabeledDot(Text("ii", color=BLUE)).shift(8 * RIGHT)
        utils.move_group(rect_LabeledDot)
        self.play(labeledDot.animate.shift(4 * LEFT))
        self.wait(0.75)
        self.play(FadeOut(labeledDot), rect_LabeledDot.animate.next_to(rect_Ellipse, DOWN), run_time = 0.5)

        rect_Sector = utils.create_rect_group("Sector").shift(RIGHT)
        utils.show_group_no_text_scale(rect_Sector)
        sector = Sector(outer_radius=2, inner_radius=1).shift(8 * RIGHT + DOWN)
        utils.move_group(rect_Sector)
        self.play(sector.animate.shift(4 * LEFT))
        self.wait(0.75)
        self.play(FadeOut(sector), rect_Sector.animate.next_to(rect_LabeledDot, DOWN), run_time = 0.5)

        all_mobjects = Group(*self.mobjects) 
        all_mobjects.remove(question2).remove(rect_mobjects) 
        self.play(all_mobjects.animate.to_edge(DOWN)) 
        self.play(all_mobjects.animate.shift(10*DOWN), run_time = 0.5) 


  
class Question2Scene3(Scene):
    def construct(self):
        utils = Utils(self)
        question2 = utils.create_underline_text("2.Manim包含哪些对象？")
        question2.scale(0.75).move_to(UP * 3.5)
        self.add(question2)

        rect_mobjects = utils.create_rect_group("Mobjects", width=4.5, height= 1.5).move_to([-5.9625, 0., -0.125 ])
        rect_mobjects[0].scale(SCALE_VALUE)
        self.add(rect_mobjects)

        rect_Arrow = utils.create_rect_group("Arrow").shift(RIGHT)
        self.play(FadeIn(rect_Arrow))
        rect_Arrow.generate_target()
        rect_Arrow.target[0].scale(SCALE_VALUE)
        rect_Arrow.target.next_to(rect_mobjects, UR + 7*UP)
        self.play(MoveToTarget(rect_Arrow), run_time = 0.5)

        rect_DashedLine = utils.create_rect_group("DashedLine").shift(RIGHT)
        utils.show_group_no_text_scale(rect_DashedLine)
        dashed = DashedLine(LEFT, RIGHT).shift(8 * RIGHT)
        utils.move_group(rect_DashedLine)
        self.play(dashed.animate.shift(4 * LEFT))
        self.wait(0.75)
        self.play(FadeOut(dashed), rect_DashedLine.animate.next_to(rect_Arrow, DOWN), run_time = 0.5)
        
        rect_DoubleArrow = utils.create_rect_group("DoubleArrow").shift(RIGHT)
        utils.show_group(rect_DoubleArrow)
        d_arrow = DoubleArrow(LEFT, RIGHT).shift(8 * RIGHT)
        utils.move_group(rect_DoubleArrow)
        self.play(d_arrow.animate.shift(4 * LEFT))
        self.wait(0.75)
        self.play(FadeOut(d_arrow), rect_DoubleArrow.animate.next_to(rect_DashedLine, DOWN), run_time = 0.5)

        rect_Line = utils.create_rect_group("Line").shift(RIGHT)
        self.play(FadeIn(rect_Line))
        utils.create_target(rect_Line, rect_DoubleArrow)
        self.play(MoveToTarget(rect_Line), run_time = 0.5)

        rect_RoundedRectangle = utils.create_rect_group("RoundedRectangle").shift(RIGHT)
        utils.show_group(rect_RoundedRectangle)
        rect_1 = RoundedRectangle(corner_radius=0.5).shift(10 * RIGHT)
        utils.move_group(rect_RoundedRectangle)
        self.play(rect_1.animate.shift(6 * LEFT))
        self.wait(0.75)
        self.play(FadeOut(rect_1), rect_RoundedRectangle.animate.next_to(rect_Line, DOWN), run_time = 0.5)

        rect_Underline = utils.create_rect_group("Underline").shift(RIGHT)
        self.play(FadeIn(rect_Underline))
        utils.create_target(rect_Underline, rect_RoundedRectangle)
        self.play(MoveToTarget(rect_Underline), run_time = 0.5)

        rect_Code = utils.create_rect_group("Code").shift(RIGHT)
        utils.show_group_no_text_scale(rect_Code)
        code = '''from manim import Scene, Square

class FadeInSquare(Scene):
    def construct(self):
        s = Square()
        self.play(FadeIn(s))
        self.play(s.animate.scale(2))
        self.wait()
'''
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", font="Monospace").shift(12 * RIGHT+ DOWN)
        utils.move_group(rect_Code)
        self.play(rendered_code.animate.shift(10 * LEFT))
        self.wait(0.75)
        self.play(FadeOut(rendered_code), rect_Code.animate.next_to(rect_Underline, DOWN), run_time = 0.5)

        rect_MarkupText = utils.create_rect_group("MarkupText").shift(RIGHT)
        self.play(FadeIn(rect_MarkupText))
        utils.create_target(rect_MarkupText, rect_Code)
        self.play(MoveToTarget(rect_MarkupText), run_time = 0.5)

        rect_Text = utils.create_rect_group("Text").shift(RIGHT)
        utils.show_group_no_text_scale(rect_Text)

        all_mobjects = Group(*self.mobjects) 
        all_mobjects.remove(question2).remove(rect_Text) 

        self.play(rect_Text.animate.move_to(RIGHT*8),
                  all_mobjects.animate.shift(10*LEFT))
  

class Question2Scene4(Scene):
    def construct(self):
        utils = Utils(self)
        question2 = utils.create_underline_text("2.Manim包含哪些对象？")
        question2.scale(0.75).move_to(UP * 3.5)
        self.add(question2)

        rect_Aimations = utils.create_rect_group("Aimations", width=4.5, height= 1.5).to_edge(DOWN).shift(2*DOWN)
        rect_animations_copy = rect_Aimations.copy()
        rect_animations_copy[0].scale(SCALE_VALUE)
        rect_animations_copy.move_to([-5.9625, 0., -0.125 ])
        always_rotate(rect_Aimations, rate=2*PI, about_point=ORIGIN)
        self.play(Transform(rect_Aimations, rect_animations_copy), run_time = 3)
        rect_Aimations.clear_updaters()
   
        rect_AnimatedBoundary = utils.create_rect_group("AnimatedBoundary")
        utils.show_group(rect_AnimatedBoundary, 0.6)
        text = Text("So shiny!").move_to(5 * RIGHT)
        boundary = AnimatedBoundary(text, colors=[RED, GREEN, BLUE],
                                    cycle_rate=3)
        self.play(FadeIn(boundary, text), run_time = 0.5)
        self.wait(0.5)
        self.play(FadeOut(boundary), FadeOut(text), rect_AnimatedBoundary.animate.next_to(rect_Aimations, UR + 7*UP))
    
        rect_TracedPath = utils.create_rect_group("TracedPath")
        utils.show_group_no_text_scale(rect_TracedPath)
        a = Dot(RIGHT * 5)
        b = TracedPath(a.get_center, dissipating_time=0.5, stroke_opacity=[0, 1])
        self.add(a, b)
        self.play(a.animate(path_arc=PI / 4).shift(LEFT * 2))
        self.play(FadeOut(a), FadeOut(b), rect_TracedPath.animate.next_to(rect_AnimatedBoundary, DOWN))
    
        rect_Succession = utils.create_rect_group("Succession")
        utils.show_group_no_text_scale(rect_Succession)
        dot1 = Dot(RIGHT * 4, radius=0.16, color=BLUE)
        dot2 = Dot(RIGHT * 5, radius=0.16, color=MAROON)
        dot3 = Dot(RIGHT * 6, radius=0.16, color=GREEN)
        self.add(dot1, dot2, dot3)
        self.play(Succession(
            dot1.animate.move_to(dot2),
            dot2.animate.move_to(dot3),
            dot3.animate.move_to(dot1),
        ))
        self.play(FadeOut(dot1, dot2, dot3), rect_Succession.animate.next_to(rect_TracedPath, DOWN))
    
        rect_Create = utils.create_rect_group("Create + Uncreate")
        self.play(FadeIn(rect_Create))
        utils.create_target_with_text_scale(rect_Create, rect_Succession)
        self.play(MoveToTarget(rect_Create), run_time = 0.5)

        rect_Write = utils.create_rect_group("Write + Unwrite")
        self.play(FadeIn(rect_Write))
        utils.create_target_with_text_scale(rect_Write, rect_Create)
        self.play(MoveToTarget(rect_Write), run_time = 0.5)

        rect_SpiralIn = utils.create_rect_group("SpiralIn")
        utils.show_group_no_text_scale(rect_SpiralIn)
        circle = Circle(color=GREEN_C, fill_opacity=1).shift(RIGHT * 4)
        square = Square(color=BLUE_D, fill_opacity=1).shift(RIGHT * 5)
        shapes = VGroup(circle, square)
        self.play(SpiralIn(shapes))
        self.play(FadeOut(shapes), rect_SpiralIn.animate.next_to(rect_Write, DOWN), run_time = 0.5)

        rect_FadeIn = utils.create_rect_group("FadeIn + FadeOut")
        self.play(FadeIn(rect_FadeIn))
        utils.create_target_with_text_scale(rect_FadeIn, rect_SpiralIn)
        self.play(MoveToTarget(rect_FadeIn), run_time = 0.5)
    
        rect_GrowFromPoint = utils.create_rect_group("GrowFromPoint")
        utils.show_group(rect_GrowFromPoint)
        triangle = Triangle().shift(RIGHT * 4)
        self.play(GrowFromPoint(triangle, ORIGIN))
        self.play(FadeOut(triangle), rect_GrowFromPoint.animate.next_to(rect_FadeIn, DOWN), run_time = 0.5)

        rect_SpinInFromNothing = utils.create_rect_group("SpinInFromNothing")
        utils.show_group(rect_SpinInFromNothing)
        star = Star(outer_radius=2).shift(RIGHT * 4)
        self.play(SpinInFromNothing(star, point_color=RED))

        all_mobjects = Group(*self.mobjects) 
        all_mobjects.remove(question2)

        text = Text("这里只列举了部分Manim对象，\n想要了解更多，可查询官网。", color=LIGHTER_GRAY, line_spacing = 1).scale(0.75)
        
        self.play(all_mobjects.animate(run_time=2, lag_ratio=0.1).scale(0.1).fade(1))
        self.play(GrowFromCenter(text), run_time = 0.5)
        self.wait()
        self.play(Wiggle(text), run_time = 0.5)
        self.play(FadeOut(text), run_time = 0.5)