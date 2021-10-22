# Copyright 2016 Dravetech AB. All rights reserved.
#
# The contents of this file are licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

# Import stdlib
import pkg_resources

"""napalm-exos package."""
from napalm_exos.exos import ExosDriver  # noqa F401

try:
    __version__ = pkg_resources.get_distribution('napalm-exos').version
except pkg_resources.DistributionNotFound:
    __version__ = "Not installed"

__all__ = ('ExosDriver',)

# Define the Netbox plugin metadata if Netbox is installed
try:
   from extras.plugins import PluginConfig
except ImportError:
    pass
else:
    class NapalmExosConfig(PluginConfig):
        name = 'napalm_exos'
        verbose_name = 'NAPALM EXOS'
        description = 'NAPALM Driver for EXOS'
        version = '0.1.1'
        author = 'Elisa Jasinska'
        author_email = 'elisa@bigwaveit.org'
        base_url = 'napalm_exos'
        required_settings = []
        default_settings = {
        }

    config = NapalmExosConfig
