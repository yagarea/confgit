from colorama import Fore, Back, Style

# LOGGING UTILITIES

debug_mode = False


# turn on debugging mode
def turn_on_debug_mode():
    global debug_mode
    debug_mode = True


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
    if debug_mode:
        cg_print(f"{Back.WHITE}{Fore.BLACK}DEBUG:{Style.RESET_ALL} {msg}")
