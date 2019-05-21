def func_industry(industry):

	fintech = ['business services','businessservices','consulting','fintech','banking','finance','trade','trading','exchange','crowdfunding','business','investment','financial services','bank services','financialservices','bankservices','payments','banking&payments','exchanges&wallets','wallets','exchanges','asset management','assetmanagement','baking&payments','banking & payments','business services & consulting','crowdfunding&lending','crowdfunding & lending','exchanges & wallets','exchages&wallets','investment','marketing & advertising','marketing','advertising','prediction markets','commodities','trading & investing']
	blockchain = ['blockchain','currency','cryptocurrency','mining','cryptocurrency','smart contract','smartcontract','blockchain service','decentralized','blockchain infrastructure','dapp','blockchaininfrastructure']
	real_estate = ['real estate','housing','lodging','hotels','realestate','real assets']
	social_service = ['social service','community service','charity','education','socialservice','environmental services','governance & voting','social services & non-profit','socialservicesandnon-profit','non-profit','charity','charity & donations','donations']
	entertainment = ['entertainment','music','film','events','video','sports','adult','art&music','events&entertainment','events & entertainment','media','art']
	gaming = ['gaming','vr','gaming&vr','video games','virtual reality','gaming & vr','videogames','ar&vr']
	gambling = ['gambling','casino','casino & gambling','casino&gambling','betting','gambling & betting']
	ecommerce = ['ecommerce','commerce','retail','commerce&retail','commerce & retail','electronics','commerce & advertising']
	saas = ['saas','computing','data storage','datastorage','computing & data storage','software as a service','softwareasaservice','software','data services','cloud services','dataservices','cloudservices','cloud','cloud storage','cloudstorage','data','big data','internet','platform','protocol','marketing','advertising','business services','consulting','identity','verification','security','app','it','marketing & advertising','computing & data storage','computing&datastorage','data analytics','dataanalytics','identity & reputation','privacy & security','recruitment & crowdsourcing','translation','writing & editing','artificial intelligence','big data','big data & data storage','content management','machine learning']
	transportation = ['transport','infrastructure','travel','tourism','vacations','supply&logistics','supply','logistics','travel & tourism','travel&tourism','manufacturing']
	law = ['legal','law','legal services','legalservices','compliance & security','compliance','regulatory','provenance & notary','notary','provenance']
	insurances = ['insurance','health','healthcare','drugs&healthcare','drugs & healthcare']
	telecom = ['telecommunications','communication','media','social media','social network','socialnetwork','internet','internet&telecommunications','internet & telecommunications','social media & communication']
	energy = ['energy','energy&utilities','science & research','science','research','energy & utilities']
	
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
