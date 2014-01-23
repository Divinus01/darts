def start( stdscr ):
#{
	score = lines_sum_shanghai.initLinesScore( )
	percentage = lines_sum_shanghai.initLinesPerc( )
	colperc = lines_sum_shanghai.initColsPerc( )

	total = 0
	totalperc = 0.0

	x = 0
	y = 0

	colors = utility.init_colors( )

	for y in range( 2, 23 ):
	#{
		for x in range( 6, 23, 8 ):
		#{
			inp = 0 
			while ( True ):
			#{
				inp = u.getch( )
				if ( inp >= 48 and inp <= 51 and y != 22 ):
				#{
					pick = table_fill_shanghai.points( stdscr, y, x, inp, colors )
					total += ( y - 1 ) * pick
					break
				#}
				elif ( inp >= 48 and inp <= 50 ):
				#{
					pick = table_fill_shanghai.points( stdscr, y, x, inp, colors )
					total += ( y + 3 ) * ( pick - 1 )
					break
				#}
			#}
			lines_sum_shanghai.update( y, percentage, inp, stdscr, total, score, colperc, x )
		#}
	#}
#}

def init( ):
#{
	global utility
	import utility

	global u
	import unicurses as u

	global lines_sum_shanghai
	import shanghai.lines_sum_shanghai as lines_sum_shanghai

	global table_fill_shanghai
	import shanghai.table_fill_shanghai as table_fill_shanghai
#}