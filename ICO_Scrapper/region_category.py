def func_region(region):

	region1 = ['usa','united states','u.s.','united states of america','canada']
	region2 = ['russia','ukraine','belarus']
	region3 = ['china','hong kong']
	region4 = ['uk','u.k.','united kingdom','england','great britain']
	region5 = ['albania','andorra','austria','belgium','bosnia','bulgaria','croatia','czech republic','denmark','estonia','finland','france','germany','greece','hungary','iceland','ireland','italy','latvia','liechtenstein','lithuania','luxembourg','malta','moldova','monaco','netherlands','norway','poland','portugal','romania','serbia','slovakia','slovenia','spain','sweden']
	region6 = ['switzerland']
	region7 = ['singapore','cayman islands','gibraltar','isle of man','isleofman','virgin islands','british virgin islands','britishvirginislands','virginislands']
	region8 = ['japan','south korea','s. korea']
	region9 = ['australia','new zealand','solomon islands']
	region10 = ['brazil','brasil','argentina','peru','equador','costa rica','panama','nicaragua','belize','mexico','guatemala','equador','chile','venezuela','uruguay','paraguay','honduras','bolivia','colombia']
	region11 = ['south africa','angola','egypt','tunisia']
	
	if region in region1:
		area = 1
	if region in region2:
		area = 2
	if region in region3:
		area = 3
	if region in region4:
		area = 4
	if region in region5:
		area = 5
	if region in region6:
		area = 6
	if region in region7:
		area = 7
	if region in region8:
		area = 8
	if region in region9:
		area = 9
	if region in region10:
		area = 10
	if region in region11:
		area = 11
	if region not in (region1+region2+region3+region4+region5+region6+region7+region8+region9+region10+region11):
		area = 12
	
	
	return area
