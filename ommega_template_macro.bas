Option Explicit
REM  *****  BASIC  *****
Private record_doc As Object
Private m_frame As Variant
Private record_sheet As Object
Private m_dispatch As Object
Private m_uno_cmd As String
Private record_columns As Variant
Private record_rows As Variant
Private m_cursor As Object
Private m_range As Object
Private m_cell As Object

Sub SetupTemplate
	' Stores the current document on record_doc.
	record_doc = ThisComponent
	' Stores active sheet in record_sheet.
	record_sheet = record_doc.CurrentController.ActiveSheet
	' Stores sheet columns in record_columns for future use.
	record_columns = record_sheet.getColumns()
	' Stores sheet rows in record_rows for future use.
	record_rows = record_sheet.getRows()
	
	' Change color of sheet tab.
	record_sheet.tabColor = RGB(255, 203, 60)
	
	MoveContents()
	SetUpRows()
	SetUpColumns()
	GetTotalAmount()
	ApplyCellStyles()
	
	record_doc.CurrentController.select(m_cell)
	
End Sub

Function MoveContents()
	' Find last row/column used.
	Dim row As Long
	Dim col As Long
	Dim data_table As Variant
	
	m_cursor = record_sheet.createCursorByRange(record_sheet.getCellRangeByName("A1"))
	m_cursor.gotoEndOfUsedArea(True)
	m_range = record_sheet.getCellRangeByName(m_cursor.AbsoluteName)
	row = m_range.RangeAddress.EndRow
	col = m_range.RangeAddress.EndColumn
	
	' Store contents of range cells in data_table.
	data_table = m_range.DataArray
	
	' Removes Strings and Values from the range.
	m_range.clearContents(com.sun.star.sheet.CellFlags.STRING + com.sun.star.sheet.CellFlags.VALUE)
	
	' Move the data to desired location.
	m_range = record_sheet.getCellRangeByPosition(1, 1, col + 1, row + 1)
	m_range.DataArray = data_table
End Function

Function SetUpRows()
	Dim row As Variant
	Dim row_height As Double
	
	'Assign column widths in cm.
	row = record_rows(1)
  	row.Height = CInt(0.95 * 1000 + 0.5)
  	
  	row = record_rows(2)
  	row.Height = CInt(1.08 * 1000 + 0.5)
End Function

Function SetUpColumns()
  	Dim column As Variant
  	Dim column_width As Double

	'Assign column widths in cm.
  	column = record_columns.getByName("A")
  	column.Width = CInt(0.95 * 1000 + 0.5)
  	
  	column = record_columns.getByName("B")
  	column.Width = CInt(2.58 * 1000 + 0.5)
  	
  	column = record_columns.getByName("C")
  	column.Width = CInt(6.72 * 1000 + 0.5)
  	
  	column = record_columns.getByName("D")
  	column.Width = CInt(3.81 * 1000 + 0.5)
End Function

Function GetTotalAmount()
	Dim last_row As Long
	Dim last_col As Long
	Dim amount_cell as Object
	Dim amount_formula As String
	
	Dim args() As Variant
	
	m_cursor = record_sheet.createCursorByRange(record_sheet.getCellRangeByName("D6"))
	m_cursor.gotoEndOfUsedArea(True)
	m_range = record_sheet.getCellRangeByName(m_cursor.AbsoluteName)
	last_row = m_range.RangeAddress.EndRow
	last_col = m_range.RangeAddress.EndColumn
	
	record_doc.CurrentController.select(m_range)
	m_frame = record_doc.CurrentController.Frame
	m_uno_cmd = ".uno:NumberFormatCurrency"
	m_dispatch = createUnoService("com.sun.star.frame.DispatchHelper")
	m_dispatch.executeDispatch(m_frame, m_uno_cmd, "", 0, Args())
	
	amount_cell = record_sheet.getCellByPosition(last_col -1, last_row + 1)
	amount_cell.String = "VENTA TOTAL DEL DÍA"
	
	amount_cell = record_sheet.getCellByPosition(last_col, last_row + 1)
	amount_formula = "=SUM(D6:D"& last_row &")"
	amount_cell.Formula = amount_formula
	record_doc.calculateAll()
	m_cell = record_sheet.getCellRangeByName(amount_cell.AbsoluteName)
End Function

