import itunespy

try:
	moviesearch = (itunespy.search_movie('dafdsafdsa'))

	r = 1
	x = []
	for m in moviesearch:
		x.append(m)
		r += 1

	print (x)

except:
	x = []
	print ('error', x)