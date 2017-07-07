#!/usr/bin/python3
# This file is part of NDR.
#
# NDR is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# NDR is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NDR.  If not, see <http://www.gnu.org/licenses/>.

'''Creates status messages for NDR'''

import ndr

def main():
    '''Entry point'''
    ndr_config = ndr.Config('/etc/ndr/config.yml')
    ingest_message = ndr.IngestMessage(
        ndr_config, ndr.IngestMessageTypes.STATUS
    )

    ingest_message.sign_report()
    ingest_message.load_into_queue()

if __name__ == "__main__":
	main()