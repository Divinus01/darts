#!/usr/bin/env python3

import sys
from unicurses import *


def init_all( ):
#{
	global bulid_shanghai
	import build_shanghai

	global table_fill_shanghai
	import table_fill_shanghai

	global lines_sum_shanghai
	import lines_sum_shanghai

	global utility
	import utility

	build_shanghai.init()
	table_fill_shanghai.init()
	lines_sum_shanghai.init()
	utility.init()
#}

def main( ):
#{
	stdscr = initscr( )
	move( 5, 5 )
	noecho( )
	curs_set( False )
	keypad( stdscr, False )
	start_color( )
	score = lines_sum_shanghai.initLinesScore( )
	percentage = lines_sum_shanghai.initLinesPerc( )
	colperc = lines_sum_shanghai.initColsPerc( )

	total = 0
	totalperc = 0.0

	max_y, max_x = getmaxyx( stdscr )

	col_width = 7

	if not ( args[ 1 ] == None ):
	#{
		utility.startGame( args[ 1 ], max_y, max_x, stdscr, col_width )
	#}

	x = 0
	y = 0

	for y in range( 2, 23 ):
	#{
		if not ( y == 22 ):
		#{
			for x in range( 6, 6 + col_width * 3, col_width + 1 ):
			#{
				inp = 0 
				while ( True ):
				#{
					inp = getch( )
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
				utility.update( y, percentage, inp, stdscr, total, score, colperc, x )
			#}
		#}		
		else:
		#{
			for x in range( 6, 6 + col_width * 3, col_width + 1 ):
			#{
				while ( True ):
				#{
					inp = getch( )
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
				utility.update( y, percentage, inp, stdscr, total, score, colperc, x )
			#}
		#}
	#}

	while ( True ):
	#{
		key = getch( )
		if ( key == 27 ):
		#{
			break
		#}
	#}
	endwin( )
#}

if ( __name__ == "__main__" ):
#{
	init_all( )

	args = sys.argv

	start_main = utility.helpCheck( args )
	if ( start_main ):
	#{
		main( )
	#}
#}