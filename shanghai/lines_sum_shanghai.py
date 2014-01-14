class LinesScore:
#{
	def __init__( self, number ):
	#{
		self.pos_y = 1 + number
		self.pos_x = 31
		self.score = 0
	#}
#}

class LinesPerc:
#{
	def __init__( self, number ):
	#{
		self.pos_y = 1 + number
		self.pos_x = 38
		self.hit = 0
		self.call = 1
		self.perc = 0.0
	#}
#}

class ColsPerc:
#{
	def __init__( self, number ):
	#{
		self.pos_y = 24
		self.pos_x = number
		self.hit = 0
		self.call = 1
		self.perc = 0.0
	#}
#}

def initLinesScore( ):
#{
	f = { }
	for i in range( 1, 22 ):
	#{		
		f[ i ] = LinesScore( i )
	#}
	return f
#}

def initLinesPerc( ):
#{
	f = { }
	for i in range( 1, 22 ):
	#{		
		f[ i ] = LinesPerc( i )
	#}
	return f
#}

def initColsPerc( ):
#{
	f = { }
	for i in range( 6, 31, 8):
	#{		
		f[ i ] = ColsPerc( i )
	#}
	return f
#}

def updateLinesScore( line, fields, inp, stdscr ):
#{
	#print( fields )
	for i in range( 1, 22 ):
	#{
		if ( fields[ i ].pos_y == line ):
		#{
			#print( "-{:d}-".format( i ) )
			item = fields[ i ]
			if not ( i == 21 ):
			#{
				item.score += ( inp - 48 ) * i
			#}
			else:
			#{
				item.score += ( inp - 48 ) * 25
			#}

			if ( item.score >= 100 ):
			#{
				u.move( item.pos_y, item.pos_x )
			#}
			elif ( item.score >= 10 ):
			#{
				u.move( item.pos_y, item.pos_x + 1 )
			#}
			else:
			#{				
				u.move( item.pos_y, item.pos_x + 2)
			#}
			u.addstr( str( item.score ) )
			break
		#}
	#}
#}

def updateLinesPerc( line, fields, inp, stdscr ):
#{
	#print( fields )
	for i in range( 1, 22 ):
	#{
		if ( fields[ i ].pos_y == line ):
		#{
			#print( "-{:d}-".format( i ) )
			item = fields[ i ]
			if not ( i == 21 ):
			#{
				item.hit += ( inp - 48 ) / 3
				item.perc = item.hit / item.call * 100
				item.call += 1
			#}
			else:
			#{
				item.hit += ( inp - 48 ) / 2
				item.perc = item.hit / item.call * 100
				item.call += 1
			#}

			u.move( item.pos_y, item.pos_x )

			if ( item.perc >= 100 ):
			#{
				u.addstr( str( round( item.perc, 1 ) ) )
			#}
			elif ( item.perc >= 10 ):
			#{
				u.addstr( " " + str( round( item.perc, 1 ) ) )
			#}
			else:
			#{
				u.addstr( "  " + str( round( item.perc, 1 ) ) )
			#}
			break
		#}
	#}
#}

def updateTotal( tot, stdscr, percentage, y, x ):
#{
	u.move( 24, 46 )
	u.addstr( str( tot ) )
	pointperc = ( tot / getTotal( x, y ) ) * 100
	u.move( 24, 30 )

	if ( round( pointperc, 1 ) == 100 ):
	#{
		u.addstr( str( round( pointperc, 1 ) ) )
	#}
	elif ( round( pointperc, 1 ) >= 10 ):
	#{
		u.addstr( " " + str( round( pointperc, 1 ) ) )
	#}
	else:
	#{
		u.addstr( "  " + str( round( pointperc, 1 ) ) )
	#}

	yl = y
	totalperc = 0.0
	u.move( 24, 38 )
	while ( yl >= 2 ):
	#{
		totalperc += percentage[ yl - 1 ].perc
		yl -= 1
	#}
	totalperc = totalperc / ( y - 1 )

	if ( round( totalperc, 1 ) == 100 ):
	#{
		u.addstr( str( round( totalperc, 1 ) ) )
	#}
	elif ( round( totalperc, 1 ) >= 10 ):
	#{
		u.addstr( " " + str( round( totalperc, 1 ) ) )
	#}
	else:
	#{
		u.addstr( "  " + str( round( totalperc, 1 ) ) )
	#}
#}

def updateColsPerc( stdscr, colperc, x, inp, y ):
#{
	#print( fields )
	for i in range( 6, 31, 8 ):
	#{
		if ( colperc[ i ].pos_x == x ):
		#{
			#print( "-{:d}-".format( i ) )
			item = colperc[ i ]
			if not ( y == 22 ):
			#{
				item.hit += ( inp - 48 ) / 3
				item.perc = item.hit / item.call * 100
				item.call += 1
			#}
			else:
			#{
				item.hit += ( inp - 48 ) / 2
				item.perc = item.hit / item.call * 100
				item.call += 1
			#}

			u.move( item.pos_y, item.pos_x )

			if ( item.perc >= 100 ):
			#{
				u.addstr( str( round( item.perc, 1 ) ) )
			#}
			elif ( item.perc >= 10 ):
			#{
				u.addstr( " " + str( round( item.perc, 1 ) ) )
			#}
			else:
			#{
				u.addstr( "  " + str( round( item.perc, 1 ) ) )
			#}
			break
		#}
	#}
#}

def getTotal( x, y ):
#{
	maxp = 0
	xl = x
	yl = y - 1
	i = 9

	while ( yl > 1 ):
	#{
		maxp += i
		i += 9
		yl -= 1
	#}

	if not ( y == 22 ):
	#{
		if ( x == 6 ):
		#{
			maxp += i / 3
		#}
		elif ( x == 14):
		#{
			maxp += ( 2 * i ) / 3
		#}
		else:
		#{
			maxp += i
		#}
	#}
	else:
	#{
		if ( x == 6 ):
		#{
			maxp += 50
		#}
		elif ( x == 14):
		#{
			maxp += 100
		#}
		else:
		#{
			maxp += 150
		#}
	#}

	return maxp
#}

def update( y, percentage, inp, stdscr, total, score, colperc, x ):
#{
	updateLinesScore( y, score, inp, stdscr )
	updateLinesPerc( y, percentage, inp, stdscr )
	updateTotal( total, stdscr, percentage, y, x )
	updateColsPerc( stdscr, colperc, x, inp, y )
#}

def init( ):
#{
	global u
	import unicurses as u
#}