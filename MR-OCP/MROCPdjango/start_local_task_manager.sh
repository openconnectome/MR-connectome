#!/bin/bash
# Copyright 2014 Open Connectome Project (http://openconnecto.me)
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

# Coz I keep forgetting!

# Start the webserver!
sudo rabbitmq-server -detached
sudo supervisord -c /etc/supervisord.conf
#sudo rabbitmq-server
# rabbitmqctl stop
#sudo supervisorctl stop mrocp:
#sudo supervisorctl start mrocp:
#sudo supervisorctl restart mrocp: