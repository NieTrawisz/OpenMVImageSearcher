# Find Circles Example
#
# This example shows off how to find circles in the image using the Hough
# Transform. https://en.wikipedia.org/wiki/Circle_Hough_Transform
#
# Note that the find_circles() method will only find circles which are completely
# inside of the image. Circles which go outside of the image/roi are ignored...
thresholds = [(30, 100, 15, 127, 15, 127), # generic_red_thresholds -> index is 0 so
code == (1 << 0)
(30, 100, -64, -8, -32, 32)] # generic_green_thresholds -> index is 1 so code ==
(1 << 1)
import sensor, image, time
sensor.reset()
sensor.set_pixformat(sensor.RGB565) # grayscale is faster
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()
while(True):
clock.tick()
img = sensor.snapshot().lens_corr(1.8)
# Circle objects have four values: x, y, r (radius), and magnitude. The
# magnitude is the strength of the detection of the circle. Higher is
# better...
# `threshold` controls how many circles are found. Increase its value
# to decrease the number of circles detected...
# `x_margin`, `y_margin`, and `r_margin` control the merging of similar
# circles in the x, y, and r (radius) directions.
# r_min, r_max, and r_step control what radiuses of circles are tested.
# Shrinking the number of tested circle radiuses yields a big performance boost.
for c in img.find_circles(threshold = 4000, x_margin = 50, y_margin = 50, r_margin
= 5,
r_min = 10, r_max = 100, r_step = 2):
img.draw_circle(c.x(), c.y(), c.r(), color = (255, 0, 0))
print(c)
# `threshold` below should be set to a high enough value to filter out noise
# rectangles detected in the image which have low edge magnitudes. Rectangles
# have larger edge magnitudes the larger and more contrasty they are...
for r in img.find_rects(threshold = 10000):
diff=r.rect()[2]-r.rect()[3]
if diff>-10 and diff<10:
img.draw_rectangle(r.rect(), color = (255, 0, 0))
#for p in r.corners():
#img.draw_circle(p[0], p[1], 5, color = (0, 255, 0))
#print(r)
print("FPS %f" % clock.fps())
