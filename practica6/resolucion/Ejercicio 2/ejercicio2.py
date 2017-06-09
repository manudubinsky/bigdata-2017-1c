#!/usr/bin/python
# -*- coding: utf-8 -*-

import rethinkdb as r

r.connect("localhost",28015).repl()

cursor = r.table("tweets").group(lambda tweet: tweet["source"]).map(lambda tweet: 1).reduce(lambda a, b: a + b).run();

print cursor
