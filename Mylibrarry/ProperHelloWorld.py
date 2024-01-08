"""W pythonie można sprawdzić czy skrypt został uruchomiany jako główny plik czy został wywołany jako biblioteka"""
if __name__ == "__main__":#robi coś tylko kiedy plik został odpalony jako skrypt. Jest jak oznaczenie dla innych że ten plik jest do wykonywania a nie biblioteką
    print("Hello World!")
    print(__name__)