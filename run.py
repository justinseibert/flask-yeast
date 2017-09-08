import os
import sys
from app.app import create_app

try:
    config = sys.argv[1]
except:
    config = 'PRODUCTION'

app = create_app(config=config)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
