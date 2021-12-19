def on_button_pressed_a():
    basic.show_icon(IconNames.SQUARE)
    basic.show_icon(IconNames.SMALL_SQUARE)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.show_string("SAY THE FOLLOWING NUMBER IN TIME.")

    basic.show_icon(IconNames.YES)
    basic.show_string("Confirm you are not a robot")
    basic.show_string("What number is this?")
    basic.show_leds("""
        . # # # .
                # . . . #
                . . . # .
                . . # . .
                # # # # #
    """)
    basic.show_icon(IconNames.YES)
    basic.show_string("Good. Now press button b")
    basic.show_string("867902")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("Hello this is dark bit this might be a bit creepy ok.")
    basic.show_string("We're doing the Charlie Charlie challenge!")
    basic.show_icon(IconNames.SURPRISED)
    basic.show_string("So get 2 pencils and a paper balance the two pencils on each other and on the paper write yes and no on the same paper.")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("Hello this is alpha. This might be hard!")
    basic.show_string("Ok repeat the same sentence.")
    basic.show_string("This is so hard!")
    basic.show_icon(IconNames.HAPPY)
    basic.show_icon(IconNames.YES)
    basic.show_string(".correctly sentence this saY")
    basic.show_icon(IconNames.SURPRISED)
    basic.show_string("You passed this ahh fine. Press a+b")
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("Please press button a")