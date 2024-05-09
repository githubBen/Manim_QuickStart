from manim import *
from common_utils import *

class Opening(Scene):
    def construct(self):
        title = Text("我想用Manim制作动画视频，怎么做？", gradient=(RED, BLUE, GREEN), font_size=56)
        self.play(AddTextLetterByLetter(title), run_time = 2)
        self.play(FadeOut(title))

        question1 = Text("1.在哪里学习Manim？", color=RED, font_size=60)
        self.play(FadeIn(question1))
        self.play(question1.animate.scale(0.5).move_to(UP * 2.5))

        question2 = Text("2.Manim包含哪些对象？", color=RED, font_size=60)
        self.play(FadeIn(question2))
        self.play(question2.animate.scale(0.5).next_to(question1, DOWN))

        question3 = Text("3.Manim可以用来做什么类型的动画？", color=RED, font_size=60)
        self.play(FadeIn(question3))
        self.play(question3.animate.scale(0.5).next_to(question2, DOWN))

        tip = Text("我们一个个来探索！", color=BLUE, font_size=60).to_edge(DOWN)
        self.play(tip.animate.move_to(ORIGIN))
        self.play(Indicate(tip))

        self.play(*[FadeOut(mobj) for mobj in self.mobjects])


class Question1Scene1(Scene):
    def construct(self):
        utils = Utils(self)
        question1 = utils.create_underline_text("1.在哪里学习Manim？")
        self.play(AddTextLetterByLetter(question1[0]))
        self.play(Create(question1[1]))

        self.play(question1.animate.scale(0.75).move_to(UP * 3))

        tip = Text("首选官网", font_size=40, color=LIGHTER_GRAY)
        self.play(Write(tip))
        self.play(tip.animate.move_to(LEFT*5).set_color(YELLOW))

        arrow = Arrow(LEFT, RIGHT).move_to(LEFT * 2)
        self.play(GrowArrow(arrow))

        image = ImageMobject("offical_website.png").scale(0.5).move_to(RIGHT*3)
        self.play(FadeIn(image), run_time = 0.5)

        framebox = SurroundingRectangle(image, buff = .1)
        self.play(Create(framebox))

        part_framebox = Rectangle(width=1.0, height=3.0, stroke_color=YELLOW).shift(RIGHT * 0.4)
        self.play(ReplacementTransform(framebox, part_framebox))

        all_mobjects = Group(*self.mobjects)  
        all_mobjects.remove(question1)

        guide_image = ImageMobject("guide.png").scale(0.4).move_to(part_framebox.get_center())
        self.play(FadeOut(all_mobjects), guide_image.animate.scale(2.5).move_to(LEFT*5 + DOWN))


class Question1Scene2(Scene):
    def construct(self):
        utils = Utils(self)
        question1 = utils.create_underline_text("1.在哪里学习Manim？")
        question1.scale(0.75).move_to(UP * 3)
        self.add(question1)

        guide_image = ImageMobject("guide.png").shift(LEFT*5 + DOWN)
        self.add(guide_image)

        framebox = Ellipse(width=2.5, height=0.4, stroke_color=YELLOW).shift(LEFT*5 + DOWN*0.9)
        self.play(Create(framebox), run_time = 0.5)

        example = utils.create_ellipse_group("例子展示")
        self.play(GrowFromPoint(example, framebox.get_center()))

        run_time_down = 0.5
        installation = utils.create_ellipse_group("安装说明")
        self.play(framebox.animate.shift(DOWN * 0.35), run_time = run_time_down)

        example.generate_target()
        example.target[0].set_color(BLUE)
        example.target.next_to(installation, UP)
        self.play(MoveToTarget(example), 
                  GrowFromPoint(installation, framebox.get_center()))

        tutorials = utils.create_ellipse_group("教程指南").next_to(installation, DOWN)
        self.play(framebox.animate.shift(DOWN * 0.3), run_time = run_time_down)
        self.play(installation[0].animate.set_color(BLUE), 
                  GrowFromPoint(tutorials, framebox.get_center()))

        reference = utils.create_ellipse_group("参考手册").next_to(tutorials, DOWN)
        self.play(framebox.animate.shift(DOWN * 0.3), run_time = run_time_down)
        self.play(tutorials[0].animate.set_color(BLUE), GrowFromPoint(reference, framebox.get_center()))

        plugins = utils.create_ellipse_group("插件").next_to(reference, DOWN)
        self.play(framebox.animate.shift(DOWN * 0.3), run_time = run_time_down)
        self.play(reference[0].animate.set_color(BLUE), GrowFromPoint(plugins, framebox.get_center()))

        self.play(FadeOut(guide_image), FadeOut(framebox), FadeToColor(plugins[0], BLUE), run_time = 0.5)

        for _ in range(2):
            self.play(CyclicReplace(example, installation, tutorials), run_time = 0.5)
                  
        group_description = Group(installation, tutorials, example, reference, plugins)
        group_description.generate_target()
        group_description.target.shift(LEFT*5)
        for i in range(3):
            group_description.target[i][0].set_fill(color=GREEN_E, opacity=0.5)
        self.play(MoveToTarget(group_description))
        
        arrow = Arrow(installation.get_right(), [-1.5, installation.get_right()[1], 0], 
                      stroke_width=5, 
                      max_tip_length_to_length_ratio = 0.15, 
                      color=GREEN_E)
        self.play(Create(arrow))

        installation_description = Text("包括python、ffmpeg等必装项，\n还有一些选装项的说明等", 
                                        color=YELLOW, 
                                        line_spacing = 1,
                                        font_size=20).next_to(arrow, RIGHT)
        self.play(FadeIn(installation_description), Circumscribe(installation_description))
        self.wait(1)

        tutorials_arrow = arrow.copy()
        self.play(tutorials_arrow.animate.next_to(tutorials, RIGHT), 
                  arrow.animate.set_color(LIGHT_GRAY),
                  installation_description.animate.set_color(WHITE), 
                  run_time = run_time_down)
        tutorials_description = Text("包括快速入门和Manim的基本介绍等", 
                                        color=YELLOW, 
                                        line_spacing = 1,
                                        font_size=20).next_to(tutorials_arrow, RIGHT)
        self.play(FadeIn(tutorials_description), Circumscribe(tutorials_description))
        self.wait(1)

        example_arrow = tutorials_arrow.copy()
        self.play(example_arrow.animate.next_to(example, RIGHT), 
                  tutorials_arrow.animate.set_color(LIGHT_GRAY),
                  tutorials_description.animate.set_color(WHITE), 
                  run_time = run_time_down)
        example_description = Text("包括基本的几何图像动画展示等", 
                                        color=YELLOW, 
                                        line_spacing = 1,
                                        font_size=20).next_to(example_arrow, RIGHT)
        self.play(FadeIn(example_description), Circumscribe(example_description))
        self.wait(1)

        brace = BraceBetweenPoints(installation_description.get_right(), 
                                   example_description.get_right(), 
                                   RIGHT,
                                   color = LIGHT_GRAY).shift(RIGHT * 0.7)
        self.play(FadeIn(brace), 
                  example_description.animate.set_color(WHITE),
                  example_arrow.animate.set_color(LIGHT_GRAY))

        description = Text("通过这三部分学习\n基本就了解了Manim！", 
                                        color=YELLOW, 
                                        line_spacing = 1,
                                        font_size=20).next_to(brace, RIGHT)
        self.play(Write(description))
        self.wait(1)

        self.play(*[FadeOut(mobj) for mobj in self.mobjects], run_time = 0.5)