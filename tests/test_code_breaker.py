# Author: Karina Kallas
# Date Last Modified: Dec. 6, 2023
# Date Last Tested: Dec. 6, 2023

import unittest
from code_breaker import *

# #################################################################################################################### #
#                                                                                                                      #
# TESTS                                                                                                                #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #
class TestCodeBreaker(unittest.TestCase):
    # Is object created by CodeBreaker class?
    def test_create_CodeBreaker_object(self):
        result = CodeBreaker()
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()
