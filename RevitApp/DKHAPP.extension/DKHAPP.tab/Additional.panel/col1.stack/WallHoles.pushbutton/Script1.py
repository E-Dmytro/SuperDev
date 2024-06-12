# all_openings = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_SWallRectOpening).WhereElementIsNotElementType().ToElements()
# host_walls = [opening.Host for opening in all_openings]
# host_wall_ids = [wall.Id for wall in host_walls]
# print(host_wall_ids)
# t = Transaction(doc, 'Set Option1 parameter')
# t.Start()
# for opening, wall in zip(all_openings, host_walls):
#     bottom_elevation = opening.get_Parameter(BuiltInParameter.INSTANCE_SILL_HEIGHT_PARAM).AsDouble()
#     wall.LookupParameter('Option1').Set(bottom_elevation)
# t.Commit()

# all_openings = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_SWallRectOpening).WhereElementIsNotElementType().ToElements()
# host_walls = [opening.Host for opening in all_openings]
#
# t = Transaction(doc, 'Set Option1 parameter')
# t.Start()
# for opening, wall in zip(all_openings, host_walls):
#     bb = opening.get_BoundingBox(None)
#     min_point = bb.Min
#     min_value = min_point.Z
#     rounded_min_value = round(min_value, 2)
#     wall.LookupParameter('Option1').Set(str(rounded_min_value))
# t.Commit()
# all_openings = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_SWallRectOpening).WhereElementIsNotElementType().ToElements()
# host_walls = [opening.Host for opening in all_openings]
#
# project_position = doc.ActiveProjectLocation.GetProjectPosition(XYZ.Zero)
# project_elevation = project_position.Elevation
# project_base_point = XYZ(project_position.EastWest, project_position.NorthSouth, project_elevation)
#
# t = Transaction(doc, 'Set Option1 parameter')
# t.Start()
# for opening, wall in zip(all_openings, host_walls):
#     bb = opening.get_BoundingBox(None)
#     min_point = bb.Min
#     min_value = min_point.Z
#     rounded_min_value = round(min_value, 2)
#     project_base_point_value = project_base_point.Z
#     print(project_base_point_value)
#     wall.LookupParameter('Option1').Set(str(project_base_point_value))
# t.Commit()

# all_openings = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_SWallRectOpening).WhereElementIsNotElementType().ToElements()
# host_walls = [opening.Host for opening in all_openings]
#
# project_position = doc.ActiveProjectLocation.GetProjectPosition(XYZ.Zero)
# project_elevation = project_position.Elevation
# project_base_point = XYZ(project_position.EastWest, project_position.NorthSouth, project_elevation)
#
# t = Transaction(doc, 'Set Option1 parameter')
# t.Start()
# for opening, wall in zip(all_openings, host_walls):
#     bb = opening.get_BoundingBox(None)
#     max_point = bb.Max.Z
#     print (max_point)
#     rounded_min_value = round(max_point, 2)
#     x = project_base_point.Z
#     print (x)
#     project_base_point_value = rounded_min_value
#     print(project_base_point_value)
#     option1_param = wall.LookupParameter('Option1')
#     if option1_param:
#         option1_param.Set(str(project_base_point_value))
# t.Commit()

# GOOOD

# all_openings = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_SWallRectOpening).WhereElementIsNotElementType().ToElements()
# host_walls = [opening.Host for opening in all_openings]
# #
# # Get the transformation from the internal coordinate system to the shared coordinate system
# transform = doc.ActiveProjectLocation.GetTransform()
#
# t = Transaction(doc, 'Set Option1 parameter')
# t.Start()
# for opening, wall in zip(all_openings, host_walls):
#     bb = opening.get_BoundingBox(None)
#     max_point = bb.Max.Z
#     # Transform the maximum Z value from the Revit model coordinate system to the Dynamo coordinate system
#     # max_point_transformed = transform.OfPoint(XYZ(0, 0, max_point)).Z
#     z_display_units = UnitUtils.ConvertFromInternalUnits(max_point, DisplayUnitType.DUT_METERS)
#     rounded_min_value = round(z_display_units, 2)
#     project_base_point_value = rounded_min_value
#     print(project_base_point_value)
#     option1_param = wall.LookupParameter('Option1')
#     if option1_param:
#         option1_param.Set(str(project_base_point_value))
# t.Commit()

