# Copyright 2022 The etils Authors.
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

"""Typing utils."""

import os
import typing
from typing import Union

# Accept both `str` and `pathlib.Path`-like
PathLike = Union[str, os.PathLike]
if typing.TYPE_CHECKING:
  # TODO(py3.10): os.PathLike is not suscrible
  PathLike = Union[str, os.PathLike[str]]

PathLikeCls = (str, os.PathLike)  # Used in `isinstance`
