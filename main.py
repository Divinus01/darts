#!/usr/bin/env python3

import sys
import utility
from unicurses import *

import shanghai.build_shanghai as build_shanghai
import shanghai.table_fill_shanghai as table_fill_shanghai
import shanghai.lines_sum_shanghai as lines_sum_shanghai
import shanghai.game_shanghai as game_shanghai


def init_all( ):
#{
	build_shanghai.init( )
	table_fill_shanghai.init( )
	lines_sum_shanghai.init( )
	utility.init( )
	game_shanghai.init( )
#}

def main( ):
#{
	stdscr = initscr( )
	move( 5, 5 )
	noecho( )
	curs_set( False )
	keypad( stdscr, False )
	start_color( )
	game = args[ 1 ]

	max_y, max_x = getmaxyx( stdscr )

	if not ( args[ 1 ] == None ):
	#{
		utility.startGame( game, max_y, max_x, stdscr )
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
		#print ( "here" )
		#i = input()
		main( )
	#}
#}