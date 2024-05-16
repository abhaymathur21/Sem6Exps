import curses

def main(stdscr):
    # Turn off cursor blinking
    curses.curs_set(0)
    
    # Clear the screen
    stdscr.clear()

    # Print a welcome message
    stdscr.addstr(0, 0, "Welcome to My Terminal!")
    
    # Display user input
    while True:
        user_input = stdscr.getstr(2, 0, 80)
        stdscr.addstr(4, 0, "You entered: {}".format(user_input))
        stdscr.clrtoeol()  # Clear the line after displaying user input
        stdscr.refresh()

curses.wrapper(main)
