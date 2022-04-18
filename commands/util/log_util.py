from colorama import Fore, Back, Style

# LOGGING UTILITIES

debug_mode = False


# confgit: message
def cg_print(msg):
    print(f"{Back.GREEN + Fore.BLACK}confgit:{Style.RESET_ALL} {msg}")


# confgit: ERROR: message
def print_error(msg):
    cg_print(f"{Fore.RED}ERROR:{Style.RESET_ALL} {msg}")


# confgit: WARN: message
def print_warning(msg):
    cg_print(f"{Fore.LIGHTRED_EX}WARN:{Style.RESET_ALL} {msg}")


# confgit: DEBUG: message
def print_debug(msg):
    if debug_mode:
        cg_print(f"{Back.WHITE}{Fore.BLACK}DEBUG:{Style.RESET_ALL} {msg}")
