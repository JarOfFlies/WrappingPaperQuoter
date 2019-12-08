from decimal import Decimal, ROUND_HALF_UP
from math import pi
from tkinter import *
from tkinter import ttk


BOW_COST = 1.50
CHEAP_PAPER_COST = 0.4
EXPENSIVE_PAPER_COST = 0.75
GIFT_CARD_CHARACTER_COST = 0.02
GIFT_CARD_COST = 0.50


mainWindow = Tk()
mainWindow.title("Wrapping Paper Quoter")
basketDictionary = []
colourChoice = StringVar(value="Purple")
depthString = StringVar()
diameterString = StringVar()
giftcardMessageString = StringVar()
heightString = StringVar()
includeBow = IntVar()
includeGiftcard = IntVar()
paperChoice = IntVar()
presentShapeIsCube = IntVar(value=0)
totalCost = StringVar(value="£0.00")
widthString = StringVar()


def AddPresentToBasket():
    presentDictionary = dict(height=heightString.get(), width=widthString.get(), depth=depthString.get()
        , diameter=diameterString.get(), paper=paperChoice.get(), colour=colourChoice.get()
        , bow=includeBow.get(), giftcard=includeGiftcard.get(), message=giftcardMessageString.get(), cost=totalCost.get())
    basketDictionary.append(presentDictionary)
    PopulateBasketTree()
    CloseWizard()


def CalculatePaperCost(area, isExpensivePaper):
    if isExpensivePaper == 1:
        costPence = area * EXPENSIVE_PAPER_COST
    else:
        costPence = area * CHEAP_PAPER_COST
    #Used to round the values to pence
    return float(Decimal(str(costPence)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)) / 100


def ClearWizard():
    heightString.set("")
    widthString.set("")
    depthString.set("")
    diameterString.set("")
    paperChoice.set(0)
    colourChoice.set("Purple")
    includeBow.set(0)
    includeGiftcard.set(0)
    giftcardMessageString.set("")
    totalCost.set("£0.00")


def CloseWizard():
    ClearWizard()
    presentWizard.destroy()
    mainWindow.update()
    mainWindow.deiconify()


def ConvertEntryValuesToInt(string):
    if string.isdigit():
        value = int(string)
    else:
        value = 0
    return value


def CreateCuboidWizard():
    CreatePresentWizard()
    presentShapeIsCube.set(0)

    widthLabel = Label(presentWizard, text="Width:", font=("Arial", 20))
    widthLabel.grid(column=0, row=2, padx=10, pady=10)

    widthEntry = Entry(presentWizard, textvariable=widthString, font=("Arial", 20), validate='key', validatecommand=(presentWizard.register(ValidateNumericEntry), '%P', '%W'))
    widthEntry.grid(column=1, row=2, columnspan=2, padx=10, pady=10)

    depthLabel = Label(presentWizard, text="Depth:", font=("Arial", 20))
    depthLabel.grid(column=0, row=3, padx=10, pady=10)

    depthEntry = Entry(presentWizard, textvariable=depthString, font=("Arial", 20), validate='key', validatecommand=(presentWizard.register(ValidateNumericEntry), '%P', '%W'))
    depthEntry.grid(column=1, row=3, columnspan=2, padx=10, pady=10)


def CreateCylinderWizard():
    CreatePresentWizard()
    presentShapeIsCube.set(2)

    diameterLabel = Label(presentWizard, text="Diameter:", font=("Arial", 20))
    diameterLabel.grid(column=0, row=2, padx=10, pady=10)

    diameterEntry = Entry(presentWizard, textvariable=diameterString, font=("Arial", 20), validate='key', validatecommand=(presentWizard.register(ValidateNumericEntry), '%P', '%W'))
    diameterEntry.grid(column=1, row=2, columnspan=2, padx=10, pady=10)


