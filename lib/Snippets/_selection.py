# -*- coding: utf-8 -*-

# Imports
from Autodesk.Revit.DB import *

# Variables
uidoc = __revit__.ActiveUIDocument
doc   = __revit__.ActiveUIDocument.Document

# Functions
def get_selected_elements(uidoc):
    """Function to get selected elements in Revit UI."""
    docs = uidoc.Document
    print (docs.Title)
    return [docs.GetElement(e_id) for e_id in uidoc.Selection.GetElementIds()]