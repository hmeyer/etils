# Copyright 2023 The etils Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Environment utils."""

import os
import sys


def is_notebook() -> bool:
  """Returns True if running in a notebook (Colab, Jupyter) environment."""
  # Use sys.module as we do not want to trigger an import (slow)
  # Check whether we're not running in a IPython terminal
  if IPython := sys.modules.get('IPython'):  # pylint: disable=invalid-name
    get_ipython_result = IPython.get_ipython()
    if get_ipython_result and 'IPKernelApp' in get_ipython_result.config:
      return True
  return False


def is_ipython_terminal() -> bool:
  """Returns True if running in a IPython terminal environment."""
  if IPython := sys.modules.get('IPython'):  # pylint: disable=invalid-name
    get_ipython_result = IPython.get_ipython()
    if (
        get_ipython_result
        and type(get_ipython_result).__name__ == 'TerminalInteractiveShell'
    ):
      return True
