# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
Example Session Command

Make sure you can authenticate before running this command.  This command
is currently hard coded to use the Identity service.

For example:
    python -m examples.session /tenants
"""

import sys

from examples import common
from openstack.auth import service_filter
from openstack import session


def make_session(opts):
    return session.Session.create(
        username=opts.os_username,
        password=opts.os_password,
        token=opts.os_token,
        auth_url=opts.os_auth_url,
        version=opts.os_identity_api_version,
        project_name=opts.os_project_name,
        cacert=opts.os_cacert,
        insecure=opts.insecure,
        user_agent='SDKExample',
        region=opts.os_region_name,
    )


def run_session(opts):
    argument = opts.argument
    if argument is None:
        raise Exception("A path argument must be specified")
    sess = make_session(opts)
    filtration = service_filter.ServiceFilter(service_type='Identity')
    print("Session: %s" % sess)
    print(sess.get(argument, service=filtration).text)
    return


if __name__ == "__main__":
    opts = common.setup()
    sys.exit(common.main(opts, run_session))
