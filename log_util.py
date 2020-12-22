from colorama import Fore, Back, Style


# CG: message
def cg_print(msg):
    print(f"{Back.GREEN + Fore.BLACK}CG:{Style.RESET_ALL} {msg}")


# CG: ERROR: message
def print_error(msg):
    cg_print(f"{Fore.RED}ERROR:{Style.RESET_ALL} {msg}")


# CG: WARN: message
def print_warning(msg):
    cg_print(f"{Fore.LIGHTRED_EX}WARN:{Style.RESET_ALL} {msg}")


# CG: DEBUG: message
def print_debug(msg):
    cg_print(f"{Back.WHITE}{Fore.BLACK}DEBUG:{Style.RESET_ALL} {msg}")
