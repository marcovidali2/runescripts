from pynput import mouse, keyboard

coordinates = []

def on_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:
        coordinates.append((round(x), round(y)))

def on_press(key):
    try:
        if key == keyboard.Key.esc:
            mouse_listener.stop()
            keyboard_listener.stop()
    except AttributeError:
        pass

mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

mouse_listener.join()
keyboard_listener.join()

print("\ncoordinates =", coordinates)