def CreateMainMenu():
    titleLabel = Label(mainWindow, text="Wrapping Paper Quoter", font=("Arial", 32))
    titleLabel.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

    headingLabel = Label(mainWindow, text="Present Type?", font=("Arial", 24))
    headingLabel.grid(column=0, row=1, columnspan=3, padx=10, pady=10)

    cubeButton = Button(mainWindow, text="Cube", font=("Arial", 20), height=2, command=CreatePresentWizard)
    cubeButton.grid(column=1, row=2, sticky="nsew", padx=10, pady=10)

    cuboidButton = Button(mainWindow, text="Cuboid", font=("Arial", 20), height=2, command=CreateCuboidWizard)
    cuboidButton.grid(column=1, row=3, sticky="nsew", padx=10, pady=10)

    cylinderButton = Button(mainWindow, text="Cylinder", font=("Arial", 20), height=2, command=CreateCylinderWizard)
    cylinderButton.grid(column=1, row=4, sticky="nsew", padx=10, pady=10)

    global treeView

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 15))
    style.configure("Treeview.Column", font=("Arial", 15))

    treeView = ttk.Treeview(mainWindow)
    treeView.grid(column=1, row=5, sticky="nsew", padx=10, pady=10)
    treeView["columns"]=("one","two")
    treeView.column("#0", width=50)
    treeView.column("one", width=75)
    treeView.column("two", width=50)
    treeView.heading("#0", text="Present")
    treeView.heading("one", text="Dimensions")
    treeView.heading("two", text="Cost")

    global totalCostLabel
    totalCostLabel = Label(mainWindow, text="Total Cost: £0.00", font=("Arial", 20))
    totalCostLabel.grid(column=0, row=6, columnspan=3, padx=10, pady=10)

    printQuoteButton = Button(mainWindow, text="Print Quote", font=("Arial", 15), height=2, command=PrintQuote)
    printQuoteButton.grid(column=1, row=7, sticky="nsew", padx=10, pady=10)

def CreatePresentWizard():
    ClearWizard()
    global presentWizard
    presentWizard = Toplevel(mainWindow)
    presentShapeIsCube.set(1)

    headingLabel = Label(presentWizard, text="Present Measurements", font=("Arial", 24))
    headingLabel.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

    heightLabel = Label(presentWizard, text="Height:", font=("Arial", 20))
    heightLabel.grid(column=0, row=1, padx=10, pady=10)

    heightEntry = Entry(presentWizard, textvariable=heightString, font=("Arial", 20), validate='key', validatecommand=(presentWizard.register(ValidateNumericEntry), '%P', '%W'))
    heightEntry.grid(column=1, row=1, columnspan=2, padx=10, pady=10)

    paperChoiceLabel = Label(presentWizard, text="Paper Choice:", font=("Arial", 20))
    paperChoiceLabel.grid(column=0, row=4, rowspan=2, padx=10, pady=10)

    CreateWrappingPaperPreview()

    paperChoice.set(1)
    paperChoiceRadioButtonExpensive = Radiobutton(presentWizard, text="Expensive", variable=paperChoice, value=1, command=UpdateCostTotal)
    paperChoiceRadioButtonExpensive.config(font=("Arial", 16))
    paperChoiceRadioButtonExpensive.grid(column=1, row=5)

    paperChoiceRadioButtonCheap = Radiobutton(presentWizard, text="Cheap", variable=paperChoice, value=2, command=UpdateCostTotal)
    paperChoiceRadioButtonCheap.config(font=("Arial", 16))
    paperChoiceRadioButtonCheap.grid(column=2, row=5)

    colourChoiceLabel = Label(presentWizard, text="Colour:", font=("Arial", 20))
    colourChoiceLabel.grid(column=0, row=6, padx=10, pady=10)

    colours = ["Purple", "DarkSlateGray4", "Deep sky blue", "Light sea green", "VioletRed2", "Gold"]
    colourOptionMenu = OptionMenu(presentWizard, colourChoice, *colours, command=RefreshPreview)
    colourOptionMenu.config(font=("Arial", 16))
    colourOptionMenu.grid(column=1, columnspan=2, row=6, sticky="nsew", padx=10, pady=10)

    includeBowLabel = Label(presentWizard, text="Include Bow?:", font=("Arial", 20))
    includeBowLabel.grid(column=0, row=7, padx=10, pady=10)

    bowCheckButton = Checkbutton(presentWizard, variable=includeBow, text=": Yes", font=("Arial", 16), command=UpdateCostTotal)
    bowCheckButton.grid(column=1, row=7, padx=10, pady=10)

    giftcardLabel = Label(presentWizard, text="Include Girftcard?:", font=("Arial", 20))
    giftcardLabel.grid(column=0, row=8, padx=10, pady=10)

    giftcardCheckButton = Checkbutton(presentWizard, variable=includeGiftcard, text=": Yes", font=("Arial", 16), command=UpdateCostTotal)
    giftcardCheckButton.grid(column=1, row=8, padx=10, pady=10)

    giftcardMessageLabel = Label(presentWizard, text="Giftcard Message:", font=("Arial", 20))
    giftcardMessageLabel.grid(column=0, row=9, padx=10, pady=10)

    giftcardMessageEntry = Entry(presentWizard, textvariable=giftcardMessageString, font=("Arial", 20), validate='key', validatecommand=(presentWizard.register(EnableGiftMessage), '%d'))
    giftcardMessageEntry.grid(column=1, row=9, columnspan=2, padx=10, pady=10)

    costLabel = Label(presentWizard, text="Cost:", font=("Arial", 20))
    costLabel.grid(column=0, row=10, padx=10, pady=10)

    totalCostLabel = Label(presentWizard, textvariable=totalCost, font=("Arial", 20))
    totalCostLabel.grid(column=1, row=10, padx=10, pady=10)

    closeButton = Button(presentWizard, text="Close", command=CloseWizard, font=("Arial", 12))
    closeButton.grid(column=0, row=11, sticky="nsew", padx=10, pady=10)

    addButton = Button(presentWizard, text="Add To Basket", command=AddPresentToBasket, font=("Arial", 12))
    addButton.grid(column=2, row=11, sticky="nsew", padx=10, pady=10)


