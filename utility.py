def helpCheck( arguments ):
#{
	for item in arguments:
	#{
		if ( item  == "help" ):
		#{
			return False
		#}
		else:
		#{
			return True
		#}
	#}
#}

def startGame( game, max_y, max_x, stdscr, col_width ):
#{
	back = 0
	if ( game.lower( ) == "shanghai" ):
	#{
		back = build_shanghai.build( stdscr, max_y, max_x, col_width )
	#}
	return back
#}

def update( y, percentage, inp, stdscr, total, score, colperc, x ):
#{
	lines_sum_shanghai.updateLinesScore( y, score, inp, stdscr )
	lines_sum_shanghai.updateLinesPerc( y, percentage, inp, stdscr )
	lines_sum_shanghai.updateTotal( total, stdscr, percentage, y, x )
	lines_sum_shanghai.updateColsPerc( stdscr, colperc, x, inp, y )
#}

def init( ):
#{
	global main
	import main

	global table_fill_shanghai
	import table_fill_shanghai

	global lines_sum_shanghai
	import lines_sum_shanghai

	global build_shanghai
	import build_shanghai
	
	global u
	import unicurses as u
#}