# Good 2

# all_openings = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_SWallRectOpening).WhereElementIsNotElementType().ToElements()
# host_walls = [opening.Host for opening in all_openings]
#
# # Get the transformation from the internal coordinate system to the shared coordinate system
# transform = doc.ActiveProjectLocation.GetTransform()
#
# t = Transaction(doc, 'Set Option1 parameter')
# t.Start()
# for opening, wall in zip(all_openings, host_walls):
#     bb = opening.get_BoundingBox(None)
#     max_point = bb.Max.Z
#     # Transform the maximum Z value from the Revit model coordinate system to the Dynamo coordinate system
#     # max_point_transformed = transform.OfPoint(XYZ(0, 0, max_point)).Z
#     z_display_units = UnitUtils.ConvertFromInternalUnits(max_point, DisplayUnitType.DUT_METERS)
#     print (z_display_units)
#     rounded_min_value = round(z_display_units, 2)
#     project_base_point_value = rounded_min_value
#     print(project_base_point_value)
#     option1_param = wall.LookupParameter('Option1')
#     if option1_param:
#         if len(all_openings) > 1:
#             z_display_units_values = [round(UnitUtils.ConvertFromInternalUnits(opening.get_BoundingBox(None).Max.Z, DisplayUnitType.DUT_METERS), 2) for opening in all_openings]
#             if len(set(z_display_units_values)) > 1:
#                 option1_param.Set(str(project_base_point_value) + ', ' + ', '.join(map(str, z_display_units_values)))
#             else:
#                 option1_param.Set(str(project_base_point_value))
#         else:
#             option1_param.Set(str(project_base_point_value))
# t.Commit()

# Good 3

# all_openings = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_SWallRectOpening).WhereElementIsNotElementType().ToElements()
# host_walls = [opening.Host for opening in all_openings]
#
# # Get the transformation from the internal coordinate system to the shared coordinate system
# transform = doc.ActiveProjectLocation.GetTransform()
#
# t = Transaction(doc, 'Set Option1 parameter')
# t.Start()
# for opening, wall in zip(all_openings, host_walls):
#     bb = opening.get_BoundingBox(None)
#     max_point = bb.Max.Z
#     # Transform the maximum Z value from the Revit model coordinate system to the Dynamo coordinate system
#     # max_point_transformed = transform.OfPoint(XYZ(0, 0, max_point)).Z
#     z_display_units = UnitUtils.ConvertFromInternalUnits(max_point, DisplayUnitType.DUT_METERS)
#     print (z_display_units)
#     rounded_min_value = round(z_display_units, 2)
#     project_base_point_value = rounded_min_value
#     print(project_base_point_value)
#     option1_param = wall.LookupParameter('Option1')
#     if option1_param:
#         wall_openings = [opening for opening in all_openings if opening.Host.Id == wall.Id]
#         if len(wall_openings) > 1:
#             z_display_units_values = [round(UnitUtils.ConvertFromInternalUnits(opening.get_BoundingBox(None).Max.Z, DisplayUnitType.DUT_METERS), 2) for opening in wall_openings]
#             if len(set(z_display_units_values)) > 1:
#                 option1_param.Set(str(project_base_point_value) + ', ' + ', '.join(map(str, z_display_units_values)))
#             else:
#                 option1_param.Set(str(project_base_point_value))
#         else:
#             option1_param.Set(str(project_base_point_value))
# t.Commit()







# How to write as level elevation height

# import clr
# clr.AddReference('RevitAPI')
# from Autodesk.Revit.DB import *
#
# doc = __revit__.ActiveUIDocument.Document
#
# # Get all walls in the document
# walls = FilteredElementCollector(doc).OfClass(Wall).ToElements()
#
# # Iterate through each wall
# for opening, wall in zip(all_openings, host_walls):
#
#     bb = opening.get_BoundingBox(None)
#     # Calculate the center of the bounding box
#     center = bb.Max
#     # Convert the X, Y, and Z values of the center point from internal Revit units to display units
#     x_display_units = UnitUtils.ConvertFromInternalUnits(center.X, DisplayUnitType.DUT_METERS)
#     y_display_units = UnitUtils.ConvertFromInternalUnits(center.Y, DisplayUnitType.DUT_METERS)
#     z_display_units = UnitUtils.ConvertFromInternalUnits(center.Z, DisplayUnitType.DUT_METERS)
#     # Print the coordinates of the center point
#     print("Wall: {}, X: {}, Y: {}, Z: {}".format(wall.Id, x_display_units, y_display_units, z_display_units))







