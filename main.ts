input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Square)
    basic.showIcon(IconNames.SmallSquare)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.showString("SAY THE FOLLOWING NUMBER IN TIME.")
    basic.showString("8769532")
    basic.showIcon(IconNames.Yes)
    basic.showString("Confirm you are not a robot")
    basic.showString("What number is this?")
    basic.showLeds(`
        . # # # .
        # . . . #
        . . . # .
        . . # . .
        # # # # #
        `)
    basic.showIcon(IconNames.Yes)
    basic.showString("Good. Now press button b")
    basic.showString("867902")
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("Hello this is dark bit this might be a bit creepy ok.")
    basic.showString("We're doing the Charlie Charlie challenge!")
    basic.showIcon(IconNames.Surprised)
    basic.showString("So get 2 pencils and a paper balance the two pencils on each other and on the paper write yes and no on the same paper.")
})
input.onButtonPressed(Button.B, function () {
    basic.showString("Hello this is alpha. This might be hard!")
    basic.showString("Ok repeat the same sentence.")
    basic.showString("This is so hard!")
    basic.showIcon(IconNames.Happy)
    basic.showIcon(IconNames.Yes)
    basic.showString(".correctly sentence this saY")
    basic.showIcon(IconNames.Surprised)
    basic.showString("You passed this ahh fine. Press a+b")
})
basic.showString("Please press button a")
