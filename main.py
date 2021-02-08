"""
Main script for service
"""
import wx
import registration

if __name__ == '__main__':
    # When this module is run (not imported) then:
    # Create the app.
    app = wx.App()

    # Create a frame.
    frame = registration.RegistrationFrame(None, title="Photo Accounting")

    # Show the frame.
    frame.Show()

    # Start event loop.
    app.MainLoop()
    