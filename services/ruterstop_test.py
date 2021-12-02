import ruterstop
import os
import subprocess


def init_ruterstop():
    init_cmd = os.system('ruterstop --search-stop stig')
    if init_cmd is not None:
        return True
    else:
        return False


def ruterstop_cmd():
    output = subprocess.check_output("ruterstop --search-stop stig", shell=True)
    if output is not None:
        return True
    else:
        return False


