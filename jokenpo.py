import random
import PySimpleGUI as sg


class Jokenpo:
    def __init__(self):
        self.random_value = 0
        self.min_value = 1
        self.max_value = 3
        self.name_image1 = 'img/pattern_game.png'
        self.name_image2 = 'img/pattern_game.png'

    def start(self):
        sg.theme('Default')
        layout = [
            [sg.Text('Jokenpo Game')],
            [sg.Text('Opponent')],
            [sg.Image(filename=self.name_image1, key='-IMAGE1-')],
            [sg.Text('Your Choose')],
            [sg.Image(filename=self.name_image2, key='-IMAGE2-')],
            [

                [sg.Text('The Winner is: ?????', key='-TXTWIN-')],
                [sg.Button('Rock')],
                [sg.Button('Paper')],
                [sg.Button('Scissor')]
            ]
        ]

        self.window = sg.Window('Game', layout=layout)

        try:
            while True:
                self.event, self.value = self.window.Read()
                if self.event == sg.WIN_CLOSED:
                    print('The game will end')
                    break
                else:
                    if self.event == 'Rock':
                        self.name_image2 = 'img/rock.png'
                        self.window['-IMAGE2-'].update(filename=self.name_image2)
                        print('Rock')
                        self.randomNumberGenerator()
                        self.window['-IMAGE1-'].update(filename=self.name_image1)
                        self.callTheWinner()
                    elif self.event == 'Paper':
                        self.name_image2 = 'img/paper.png'
                        self.window['-IMAGE2-'].update(filename=self.name_image2)
                        print('Paper')
                        self.randomNumberGenerator()
                        self.window['-IMAGE1-'].update(filename=self.name_image1)
                        self.callTheWinner()
                    elif self.event == 'Scissor':
                        self.name_image2 = 'img/scissor.png'
                        self.window['-IMAGE2-'].update(filename=self.name_image2)
                        print('Scissor')
                        self.randomNumberGenerator()
                        self.window['-IMAGE1-'].update(filename=self.name_image1)
                        self.callTheWinner()

            print('the window is closing')
            self.window.Close()

        except:
            print('Please enter only numbers')
            self.start()

    def randomNumberGenerator(self):
        random_value = random.randint(self.min_value, self.max_value)
        if random_value == 1:
            self.name_image1 = 'img/rock.png'
        elif random_value == 2:
            self.name_image1 = 'img/paper.png'
        elif random_value == 3:
            self.name_image1 = 'img/scissor.png'
        else:
            print('We have a problem in randomNumberGenerator function')

    def callTheWinner(self):
        if self.name_image2 == self.name_image1:
            self.window['-TXTWIN-'].update('The Winner is: None!')
        else:
            if self.name_image2 == 'img/rock.png' and self.name_image1 == 'img/scissor.png' \
                    or self.name_image2 == 'img/paper.png' and self.name_image1 == 'img/rock.png' \
                    or self.name_image2 == 'img/scissor.png' and self.name_image1 == 'img/paper.png':
                self.window['-TXTWIN-'].update('The Winner is: YOU')
            else:
                self.window['-TXTWIN-'].update('The Winner is: PC')


start_game = Jokenpo()
start_game.start()
