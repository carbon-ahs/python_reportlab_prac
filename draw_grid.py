#draw a grid across the border
def draw_grid(pdf):
    #y-axis
    i = 0
    label = ''
    while(i <= 840):
        label = '' + str(int(i/20))
        pdf.drawString(0, i, label)
        i += 20

    #y-axis
    i = 0
    label = ''
    while(i <= 840):
        label = '' + str(int(i/20))
        pdf.drawString(580, i, label)
        i += 20

    #x-axis
    i = 0
    label = ''
    while(i <= 580):
        label = '' + str(int(i/20))
        pdf.drawString(i, 0, label)
        i += 20

    #x-axis
    i = 0
    label = ''
    while(i <= 580):
        label = '' + str(int(i/20))
        pdf.drawString(i, 835, label)
        i += 20

    return pdf
