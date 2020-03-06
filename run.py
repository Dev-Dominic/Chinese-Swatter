#! /usr/bin/env python 
# Flask run script

from app import app

if __name__ == "__main__": 
    # Parameters: host, port, debug, options
    app.run("localhost", 8080, True)
