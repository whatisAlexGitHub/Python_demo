from netmiko import ConnectHandler
def console_port_security(connection):
    username = '' or input('username:')
    secret = '' or input('secret:')

    config_commands = [
        f'username {username} secret {secret}',
        f'line console 0',
        'login local', 
        'exit',
    ]
    output = connection.send_config_set(config_commands)
    print(output)

def ssh(connection):
    hostname = '' or input('hostname:')
    domain_name = '' or input('domain_name:')
    ssh_username = '' or input('ssh_username:')
    ssh_password = '' or input('ssh_password:')
    line_vty_num = '' or input('line_vty_num [4-15]:')

    config_commands = [
        f'hostname {hostname}',
        f'ip domain-name {domain_name}',
        'crypto key generate rsa',
        '2048',
        f'username {ssh_username} privilege 15 secret {ssh_password}',
        'ip ssh version 2',
        f'line vty 0 {line_vty_num}',
        'transport input ssh',
        'login local', 
        'exit',
    ]
    output = connection.send_config_set(config_commands)
    print(output)

def DHCP_pool(connection):
    excluded_start_ip = '' or input('excluded_start_ip:')
    excluded_end_ip = '' or input('excluded_end_ip:')
    dhcp_pool_name = '' or input('dhcp_pool_name:')
    network = '' or input('network:')
    subnet_mask = '' or input('subnet_mask:')
    default_router = '' or input('default-router:')
    dns_server = '' or input('dns-server:')
    domain_name = '' or input('domain-name:')

    config_commands = [
        f'ip dhcp excluded-address {excluded_start_ip} {excluded_end_ip}',
        f'ip dhcp pool {dhcp_pool_name}',
        f'network {network} {subnet_mask}', 
        f'default-router {default_router}',
        f'dns-server {dns_server}',
        f'domain-name {domain_name}',
        'exit',
    ]
    output = connection.send_config_set(config_commands)
    print(output)

def interface_ip(connection):
    interface = '' or input('interface:')  
    ip_address = '' or input('ip_address [ip] [subnet mask]:')
    
    config_commands = [
        f'interface {interface}',
        f'ip address {ip_address}',
        'exit',
    ]
    output = connection.send_config_set(config_commands)
    print(output)

def ROAS_router(connection):
    ROAS_interface = '' or input('ROAS_interface: ')
    vlan_number = '' or input("VLAN number: ")
    first_usable_subnet_ip = '' or input('[first_usable_subnet_IP] [subnet_mask]: ')
    
    config_commands = [
        f'interface {ROAS_interface}.{vlan_number}',
        f'encapsulation dot1Q {vlan_number}',
        f'ip address {first_usable_subnet_ip}',
        'exit',
    ]
    output = connection.send_config_set(config_commands)
    print(output)

def save(connection):
    config_commands = [
        'do wr',
    ]
    output = connection.send_config_set(config_commands)
    print(output)

def main():
    # Cisco 設備參數
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': '',
        'username': '',
        'password': '',
        'port': 22,
    }
    connection = ConnectHandler(**cisco_device)

    while True:
        print("主目錄")
        print("1. set Console port security")
        print('2. set ssh')
        print('3. create DHCP_pool')
        print("4: set interface IP")
        print("5: set ROAS")
        print("6: save")
        print("7: exit")
        
        choice = input("請選擇操作 (1/2/3/4/5/6/7): ")
        
        if choice == '1':
            console_port_security(connection)
        elif choice == '2':
            ssh(connection)
        elif choice == '3':
            DHCP_pool(connection)
        elif choice == '4':
           interface_ip(connection)
        elif choice == '5':
            ROAS_router(connection)
        elif choice == '6':
            save(connection)
        elif choice == '7':
            break
        else:
            print("無效的選擇，請重試。")

    connection.disconnect()

if __name__ == "__main__":
    main()
