from prompt_toolkit import PromptSession
from prompt_toolkit import prompt



#
def case_1():
    pass

def case_2():
    pass


# Switch logic. This method determines which case to enter into
def switch():
    pass


# Dictionary outlining the possible cases to switch to
switcher = {
    1: case_1,
    2: case_2,

}


def main():
    #os.system('cls')

    while True:
        switch()

if __name__ == '__main__':
    main()