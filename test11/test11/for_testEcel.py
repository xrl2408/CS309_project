import xlrd
guy1 = ''
guy = 'zdh/xrl/ z k /'
k1 = "PHY103A"
k = "PHY103A&PHY103B"
guy_list = k1.split('&')
print(guy_list)



# bok = xlrd.open_workbook(r'/Users/kumazuirin/Desktop/PHY_exp.xlsx')
# sht = bok.sheets()[0]
# row1 = sht.row_values(0)
# cell_d4 = sht.cell(1,1).value
# print(len(sht.col_values(1)))
# print(len(sht.row_values(1)))
# print(sht.cell(5,5).value == '')
# row_num =sht.nrows
#
#
# name_of_department = ""
# error = 0
# errors = []
# pre_course_1 = []
# pre_course_1_addi = []
# pre_course_2 = []
# pre_course_2_addi = []
# req_course_base = []
# req_course_base_addi = []
# req_course_core = []
# req_course_core_addi = []
# req_course_exp = []
# req_course_exp_addi = []
# ele_course = []
# ele_course_addi = []
# exp_course = []
# exp_course_addi = []
# tb = []
# fun_of_sci_eng = []
# fun_of_sci_eng_addi = []
# Eng = []
# Eng_addi = []
# Ipe = []
# Ipe_addi = []
# Pe = []
# Pe_addi = []
# W_c = []
# W_c_addi = []
#
#
# tb.append(int(sht.cell(1,10).value))
# tb.append(int(sht.cell(2,10).value))
# tb.append(int(sht.cell(3,10).value))
# tb.append(int(sht.cell(4,10).value))
# tb.append(int(sht.cell(5,10).value))
# tb.append(int(sht.cell(6,10).value))
# tb.append(int(sht.cell(7,10).value))
# tb.append(int(sht.cell(8,10).value))
# tb.append(int(sht.cell(9,10).value))
# tb.append(int(sht.cell(10,10).value))
# tb.append(int(sht.cell(11,10).value))
#
#
#
#
#
#
# if sht.cell(0,0).value == "Code for department":
#     name_of_department = sht.cell(1, 0).value
#     pass
# else:
#     error = 1
# if sht.cell(0,1).value == "Prerequisite courses for 1":
#     for i in range(1,row_num):
#         out = 0
#         if (sht.cell(i,1).value == ""):
#             break;
#         if (sht.cell(i,1).value == "Additional"):
#             out = 1
#             for j in range(i+1,row_num):
#                 if (sht.cell(j, 1).value == ""):
#                     break;
#                 pre_course_1_addi.append(sht.cell(j,1).value)
#         if out == 1 :
#             break
#         pre_course_1.append(sht.cell(i,1).value)
#
# else:
#     error = 1
# if sht.cell(0,2).value == "Prerequisite courses for 2":
#     for i in range(1,row_num):
#         out = 0
#         if (sht.cell(i,2).value == ""):
#             break;
#         if (sht.cell(i,2).value == "Additional"):
#             out = 1
#             for j in range(i+1,row_num):
#                 if (sht.cell(j, 2).value == ""):
#                     break;
#                 pre_course_2_addi.append(sht.cell(j,2).value)
#         if out == 1 :
#             break
#         pre_course_2.append(sht.cell(i,2).value)
#
# else:
#     error = 1
# if sht.cell(0,3).value == "Required course base":
#     for i in range(1,row_num):
#         out = 0
#         if (sht.cell(i,3).value == ""):
#             break;
#         if (sht.cell(i,3).value == "Additional"):
#             out = 1
#             for j in range(i+1,row_num):
#                 if (sht.cell(j, 3).value == ""):
#                     break;
#                 req_course_base_addi.append(sht.cell(j,3).value)
#         if out == 1 :
#             break
#         req_course_base.append(sht.cell(i,3).value)
# else:
#     error = 1
#
# if sht.cell(0, 4).value == "Required course core":
#     for i in range(1, row_num):
#         out = 0
#         if (sht.cell(i, 4).value == ""):
#             break;
#         if (sht.cell(i, 4).value == "Additional"):
#             out = 1
#             for j in range(i + 1, row_num):
#                 if (sht.cell(j, 4).value == ""):
#                     break;
#                 req_course_core_addi.append(sht.cell(j, 4).value)
#         if out == 1:
#             break
#         req_course_core.append(sht.cell(i, 4).value)
# else:
#     error = 1
#
# if sht.cell(0, 5).value == "Required course experience":
#     for i in range(1, row_num):
#         out = 0
#         if (sht.cell(i, 5).value == ""):
#             break;
#         if (sht.cell(i, 5).value == "Additional"):
#             out = 1
#             for j in range(i + 1, row_num):
#                 if (sht.cell(j, 5).value == ""):
#                     break;
#                 req_course_exp_addi.append(sht.cell(j, 5).value)
#         if out == 1:
#             break
#         req_course_exp.append(sht.cell(i, 5).value)
# else:
#     error = 1
#
# if sht.cell(0,6).value == "Election":
#     for i in range(1,row_num):
#         out = 0
#         if (sht.cell(i,6).value == ""):
#             break;
#         if (sht.cell(i,6).value == "Additional"):
#             out = 1
#             for j in range(i+1,row_num):
#                 if (sht.cell(j, 6).value == ""):
#                     break;
#                 ele_course_addi.append(sht.cell(j,6).value)
#         if out == 1 :
#             break
#         ele_course.append(sht.cell(i,6).value)
# else:
#     error = 1
#
#
# if sht.cell(0,7).value == "Experience":
#     for i in range(1,row_num):
#         out = 0
#         if (sht.cell(i,7).value == ""):
#             break;
#         if (sht.cell(i,7).value == "Additional"):
#             out = 1
#             for j in range(i+1,row_num):
#                 if (sht.cell(j, 7).value == ""):
#                     break;
#                 exp_course_addi.append(sht.cell(j,7).value)
#         if out == 1 :
#             break
#         exp_course.append(sht.cell(i,7).value)
# else:
#     error = 1
#
#
# if sht.cell(0,11).value == "Fundamentals of science and Engineering":
#     for i in range(1,row_num):
#         out = 0
#         if (sht.cell(i,11).value == ""):
#             break;
#         if (sht.cell(i,11).value == "Additional"):
#             out = 1
#             for j in range(i+1,row_num):
#                 if (sht.cell(j, 11).value == ""):
#                     break;
#                 fun_of_sci_eng_addi.append(sht.cell(j,11).value)
#         if out == 1 :
#             break
#         fun_of_sci_eng.append(sht.cell(i,11).value)
#         print(sht.cell(i,11).value)
# else:
#     error = 1
#
# if sht.cell(0,12).value == "English":
#     for i in range(1,row_num):
#         out = 0
#         if (sht.cell(i,12).value == ""):
#             break;
#         if (sht.cell(i,12).value == "Additional"):
#             out = 1
#             for j in range(i+1,row_num):
#                 if (sht.cell(j, 12).value == ""):
#                     break;
#                 Eng_addi.append(sht.cell(j,12).value)
#         if out == 1 :
#             break
#         Eng.append(sht.cell(i,12).value)
# else:
#     error = 1
#
# if sht.cell(0,13).value == "IPE":
#     for i in range(1,row_num):
#         out = 0
#         if (sht.cell(i,13).value == ""):
#             break;
#         if (sht.cell(i,13).value == "Additional"):
#             out = 1
#             for j in range(i+1,row_num):
#                 if (sht.cell(j, 13).value == ""):
#                     break;
#                 Ipe_addi.append(sht.cell(j,13).value)
#         if out == 1 :
#             break
#         Ipe.append(sht.cell(i,13).value)
# else:
#     error = 1
#
# if sht.cell(0,14).value == "PE":
#     for i in range(1,row_num):
#         out = 0
#         if (sht.cell(i,14).value == ""):
#             break;
#         if (sht.cell(i,14).value == "Additional"):
#             out = 1
#             for j in range(i+1,row_num):
#                 if (sht.cell(j, 14).value == ""):
#                     break;
#                 Pe_addi.append(sht.cell(j,14).value)
#         if out == 1 :
#             break
#         Pe.append(sht.cell(i,14).value)
# else:
#     error = 1
#
# if sht.cell(0,15).value == "Writing and Comunication":
#     for i in range(1,row_num):
#         out = 0
#         if (sht.cell(i,15).value == ""):
#             break;
#         if (sht.cell(i,15).value == "Additional"):
#             out = 1
#             for j in range(i+1,row_num):
#                 if (sht.cell(j, 15).value == ""):
#                     break;
#                 W_c_addi.append(sht.cell(j,15).value)
#         if out == 1 :
#             break
#         W_c.append(sht.cell(i,15).value)
# else:
#     error = 1
#
#
# print(name_of_department)
# print(pre_course_1)
# print(pre_course_1_addi)
# print(pre_course_2)
# print(pre_course_2_addi)
# print(req_course_base)
# print(req_course_base_addi)
# print(req_course_core)
# print(req_course_core_addi)
# print(req_course_exp)
# print(req_course_exp_addi)
# print(ele_course)
# print(ele_course_addi)
# print(exp_course)
# print(exp_course_addi)
# print(tb)
# print(fun_of_sci_eng)
# print(fun_of_sci_eng_addi)
# print(Eng)
# print(Eng_addi)
# print(Ipe)
# print(Ipe_addi)
# print(Pe)
# print(Pe_addi)
# print(W_c)
# print(W_c_addi)
