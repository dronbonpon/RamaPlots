import PySimpleGUI as sg
from Functions import covid_rama_plot, sars_rama_plot, ncov_rama_plot

sg.theme('SystemDefault')

layout = [[sg.Text('You can select one of the compounds and see the Ramachandran plot for it.'),
           sg.Text(size=(15, 1))],
          [sg.Button('COVID-19')],
          [sg.Button('SARS CoV-2')],
          [sg.Button('2019-nCoV')],
          [sg.Button('Exit')]]

window = sg.Window('Ramachandran plots', layout)

event, value = window.read()
window.close()

if event == 'COVID-19':
    covid_rama_plot()

if event == 'SARS CoV-2':
    sars_rama_plot()

if event == '2019-nCoV':
    ncov_rama_plot()