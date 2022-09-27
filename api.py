import requests
import base64
import time
import json

class YacineTV:

  api_url = "http://ver3.yacinelive.com"
  key = "c!xZj+N9&G@Ev@vw"

  def __init__(self):
    pass

  def decrypt(self, enc, key=key):
    enc = base64.b64decode(enc.encode("ascii")).decode("ascii")
    result = ""
    for i in range(len(enc)):
      result = result + chr(ord(enc[i]) ^ ord(key[i % len(key)]))
    return result

  def req(self, path):
    r = requests.get(self.api_url + path)
    timestamp = str(int(time.time()))
    if "t" in r.headers:
      timestamp = r.headers["t"]

    try:
      return json.loads(self.decrypt(r.text, key=self.key + timestamp))

    except:
      return {
        "success": False,
        "error": "can't parse json."
      }
  
  def get_categories(self):
    return self.req("/api/categories")

  def get_category(self, category_id):
    return self.req("/api/categories/" + str(category_id))

  def get_category_channels(self, category_id):
    return self.req("/api/categories/" + str(category_id) + "/channels")

  def get_channel(self, channel_id):
    return self.req("/api/channel/" + str(channel_id))
  