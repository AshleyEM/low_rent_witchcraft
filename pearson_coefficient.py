# Calculate the Pearson's correlation coefficient and linear regression line given data points [xi],[yi]
# English: Find out if two things are strongly correlated 
# NOTE: This only calculates linear correlations between interval/ratio (numerical) values

from __future__ import division

listx = [88,98,96,98,101,100,168,106,104,122,155,150,123,103,98,103,106] # bpm 
listy = [6,5,4,3.5,3,3,3,3,3,3,3,1,1,3,2,2,2] # plays on spotify in millions rounded 

# takes xi and yi lists; independant variable string name and dependant variable string name
def linearRegression(listx,listy, varX, varY):
		
	# RETURN mean (float)
	def mean(list):
		x = 0;
		n = 0;
		for i in list:
			x+=i
			n+=1;
		return x/n	
	
	# RETURN Pearson's r (float)	
	def pearsonR(listx,listy): # sum( (x-xb)(y-yb) ) / sq[ sum( (x-xb)^2 ) ] * sq[ sum( (x-yb)^2 ) ]
		covar = 0.0
		sumx = 0.0
		sumy = 0.0
		rootsumx = 0.0
		rootsumy = 0.0
		
		for x,y in zip(listx,listy):
			covar += ( x-mean(listx) )*( y-mean(listy) ) 
		
		for x,y in zip(listx,listy):
			sumx += (x-mean(listx))**2
			sumy += (y-mean(listy))**2
			
		rootsumx += (sumx)**0.5
		rootsumy += (sumy)**0.5
			
		r = covar/(rootsumx*rootsumy)
		return r			

	# PRINT description of linear regression line  Y = a + bX
	def line(listx,listy):
		# calculate b
		def b(listx,listy):
			covar = 0.0 # covariance
			var = 0.0 # variance
			for x,y in zip(listx,listy):
				covar += ( x-mean(listx) )*( y-mean(listy) )
				var += ( x-mean(listx) )**2
			return covar/var	
				
		b = round(b(listx,listy),2)
		a = mean(listy) - ( b*mean(listx) )
		
		if b < 0:
			print "For every 1 increase in ["+varX+"] there is a",b,"decrease in ["+varY+"]."
		else:
			print "For every 1 increase in ["+varX+"] there is a",b,"increase in ["+varY+"]."
			
			
		
	if abs(pearsonR(listx,listy)) <= 0.7 and abs(pearsonR(listx,listy)) > 0.5:
		print "r =",pearsonR(listx,listy)
		print "There is a moderate correlation between ["+varX+"] and ["+varY+"]."
		print ""
		line(listx,listy)
	elif abs(pearsonR(listx,listy)) <= 0.5 and abs(pearsonR(listx,listy)) >= 0.4:
		print "r =",pearsonR(listx,listy)
		print "(!) The correlation between ["+varX+"] and ["+varY+"] is weak; I wouldn't make any solid conclusions."
		print ""
		line(listx,listy)	
	elif abs(pearsonR(listx,listy)) <= 0.3 and abs(pearsonR(listx,listy)) > 0:
		print "r =",pearsonR(listx,listy)
		print "(!) The correlation between ["+varX+"] and ["+varY+"] is negligable."
	elif pearsonR(listx,listy) == 0:
		print "(!) There is no correlation between ["+varX+"] and ["+varY+"]."
	else:
		print "r =",pearsonR(listx,listy)
		print "There is a strong correlation between ["+varX+"] and ["+varY+"]."
		line(listx,listy)	
# -------------------

linearRegression(listx,listy,"beats per minute","plays on spotify (millions)")

