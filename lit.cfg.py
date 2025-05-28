import os
import sys
import lit.formats
from lit.llvm import llvm_config
import lit.formats

config.test_format = lit.formats.ShTest()

# Configuration file for the 'lit' test runner.

# name: The name of this test suite.
config.name = "allow-retries"

# # testFormat: The test format to use to interpret tests.
# config.test_format = lit.formats.ShTest(execute_external=False)

# suffixes: A list of file extensions to treat as test files.
config.suffixes = [".py"]

# test_source_root: The root path where tests are located.
config.test_source_root = os.path.dirname(__file__)
config.test_exec_root = os.path.dirname(__file__)

config.allowed_retries = 15

config.substitutions.append(("%{current_second}", lit_config.params.get("current_second", "")))

