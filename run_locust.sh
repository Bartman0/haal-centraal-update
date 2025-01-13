#!/bin/bash
locust -f locust/locustfile.py -H http://localhost:8083 --headless -u 100 -r 10 -t 15
