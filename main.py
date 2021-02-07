import one, two
import PySimpleGUI as sg
def main():
    event, values = sg.Window('Choose an option', [[sg.Text('Select one->'), sg.Listbox(['Form', 'Execute', 'Auto'], size=(40, 10), key='LB')],
        [sg.Button('Ok'), sg.Button('Cancel')]]).read(close=True)


    if event == 'Ok':
        if values["LB"][0]=='Form':
            one.main() 
        elif values["LB"][0]=='Execute':
            two.main() 
        else:
            return
    else:
        return
    
    
        
if __name__=="__main__": 
    main() 
