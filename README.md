# README

I try to find out how we can run LLVM `lit` tests and configure them.

## Artificial flakiness

When building LLVM and running its test we sometime experience flaky tests the
work the second time you run them.

To reproduce this flakyness I've created a test called `allow-retries.py`.

The `allow-retries.py` test file will only succeed (exit with `0`)
when the current second is a multiple of `7`.

When it succeeds it prints: `Current second IS a multiple of 7`.
When it fails it prints: `Current second is NOT a multiple of 7`

The LLVM codebase also has an
[`allow-retries.py`](https://github.com/llvm/llvm-project/blob/main/llvm/utils/lit/tests/allow-retries.py)
test file from which I borrowed ideas on how to instruct `lit` to retry the test execution.

1. `# ALLOW_RETRIES: 10` in the test file
2. `config.allowed_retries = 15` in the config file (`lit.cfg.py`)
3. `-Dtest_retry_attempts=20` in the call to `lit` (see `Makefile`)

None of the above trigger a re-run of the test. 

## Example output

```console
$ make
lit allow-retries.py -Dcurrent_second=1748445674 -Dtest_retry_attempts=20 -vv --debug
lit: /usr/lib/python3.13/site-packages/lit/discovery.py:66: note: loading suite config '/home/fedora/src/allow-retries/lit.cfg.py'
lit: /usr/lib/python3.13/site-packages/lit/TestingConfig.py:142: note: ... loaded config '/home/fedora/src/allow-retries/lit.cfg.py'
lit: /usr/lib/python3.13/site-packages/lit/discovery.py:141: note: resolved input 'allow-retries.py' to 'allow-retries'::('allow-retries.py',)
-- Testing: 1 tests, 1 workers --
FAIL: allow-retries :: allow-retries.py (1 of 1)
******************** TEST 'allow-retries :: allow-retries.py' FAILED ********************
Exit Code: 1

Command Output (stdout):
--
# RUN: at line 3
/usr/bin/python3 "/home/fedora/src/allow-retries/allow-retries.py" "1748445674" | FileCheck --color --dump-input=always "/home/fedora/src/allow-retries/allow-retries.py"
# executed command: /usr/bin/python3 /home/fedora/src/allow-retries/allow-retries.py 1748445674
# note: command had no output on stdout or stderr
# error: command failed with exit status: 1
# executed command: FileCheck --color --dump-input=always /home/fedora/src/allow-retries/allow-retries.py
# .---command stderr------------
# | /home/fedora/src/allow-retries/allow-retries.py:16:11: error: CHECK: expected string not found in input
# |  # CHECK: Current second IS a multiple of 7
# |           ^
# | <stdin>:1:13: note: scanning from here
# | Running test
# |             ^
# | <stdin>:2:1: note: possible intended match here
# | Current second is NOT a multiple of 7: 1748445674
# | ^
# | 
# | Input file: <stdin>
# | Check file: /home/fedora/src/allow-retries/allow-retries.py
# | 
# | -dump-input=help explains the following input dump.
# | 
# | Input was:
# | <<<<<<
# |             1: Running test 
# | check:16'0                 X error: no match found
# |             2: Current second is NOT a multiple of 7: 1748445674 
# | check:16'0     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# | check:16'1     ?                                                  possible intended match
# | >>>>>>
# `-----------------------------
# error: command failed with exit status: 1

--

********************
********************
Failed Tests (1):
  allow-retries :: allow-retries.py


Testing Time: 0.20s

Total Discovered Tests: 1
  Failed: 1 (100.00%)
make: *** [Makefile:3: all] Error 1
```


## Lit version in use

```console
$ lit --version
lit 19.1.7dev
```

# Open questions

* What am I doing wrong?
* How can I make lit retry test execution?
* Is lit not retrying the test because the input to the test hasn't changed?
  * In fact, there's none in my test. Notice the `# note: command had no output on stdout or stderr`
    output in the lit execution.
    * UPDATE: I'm now passing the current second from the command line to the python and no change.



