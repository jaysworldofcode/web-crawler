import sys
import os
from starter import Starter
from lib.modules.selenium_parser import SeleniumParser
from dotenv import load_dotenv

load_dotenv()


print('░░░█░█░█▀▀░█▀▄░░░█▀▀░█▀▄░█▀█░█░█░█░░░█▀▀░█▀▄░░░')
print('░░░█▄█░█▀▀░█▀▄░░░█░░░█▀▄░█▀█░█▄█░█░░░█▀▀░█▀▄░░░')
print('░░░▀░▀░▀▀▀░▀▀░░░░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀░░░')

Starter(
    command_args=sys.argv,
    parser=SeleniumParser,
    generated_report=os.environ.get("GENERATED_REPORT")
)