def build( stdscr, max_y, max_x ):
#{
	u.move( 1, 0 )
	u.hline( u.ACS_HLINE, 52 )
	u.move( 23, 0 )
	u.hline( u.ACS_HLINE, 52 )
	u.move( 1, 4 )
	downs( stdscr, 4, 6, 7 )

	i = 1
	while i != 24:
	#{
		if ( i - 10 < 0 ):
		#{
			u.move( i + 1, 2 )
			u.addstr( str( i ) )
		#}
		elif ( i == 21 ):
		#{
			u.move( i + 1, 0 )
			u.addstr( "BULL" )
		#}
		elif ( i == 22 ):
		#{
			i += 1
			continue
		#}
		elif ( i == 23 ):
		#{
			u.move( i + 1, 0 )
			u.addstr( "  % " )
		#}
		else:
		#{
			u.move( i + 1, 1 )
			u.addstr( str( i ) )
		#}
		i += 1
	#}
	u.move( 22, 46 )
	u.addstr( "TOTAL" )
#}

def downs( stdscr, start, count, cols ):
#{
	num = 1
	for i in range( start, start + ( cols + 1 ) * count, cols + 1 ):
	#{
		u.move( 0, i )
		u.vline( u.ACS_VLINE, 25 )
		u.move( 0, i + 2 ) 
		if ( num <= 3 ):
		#{
			u.addstr( "DART{:d}".format( num ) )
		#}
		elif ( num == 4 ):
		#{
			u.addstr( "POINT" )
		#}	
		elif ( num == 5 ):
		#{
			u.addstr( "  %  " )
		#}	
		num += 1
	#}
#}

def init( ):
#{
	global u
	import unicurses as u
#}