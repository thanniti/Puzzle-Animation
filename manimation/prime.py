from manim import*
import math
class Spiral(MovingCameraScene):
	def construct(self):
		pp = PolarPlane(
            azimuth_units="PI radians",
            size=60,
            radius_max=30,
            azimuth_label_scale=0.7,
            radius_config={"number_scale_value": 0.7},
        )
		self.add(pp)
		self.camera.frame.set(width=30)
		def prime(n):
			if n == 1:
				return False

			if n == 2:
				return True
			if n > 2 and n % 2 == 0:
				return False

			max_divisor = math.floor(math.sqrt(n))
			for d in range(3, 1 + max_divisor, 2):
				if n % d == 0:
					return False
			return True

		for n in range(1, 50):
			pdot = Dot(pp.polar_to_point(n, prime(n)),radius=1)
			pdot.set_color(YELLOW_C)
			self.add(pdot)
			
			
			

		
		





