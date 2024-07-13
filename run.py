from xemijobs import create_app
import os
from dotenv import load_dotenv
load_dotenv()

app = create_app()

if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG'))
