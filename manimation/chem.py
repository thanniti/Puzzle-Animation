from chanim import *

class ChanimScene(Scene):
    def construct(self):
        ## ChemWithName creates a chemical diagram with a name label
        grid = NumberPlane()
        
        t0 = Text("there are many type of C3H6O")
        t = Text("How many type of C3H6O that non-reactive with Na metal ").scale(0.7)
        t1 = Text("Answer").scale(0.7).to_edge(UP)


        chem = ChemWithName("H-c(-[2]H)(-[6]H)-c(=[2]O)-c(-[2]H)(-H)(-[6]H)", "C3H6O")
        chem2 = ChemWithName("H_3C-[7]CH_2-[1]C(=[2]O)-[7]H","C3H6O\npropane")
        chem3 = ChemWithName("H_3C-[1]C(=[2]O)-[7]CH_3","C3H6O\nacetone")
        chem4 = ChemWithName("H_2C=CH-[7]CH_2-[1]O-H","C3H6O\n2-propen-1-ol")

        x1 = Tex("C3H6O")
        x2 = Tex("C=C").shift(2*LEFT)
        x3 = Tex("C=O").shift(2*RIGHT)
        x4 = Tex("Ether").shift(2*LEFT)
        x5 = Tex("Alcohol").shift(5*LEFT)
        x6 = Tex("Aldehyde").shift(2*RIGHT)
        x7 = Tex("Ketone").shift(5*RIGHT)
        a1 = Arrow([-2,1.5,0],x4)
        a2 = Arrow([-2,1.5,0],x5)
        a3 = Arrow([2,1.5,0],x6)
        a4 = Arrow([2,1.5,0],x7)
        a = VGroup(a1,a2,a3,a4)
        c = Cross(x5,stroke_color=RED,stroke_width=7)

        
        
        self.play(Write(t0))
        self.wait(2)
        self.play(FadeOut(t0))
        self.play(chem.creation_anim())
        self.wait()
        self.play(Transform(chem,chem2))
        self.wait()
        self.play(Transform(chem,chem3))
        self.wait()
        self.play(Transform(chem,chem4))
        self.wait()
        self.wait()
        self.clear()
        #self.add(grid)
        self.play(FadeInFromLarge(t))
        self.wait(5)
        self.play(t.animate.shift(2.8*UP))
        self.play(Transform(t,t1))
        self.play(FadeOut(t))
        self.play(Write(x1))
        self.play(TransformFromCopy (x1,x2),TransformFromCopy (x1,x3))
        self.play(FadeOut(x1))
        self.play(x2.animate.shift(2*UP),x3.animate.shift(2*UP))
        self.play(Write(a))
        self.play(Write(x4),Write(x5),Write(x6),Write(x7),run_time=4)
        self.play(Indicate(x5))
        self.play(Indicate(x4))
        self.wait(2)
        self.play(Indicate(x6))
        self.play(Indicate(x7))
        self.wait()
        
        self.play(FocusOn(x5))
        self.wait(3)
        self.play(Create(c))

        self.wait(3)