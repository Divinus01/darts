def start( stdscr ):
#{
	score = lines_sum_shanghai.initLinesScore( )
	percentage = lines_sum_shanghai.initLinesPerc( )
	colperc = lines_sum_shanghai.initColsPerc( )

	total = 0
	totalperc = 0.0

	x = 0
	y = 0

	for y in range( 2, 23 ):
	#{
		if not ( y == 22 ):
		#{
			for x in range( 6, 23, 8 ):
			#{
				inp = 0 
				while ( True ):
				#{
					inp = u.getch( )
					if ( inp == 48 ):
					#{
						table_fill_shanghai.pointNoScore( stdscr, y, x )
						break
					#}
					elif ( inp == 49 ):
					#{
						table_fill_shanghai.pointSingle( stdscr, y, x )
						total += ( y - 1 )
						break
					#}
					elif ( inp == 50 ):
					#{
						table_fill_shanghai.pointDouble( stdscr, y, x )
						total += ( y - 1 ) * 2
						break
					#}
					elif ( inp == 51 ):
					#{
						table_fill_shanghai.pointTriple( stdscr, y, x )
						total += ( y - 1 ) * 3
						break
					#}
				#}
				lines_sum_shanghai.update( y, percentage, inp, stdscr, total, score, colperc, x )
			#}
		#}		
		else:
		#{
			for x in range( 6, 23, 8 ):
			#{
				while ( True ):
				#{
					inp = u.getch( )
					if ( inp >= 48 and inp <= 50 ):
					#{
						type_ = table_fill_shanghai.pointBull( stdscr, y, x, inp - 48 )
						#print( str( inp - 48 ) )
						if ( inp - 48 == 1 ):
							total += ( y + 3 )
						elif ( inp - 48 == 2 ):
							total += ( y + 3 ) * 2
						break
					#}
				#}
				lines_sum_shanghai.update( y, percentage, inp, stdscr, total, score, colperc, x )
			#}
		#}
	#}
#}

def init( ):
#{
	global u
	import unicurses as u

	global lines_sum_shanghai
	import shanghai.lines_sum_shanghai as lines_sum_shanghai

	global table_fill_shanghai
	import shanghai.table_fill_shanghai as table_fill_shanghai
#}