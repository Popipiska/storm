import os
import json
import shutil

currentDir = os.path.dirname(os.path.realpath(__file__))

def main() -> None:
    with open(currentDir + '/machines_list.json') as json_file:
        machines_list = json.load(json_file)

    if not os.path.isfile(currentDir + "/storm-force.zip"):
        shutil.make_archive("storm-force", "zip", root_dir=currentDir+"/../", base_dir="storm-force/")

    for ip in machines_list:
        firstPartSshQuery = f"sshpass -p '{machines_list[ip]['password']}'"
        os.system(f"{firstPartSshQuery} scp {currentDir}/install.sh {machines_list[ip]['user']}@{ip}:/tmp/")
        os.system(f"{firstPartSshQuery} scp {currentDir}/storm-force.zip {machines_list[ip]['user']}@{ip}:/tmp/")
        os.system(f"{firstPartSshQuery} ssh {machines_list[ip]['user']}@{ip} 'cd /tmp && sudo sh ./install.sh'")
        commandInstallRequirements = f"{firstPartSshQuery} ssh {machines_list[ip]['user']}@{ip} 'cd /tmp/storm-force && source ./venv/bin/activate && pip3 install -r ./requirements.txt'"
        os.system(f"{commandInstallRequirements} &")

if __name__ == "__main__":
    main()