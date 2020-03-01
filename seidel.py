#!/usr/bin/env python3

import pandas as pd
from simpleeval import simple_eval

# Nilai awal
x = y = z = 0

# Toleransi error
epsilon = 10e-10

persamaan_x = input("x = ")
persamaan_y = input("y = ")
persamaan_z = input("z = ")

# Iterasi
i = 0

# df = tabel
df = pd.DataFrame(columns = ['x', 'y', 'z', 'Error x', 'Error y', 'Error z'])
df.loc[i] = [x, y, z, '-', '-', '-']

i += 1

while True:
	# Tampung Xi-1, Yi-1, Zi-1
	x_prev = x
	y_prev = y
	z_prev = z
	
	x = simple_eval(persamaan_x, names={"y":y, "z":z})
	y = simple_eval(persamaan_y, names={"x":x, "z":z})
	z = simple_eval(persamaan_z, names={"x":x, "y":y})
    
	# Hitung masing-masing error
	error_x = abs(x - x_prev)
	error_y = abs(y - y_prev)
	error_z = abs(z - z_prev)
	
	df.loc[i] = [x, y, z, error_x, error_y, error_z]
	
	# Cek Toleransi error
	if error_x <= epsilon or error_y <= epsilon or error_z <= epsilon:
		break
	
	i += 1

# Set banyak kolom yang ditampilkan
pd.set_option('display.max_columns', 7)

# Print tabel
print(df)
