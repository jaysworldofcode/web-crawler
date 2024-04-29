from lib.interface.iurl_parser import IUrlParser

class AppState(object):
    
	target_site:str = None
	recursion_depth_limit:int = 0
	parser:IUrlParser = None
	next_url_target:list[str] = None
	web_driver = None
	generated_report = None
	found_hostnames:list[str] = []
	found_hostnames_count:list[int] = []
	total_pages_scanned:int = 0

	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(AppState, cls).__new__(cls)
		return cls.instance