# import clr
#
# clr.AddReference('RevitAPI')
# from Autodesk.Revit.DB import *
#
# doc = __revit__.ActiveUIDocument.Document
#
# # Get all wall instances in the current document
# walls = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()
#
# # Start a new transaction
# t = Transaction(doc, 'Add Annotations to Wall Openings')
# t.Start()
#
# # Set the annotation text here
# annotation_text = 'W Shapes-Section'  # <--- Change this text to your desired annotation
#
# # Get the default text note type
# textNoteType = doc.GetDefaultElementTypeId(ElementTypeGroup.TextNoteType)
#
# # Iterate through all walls
# # for wall in walls:
# #     # Get the wall's geometry
# #     wallGeo = wall.get_Geometry(Options())
# #
# #     # Calculate the area of the wall
# #     wallArea = 0
# #     for materialId in wall.GetMaterialIds(False):
# #         wallArea += wall.GetMaterialArea(materialId, False)
# #
# #     # Iterate through all solids in the wall's geometry
# #     for solid in wallGeo:
# #         if isinstance(solid, Solid):
# #             # Iterate through all faces of the solid
# #             for face in solid.Faces:
# #                 # Check if the face is an opening (i.e. has an area smaller than the wall's area)
# #                 if face.Area < wallArea:
# #                     # Get the center point of the face
# #                     center = face.Evaluate(UV(0.5, 0.5))
# #
# #                     # Create a new text note at the center point of the face with the specified annotation text and text note type
# #                     textNote = TextNote.Create(doc, doc.ActiveView.Id, center, annotation_text, textNoteType)
#
# # Commit the transaction
# t.Commit()

# import clr
# clr.AddReference('RevitAPI')
# from Autodesk.Revit.DB import *
#
# doc = __revit__.ActiveUIDocument.Document
# uidoc = __revit__.ActiveUIDocument
#
# # Start a transaction
# t = Transaction(doc, "Create Wall Annotations")
# t.Start()
#
# # Get all walls in the active view
# walls = FilteredElementCollector(doc, doc.ActiveView.Id).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()
#
# # Get a text note type to use for the new text notes
# textNoteType = FilteredElementCollector(doc).OfClass(TextNoteType).FirstElement()
#
# # Create a text note at the midpoint of each wall
# for wall in walls:
#     midpoint = (wall.Location.Curve.GetEndPoint(0) + wall.Location.Curve.GetEndPoint(1)) / 2
#     textNote = TextNote.Create(doc, doc.ActiveView.Id, midpoint, "Wall Annotation", textNoteType.Id)
#
# # Commit the transaction
# t.Commit()


# # 50/50
# import clr
# clr.AddReference('RevitAPI')
# from Autodesk.Revit.DB import *
#
# doc = __revit__.ActiveUIDocument.Document
# uidoc = __revit__.ActiveUIDocument
#
# # Start a transaction
# t = Transaction(doc, "Create Wall Annotations")
# t.Start()
#
# # Get all walls in the active view
# walls = FilteredElementCollector(doc, doc.ActiveView.Id).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()
#
# # Get a text note type to use for the new text notes
# textNoteType = FilteredElementCollector(doc).OfClass(TextNoteType).FirstElement()
#
# # Create a text note at the midpoint of each wall
# for wall in walls:
#     midpoint = (wall.Location.Curve.GetEndPoint(0) + wall.Location.Curve.GetEndPoint(1)) / 2
#     textNote = TextNote.Create(doc, doc.ActiveView.Id, midpoint, "Wall Annotation", textNoteType.Id)
#
#     # Check if the wall has a curtain grid
#     if wall.CurtainGrid:
#         # Get all wall openings in the current wall
#         openings = wall.CurtainGrid.GetCurtainCells()
#         for opening in openings:
#             # Get the center point of the opening
#             openingCenter = opening.Center
#             # Create a text note at the center of the opening
#             openingTextNote = TextNote.Create(doc, doc.ActiveView.Id, openingCenter, "Opening Annotation", textNoteType.Id)
#
# # Commit the transaction
# t.Commit()


