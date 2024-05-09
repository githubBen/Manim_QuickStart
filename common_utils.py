from manim import *

SCALE_VALUE = 0.35
TEXT_SCALE_VALUE = 0.65

class Utils:
    def __init__(self, scene:Scene) -> None:
        self.scene = scene

    def create_underline_text(self, text_name: str):
        text = Text(text_name, color=LIGHTER_GRAY)
        line = Underline(text, color=LIGHTER_GRAY)
        group = VGroup(text, line)
        return group
    
    def create_ellipse_group(self, text_name: str):
        ellipse = Ellipse(width=2.5, height= 0.5, color=YELLOW)
        text = Text(text_name, font_size=20).next_to(ellipse, IN)
        group = VGroup(ellipse, text)
        return group
    
    def create_rect_group(self, text_name: str, width: float=4.5, height: float= 1.5):
        rect = Rectangle(width=width, height=height, color=DARK_BLUE)
        text = Text(text_name, font_size=20, color=LIGHTER_GRAY).next_to(rect, IN)
        group = VGroup(rect, text)
        return group    
    
    def show_group(self, group: VGroup, text_scale_value:float=TEXT_SCALE_VALUE):
        self.scene.play(FadeIn(group))
        self.scene.play(group[0].animate.scale(SCALE_VALUE),
                  group[1].animate.scale(text_scale_value), run_time = 0.5)
        
    def show_group_no_text_scale(self, group: VGroup):
        self.scene.play(FadeIn(group))
        self.scene.play(group[0].animate.scale(SCALE_VALUE), run_time = 0.5)
        
    def move_group(self, group: VGroup):
        self.scene.play(group.animate.move_to(RIGHT* 4 + UP * 2), run_time = 0.5) 

    def play_move_along(self, mobject: Mobject, color):
        dot = Dot(fill_opacity=0)
        line = VMobject()
        self.scene.add(line)
        line.add_updater(lambda x: x.become(Line(mobject.get_start(), dot.get_center()).set_color(color)))
        self.scene.play(MoveAlongPath(dot, mobject), rate_func=linear, run_time=0.5)
        line.clear_updaters()

    def create_target(self, group: VGroup, next_to_group: VGroup):
        group.generate_target()
        group.target[0].scale(SCALE_VALUE)
        group.target.next_to(next_to_group, DOWN)

    def create_target_with_text_scale(self, group: VGroup, next_to_group: VGroup):
        group.generate_target()
        group.target[0].scale(SCALE_VALUE)
        group.target[1].scale(TEXT_SCALE_VALUE)
        group.target.next_to(next_to_group, DOWN)