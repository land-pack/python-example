import os
from project.utils.conf import Config
#import ConfigParser

#Config = ConfigParser.ConfigParser()
#prefix_path = os.path.dirname(os.path.abspath(__file__))
#final_path = os.path.join(prefix_path, 'config.ini')
#Config.read(final_path)
print(Config.sections())

from project.api import create_app




app = create_app()

if __name__ == '__main__':
    port = int(Config.get('server', 'port'))
    print(port)
    app.run(debug=True, port=port)