# import clr
# clr.AddReference('RevitAPI')
# from Autodesk.Revit.DB import *
#
# doc = __revit__.ActiveUIDocument.Document
# uidoc = __revit__.ActiveUIDocument
#
# # Start a transaction
# t = Transaction(doc, "Create Wall Annotations")
# t.Start()
#
# # Get all walls in the active view
# walls = FilteredElementCollector(doc, doc.ActiveView.Id).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()
#
# # Get a text note type to use for the new text notes
# textNoteType = FilteredElementCollector(doc).OfClass(TextNoteType).FirstElement()
#
# # Create a text note at the midpoint of each wall
# for wall in walls:
#     midpoint = (wall.Location.Curve.GetEndPoint(0) + wall.Location.Curve.GetEndPoint(1)) / 2
#     textNote = TextNote.Create(doc, doc.ActiveView.Id, midpoint, "Wall Annotation", textNoteType.Id)
#
#     # Get all wall openings in the current wall
#     openings = []
#     for opening in wall.CurtainGrid.GetCurtainCells():
#         openings.append(opening)
#     for opening in wall.FamilyInstanceVoidCuts:
#         openings.append(opening)
#
#     for opening in openings:
#         # Get the center point of the opening
#         openingCenter = opening.Center
#         # Create a text note at the center of the opening
#         openingTextNote = TextNote.Create(doc, doc.ActiveView.Id, openingCenter, "Opening Annotation", textNoteType.Id)
#
# # Commit the transaction
# t.Commit()





# import clr
# clr.AddReference('RevitAPI')
# from Autodesk.Revit.DB import *
#
# doc = __revit__.ActiveUIDocument.Document
# uidoc = __revit__.ActiveUIDocument
#
# # Start a transaction
# t = Transaction(doc, "Create Wall Annotations")
# t.Start()
#
# # Get all walls in the active view
# walls = FilteredElementCollector(doc, doc.ActiveView.Id).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()
#
# # Get a text note type to use for the new text notes
# textNoteType = FilteredElementCollector(doc).OfClass(TextNoteType).FirstElement()
#
# # Create a text note at the midpoint of each wall
# for wall in walls:
#     midpoint = (wall.Location.Curve.GetEndPoint(0) + wall.Location.Curve.GetEndPoint(1)) / 2
#     textNote = TextNote.Create(doc, doc.ActiveView.Id, midpoint, "Wall Annotation", textNoteType.Id)
#
#     # Check if the wall has a curtain grid
#     if wall.CurtainGrid:
#         # Get all wall openings in the current wall
#         openings = []
#         for opening in wall.CurtainGrid.GetCurtainCells():
#             openings.append(opening)
#         for opening in wall.FamilyInstanceVoidCuts:
#             openings.append(opening)
#
#         for opening in openings:
#             # Get the center point of the opening
#             openingCenter = opening.Center
#             # Create a text note at the center of the opening
#             openingTextNote = TextNote.Create(doc, doc.ActiveView.Id, openingCenter, "Opening Annotation", textNoteType.Id)
#
# # Commit the transaction
# t.Commit()


# for opening, wall in zip(all_openings, host_walls):
#     bb = opening.get_BoundingBox(None)
#     max_point = bb.Max.Z
#     max_pointX = bb.Max.X
#     min_pointX = bb.Min.X
#     mid_pointX = (max_pointX + min_pointX) / 2
#     print("X= " + str(mid_pointX))
#     textNoteType = FilteredElementCollector(doc).OfClass(TextNoteType).FirstElement()
#
#     # Create an XYZ object using the mid_pointX value
#     location = XYZ(mid_pointX, 0, 0)
#
#     # Pass the XYZ object as the third argument to the TextNote.Create method
#     textNote = TextNote.Create(doc, doc.ActiveView.Id, location, "Wall Annotation", textNoteType.Id)


