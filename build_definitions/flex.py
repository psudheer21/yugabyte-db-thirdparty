#
# Copyright (c) YugaByte, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations
# under the License.
#

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from build_definitions import *

class FlexDependency(Dependency):
    def __init__(self):
        super(FlexDependency, self).__init__(
                'flex', '2.6.4',
                'https://github.com/westes/flex/releases/download/v{0}/flex-{0}.tar.gz',
                BUILD_GROUP_COMMON)
        self.copy_sources = True

    def build(self, builder):
        builder.build_with_configure(builder.log_prefix(self), ['--with-pic'])
