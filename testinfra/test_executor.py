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

testinfra_hosts = ['executor.f32', 'executor.focal']


def test_executor_config(host):
    config = host.file('/etc/apimon/apimon-executor.yaml')
    secure_config = host.file('/etc/apimon/apimon-executor-secure.yaml')
    assert config.exists
    assert secure_config.exists

    assert b'test_alerta_endpoint' in config.content
    assert b'alerta_token' in secure_config.content

    assert b'db_url: postgresql://dummy' in secure_config.content


def test_executor_systemd(host):
    service = host.service('apimon-executor')
    assert service.is_enabled
