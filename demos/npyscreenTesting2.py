#!/usr/bin/python3


import npyscreen
import curses


class MySplitForm(npyscreen.SplitForm):
    MOVE_LINE_ON_RESIZE = True
    ''' Inherits and overrides methods from Nicholas Cole's npyscreen.SplitForm, to add a vertical line'''
    """Just the same as the Title Form, but with a horizontal line"""

    def __init__(self, draw_horline_at=None, draw_vertline_at=None, *args, **keywords):
        super(MySplitForm, self).__init__(*args, **keywords)
        if not hasattr(self, 'draw_horline_at'):
            if draw_horline_at != None:
                self.draw_horline_at = draw_horline_at
            else:
                self.draw_horline_at = self.get_horizontal_half_way()
            if draw_vertline_at != None:
                self.draw_vertline_at = draw_vertline_at
            else:
                self.draw_vertline_at = self.get_vertical_half_way()

    def draw_form(self, ):
        MAXY, MAXX = self.curses_pad.getmaxyx()
        super(MySplitForm, self).draw_form()
        self.curses_pad.hline(self.draw_horline_at, 1, curses.ACS_HLINE, MAXX - 2)
        self.curses_pad.vline(1, self.draw_vertline_at, curses.ACS_VLINE, self.draw_horline_at - 1)

    def get_horizontal_half_way(self):
        return self.curses_pad.getmaxyx()[0] // 2

    def get_vertical_half_way(self):
        return self.curses_pad.getmaxyx()[1] // 2

    def resize(self):
        super(MySplitForm, self).resize()
        if self.MOVE_LINE_ON_RESIZE:
            self.draw_horline_at = self.get_horizontal_half_way()
            self.draw_vertline_at = self.get_vertical_half_way()


class MyTitleFixedTextB(npyscreen.TitleFixedText):
    # Attempt to override Widget.resize() to keep the starting point of the
    # widget at the middle of the screen
    def get_horizontal_half_way(self):
        return self.parent.curses_pad.getmaxyx()[0] // 2

    def get_vertical_half_way(self):
        return self.parent.curses_pad.getmaxyx()[1] // 2

    def resize(self):
        super(MyTitleFixedTextB, self).resize()
        self.relx = self.get_vertical_half_way() + 2

class MyMultiLineEditA(npyscreen.MultiLineEdit):
    # Attempt to override Widget.resize() to keep bottom right corner
    # of widget near the center of the screen
    def get_horizontal_half_way(self):
        return self.parent.curses_pad.getmaxyx()[0] // 2

    def get_vertical_half_way(self):
        return self.parent.curses_pad.getmaxyx()[1] // 2

    def update(self, clear=True):
        super(MyMultiLineEditA, self).update()

    def resize(self):
        super(MyMultiLineEditA, self).resize()
        self.max_width = self.get_vertical_half_way() - 2
        self.max_height = self.get_horizontal_half_way() - 2


class MyMultiLineEditB(npyscreen.MultiLineEdit):
    # Attempt to override Widget.resize() to keep upper left corner
    # of widget near the top middle of the screen
    def get_horizontal_half_way(self):
        return self.parent.curses_pad.getmaxyx()[0] // 2

    def get_vertical_half_way(self):
        return self.parent.curses_pad.getmaxyx()[1] // 2

    def update(self, clear=True):
        super(MyMultiLineEditB, self).update()

    def resize(self):
        super(MyMultiLineEditB, self).resize()
        self.relx = self.get_vertical_half_way() + 2
        self.max_height = self.get_horizontal_half_way() - 2


class FormObject(npyscreen.ActionForm, npyscreen.FormWithMenus, MySplitForm):
    def create(self):

        self.file_a_header = self.add(npyscreen.TitleFixedText, name='File A:',
                                      value='Please Select file from menu using Ctrl-x', begin_entry_at=8,
                                      use_two_lines=False, max_width=self.get_vertical_half_way() - 2, rely=1)
        self.file_b_header = self.add(MyTitleFixedTextB, name='File B:',
                                      value='Please Select file from menu using Ctrl-x', begin_entry_at=8,
                                      use_two_lines=False, rely=1, relx=self.get_vertical_half_way() + 2)

        self.multi_line_edit_a = self.add(MyMultiLineEditA, value='',
                                          max_width=self.get_vertical_half_way() - 2,
                                          max_height=self.get_horizontal_half_way() - 2, rely=2)
        self.multi_line_edit_b = self.add(MyMultiLineEditB, value='', rely=2,
                                          max_height=self.get_horizontal_half_way() - 2,
                                          relx=self.get_vertical_half_way() + 2)

        self.menu = self.new_menu(name= 'Main Menu', shortcut='m')

        self.menu.addItem('Select file A:', self.press_a, 'a')
        self.menu.addItem('Select file B:', self.press_b, 'b')

        self.menu.addItem('Merge files', self.press_3, 'm')
        self.menu.addItem('Exit without saving', self.exit_form, '^X')
        self.submenu = self.menu.addNewSubmenu('A sub Menu', 's')
        self.submenu.addItem('Um, ok whereare we again?')

    def press_a(self):
        file_a_path = npyscreen.selectFile()
        #npyscreen.notify_wait('That returned: {}'.format(file_a_path), title='results')
        self.file_a_header.value = file_a_path

        self.infile_a = open(file_a_path, 'r')
        self.infile_a_contents_list = ['']
        for line in self.infile_a:
            line = line.rstrip('\n')
            self.infile_a_contents_list.append(line)

        self.multi_line_edit_a.value = '\n'.join(self.infile_a_contents_list)

    def press_b(self):
        file_b_path = npyscreen.selectFile()
        #npyscreen.notify_wait('That returned: {}'.format(file_b_path), title='results')
        self.file_b_header.value = file_b_path

        self.infile_b = open(file_b_path, 'r')
        self.infile_b_contents_list = ['']
        for line in self.infile_b:
            line = line.rstrip('\n')
            self.infile_b_contents_list.append(line)

        self.multi_line_edit_b.value = '\n'.join(self.infile_b_contents_list)

    def press_3(self):
        pass

    def exit_form(self):
        npyscreen.notify_confirm('You pressed, exit_form', 'Exiting', editw=1)
        self.parentApp.switchForm(None)
        npyscreen.noti
    def on_ok(self):
        npyscreen.notify_confirm('Ok Your stuff is saved', "Saving some stuff!")
        self.parentApp.setNextForm(None)

    def on_cancel(self):
        exiting = npyscreen.notify_yes_no('Are you sure you want to cancel?', "You sure?")
        if (exiting):
            npyscreen.notify_confirm('Ok. Your stuffs not saved! Laterz!')
            self.parentApp.setNextForm(None)
        else:
            npyscreen.notify_confirm('Thats what I thought', "Pffft!")


class EasyDiffApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', FormObject, name = 'Easy Diff')


if __name__ == '__main__':

    myApp = EasyDiffApplication()
    myApp.run()
