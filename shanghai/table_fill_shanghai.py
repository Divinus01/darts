def pointNoScore( stdscr, y, x ):
#{
	pos_y = y
	pos_x = x
	u.move( pos_y, pos_x )
	u.addstr( " --- " )
#}

def pointSingle( stdscr, y, x ):
#{
	pos_y = y
	pos_x = x
	u.move( pos_y, pos_x )
	u.init_pair( 1, u.COLOR_YELLOW, u.COLOR_BLACK )
	if ( y < 11 ):
	#{
		u.addstr( "  0{:d} ".format( y - 1 ), u.color_pair( 1 ) )
	#}
	else:
	#{
		u.addstr( "  {:d} ".format( y - 1 ), u.color_pair( 1 ) )
	#}
#}

def pointDouble( stdscr, y, x ):
#{
	pos_y = y
	pos_x = x
	u.move( pos_y, pos_x )
	u.init_pair( 2, u.COLOR_GREEN, u.COLOR_BLACK )
	if ( y < 11 ):
	#{
		u.addstr( " D0{:d} ".format( y - 1 ), u.color_pair( 2 ) )
	#}
	else:
	#{
		u.addstr( " D{:d} ".format( y - 1 ), u.color_pair( 2 ) )
	#}
#}

def pointTriple( stdscr, y, x ):
#{
	pos_y = y
	pos_x = x
	u.move( pos_y, pos_x )
	u.init_pair( 3, u.COLOR_RED, u.COLOR_BLACK )
	if ( y < 11 ):
	#{
		u.addstr( " T0{:d} ".format( y - 1 ), u.color_pair( 3 ) )
	#}
	else:
	#{
		u.addstr( " T{:d} ".format( y - 1 ), u.color_pair( 3 ) )
	#}
#}

def pointBull( stdscr, y, x, hit ):
#{
	pos_y = y
	pos_x = x
	u.move( pos_y, pos_x )
	u.init_pair( 2, u.COLOR_GREEN, u.COLOR_BLACK )
	u.init_pair( 3, u.COLOR_RED, u.COLOR_BLACK )
	if ( hit == 0 ):
	#{
		u.addstr( " --- " )
	#}
	elif ( hit == 1 ):
	#{
		u.addstr( " SBL ", u.color_pair( 2 ))
	#}
	elif ( hit == 2 ):
	#{
		u.addstr( " DBL ", u.color_pair( 3 ) )
	#}
#}

def updates( ):
#{
	u.update_panels( )
	u.doupdate( )
#}

def init( ):
#{
	global u
	import unicurses as u
#}