from os import listdir, system, path
from sys import exit
from random import choice
from sys import argv
import dbm


def set_path() -> str:
    with dbm.open('.database.db', 'c') as db:
        try:
            has_args: bool = bool(argv[1] in ['-c', '--change-dir'])
        except IndexError:
            has_args: bool = False

        if (not db or has_args):
            usr_path: str = input('Digite o caminho para a pasta de imagens: ')

            if not (path.exists(usr_path)):
                print("A pasta informada não existe")
                exit()

            db["path"]: str = usr_path

            return usr_path

        return db["path"].decode('utf-8')


def set_wallpaper() -> None:
    root_path: str = set_path()
    root_path: str = root_path.replace('//', '/')
    galery: list = listdir(root_path)
    img: str = choice(galery)
    wallpaper: str = root_path + img

    system(f'termux-wallpaper -f {wallpaper}')


set_wallpaper()
