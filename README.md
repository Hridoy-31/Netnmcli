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

### Connecting two network namespaces with veth pair
For connecting two existing network namespaces with veth pair, type the following command:   
    `sudo ./netns_tool.py connect <namespace_name1> <namespace_name2>`   
    where, `<namespace_name1>` is the name of first network namespace for creating a connection. On the other hand, `<namespace_name2>` is the name of the other network namespace that we want to connect with the first network namespace.

 