# from Autodesk.Revit.DB import *
#
# all_openings = FilteredElementCollector(doc).OfCategory(
#     BuiltInCategory.OST_SWallRectOpening).WhereElementIsNotElementType().ToElements()
# host_walls = [opening.Host for opening in all_openings]
#
# # Get the transformation from the internal coordinate system to the shared coordinate system
# transform = doc.ActiveProjectLocation.GetTransform()
#
# t = Transaction(doc, 'Set Option1 parameter')
# t.Start()
# for opening, wall in zip(all_openings, host_walls):
#     bb = opening.get_BoundingBox(None)
#     max_point = bb.Max.Z
#     max_pointX = bb.Max.X
#     min_pointX = bb.Min.X
#     max_pointY = bb.Max.Y
#     min_pointY = bb.Min.Y
#     mid_pointY = (max_pointY + min_pointY) / 2
#     mid_pointX = (max_pointX + min_pointX) / 2
#     print("X= " + str(mid_pointX))
#     textNoteType = FilteredElementCollector(doc).OfClass(TextNoteType).FirstElement()
#     location = XYZ(mid_pointX, mid_pointY, 0)
#
#     # Transform the maximum Z value from the Revit model coordinate system to the Dynamo coordinate system
#     # max_point_transformed = transform.OfPoint(XYZ(0, 0, max_point)).Z
#     z_display_units = UnitUtils.ConvertFromInternalUnits(max_point, DisplayUnitType.DUT_METERS)
#     print(z_display_units)
#     rounded_min_value = round(z_display_units, 2)
#     project_base_point_value = rounded_min_value
#     print(project_base_point_value)
#
#     # Insert the relevant z_display_units_value into the text note
#     textNote = TextNote.Create(doc, doc.ActiveView.Id, location, str(project_base_point_value), textNoteType.Id)
#
#     option1_param = wall.LookupParameter('Option1')
#     if option1_param:
#         wall_openings = [opening for opening in all_openings if opening.Host.Id == wall.Id]
#         if len(wall_openings) > 1:
#             z_display_units_values = [round(
#                 UnitUtils.ConvertFromInternalUnits(opening.get_BoundingBox(None).Max.Z, DisplayUnitType.DUT_METERS), 2)
#                                       for opening in wall_openings]
#             if len(set(z_display_units_values)) > 1:
#                 option1_param.Set(', '.join(map(str, z_display_units_values)))
#             else:
#                 option1_param.Set(str(project_base_point_value))
#         else:
#             option1_param.Set(str(project_base_point_value))
# t.Commit()



# # Get the level by its name
# level = FilteredElementCollector(doc).OfClass(Level).Where(lambda x: x.Name == "Level 1").FirstElement()
#
# # Get all walls in the active view that are on the specified level
# walls = FilteredElementCollector(doc, doc.ActiveView.Id).\
#     OfCategory(BuiltInCategory.OST_Walls).\
#     WhereElementIsNotElementType().\
#     Where(lambda x: x.LevelId == level.Id).\
#     ToElements()






# import clr
# clr.AddReference('RevitAPI')
# from Autodesk.Revit.DB import *
#
# doc = __revit__.ActiveUIDocument.Document
#
# # Get all walls in the document
# walls = FilteredElementCollector(doc).OfClass(Wall).ToElements()
#
# # Iterate through each wall
# for opening, wall in zip(all_openings, host_walls):
#
#     bb = opening.get_BoundingBox(None)
#     # Calculate the center of the bounding box
#     center = bb.Max
#     # Convert the X, Y, and Z values of the center point from internal Revit units to display units
#     x_display_units = UnitUtils.ConvertFromInternalUnits(center.X, DisplayUnitType.DUT_METERS)
#     y_display_units = UnitUtils.ConvertFromInternalUnits(center.Y, DisplayUnitType.DUT_METERS)
#     z_display_units = UnitUtils.ConvertFromInternalUnits(center.Z, DisplayUnitType.DUT_METERS)
#     # Print the coordinates of the center point
#     print("Wall: {}, X: {}, Y: {}, Z: {}".format(wall.Id, x_display_units, y_display_units, z_display_units))


