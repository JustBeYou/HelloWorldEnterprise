import unittest
from . import Hello

loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(Hello))

runner = unittest.TextTestRunner(verbosity = 3)
result = runner.run(suite)
