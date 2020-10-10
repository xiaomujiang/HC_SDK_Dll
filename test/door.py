import time

from src.interface import HKDoor

if __name__ == '__main__':
    # tool = DoorMaster('10.86.77.119', 'admin', 'admin777')  # 门禁
    tool = HKDoor('10.10.111.170', 'admin', '2020')  # 门禁2
    tool.sys_login()

    tool.setup_alarm_chan()
    tool.door_open(2)
    time.sleep(2)

    tool.sys_clean_up()