def CreateWrappingPaperPreview():
    width = 104
    height = 104
    pad = 10
    row = 4
    highlightThickness = 0
    borderWidth = 0
    global expensiveCanvas
    expensiveCanvas = Canvas(presentWizard, width = width, height = height)
    expensiveCanvas.grid(column=1, row=row, padx=pad, pady=pad)
    expensiveCanvas.configure(highlightthickness=highlightThickness, borderwidth=borderWidth)
    DrawStars(expensiveCanvas)
    global cheapCanvas
    cheapCanvas = Canvas(presentWizard, width = width, height = height)
    cheapCanvas.grid(column=2, row=row, padx=pad, pady=pad)
    cheapCanvas.configure(highlightthickness=highlightThickness, borderwidth=borderWidth)
    DrawCircles(cheapCanvas)


def DrawCircles(canvas):
    fill = True
    for y in range(0,5):
        y1 = 0 + (y*20)
        y2 = 20 + (y*20)

        for x in range(0,5):
            x1 = 0 + (x*20)
            x2 = 20 + (x*20)

            if fill:
                fillColour = colourChoice.get()
            else:
                fillColour = ""
            canvas.create_oval(x1, y1, x2, y2, outline=colourChoice.get(), fill=fillColour)
            fill = not fill


def DrawStars(canvas):
    for i in range(0,5):
        x1=10+(i*20)
        x2=5+(i*20)
        x3=0+(i*20)
        x4=2.5+(i*20)
        x5=0+(i*20)
        x6=5+(i*20)
        x7=10+(i*20)
        x8=15+(i*20)
        x9=20+(i*20)
        x10=17.5+(i*20)
        x11=20+(i*20)
        x12=15+(i*20)

        for y in range(0,2):
            y1=0+(y*40)
            y2=10+(y*40)
            y3=10+(y*40)
            y4=20+(y*40)
            y5=30+(y*40)
            y6=30+(y*40)
            y7=40+(y*40)
            y8=30+(y*40)
            y9=30+(y*40)
            y10=20+(y*40)
            y11=10+(y*40)
            y12=10+(y*40)
            
            canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5 , x6, y6, x7, y7, x8, y8, x9, y9, x10, y10
                , x11, y11, x12, y12, fill = colourChoice.get(), outline = colourChoice.get())


def EnableGiftMessage(action):
    isEnabled = includeGiftcard.get() == 1
    if isEnabled:
        if action == '0':
            UpdateCostTotal(-1)
        elif action == '1':
            UpdateCostTotal(1)
        else:
            UpdateCostTotal()
    return isEnabled


def PopulateBasketTree():
    x = len(basketDictionary)
    present = basketDictionary[x - 1]
    height = present["height"]
    if present["diameter"] == "":
        width = present["width"]
        depth = present["depth"]
        if width == "" and depth == "":
            width = depth = height
        dimensions = f"{height}x{width}x{depth}"
    else:
        diameter = present["diameter"]
        dimensions = f"{height}x{diameter}"
    treeView.insert("" , 0,    text=x, values=(dimensions, present["cost"]), tags="T")
    treeView.tag_configure(tagname="T", font=("Arial", 12))
    total = 0
    for presents in basketDictionary:
        cost = presents["cost"]
        total += float(cost[1:])
    totalCostLabel.configure(text=f"Total Cost: £{total:.2f}")


