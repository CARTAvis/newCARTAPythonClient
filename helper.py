# https://stackoverflow.com/a/39662359/7354486
import __main__ as main
# print()
def isnotebook():
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter

# https://stackoverflow.com/a/5377051/7354486
def run_from_interactive():
    try:
        __IPYTHON__
        return True
    except NameError:
        if hasattr(main, '__file__') == False:
            print("ordinary interpreter")
            return True
        return False #program or ordinary interpreter

def run_from_iPython():
    try:
        __IPYTHON__
        return True
    except NameError:
        return False