################### Exercice 1

# 1

# def find(file,key):
#     lis = []
#
#     def _json_object_hook(d):
#         try:
#             if key in d:
#                 lis.append(d[key])
#
#         except KeyError:
#             pass
#
#         return
#
#
#     with open(file) as f:
#         json.load(f, object_hook = _json_object_hook)
#         fin_lis = []
#         for item in lis:
#             # if key in item:
#
#             our_set = set()
#             for i in range(0, len):
#                 if type(lis[i]) == list:
#                     our_set.update(lis[i])
#                 if type(lis[i]) == str:
#                     our_set.add(lis[i])
#             fin_lis = list(our_set)
#
#         return fin_lis

# 2

# def get_values(item, needle, result=None):
#     if result is None:
#         result = []
#
#     for val in item:
#         if isinstance(item, dict):
#             get_values(item[val], needle, result)
#         elif isinstance(item,list):
#             get_values(val, needle, result)
#
#         if val == needle:
#             if isinstance(item[needle], list):
#                 result.extend([i for i in item[needle] if i not in result ])
#             else:
#                 result.append(item[needle])
#
#     return result
#
# def find(json, key):
#     with open(json,'r') as f:
#         data = json.load(f)
#         res = get_values(data,key)
#         return res


# 3

# def find(file, key):
#     passwords_set = set()
#
#     def get_password(dct):
#         if key in dct:
#             value = dct.get(key)
#             passwords_set.update(value) if isinstance(value, list) else passwords_set.add(value)
#
# with open(file, 'r') as f:
#     json.load(f, object_hook=get_password)
#
# return list(passwords_get)




################### Exercice 2

# 1
# import json
# import logging
#
# def parse_user(output_file, *input_file):
#
#     result = []
#     names = []
#
#     for file in input_file:
#         # print(data)
#         try:
#             with open(file,'r') as file:
#                 data = json.load(file)
#                 # print(data)
#                 for d in data:
#                     # print(d)
#                     for key, value in d.items():
#                         # print(f'key = {key}, value = {value}')
#                         if key == 'name':
#                             if value not in names:
#                                 names.append(value)
#                                 result.append(d)
#         except:
#             # print('Eroor')
#             logging.error(f"File {file} doesn't exist")
#
#         # print(json.dumps(result, ident=4, sort_keys=False))
#         with open(output_file,"w") as file:
#             json.dump(result, file, indent=4, sort_keys=False)
#         # return result


################### Exercice 3

# 1
# import csv
# import json
#
#
# def user_with_department(csv_file, user_json, department_json):
#     c=0
#     my_dict = []
#     res_dict = []
#     res_user = None
#     res_depart = None
#
#     with open(user_json, 'r') as file_user:
#         data_user = json.load(file_user)
#     with open(department_json, 'r') as file_department:
#         data_department =json.load(file_department)
#     for d_u in data_user:
#
#         if validate_json(d_u, schema_user, 'user') is not None:
#             res_user = 1
#     for d_d in data_department:
#
#         if validate_json(d_d, schema_department, 'department') is not None:
#             res_depart = 1
#
#     if res_user == None and res_depart==None:
#         for l in data_user:
#             for l_d in data_department:
#                 try:
#                     if l_d['id'] == l['department_id']:
#                         my_dict.append({'name': l['name'], 'department':l_d['name']})
#                     else:
#                         c += 1
#                     if c == len(data_department):
#                         raise DepartmentName(f"Department with id {l['department_id']}does't exist")
#                 except DepartmentName as e:
#                     print(e)
#
#             c = 0
#     if len(data_user) == len(my_dict):
#         fields = ['name', 'department']
#     with open(csv_file, 'w', newline='') as csvfile:
#         write = csv.DictWriter(csvfile, fieldnames=fields)
#         write.writeheader()
#         write.writerows(my_dict)



# user_schema = {
#     "owner": "user",
#     "type" : "object",
#     "properties" : {
#         "id" : {"type":"number"},
#         "name" :{"type": "number"}
#     },
#     "required": ["id", "name", "department_id"]
# }
#
# department_schema = {
#     "owner": "department",
#     "type": "array",
#     "items": {
#         "type": "object",
#         "properties": {
#             "id": {"type": "number"},
#             "name": {"type": "string"},
#         },
#         "required": ["id","name"]
#     }
# }
#
# class DepartmentName(Exception):
#     pass
#
# class InvalidInstanceError(Exception):
#     pass
#
# def validate_json(data,schema):
#     try:
#         validate_json(data, schema)
#         return data
#     except:
#         raise InvalidInstanceError(f"Error in {schema['owner']} schema")
#
#
############2

