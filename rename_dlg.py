"""
###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
"""
import wx
import wx.xrc
from date_validator import DateValidator

DAY_NUMBER = 0
MONTH_NAME = 1
YEAR_NUMBER = 2
###########################################################################
## Class RenameDialog
###########################################################################

class RenameDialog ( wx.Dialog ):
    """
    Dialog used to handle the renaming of folders to be able to archive them.
    """
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        main_vbox = wx.BoxSizer( wx.VERTICAL )

        input_gbox = wx.GridSizer( 0, 3, 0, 0 )

        self.day_lbl = wx.StaticText( self, wx.ID_ANY, u"Día:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.day_lbl.Wrap( -1 )

        self.day_lbl.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        input_gbox.Add( self.day_lbl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.day_txtctrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        input_gbox.Add( self.day_txtctrl, 1, wx.ALL, 5 )

        self.day_ex_lbl = wx.StaticText( self, wx.ID_ANY, u"Ej: 01", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.day_ex_lbl.Wrap( -1 )

        self.day_ex_lbl.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        input_gbox.Add( self.day_ex_lbl, 0, wx.ALL, 5 )

        self.month_lbl = wx.StaticText( self, wx.ID_ANY, u"Mes:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.month_lbl.Wrap( -1 )

        self.month_lbl.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        input_gbox.Add( self.month_lbl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.month_txtctrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        input_gbox.Add( self.month_txtctrl, 1, wx.ALL, 5 )

        self.month_ex_lbl = wx.StaticText( self, wx.ID_ANY, u"Ej: NOVIEMBRE", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.month_ex_lbl.Wrap( -1 )

        self.month_ex_lbl.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        input_gbox.Add( self.month_ex_lbl, 0, wx.ALL, 5 )

        self.year_lbl = wx.StaticText( self, wx.ID_ANY, u"Año:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.year_lbl.Wrap( -1 )

        self.year_lbl.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        input_gbox.Add( self.year_lbl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.year_txtctrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        input_gbox.Add( self.year_txtctrl, 1, wx.ALL, 5 )

        self.year_ex_lbl = wx.StaticText( self, wx.ID_ANY, u"Ej: 1994", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.year_ex_lbl.Wrap( -1 )

        self.year_ex_lbl.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        input_gbox.Add( self.year_ex_lbl, 0, wx.ALL, 5 )


        main_vbox.Add( input_gbox, 1, 5 )

        self.dlg_separator = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        main_vbox.Add( self.dlg_separator, 0, wx.EXPAND |wx.ALL, 5 )

        actions_hbox = wx.BoxSizer( wx.HORIZONTAL )

        self.accept_btn = wx.Button( self, wx.ID_OK)
        self.accept_btn.SetDefault()
        actions_hbox.Add( self.accept_btn, 1, wx.ALL, 5 )

        self.cancel_btn = wx.Button( self, wx.ID_CANCEL)
        self.cancel_btn.SetDefault()
        actions_hbox.Add( self.cancel_btn, 1, wx.ALL, 5 )


        main_vbox.Add( actions_hbox, 0, wx.EXPAND, 5 )

        self.SetSizer( main_vbox )
        self.Layout()

        self.Centre( wx.BOTH )

        self.day_txtctrl.SetValidator(DateValidator(DAY_NUMBER))
        self.month_txtctrl.SetValidator(DateValidator(MONTH_NAME))
        self.year_txtctrl.SetValidator(DateValidator(YEAR_NUMBER))

    def get_value(self):
        """
        Returns a string that combines all the input paremeters of the date.
        """
        date = [
            self.day_txtctrl.GetValue(),
            self.month_txtctrl.GetValue(),
            self.year_txtctrl.GetValue()
        ]
        return " ".join(date)

    def OnOk(self, event):
        """
        Called on btn OK inside the dialog.
        """
        if self.day_txtctrl.Validate() and self.day_txtctrl.TransferDataFromWindow():
            if self.IsModal():
                self.EndModal(wx.ID_OK)
            else:
                self.SetReturnCode(wx.ID_OK)
                self.Show(False)

    def __del__( self ):
        pass
