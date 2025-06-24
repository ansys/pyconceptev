# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Get optislang version and integration (wrong way round) so special python
# version and inject my code into it.
# Or inject optislang into my code. For the e2e it has to be the first one.
# Therefore lets do the same here.

# USE OPTISLANG PYTHON
import sys

sys.path.append("C:\\Program Files\\ANSYS Inc\\v251\\optiSLang\\lib\\python-modules")
sys.path.append("C:\\Program Files\\ANSYS Inc\\v251\\optiSLang\\scripting\\integrations")

print(sys.path)
import conceptev_ci as conceptev_ci


def test_pass():
    """Test that the optislang integration works."""
    print(dir(conceptev_ci))
    assert True
