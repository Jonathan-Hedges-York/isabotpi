from hokuyolx import HokuyoLX
laser = HokuyoLX()
for timestamp, scan in laser.iter_dist(0):
	print(timestamp)
