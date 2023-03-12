
class Godzilla:
    def __init__(self, stomach_vol):
        self.stomach_vol = stomach_vol
        self.current_stomach_volume = 0

    def eat(self, human_vol):
        if self.current_stomach_volume + human_vol > 0.9 * self.stomach_vol:
            print('Я з\'їв надто багато людей, більше не можу')
        else:
            self.current_stomach_volume += human_vol
            print('Я голодний!')


def main():
    a = Godzilla(50)
    a.eat(20)
    a.eat(26)


if __name__ == '__main__':
    main()
