from app_state import AppState
from lib.interface.iurl_parser import IUrlParser
from lib.helpers.csv_helper import write_csv_line, delete_old_report
from lib.helpers.terminal_args_validation_helper import terminal_args_validator
from lib.helpers.get_hostname_from_url_helper import get_hostname_from_url
from lib.helpers.ratio_calculator_helper import ratio_calculator_helper

class Starter:
    
    def __init__(self, parser:IUrlParser, command_args:list[str], generated_report:str):
        print("APP_STARTER_INITIALIZED")

        # validate terminal arguments
        terminal_args_validator(args=command_args)
        # delete old report
        delete_old_report(generated_report)
        
        AppState.target_site            = command_args[1]
        AppState.recursion_depth_limit  = int(command_args[2])
        AppState.generated_report       = generated_report
        AppState.parser                 = parser()

        self.__()
        
    def __(self):
        AppState.next_url_target = self.__fetch_links(url = AppState.target_site)
        
        for x in range(0, AppState.recursion_depth_limit):
            page_depth = x+1
            print(f"====> fetch site dept: {page_depth}")
            results = []
            
            for url in AppState.next_url_target:
                hostname = get_hostname_from_url(url)
                print(f"====> fetching links on url: {hostname}")
                print(f'====> total url found: {len(AppState.next_url_target)}')
                # writing data line by line to avoid corrupt data
                ratio = round(self.__process_url_and_get_ratio(hostname=hostname), 2)
                self.__write_line(url, page_depth, ratio)
                results = results+self.__fetch_links(url)

            # making sure old urls is release
            AppState.next_url_target.clear()
            AppState.next_url_target = results

    def __write_line(self, url:str, depth:int, ratio):
        print(f'====> line added: {url} | {depth} | {ratio}')
        write_csv_line(data=[url,depth,ratio], path=AppState.generated_report)

    def __process_url_and_get_ratio(self, hostname:str):
        AppState.total_pages_scanned += 1
        
        if hostname in AppState.found_hostnames:
            index = AppState.found_hostnames.index(hostname)
            AppState.found_hostnames_count[index] += 1
        else: 
            AppState.found_hostnames.append(hostname)
            AppState.found_hostnames_count.append(1)
            index = len(AppState.found_hostnames)-1
            
        return ratio_calculator_helper(
            total_count_pages_found=AppState.found_hostnames_count[index],
            all_pages_found=AppState.total_pages_scanned
        )
            
    def __fetch_links(self, url:str):
        try:
            parser:IUrlParser = AppState.parser
            parser.parse(url)
        except OSError:
            print(f"====> encounter an error parsing {url}")
            return []
        
        return parser.getLinks()