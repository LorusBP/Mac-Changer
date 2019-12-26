import subprocess
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", help="Interface that is being used", action="store")
    parser.add_argument("-m", "--mac", action="store", help="New Mac Address")

    return parser.parse_args()


given_args = get_arguments()


def change_mac(interface, newMac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", newMac])
    subprocess.call(["ifconfig", interface, "up"])


def main():

    if given_args.interface and given_args.mac is not None:
        change_mac(given_args.interface, given_args.mac)


if __name__ == '__main__':
    main()
