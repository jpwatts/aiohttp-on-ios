import functools

import json


json_encode = functools.partial(json.dumps, separators=(',', ':'), sort_keys=True)
json_decode = json.loads
