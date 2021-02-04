"""
###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
"""
import io
import os
import glob
import re
import functools
import math
import csv
from PIL import Image
import wx
import wx.xrc

###########################################################################
## Class RegistrationFrame
###########################################################################

class RegistrationFrame ( wx.Frame ):
    """
    Displays photos in a scrolled window when a selected directory has met some conditions.
    The photos can then be selected via ToggleButton, then processed:

    -When a file is processed, their filename changes to fit a certain code that describes the
    size, quantity, color and the number id of the photo.

    -When a file is processed it's filename gets decoded and archived in a csv file.
    -The csv file is a basic accounting template.
    """

    def __init__( self, *args, **kw ):
        super().__init__( *args, **kw)

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.rf_mbar = wx.MenuBar( 0 )
        self.SetMenuBar( self.rf_mbar )

        self.rf_sbar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
        rf_main_hbox = wx.BoxSizer( wx.HORIZONTAL )

        self.rf_left_pnl = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        rf_left_vbox = wx.BoxSizer( wx.VERTICAL )

        self.rf_dirctrl = wx.GenericDirCtrl(
            self.rf_left_pnl, wx.ID_ANY,
            "C:/Users/Azael/Documents/Proyectos/Ommega/Contabilidad/Testing Data",
            wx.DefaultPosition, wx.DefaultSize,
            wx.DIRCTRL_DIR_ONLY|wx.DIRCTRL_3D_INTERNAL|wx.SUNKEN_BORDER,
            wx.EmptyString, 0
        )

        self.rf_dirctrl.ShowHidden( False )
        rf_left_vbox.Add( self.rf_dirctrl, 1, wx.ALL|wx.EXPAND, 5 )
        self.Bind(wx.EVT_DIRCTRL_SELECTIONCHANGED, self.on_directory_changed, self.rf_dirctrl)

        self.quantity_lbl = wx.StaticText( self.rf_left_pnl, wx.ID_ANY, u"Cantidad:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.quantity_lbl.Wrap( -1 )

        rf_left_vbox.Add( self.quantity_lbl, 0, wx.ALL|wx.EXPAND, 5 )

        rf_quantity_chlist = [ u"3", u"4", u"5", u"6", u"8", u"9", u"10", u"12" ]
        self.rf_quantity_ch = wx.Choice( self.rf_left_pnl, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, rf_quantity_chlist, 0 )
        self.rf_quantity_ch.SetSelection( 3 )
        rf_left_vbox.Add( self.rf_quantity_ch, 0, wx.ALL|wx.EXPAND, 5 )

        rf_size_rboxchlist = [ u"Infantil", u"Pasaporte", u"Credencial Ovalada", u"Visa Americana", u"Diploma", u"Título" ]
        self.rf_size_rbox = wx.RadioBox( self.rf_left_pnl, wx.ID_ANY, u"Tamaño:", wx.DefaultPosition, wx.DefaultSize, rf_size_rboxchlist, 1, wx.RA_SPECIFY_COLS )
        self.rf_size_rbox.SetSelection( 0 )
        rf_left_vbox.Add( self.rf_size_rbox, 0, wx.ALL|wx.EXPAND, 5 )

        rf_color_rboxchlist = [ u"Color", u"Blanco y Negro" ]
        self.rf_color_rbox = wx.RadioBox( self.rf_left_pnl, wx.ID_ANY, u"Color:", wx.DefaultPosition, wx.DefaultSize, rf_color_rboxchlist, 1, wx.RA_SPECIFY_COLS )
        self.rf_color_rbox.SetSelection( 0 )
        rf_left_vbox.Add( self.rf_color_rbox, 0, wx.ALL|wx.EXPAND, 5 )

        self.rf_left_pnl.SetSizer( rf_left_vbox )
        self.rf_left_pnl.Layout()
        rf_left_vbox.Fit( self.rf_left_pnl )
        rf_main_hbox.Add( self.rf_left_pnl, 1, wx.ALL|wx.EXPAND, 5 )

        self.rf_right_pnl = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        rf_right_vbox = wx.BoxSizer( wx.VERTICAL )

        self.file_display_swindow = wx.ScrolledWindow( self.rf_right_pnl, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.file_display_swindow.SetScrollRate( 25, 25 )
        self.file_display_swindow.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

        display_gridbox = wx.GridSizer( 0, 4, 0, 0 )

        self.file_display_swindow.SetSizer( display_gridbox )
        self.file_display_swindow.Layout()
        display_gridbox.Fit( self.file_display_swindow )
        rf_right_vbox.Add( self.file_display_swindow, 5, wx.EXPAND |wx.ALL, 5 )

        self.rf_actions_pnl = wx.Panel( self.rf_right_pnl, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        rf_actions_vbox = wx.BoxSizer( wx.VERTICAL )

        self.register_btn = wx.Button( self.rf_actions_pnl, wx.ID_ANY, u"Registrar", wx.DefaultPosition, wx.DefaultSize, 0 )
        rf_actions_vbox.Add( self.register_btn, 1, wx.EXPAND|wx.ALL, 5 )
        self.Bind(wx.EVT_BUTTON, self.on_register, self.register_btn)

        self.ignore_btn = wx.Button( self.rf_actions_pnl, wx.ID_ANY, u"Ignorar", wx.DefaultPosition, wx.DefaultSize, 0 )
        rf_actions_vbox.Add( self.ignore_btn, 1, wx.EXPAND|wx.ALL, 5 )
        self.Bind(wx.EVT_BUTTON, self.on_ignore, self.ignore_btn)

        self.rf_actions_pnl.SetSizer( rf_actions_vbox )
        self.rf_actions_pnl.Layout()
        rf_actions_vbox.Fit( self.rf_actions_pnl )
        rf_right_vbox.Add( self.rf_actions_pnl, 1, wx.ALL|wx.EXPAND, 5 )

        self.rf_right_pnl.SetSizer( rf_right_vbox )
        self.rf_right_pnl.Layout()
        rf_right_vbox.Fit( self.rf_right_pnl )
        rf_main_hbox.Add( self.rf_right_pnl, 3, wx.ALL|wx.EXPAND, 5 )

        self.SetSizer( rf_main_hbox )
        self.Layout()

        self.Centre( wx.BOTH )

        self.selected_dir_path = ""
        self.selected_dir_name = ""
        self.folder_name_pattern = r"\d{1,2}\s+[a-zA-Z]+\s\d{4}"
        self.file_name_pattern = re.compile(r"(\d{1,3})_(\d{1,2})_([A-V]{1,2})_[B-C]{1}")
        self.coded_files = []
        self.uncoded_files = []
        self.file_btn_list = []
        self.coded_count = 0

        self.size_dict = {
            "CODING":{
                "Infantil":"IN", "Pasaporte":"PA", "Credencial Ovalada":"CR",
                "Visa Americana":"VI", "Diploma":"DI", "Título":"TI"
            },
            "DECODING":{
                "IN":"INFANTIL", "PA":"PASAPORTE", "CR":"CREDENCIAL OVALO",
                "VI":"VISA AMERICANA", "DI":"DIPLOMA", "TI":"TÍTULO"
            }
        }
        self.color_dict = {
            "CODING":{
                "Color":"C", "Blanco y Negro":"B"
            },
            "DECODING":{
                "C":"COLOR", "B":"BYN"
            }
        }
        self.costs_dict = {
            # MIN -> Minimum photo quantity (order).
            # DIV -> Numeric validator (Photo Quantity must be divisible by this value.)
            # CPP -> Cost per photo.
            # CPO -> Cost per order.
            "IN":{
                "MIN":6, "DIV":6, "CPP":0, "CPO":70.00
            },
            "PA":{
                "MIN":5, "DIV":5, "CPP":23, "CPO":115.00
            },
            "CR":{
                "MIN":4, "DIV":4, "CPP":28.75, "CPO":115.00
            },
            "VI":{
                "MIN":3, "DIV":3, "CPP":0, "CPO":115.00
            },
            "DI":{
                "MIN":4, "DIV":2, "CPP":43.75, "CPO":175.00
            },
            "TI":{
                "MIN":4, "CPP":55.00, "CPO":220.00
            }
        }
        self.record_file_path = ""
        self.record_date = ""

###########################################################################
## Registraion Frame Events.
###########################################################################
    def on_directory_changed(self, event):
        """
        Selected directory has changed.
        Verifies if the new directory name is valid for registration.
        If the selected dir is accepted, scanning of the dir contents is called.
        """
        self.selected_dir_path = self.rf_dirctrl.GetPath()
        self.selected_dir_name = self.selected_dir_path.split("\\")[-1]
        # Verify folder's name.
        folder_match = re.search(self.folder_name_pattern, self.selected_dir_name)
        if folder_match is  None:
            # Folder's name is invalid.
            # Rename folder if the error in the folder's name is minimal.
            ###########################################################################
            ## TO DOOOOOOOOOOOOOOOOOOOOOOOOOOO
            ###########################################################################
            print("The folder's name is not viable for registration.\n")
        else:
             # Folder's name is valid.
            print(f"The folder's name {self.selected_dir_name} is viable for registration.\n")
            # Date doesn't change unless folder changes
            # so we can use the record date as a global variable.
            aux_date = wx.DateTime()
            aux_date.ParseDate(self.selected_dir_name)
            self.record_date = str(aux_date.GetDateOnly()).split(" ")[0]
            print(f"Date of selected folder: {self.record_date}\n")

            self.record_file_path = (
                self.selected_dir_path + "\\" +
                self.selected_dir_name.upper() + ".csv"
            )
            self.scan_directory()

    def on_register(self, event):
        """
        Check numeration of files already coded and generate new key/s based on them.
        """
        photo_quantity = int(self.rf_quantity_ch.GetStringSelection())
        photo_size = self.rf_size_rbox.GetStringSelection()

        # Verify integrity of the record to be processed.
        if not self.verify_record(photo_quantity, photo_size):
            print("Incorrect record data.")
        else:
            # Get selected files to register.
            something_toggled = False
            for file_btn in self.file_btn_list:
                if not file_btn.GetValue():
                    pass
                else:
                    something_toggled = True
                    prev_file_path = self.selected_dir_path + "\\" + file_btn.GetLabel()
                    if len(self.coded_files) == 0:
                        self.coded_count = 0
                    else:
                        self.coded_count = len(self.coded_files)
                        # Take into account when a coded file is deleted
                        ###########################################################################
                        ## TO DOOOOOOOOOOOOOOOOOOOOOOOOOOO
                        ###########################################################################

                    new_file_name = self.generate_code(photo_quantity, photo_size)
                    new_file_path = self.selected_dir_path + "\\" + new_file_name

                    os.rename(prev_file_path, new_file_path)
                    # Verify renamed file exists
                    if not os.path.isfile(new_file_path):
                        # Processed file NOT FOUND.
                        ###########################################################################
                        ## TO DOOOOOOOOOOOOOOOOOOOOOOOOOOO
                        ###########################################################################
                        break
                    else:
                        self.write_record(new_file_name)
                        self.coded_files.append(new_file_name)

            if something_toggled:
                self.clear_file_display()
                self.scan_directory()
            else:
                print("No files selected.\n")

    def on_ignore(self, event):
        """
        ignore_btn button has been pressed.
        """
        print("Ignorar.\n")
        print(f"Local month name: {wx.DateTime.GetMonthName(wx.DateTime.Jan)}")

###########################################################################
## Registration Frame Complementary Methods
###########################################################################
    def clear_file_display(self):
        """
        Destroys scrolled window used as file display and then creates a new one,
        setting it up for later file display
        """
        self.file_display_swindow.Destroy()
        self.file_display_swindow = wx.ScrolledWindow( self.rf_right_pnl, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.file_display_swindow.SetScrollRate( 25, 25 )
        self.file_display_swindow.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DDKSHADOW))
        display_gridbox = wx.GridSizer( 0, 4, 0, 0 )
        self.file_display_swindow.SetSizer( display_gridbox )
        self.file_display_swindow.Layout()
        display_gridbox.Fit( self.file_display_swindow )
        self.rf_right_pnl.GetSizer().Insert(0, self.file_display_swindow, 5, wx.EXPAND|wx.ALL, 5)
        self.GetSizer().Layout()

    def image_transpose_exif(self, image):
        """
        Apply Image.transpose to ensure 0th row of pixels is at the visual
        top of the image, and 0th column is the visual left-hand side.
        Return the original image if unable to determine the orientation.

        As per CIPA DC-008-2012, the orientation field contains an integer,
        1 through 8. Other values are reserved.

        Parameters
        ----------
        im: PIL.Image
        The image to be rotated.
        """

        exif_orientation_tag = 0x0112
        exif_transpose_sequences = [                   # Val  0th row  0th col
            [],                                        #  0    (reserved)
            [],                                        #  1   top      left
            [Image.FLIP_LEFT_RIGHT],                   #  2   top      right
            [Image.ROTATE_180],                        #  3   bottom   right
            [Image.FLIP_TOP_BOTTOM],                   #  4   bottom   left
            [Image.FLIP_LEFT_RIGHT, Image.ROTATE_90],  #  5   left     top
            [Image.ROTATE_270],                        #  6   right    top
            [Image.FLIP_TOP_BOTTOM, Image.ROTATE_90],  #  7   right    bottom
            [Image.ROTATE_90],                         #  8   left     bottom
        ]

        try:
            seq = exif_transpose_sequences[image.getexif()[exif_orientation_tag]]
        except Exception:
            return image
        else:
            return functools.reduce(type(image).transpose, seq, image)

    def generate_bitmap_buttons(self):
        """
        Generates toggle buttons with Bitmaps on them of the uncoded files found in the scan.
        """
        self.clear_file_display()
        display_gridbox = self.file_display_swindow.GetSizer()
        for filename in self.uncoded_files:
            file_path = self.selected_dir_path + "\\" + filename
            pil_img = Image.open(file_path)
            pil_img = self.image_transpose_exif(pil_img)
            pil_img = pil_img.resize((160,260))

            try:
                bmp = wx.Bitmap.FromBuffer(pil_img.size[0], pil_img.size[1], pil_img.tobytes())
            except Exception as excn:
                print(f"{excn}\nImage being processed as PNG: {file_path}\n")
                bytes_img = io.BytesIO()
                pil_img.save(bytes_img, format="PNG")
                bmp = wx.Bitmap.FromPNGData(bytes_img.getvalue())

            btn = wx.ToggleButton(
                self.file_display_swindow, wx.ID_ANY, filename, wx.DefaultPosition,
                wx.Size(170,280), wx.BU_BOTTOM
            )
            btn.SetBitmap(bmp, wx.TOP)
            btn.SetMinSize(wx.Size(170,280))
            display_gridbox.Add(btn, 0, wx.ALL|wx.EXPAND, 5)
            self.file_btn_list.append(btn)

        self.file_display_swindow.Layout()
        display_gridbox.Fit(self.file_display_swindow)
        self.GetSizer().Layout()

    def scan_directory(self):
        """
        Scans current selected directory obtaining the files that have already been processed
        and the ones that arent.
        If there's uncoded files inside the directory, it calls for button generation
        with these file's attributes.
        """
        self.uncoded_files.clear()
        self.coded_files.clear()
        self.file_btn_list.clear()

        print(f"Path being scanned:\n{self.selected_dir_path}\n")

        print(f"Folder being scanned:\n{self.selected_dir_name}\n")

        for walk_tuple in os.walk(self.selected_dir_path):
            if walk_tuple[0] != self.selected_dir_path:
                # Subfolder being scanned.
                print("Subfolder detected terminating scan.\n")
                break

            # Get all jpg files in selected folder ignoring hidden files.
            os.chdir(walk_tuple[0])
            #filenames = glob.glob("*.JPG")

            # Check for already coded files in folder.
            for filename in glob.glob("*.JPG"):
                if re.search(self.file_name_pattern, filename):
                    self.coded_files.append(filename)
                else:
                    self.uncoded_files.append(filename)

            self.coded_files.sort()
            self.uncoded_files.sort()

            print(f"Coded files found: {len(self.coded_files)}\n{self.coded_files}\n")
            print(f"Uncoded files found: {len(self.uncoded_files)}\n{self.uncoded_files}\n")

            if len(self.uncoded_files) == 0:
                print("All the files in this folder have been processed already.")
            else:
                self.generate_bitmap_buttons()

    def verify_record(self, photo_quantity, photo_size):
        """
        Verifies the record to be archived meets the logical requirements of it's nature.
        """
        print("Verifying record parameters...\n")
        verified = False
        if photo_size == "Infantil":
            if (photo_quantity >= self.costs_dict["IN"]["MIN"] and
                photo_quantity % self.costs_dict["IN"]["DIV"] == 0):
                verified = True

        elif photo_size == "Pasaporte":
            if (photo_quantity >= self.costs_dict["PA"]["MIN"] and
                photo_quantity % self.costs_dict["PA"]["DIV"] == 0):
                verified = True

        elif photo_size == "Credencial Ovalada":
            if (photo_quantity >= self.costs_dict["CR"]["MIN"] and
                photo_quantity % self.costs_dict["CR"]["DIV"] == 0):
                verified = True

        elif photo_size == "Visa Americana":
            if (photo_quantity >= self.costs_dict["VI"]["MIN"] and
                photo_quantity % self.costs_dict["VI"]["DIV"] == 0):
                verified = True

        elif photo_size == "Diploma" or photo_size == "Título":
            if (photo_quantity >= self.costs_dict["DI"]["MIN"] and
                photo_quantity % self.costs_dict["DI"]["DIV"] == 0):
                verified = True

        return verified

    def generate_code(self, photo_quantity, photo_size):
        """
        Generates a new coded name for a file.
        """
        # Obtain record values.
        self.coded_count += 1
        filename_param = [
            str(self.coded_count),
            str(photo_quantity),
            self.size_dict["CODING"][photo_size],
            self.color_dict["CODING"][self.rf_color_rbox.GetStringSelection()],
            ".JPG"
        ]
        filename = "_".join(filename_param)
        return filename

    def write_record(self, new_file_name):
        """
        Writes the decoded information from a processed file to a csv file.
        """
        # Generate the concept by DECODING the filename.
        name_param = new_file_name.split("_")
        photo_quantity = name_param[1]
        coded_size = name_param[2]
        coded_color = name_param[3]

        decoded_name_param = [
            photo_quantity,
            self.color_dict["DECODING"][coded_color],
            self.size_dict["DECODING"][coded_size]
        ]
        print(f"Filename {new_file_name} has been decoded:\n{decoded_name_param}\n")
        concept = " ".join(decoded_name_param)
        print(f"Concept cell content generated:\n{concept}\n")

        # Calculate the amount.
        ind_cost = self.costs_dict[coded_size]["CPP"]
        if ind_cost > 0:
            amount =  float(photo_quantity) * float(ind_cost)
            # Round cost to be divisible by 5.
            if amount % 5 != 0:
                amount = math.ceil(amount)
                amount = amount + abs(math.remainder(amount,5))
        else:
            amount = (
                float(photo_quantity) /
                float(self.costs_dict[coded_size]["MIN"]) *
                self.costs_dict[coded_size]["CPO"]
            )
        amount = "$" + str(amount)
        print(f"Amount cell content generated:\n{amount}\n")
        # CSV Accounting template:
        # _,      MES + " " + AÑO
        # _,  ESTUDIO FOTOGRÁFICO OMEGA
        # _,FECHA,        CONCEPTO,               IMPORTE
        # _,DD/MM/AAA,    6 COLOR INFANTIL,       $70.00
        # _,_,            VENTA TOTAL DEL DÍA,    $70.00

        # Check if csv file is already created.
        if os.path.isfile(self.record_file_path):
            # Record file already exists.
            mode = "a"
        else:
            # Record file doesn't exist.
            mode = "w"

        record_file = open(f"{self.selected_dir_name}.csv", mode=mode, newline="")
        record_file_writer = csv.writer(record_file, delimiter=",")
        record_file_writer.writerow([self.record_date, concept, amount])
        record_file.close()

    def __del__( self ):
        """
        Destructor for Registration frame.
        """
        print("Deleting Registration Frame.\n")
