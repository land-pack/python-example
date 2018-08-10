import os
import ConfigParser

Config = ConfigParser.ConfigParser()
final_path = '/app/config.ini'
if os.path.exists(final_path):
    Config.read(final_path)
else:
    prefix_path = os.path.dirname(os.path.abspath(__file__))
    final_path = os.path.join(prefix_path, 'config.ini')

Config.read(final_path)

print(">>>>>>>>>>>>", final_path)