# import csv
# import json
#
# schemaUser = {
#     "type" : "object",
#     "properties" : {
#         "id" : {"type":"number"},
#         "name" :{"type": "string"},
#         "department_id": {'type':"number"}
#     },
#     "required": ["id", "name", "department_id"]
# }
#
# schemaDepart = {
#     "type": "object",
#     "properties": {
#         "id": {"type": "number"},
#         "name": {"type": "string"},
#     },
#     "required": ["id","name"]
#
#
# }
#
#
# class DepartmentName(Exception):
#     def __init__(self,dep ):
#         self.dep=dep
#     def __str__(self):
#         return f"Department with id{self.dep} doesn't exist"
# class InvalidInstanceError(Exception):
#     def __init__(self,text):
#         self.text = text
#
#
# def validate_json(data,schema,name):
#     try:
#         for line in data:
#             validate(line,schema)
#
#     except jsonschema.exceptions.ValidationError:
#         raise InvalidInstanceError(f"Error in {schema['owner']} schema")
#
# def user_with_department(csv_file, user_json, department_json):
#     try:
#         with open(user_json) as f:
#             data_user = json.load(f)
#             validate_json(data_user, schemaUser, 'user schema')
#         with open(department_json) as ff:
#             data_dep = json.load(ff)
#             validate_json(data_dep, schemaDepart, 'department schema')
#         list_to_write = [["name","department"]]
#         for i in data_user:
#             flag = False
#             for j in data_dep:
#                 if i["department_id"] == j["id"]:
#                     flag = True
#                     user_named = i['name']
#                     dep_name = j["name"]
#             if flag == True:
#                 empty_list = []
#                 empty_list.append(user_named)
#                 empty_list.append(dep_name)
#                 list_to_write.append(empty_list)
#             else:
#                 raise DepartmentName(i["department_id"])
#
#         with open(csv_file,'w') as file:
#             write = csv.writer(file,delimiter = ',')
#             for line in list_to_write:
#                 write.writerow(line)
#     except FileNotFoundError:
#         pass
#
# def validate_json(data, schema, who):
#     try:
#         if validate(data,schema)is None:
#             return None
#     except jsonschema.exceptions.ValidationError as e:
#         print(f"Error in {who} schema")
#         return 1
#



################### Exercice 4


# 1
# class Student:
#     def __init__(self, full_name : str, avg_rank: float, courses: list ):
#         self.full_name = full_name
#         self.avg_rank = avg_rank
#         self.courses = courses
#
#     def __str__(self):
#         return f"{self.full_name} ({self.avg_rank}):{self.courses}"
#
#     @staticmethod
#     def from_json(json_file):
#         with open(json_file, "r") as f:
#             data = json.load(f)
#             return Student(**data)
#
# class Group:
#     def __init__(self, title: str, students: list):
#         self.title = title
#         self.students = students
#
#     def __str__(self):
#         return f"{self.title}: {[str(x) for x in self.students]}"
#
#     @staticmethod
#     def create_group_from_file(students_file):
#         name = students_file.replace(".json","")
#         students = []
#         with open(students_file, "r") as f:
#             data = json.load(f)
#             if isinstance(data, list):
#                 for i in data:
#                     students.append(Student(**i))
#             else:
#                 students.append(Student(**data))
#         return Group(name, students)
#
#     @staticmethod
#     def serialize_to_json(list_of_groups, filename):
#         with open(filename, "w") as f:
#             data = json.dumps(list_of_groups, default = lambda o:o.__dict__, sort_keys = False)
#             f.write(data)





################### Exercice 5

# 1
# import json
# import pickle
#
#
# class FileType(str, Enum):
#     JSON = 'JSON'
#     BYTE = 'BYTE'
#
# class SerializeManager():
#     def __init__(self, filename, type):
#         self.filename = filename
#         self.type = type
#
#     def __enter__(self):
#         if self.type == 'JSON':
#             self.file = open(self.filename,'w')
#         elif self.type == 'BYTE':
#             self.file = open(self.filename, "wb")
#         return  self
#
#     def serialize(self, obj):
#         if self.type == 'JSON':
#             return json.dump(obj, self.file, default=lambda o: o.__dict__)
#         elif self.type == 'BYTE' :
#             return pickle.dump(obj, self.file)
#
#     def __exit__(self, exc_type, exc_val, traceback):
#         self.file.close()
#
# def serialize(object, filename, fileType):
#     with SerializeManager(filename, fileType) as manager:
#         manager.serialize(object)