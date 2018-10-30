import os
import subprocess

from ClientConfiguration import COMM_HASH

my_env = os.environ.copy()
my_env["TEZOS_CLIENT_UNSAFE_DISABLE_DISCLAIMER"] = "Y"

from NetworkConfiguration import network_config_map

network_config = network_config_map["ZERONET"]
process = subprocess.Popen(COMM_HASH.replace("%network%", network_config['NAME'].lower()), shell=True, stdout=subprocess.PIPE,env=my_env,bufsize=1,universal_newlines=True)

for line in process.stdout:
    print(line,end='')

process.wait()