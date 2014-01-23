def helpCheck( arguments ):
#{
	#print( type(arguments) )
	for item in arguments:
	#{
		#print ( item )
		if ( item.lower()  == "help" ):
		#{
			return False
		#}
		elif ( item.lower() == "version" or item.lower() == "copyright" ):
		#{
			print( "(C) 2014 by Divinus01 \nVersion: 1.02.00 \nGNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007 \nFor further information see LICENCE" )
			return False
		#}
	#}
	return True
#}

def startGame( game, max_y, max_x, stdscr ):
#{
	if ( game.lower( ) == "shanghai" ):
	#{
		build_shanghai.build( stdscr, max_y, max_x )
		game_shanghai.start( stdscr )
	#}
#}

def init_colors( ):
#{
	colors = [ ]
	colors.append( None )
	u.init_pair( 1, u.COLOR_YELLOW, u.COLOR_BLACK )
	u.init_pair( 2, u.COLOR_GREEN, u.COLOR_BLACK )
	u.init_pair( 3, u.COLOR_RED, u.COLOR_BLACK )
	colors.append( u.color_pair( 1 ) )
	colors.append( u.color_pair( 2 ) )
	colors.append( u.color_pair( 3 ) )
	return colors
#}

def init( ):
#{
	global lines_sum_shanghai
	import shanghai.lines_sum_shanghai as lines_sum_shanghai

	global build_shanghai
	import shanghai.build_shanghai as build_shanghai

	global game_shanghai
	import shanghai.game_shanghai as game_shanghai

	global u
	import unicurses as u
#}