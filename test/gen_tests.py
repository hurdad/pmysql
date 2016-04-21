#!/usr/bin/env python

import os

header = """import shutil
import os
import pytest
import subprocess

"""

test_func =  """
def test_{0}():
	proc = subprocess.Popen(['../pmysql', 'query/{1}'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		
"""

fo = open("test_query.py", "w")
fo.write( header)
indir = 'query'
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        fo.write(test_func.format(f.replace('.', '_'), f))

fo.close()