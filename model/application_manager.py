from model.pages.main_desktop import MainDesktop
from model.pages.main_mobile import MainMobile


class Application:
    def __init__(self):
        self.main_desktop = MainDesktop()
        self.main_mobile = MainMobile()


app = Application()
