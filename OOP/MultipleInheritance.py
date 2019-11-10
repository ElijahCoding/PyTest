class Horse:
    def run(self):
        print("I am running.")


class Bird:
    def flay(self):
        print('Im flying')


class Pengasus(Horse, Bird):
    pass

def main():
    pegasus  = Pengasus()
    pegasus.run()
    pegasus.flay()

if __name__ == '__main__':
    main()