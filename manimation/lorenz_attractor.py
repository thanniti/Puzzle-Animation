from manim import *
import numpy as np
import hashlib
##### Intro #####
class Introduction_to_lorenzAttractor(Scene):
    def construct(self):
        tex = Tex("Lorenz Attractor","(Butterfly effect)").shift(3.4*UP).scale(0.8)
        tex2 = Tex("Lorenz Attractor is a set of"," ordinary differential equation").scale(0.8).next_to(tex,DOWN)
        math = MathTex(r"\frac{\mathrm{d} x}{\mathrm{d} t}=\sigma (y-x)")
        math2 = MathTex(r"\frac{\mathrm{d} y}{\mathrm{d} t}=x (\rho -z)-y").next_to(math,DOWN)
        math3 = MathTex(r"\frac{\mathrm{d} z}{\mathrm{d} t}=xy-\beta z").next_to(math2,DOWN)
        mat = VGroup(math,math2,math3).scale(0.9).shift(0.7*UP)
        box = SurroundingRectangle(mat)
        matbox = VGroup(math,math2,math3,box)
        
        self.wait()
        self.play(Write(tex))
        self.play(tex[1].animate.set_color(BLUE))
        self.play(Write(tex2))
        self.play(Write(math),Write(math2),Write(math3),Create(box),run_time=2)
        self.play(ShowPassingFlashAround(tex2[1]),rate_func=rate_functions.ease_in_out_expo,run_time=2)
        self.wait()
        self.play(FadeOut(tex[0]),FadeOut(tex2),FadeOut(matbox))
        self.play(tex[1].animate.shift(1.5*LEFT))
        self.play(tex[1].animate.scale(1.5))

        sha = Text('SHA256').next_to(tex[1],DOWN).scale(0.8)
        self.play(FadeInFromLarge(sha))

        myMsg = "11111"
        myMsg2 = "01111"

        myMsgEncoded = myMsg.encode()
        print(f"Original message: {myMsg}")
        m = hashlib.sha256(myMsgEncoded)
        msgHash = m.hexdigest()
        msgHash = msgHash[:16]+'\n'+msgHash[16:]
        msgHash = msgHash[:32]+'\n'+msgHash[32:]
        msgHash = msgHash[:48]+'\n'+msgHash[48:]
        print(f"Message hash: {msgHash}")
        string = f"{msgHash}"

        myMsg2Encoded = myMsg2.encode()
        print(f"Original message: {myMsg2}")
        m = hashlib.sha256(myMsg2Encoded)
        msg2Hash = m.hexdigest()
        msg2Hash = msg2Hash[:16]+'\n'+msg2Hash[16:]
        msg2Hash = msg2Hash[:32]+'\n'+msg2Hash[32:]
        msg2Hash = msg2Hash[:48]+'\n'+msg2Hash[48:]
        print(f"Message hash: {msg2Hash}")
        string2 = f"{msg2Hash}"

        hash_string = Text(string).scale(0.5).shift(3*RIGHT)
        box2 = SurroundingRectangle(hash_string,color=YELLOW, buff=0.25)
        hexdi = VGroup(hash_string,box2)

        hash_string2 = Text(string2).scale(0.5).shift(3*RIGHT)
        box22 = SurroundingRectangle(hash_string2,color=YELLOW, buff=0.25)
        hexdi2 = VGroup(hash_string2,box22)

        inp = Text(f"SHA({myMsg})").scale(0.5).shift(2*LEFT)
        inp2 = Text(f"SHA({myMsg2})").scale(0.5).shift(2*LEFT)
        
        arrow = Arrow(inp, [1,0,0])
        hashtext = Text("hash").scale(0.3)
        hashtext.next_to(arrow,0.5*UP)

        self.play(Write(inp))
        self.play(Write(hexdi),GrowArrow(arrow),Write(hashtext))
        self.wait(2)
        self.play(Transform(inp,inp2))
        self.play(FocusOn(inp2))
        self.play(Transform(hexdi,hexdi2))

        br = Brace(box2, sharpness=1.0)
        change = br.get_text('output completely change').scale(0.8)
        self.play(FadeIn(br))
        self.play(Write(change))

        self.wait(2)
        self.clear()
        self.wait()
##########################################################################################################################
class Lorenz_Attractor(ThreeDScene):
    def construct(self):
        
        dot = Sphere(radius=0.001,fill_color=BLUE,fill_opacity=0).move_to(0*RIGHT + 0.1*UP + 0.105*OUT)
        
        self.set_camera_orientation(phi=65 * DEGREES,theta=30*DEGREES) 
        self.begin_ambient_camera_rotation(rate=0.01)            #Start move camera

        dtime = 0.005
        numsteps = 30

        self.add(dot)

        def lorenz(x, y, z, s=10, r=28, b=2.667):
            x_dot = s*(y - x)
            y_dot = r*x - y - x*z
            z_dot = x*y - b*z
            return x_dot, y_dot, z_dot

        def update_trajectory(self, dt):
            new_point = dot.get_center()
            if np.linalg.norm(new_point - self.points[-1]) > 0.01:
                self.add_smooth_curve_to(new_point)

        traj = VMobject()
        traj.start_new_path(dot.get_center())
        traj.set_stroke(BLUE, 1.5, opacity=0.8)
        traj.add_updater(update_trajectory)
        self.add(traj)

        def update_position(self,dt):
            x_dot, y_dot, z_dot = lorenz(dot.get_center()[0]*10, dot.get_center()[1]*10, dot.get_center()[2]*10)
            x = x_dot * dt/10
            y = y_dot * dt/10
            z = z_dot * dt/10
            self.shift(x/10*RIGHT + y/10*UP + z/10*OUT)

        dot.add_updater(update_position)
        self.wait(420)


       


        
        
