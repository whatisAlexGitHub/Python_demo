from netmiko import ConnectHandler

def interface_ip(connection):
    # 手動修改方法
    interface_name = ''  
    ip_address = ''      #[ip] [subnet mask] 或dhcp或pool [num]
    
    # 提問修改方法
    change_interface = input(f"將會修改的interface為'{interface_name}'，是否修改？(y/n): ")
    if change_interface.lower() == 'y':
        interface_name = input("新的接口名稱: ")
    
    change_ip = input(f"將會修改其ip為'{ip_address}'，是否修改？(y/n): ")
    if change_ip.lower() == 'y':
        ip_address = input("新的IP([ip] [subnet mask] 或dhcp或pool [num]): ")

    # 預防錯誤輸入
    if len(interface_name) > 2 and len(ip_address) > 2:
        config_commands = [
            'conf t',
            f'interface {interface_name}',
            f'ip address {ip_address}',
            'no shutdown',
            'exit',
        ]
        output = connection.send_config_set(config_commands)
        print(output)
    else:
        print("未進行任何配置。")

def ROAS_router(connection):
    ROAS_interface = input("設置ROAS的Interface: ")
    vlan_number = input("VLAN number: ")
    first_usable_subnet_ip = input("[first_usable_subnet_IP] [subnet_mask]: ")
    
    config_commands = [
        'conf t',
        f'interface {ROAS_interface}.{vlan_number}',
        f'encapsulation dot1Q {vlan_number}',
        f'ip address {first_usable_subnet_ip}',
        'no shutdown',
        'exit',
    ]
    output = connection.send_config_set(config_commands)
    print(output)

def save(connection):
    config_commands = [
        'conf t',
        'do wr',
    ]
    output = connection.send_config_set(config_commands)
    print(output)

def main():
    # Cisco 設備參數
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': '',
        'username': 'admin',
        'password': 'admin',
        'port': 22,
    }
    connection = ConnectHandler(**cisco_device)

    while True:
        print("主目錄")
        print("1: 設置接口 IP")
        print("2: 設置 ROAS")
        print("3: save")
        print("4: 退出")
        
        choice = input("請選擇操作 (1/2/3/4): ")
        
        if choice == '1':
            interface_ip(connection)
        elif choice == '2':
            ROAS_router(connection)
        elif choice == '3':
            save(connection)
        elif choice == '4':
            break
        else:
            print("無效的選擇，請重試。")

    connection.disconnect()

if __name__ == "__main__":
    main()