def points( stdscr, y, x, inp, colors ):
#{
	pos_y = y
	pos_x = x
	u.move( pos_y, pos_x )
	prfix = ""
	suffix = None
	pick = 0

	if ( inp == 48 ):
	#{
		u.addstr( " --- " )
		return pick
	#}
	elif ( inp == 49 ):
	#{
		prfix = " "
		pick = 1
	#}
	elif ( inp == 50 ):
	#{
		prfix = "D"
		pick = 2
	#}
	elif ( inp == 51 ):
	#{
		prfix = "T"
		pick = 3
	#}

	if ( y != 22 ):
	#{
		suffix = y - 1
	#}
	else:
	#{
		suffix = "BL"
		pick = 2
		if ( inp == 50 ):
		#{
			prfix = "B"
			suffix = "LL"
			pick = 3
		#}
	#}

	if ( pick != None ):
	#{
		if ( y < 11 ):
		#{
			u.addstr( " {}0{} ".format( prfix, suffix ), colors[ pick ]  )
		#}
		else:
		#{
			u.addstr( " {}{} ".format( prfix, suffix ), colors[ pick ] )
		#}
	#}
	return pick
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