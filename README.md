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

```console
$ lit --version
lit 19.1.7dev
```

What am I doing wrong?

