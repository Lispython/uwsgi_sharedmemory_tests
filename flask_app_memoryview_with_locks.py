#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Working with sharedmemory counters with locks
"""

import os
import uwsgi
import struct

from flask import request, Response, Flask
from string import ascii_letters
from random import choice


app = Flask(__name__)
app.debug = True



@app.route('/<path:path>')
@app.route('/')
def index(path='/'):
    uwsgi.sharedarea_wlock(0)
    memoryview = uwsgi.sharedarea_memoryview(0)
    counter = struct.unpack(b'i', memoryview[0:4])[0]
    new_counter = counter + 1
    memoryview[0:4] = struct.pack(b'i', new_counter)
    uwsgi.sharedarea_unlock(0)
    counter = struct.unpack(b'i', memoryview[0:4])[0]

    if new_counter != counter:
        print("Invalid data: {0} - {1}".format(new_counter, counter))

    text = "# Process in {0}\nCounter: {1}\n\n".format(os.getpid(), new_counter)
    return Response(text, mimetype="text/plain")


application = app
print("Debug app init")
