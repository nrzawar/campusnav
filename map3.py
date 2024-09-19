import ipywidgets

wid1 = ipywidgets.Select(
    options=['Main Gate', 'Tuck Shop', 'Manet Hostel'], 
    value='Main Gate',
    description='Select Source',
    disabled=False
)
def selectstart(opt1):
    if opt1 == "Main Gate":
        print('M')
    elif opt1 == "Tuck Shop":
        print('T')
    elif opt1 == "Manet Hostel":
        print('H')
ipywidgets.interact(selectstart, opt1=wid1)

wid2 = ipywidgets.Select(
    options=['SOE', 'ISB', 'Boat Club'],
    value='SOE',
    description='Select Destination',
    disabled=False
)

def selectdes(opt2):
    if opt2 == 'SOE':
        print('S')
    elif opt2 == 'ISB':
        print('I')
    elif opt2 == 'Boat Club':
        print('B')

ipywidgets.interact(selectdes, opt2=wid2)
