import curses
import asyncio
import multitap_settings


class MultiTap:
    def __init__(self, stdscr):
        self.stdscr = stdscr

    def updateScreen(self):
        # render ui
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, multitap_settings.LOGO, curses.color_pair(1))
        self.stdscr.addstr(15, 0,
                      "Press 's' to start the delayed stream")  # if not streaming else "Press 's' to stop the delayed stream"
        self.stdscr.refresh()

    async def run(self):
        max_y, max_x = self.stdscr.getmaxyx()
        update_needed = True
        curses.curs_set(0)
        self.stdscr.nodelay(True)
        if curses.has_colors():
            curses.start_color()
            curses.use_default_colors()
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        stream_count = 0
        streaming = False
        while True:
            c = self.stdscr.getch()
            if c == curses.ERR:
                await asyncio.sleep(0.1)
            if c == ord('q'):
                break
            if c == ord('s'):
                if not streaming:
                    pass  # start
                else:
                    pass  # stop
                streaming = not streaming
            self.updateScreen()


def main(stdscr) -> None:
    mtap = MultiTap(stdscr)
    asyncio.run(mtap.run())
    pass


curses.wrapper(main)
