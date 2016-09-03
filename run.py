#!/usr/bin/env python

from app import app

# [WARNING!]
#   Only if you switched on the debug switch can you check out any error messages.
#   Or even a fatal error occurred, you can only see an "Internal Server Error" page without any further detail.
app.run(debug=True)

