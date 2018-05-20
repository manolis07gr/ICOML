def func_industry(industry):

	fintech = ['business services','businessservices','consulting','fintech','banking','finance','trade','trading','exchange','crowdfunding','business','investment','financial services','bank services','financialservices','bankservices','payments','banking&payments']
	blockchain = ['blockchain','mining','cryptocurrency','smart contract','smartcontract','blockchain service','decentralized','blockchain infrastructure','dapp','blockchaininfrastructure']
	real_estate = ['real estate','housing','lodging','hotels','realestate']
	social_service = ['social service','community service','charity','education','socialservice']
	entertainment = ['entertainment','music','film','events','video','sports']
	gaming = ['gaming','vr','gaming&vr','video games','virtual reality','gaming & vr','videogames']
	gambling = ['gambling','casino','casino & gambling','casino&gambling','betting']
	ecommerce = ['ecommerce','commerce','retail']
	saas = ['saas','computing','data storage','datastorage','computing & data storage','software as a service','softwareasaservice','software','data services','cloud services','dataservices','cloudservices','cloud','cloud storage','cloudstorage','data','big data','internet','platform','protocol','marketing','advertising','identity','verification','security','app','it']
	transportation = ['transport','infrastructure','travel','tourism','vacations']
	law = ['legal','law','legal services','legalservices']
	insurances = ['insurance','health','healthcare']
	telecom = ['telecommunications','communication','media','social media','social network','socialnetwork']
	energy = ['energy']
	
	if industry in fintech:
		industry_category = 'fintech'
	if industry in blockchain:
		industry_category = 'blockchain'
	if industry in real_estate:
		industry_category = 'real estate'
	if industry in social_service:
		industry_category = 'social services'
	if industry in entertainment:
		industry_category = 'entertainment'
	if industry in gaming:
		industry_category = 'gaming'
	if industry in gambling:
		industry_category = 'gambling'
	if industry in ecommerce:
		industry_category = 'ecommerce'
	if industry in saas:
		industry_category = 'saas'
	if industry in transportation:
		industry_category = 'transportation'
	if industry in law:
		industry_category = 'legal services'
	if industry in insurances:
		industry_category = 'insurance services'
	if industry in telecom:
		industry_category = 'telecommunications'
	if industry in energy:
		industry_category = 'energy'
	if industry not in (fintech+blockchain+real_estate+social_service+entertainment+gaming+gambling+ecommerce+saas+transportation+law+insurances+telecom+energy):
		industry_category = 'other'
	
	
	return industry_category