def PrintQuote():
    if len(basketDictionary) > 0:
        quote = open("PresentQuote.txt", "w+")
        quote.write("Wrapping Paper Quote \n \n")
        index = 1
        for present in basketDictionary:
            height = present["height"]
            if present["diameter"] == "":
                width = present["width"]
                depth = present["depth"]
                if width == "" and depth == "":
                    width = depth = height
                dimensions = f"{height}x{width}x{depth}"
            else:
                diameter = present["diameter"]
                dimensions = f"{height}x{diameter}"
            quote.write(f"Prensent {index}:\n")
            quote.write(f"   {dimensions} \n")
            index += 1
            paper = present["paper"]
            if paper == "1":
                quote.write("   Expensive Paper \n")
            else:
                quote.write("   Cheap Paper \n")
            colour = present["colour"]
            quote.write(f"   {colour} \n")
            bow = present["bow"]
            if bow == "1":
                quote.write("   Bow \n")
            giftcard = present["giftcard"]
            if giftcard == "1":
                message = present["message"]
                quote.write(f"   Giftcard message: {message} \n")
            presentCost = present["cost"]
            quote.write(f"   Total: {presentCost} \n\n")
        total = 0
        for presents in basketDictionary:
            cost = presents["cost"]
            total += float(cost[1:])
        totalWithVAT = total * 1.2
        quote.write(f"Total(Excluding VAT): £{total:.2f} \n")
        quote.write(f"Total(Including VAT): £{float(Decimal(str(totalWithVAT)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)):.2f}")
        quote.close()


def RefreshPreview(e):
    expensiveCanvas.delete("all")
    cheapCanvas.delete("all")
    DrawStars(expensiveCanvas)
    DrawCircles(cheapCanvas)


def UpdateCostTotal(giftStringLength = 0, heightOveride=None, widthOveride=None, depthOveride=None, diameterOveride=None):
    if presentShapeIsCube.get() == 2:
        if heightOveride != None:
            area = WrappingPaperAreaCylinder(heightOveride, ConvertEntryValuesToInt(diameterString.get()))
        elif diameterOveride != None:
            area = WrappingPaperAreaCylinder(ConvertEntryValuesToInt(heightString.get()), diameterOveride)
        else:
            area = WrappingPaperAreaCylinder(ConvertEntryValuesToInt(heightString.get()), ConvertEntryValuesToInt(diameterString.get()))
    else:
        if heightOveride != None:
            area = WrappingPaperAreaCuboid(ConvertEntryValuesToInt(widthString.get()), heightOveride, ConvertEntryValuesToInt(depthString.get()))
        elif widthOveride != None:
            area = WrappingPaperAreaCuboid(widthOveride, ConvertEntryValuesToInt(heightString.get()), ConvertEntryValuesToInt(depthString.get()))
        elif depthOveride != None:
            area = WrappingPaperAreaCuboid(ConvertEntryValuesToInt(widthString.get()), ConvertEntryValuesToInt(heightString.get()), depthOveride)
        else:
            area = WrappingPaperAreaCuboid(ConvertEntryValuesToInt(widthString.get()), ConvertEntryValuesToInt(heightString.get()), ConvertEntryValuesToInt(depthString.get()))
    if area == 0:
        totalCost.set(f"£0.00")
    else:
        cost = CalculatePaperCost(area, paperChoice.get())
        if includeGiftcard.get() == 1:
            cost += GIFT_CARD_COST
            cost += (GIFT_CARD_CHARACTER_COST * (len(giftcardMessageString.get()) + int(giftStringLength)))
        if includeBow.get() == 1:
            cost += BOW_COST
        totalCost.set(f"£{float(Decimal(str(cost)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)):.2f}")


def ValidateNumericEntry(entryString, widgetName):
    if entryString.isdigit() or entryString == "":
        valid = True
        if widgetName.endswith("3"):
            if presentShapeIsCube.get() == 2:
                UpdateCostTotal(diameterOveride=ConvertEntryValuesToInt(entryString))
            else:
                UpdateCostTotal(widthOveride=ConvertEntryValuesToInt(entryString))
        elif widgetName.endswith("4"):
            UpdateCostTotal(depthOveride=ConvertEntryValuesToInt(entryString))
        else:
            UpdateCostTotal(heightOveride=ConvertEntryValuesToInt(entryString))
    else:
        valid = False
    return valid


def WrappingPaperAreaCuboid(width, height, depth):
    area = 0
    if presentShapeIsCube.get() == 1:
        if height != 0:
            area = (12 * height * height) + (42* height) + 36
    else:
        if height != 0 and width != 0 and depth != 0:
            area = (12 * width) + (4 * width * height) + (2 * width * depth) + (24 * height) + (4 * height * height) + (2 * height * depth) + (6 * depth) + 36
    return area


def WrappingPaperAreaCylinder(height, diameter):
    area = 0
    if height != 0 and diameter != 0:
        area = (pi * height * diameter) + (2 * pi * diameter * diameter) + (6 * pi * diameter) + (6* height) + (12 * diameter) + 36
    return area


if __name__ == '__main__':
    CreateMainMenu()
    mainWindow.mainloop()