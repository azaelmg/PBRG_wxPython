"""
Custom validator that validates the format needed for PBRG to
get the record date from a folder name.
"""
import re
import string
import wx

DAY_NUMBER = 0
MONTH_NAME = 1
YEAR_NUMBER = 2

class DateValidator (wx.Validator):
    """
    Validates input date has the next format:
    DD MONTH_NAME YYYY
    """
    def __init__(self, flag=None, pyVar=None):
        wx.Validator.__init__(self)
        self.flag = flag
        self.Bind(wx.EVT_CHAR, self.on_char)

        self.day_pattern = r"[0-31]{1}"
        self.month_pattern = r"[A-Z]{4,11}"
        self.year_pattern = r"[0-9]{4}"

    def Clone(self):
        """
        Every validator must have this method.
        """
        return DateValidator(self.flag)

    def Validate(self, win):
        """
        Validates the format of the date.
        """
        txt_ctrl = self.GetWindow()
        data = txt_ctrl.GetValue()
        # Using re mod.
        if self.flag == DAY_NUMBER:
            if not re.search(self.day_pattern, data):
                return False

        elif self.flag == MONTH_NAME:
            if not re.search(self.month_pattern, data):
                return False

        elif self.flag == YEAR_NUMBER:
            if not re.search(self.year_pattern, data):
                return False

        return True

    def on_char(self, event):
        """
        Called every time a char is typed in the text ctrl.
        """
        key = event.GetKeyCode()
        data_len = len(self.GetWindow().GetValue())

        if key < wx.WXK_SPACE or key == wx.WXK_DELETE or key > 255:
            event.Skip()
            return

        if self.flag == DAY_NUMBER and chr(key) in string.digits and data_len <= 1:
            event.Skip()
            return

        if self.flag == MONTH_NAME and chr(key) in string.ascii_uppercase and data_len <= 9:
            event.Skip()
            return

        if self.flag== YEAR_NUMBER and chr(key) in string.digits and data_len <= 3:
            event.Skip()
            return

        return

    def TransferToWindow(self):
        """
        Called when the value associated with the validator must be transferred to the window.
        """
        return True

    def TransferFromWindow(self):
        """
        Called when the value in the window must be transferred to the validator.
        """
        return True