Function CreateCellStyle(style_name As String, font_name As String, font_size As Integer, font_weight As Double) As Boolean
	Dim style_families As Object
	Dim cell_styles As Object
	Dim cell_style As Object
	Dim new_style As Object
	
	style_families = record_doc.StyleFamilies
	cell_styles = style_families.getByName("CellStyles")
	If cell_styles.hasByName(style_name) Then
		CreateCellStyle = False
	Else
		new_style = record_doc.createInstance("com.sun.star.style.CellStyle")
		cell_styles.insertByName(style_name, new_style)
		new_style.ParentStyle = "Default"
		cell_style = cell_styles.getByName(style_name)
		With cell_style
			.CharWeight = font_weight
			.CharFontName = font_name
			.CharHeight = font_size
		End With
	End If
End Function

Function ApplyCellStyles()
	Dim mn_range As Object
	Dim bn_range As Object
	Dim data_names_range As Object
	Dim data_cells_range As Object
	Dim concept_cells_range As Object
	
	Dim args() As Variant

	' Define and create if necessary the multiple styles used on the record.
	' Month NameHeader(row).
	CreateCellStyle("mn_header", "Calibri", 20, 100.00)
	' Bussiness Name Header(row).
	CreateCellStyle("bn_header", "Calibri", 16, 150.00)
	' Data Names(row).
	CreateCellStyle("data_names", "Calibri", 11, 100.00)
	
	' Obtain the main ranges.
	mn_range = record_sheet.getCellRangeByName("B2:D2")
	bn_range = record_sheet.getCellRangeByName("B3:D3")
	data_names_range = record_sheet.getCellRangeByName("B5:D5")
	
	' Obtain secondary ranges.
	m_cursor = record_sheet.createCursorByRange(record_sheet.getCellRangeByName("B6"))
	m_cursor.gotoEndOfUsedArea(True)
	data_cells_range = record_sheet.getCellRangeByName(m_cursor.AbsoluteName)
	' Obtain the concept cells.
	concept_cells_range = data_cells_range.Columns(1)
	
	
	' Merge the rows of the headers.
	mn_range.Merge(True)
	bn_range.Merge(True)
	
	' Apply borders.
	record_doc.CurrentController.select(mn_range)
	ApplyBorderToRange(61)
	record_doc.CurrentController.select(bn_range)
	ApplyBorderToRange(61)
	record_doc.CurrentController.select(data_names_range)
	ApplyBorderToRange(26)
	record_doc.CurrentController.select(data_cells_range)
	ApplyBorderToRange(26)
	
	' Allign center bottom the main ranges.
	m_range = record_sheet.getCellRangeByName("B2:D5")
	record_doc.CurrentController.select(m_range)
	m_frame = record_doc.CurrentController.Frame

	m_uno_cmd = ".uno:CommonAlignHorizontalCenter"
	m_dispatch = createUnoService("com.sun.star.frame.DispatchHelper")
	m_dispatch.executeDispatch(m_frame, m_uno_cmd, "", 0, args())

	m_uno_cmd = ".uno:CommonAlignBottom"
	m_dispatch.executeDispatch(m_frame, m_uno_cmd, "", 0, args())
	
	' Allign data ranges.
	record_doc.CurrentController.select(data_cells_range)
	m_uno_cmd = ".uno:CommonAlignRight"
	m_dispatch = createUnoService("com.sun.star.frame.DispatchHelper")
	m_dispatch.executeDispatch(m_frame, m_uno_cmd, "", 0, args())
	
	record_doc.CurrentController.select(concept_cells_range)
	m_uno_cmd = ".uno:CommonAlignHorizontalCenter"
	m_dispatch = createUnoService("com.sun.star.frame.DispatchHelper")
	m_dispatch.executeDispatch(m_frame, m_uno_cmd, "", 0, args())
	
	mn_range.CellStyle = "mn_header"
	bn_range.CellStyle = "bn_header"
	data_names_range.CellStyle = "data_names"
	data_cells_range.CellStyle = "data_names"
End Function

Function ApplyBorderToRange(width As Long)
	Dim border_line As New com.sun.star.table.BorderLine2
	Dim table_border As New com.sun.star.table.TableBorder2

	m_range = record_doc.CurrentSelection

	border_line.Color = RGB(0, 0, 0)
	border_line.LineStyle = 0
	border_line.LineWidth = width
	
	table_border.VerticalLine = border_line
	table_border.IsVerticalLineValid = True
	
	table_border.HorizontalLine = border_line
	table_border.IsHorizontalLineValid = True
	
	table_border.TopLine = border_line
	table_border.IsTopLineValid = True
	
	table_border.RightLine = border_line
	table_border.IsRightLineValid = True
	
	table_border.LeftLine = border_line
	table_border.IsLeftLineValid = True
	
	table_border.BottomLine = border_line
	table_border.IsBottomLineValid = True
	
	m_range.TableBorder2 = table_border
End Function
