# -*- coding: utf-8 -*-

import sys
import os
import operator
sys.path.insert(1, os.path.abspath('..'))
from wsinfo import Info

cnt = 0
max_cnt = 100
servers = {}

with open("urls.txt", "r") as f:
    for url in f.readlines():
        url = url[:-1]
        try:
            w = Info(url)
            if type(w.server) == list:
                server = w.server[0]
            else:
                server = ""
            if server:
                if server not in servers:
                    servers[server] = 1
                else:
                    servers[server] += 1
            print("{:35}  {:15}  {:3}  {:15}".format(
                w._url, w.ip, w.http_status_code, server))
        except Exception as e:
            print("{:35}  {}".format(url, e))
        cnt += 1
        if cnt >= max_cnt:
            break

    print("="*80)
    print("Web server ranking:")
    rank = sorted(servers.items(), key=operator.itemgetter(1), reverse=True)
    for n in range(len(rank)):
        print("#{:2} {} ({})".format(n+1, rank[n][0], rank[n][1]))
