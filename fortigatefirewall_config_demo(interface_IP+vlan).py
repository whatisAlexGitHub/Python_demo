from netmiko import ConnectHandler

def modify_port_ip(connection):
    port_num = input('interface_port_num:')
    new_ip = input("new_static_ip([ip] [subnet_mask]): ")
    
    config_commands = [
        'config system interface',
        f'edit port{port_num}',
        f'set ip {new_ip}',
        'set allowaccess ping https ssh',
        'next',
        'end'
    ]
    
    output = connection.send_config_set(config_commands)
    print(output)

def add_vlan(connection):
    port_num = input('port_number:')
    vlan_id = input("vlan_id: ")
    vlan_ip = input("vlan_first_usable_IP([ip] [subnet_mask]): ")
    
    config_commands = [
        'config system interface',
        f'edit "MyVlan{vlan_id}"',
        'set vdom root',
        f'set ip {vlan_ip}',
        f'set interface port{port_num}',
        f'set vlanid {vlan_id}',
        'next',
        'end',

        'config system interface',
        f'edit vlan{vlan_id}',
        f'set ip {vlan_ip}',  
        'set allowaccess ping http https ssh',
        'next',
        'end'
    ]
    
    output = connection.send_config_set(config_commands)
    print(output)

def main():
    # 設置FortiGate設備參數
    fortigate_device = {
        'device_type': 'fortinet',
        'host': '',  
        'username': 'admin',      
        'password': 'admin',      
        'port': 22,               
    }

    connection = ConnectHandler(**fortigate_device)

    while True:
        print("\n主目錄")
        print("1: 修改 PORT5 IP")
        print("2: 新增 VLAN")
        print("3: 退出")

        choice = input("請選擇操作 (1/2/3): ")

        if choice == '1':
            modify_port_ip(connection)
        elif choice == '2':
            add_vlan(connection)
        elif choice == '3':
            break
        else:
            print("無效的選擇，請重試。")

    connection.disconnect()

if __name__ == "__main__":
    main()