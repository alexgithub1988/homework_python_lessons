from controller import Controller
filename = 'spavochnik.csv'


if __name__ == "__main__":
    app = Controller(filename)
    app.run()