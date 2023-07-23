# Netnmcli
A CLI Tool for Network Namespace Management and Veth Connection

## Usage
1. Clone the repository:   
    `git clone https://github.com/Hridoy-31/Netnmcli.git`

2. Change directory to `Netnmcli`:    
    `cd Netnmcli/`

3. Make `netns_tool.py` file as an executable file:   
    `chmod +x netns_tool.py`

### Creating a new network namespace
For creating a new network namespace, type the following command:   
    `sudo ./netns_tool.py create <namespace_name>`   
    where, `<namespace_name>` will be the name of the network namespace that you want to create.

