

import unittest

from tests.support.ApiV1Repositories import test_HttpApiV1Repository

def load_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_HttpApiV1Repository.TestHttpApiV1Repository_get_today_exchange_rates))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(load_tests())
