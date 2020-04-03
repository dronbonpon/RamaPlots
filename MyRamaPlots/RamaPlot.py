from Functions import read_PDB, calc_torsion, plot
import PySimpleGUI as sg

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
    file_name = '6lu7.pdb'
if event == 'SARS CoV-2':
    file_name = '6w4b.pdb'
if event == '2019-nCoV':
    file_name = '6yb7.pdb'

my_list_of_atoms = read_PDB(file_name)
# Call function to calculate torsion angles
phi, psi = calc_torsion(my_list_of_atoms)
# Call function to plot torsion angles
plot(phi, psi, "Phi(deg)", "Psi(deg)")



