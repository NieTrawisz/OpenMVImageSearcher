# Untitled - By: lsriw - Mon Oct 17 2022

thresholds = [(30, 100, 15, 127, 15, 127)] # generic_red_thresholds -> index is 0 so
code == (1 << 0)

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()

while(True):
  clock.tick()
  img = sensor.snapshot()
  for blob in img.find_blobs(thresholds, pixels_threshold=100, area_threshold=100, merge=True):
    img.draw_rectangle(blob.rect())
  print(clock.fps())
