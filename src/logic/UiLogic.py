from src.logic.Observer import Observer
from src.logic import SuperPinger


def on_sidebar_button_clicked(idx):
    print(f"Button {idx} clicked!")

    if idx == 2:
        SuperPinger.ping_range(1, 25)
    elif idx == 3:
        print(Observer().data['ping'])