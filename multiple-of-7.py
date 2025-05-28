# ALLOW_RETRIES: 10

# RUN: /usr/bin/python3 "%s" "%{current_second}" | FileCheck --color --dump-input=always "%s"

import sys
from datetime import datetime

current_second = int(sys.argv[1])

print("Running test")
# CHECK: Running test

# Make this program artificially flaky by only passing every 7th second
if current_second % 7 == 0:
    print(f"Current second IS a multiple of 7: {current_second}")
    # dddCHECK-kdkd: Current second IS a multiple of 7
    sys.exit(0)

print(f"Current second is NOT a multiple of 7: {current_second}")
sys.exit(1)