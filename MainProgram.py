from method import *
optinals = '''
    1. Thêm Sinh Viên
    2. Xóa Sinh Viên
    3. Cập nhật Sinh Viên
    4. Xem tất cả Sinh Viên
    5. Xem tất cả Sinh Viên sau khi sắp xếp theo điểm
    6. Thoát
'''

actionOptional = dict()
actionOptional["1"] = addStudent
actionOptional["2"] = removeStudent
actionOptional["3"] = updateStudent
actionOptional["4"] = viewStudent
actionOptional["5"] = viewAfterSort

print("       Chào mừng đến với chương trình quản lý sinh viên")
while True:
    print(optinals)
    print("Vui lòng nhập tùy chọn của bạn: ", end="")
    optinal = input()
    if optinal == "6":
        print("Cảm ơn bạn đã sử dụng chương trình - GOODBYE")
        break
    if optinal not in actionOptional:
        print("Không khớp với bất kỳ hành động nào, vui lòng chọn lại")
    else:
        actionOptional[optinal]()