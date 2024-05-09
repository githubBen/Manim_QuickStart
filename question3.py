from manim import *
from common_utils import *

class Question3Scene1(Scene):
    def construct(self):
        utils = Utils(self)
        question3 = utils.create_underline_text("3.Manim可以用来做什么类型的动画？")
        self.play(AddTextLetterByLetter(question3[0]))
        self.play(Create(question3[1]))
        self.play(question3.animate.scale(0.75).move_to(UP * 3))

        backgroundRectangle = RoundedRectangle(width = 10, height = 3, stroke_color=GRAY_E)
        backgroundRectangle.shift(7*DOWN).set_fill(color=BLUE, opacity=0.25)

        text = Text("\t所以Manim主要是用于数学动画的制作，\n"
                         "但是如果你发挥想象力，应该能够做出惊艳的其他类型动画效果，\n"
                         "前面说过它还有很多插件，感兴趣的可以继续了解！", color=LIGHTER_GRAY, line_spacing = 1)
        text.scale(0.5).next_to(backgroundRectangle, IN)
        self.play(backgroundRectangle.animate.move_to(ORIGIN), text.animate.move_to(ORIGIN))
        self.wait(2.5)
        self.play(ApplyWave(
            text,
            rate_func=linear,
            ripples=2,
            run_time = 2
        ))

        tip = Text("感谢观看！", color=LIGHTER_GRAY)
        self.play(Transform(text, tip))
        self.play(Flash(tip,line_length = 0.5))