#  ▄▄   ▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄   ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄ 
# █  █ █  █      █       █   █  █  █ █       █       █  █ █  █  █       █       █   █
# █  █▄█  █  ▄   █       █   █   █▄█ █    ▄▄▄█▄     ▄█  █▄█  █  █   ▄   █    ▄  █   █
# █       █ █▄█  █     ▄▄█   █       █   █▄▄▄  █   █ █       █  █  █▄█  █   █▄█ █   █
# █▄     ▄█      █    █  █   █  ▄    █    ▄▄▄█ █   █ █       █  █       █    ▄▄▄█   █
#   █   █ █  ▄   █    █▄▄█   █ █ █   █   █▄▄▄  █   █  █     █   █   ▄   █   █   █   █
#   █▄▄▄█ █▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄█▄█  █▄▄█▄▄▄▄▄▄▄█ █▄▄▄█   █▄▄▄█    █▄▄█ █▄▄█▄▄▄█   █▄▄▄█

# by aimadnet
# contact: t.me/aimadnet

from flask import Flask
from api import YacineTV

ytv = YacineTV()
app = Flask(__name__)

@app.route('/categories', methods = ['GET'])    
def categories():
  return ytv.get_categories()

@app.route('/categories/<int:category_id>', methods = ['GET'])    
def category(category_id):
  return ytv.get_category(category_id)

@app.route('/categories/<int:category_id>/channels', methods = ['GET'])    
def channels(category_id):
  return ytv.get_category_channels(category_id)

@app.route('/channel/<int:channel_id>', methods = ['GET'])    
def channel(channel_id):
  return ytv.get_channel(channel_id)

app.run(host='0.0.0.0', port=8888, threaded=True, debug=False)