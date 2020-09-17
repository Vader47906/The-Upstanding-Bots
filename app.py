import os
import json

from flask import Flask, request, Response, abort
from config import *
from bots import *

app = Flask(__name__)

bots = {#"mdavis": MattDavisBot(os.environ.get('MD_BOT_ID')),
        #"kgeorge": KyleGeorgeBot(os.environ.get('KG_BOT_ID')),
        "mklug": MichaelKlugBot(os.environ.get('MK_BOT_ID')),
        "hbreyne": HenryBreyneBot(os.environ.get('HB_BOT_ID'))
        }

@app.route('/<identifier>', methods=['POST'])
def run(identifier):
    if identifier in bots:
        bots[identifier].on_receive_message(request.json)
        return ""
    else:
        abort(404)
        
if __name__ == "__main__":
    app.run(host='0.0.0.0')
