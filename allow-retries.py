# ALLOW_RETRIES: 10

# RUN: /usr/bin/python3 "%s" | FileCheck --color --dump-input=always "%s"

import sys
from datetime import datetime

# Make this program artificially flaky by only passing every 7th second
if datetime.now().second % 7 == 0:
    print("Current second IS a multiple of 7")
    # CHECK: Current second IS a multiple of 7
    sys.exit(0)

print("Current second is NOT a multiple of 7")
sys.exit(1)