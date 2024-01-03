import subprocess

from src.logic.Observer import Observer

def ping_range(start, end):
    ip_array = []

    for i in range(start, end):
        
        ip = "192.168.178.{0}".format(i)
        try:
            output = subprocess.check_output("ping -c 1 " + ip, shell=True)
            if "1 packets transmitted, 1 received" in output:
                print(ip, 'is up!')
                ip_array.append(ip + " is up!")
            else:
                print(ip, 'is down!')
                ip_array.append(ip + " is down!")
        except subprocess.CalledProcessError:
            print(ip, 'is down!')
        
        Observer().update_data('ping', ip_array)


if __name__ == "__main__":
    ping_range(1, 255)