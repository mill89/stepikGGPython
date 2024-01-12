TYPE_OS = 1  # 1 - Windows; 2 - Linux


class Dialog:
    def __new__(cls, *args, **kwargs):
        obj = None

        if TYPE_OS == 1:
            obj = super().__new__(DialogWindows)
        else:
            obj = super().__new__(DialogLinux)

        obj.name = args[0]
        return obj


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


if __name__ == '__main__':
    dlg = Dialog('Hello')
    print(dlg)
    print(dlg.name_class)
    print(dlg.__dict__)
