from classStudent import *

def isExist(fullName):
    file = open("dataBase.txt", "r", encoding="utf-8")
    for row in file:
        if row.split(";")[0] == fullName:
            file.close()
            return True
    file.close()
    return False

def addStudent():
    try:
        fullName = input("Nhập tên đầy đủ: ")
        while True:
            sex = input("Nhập giới tính (Nam / Nữ): ")
            if sex in ["Nam", "Nữ"]:
                break
            else:
                print("Chúng tôi chỉ chấp nhận Nam hoặc Nữ")
        className = input("Nhập tên lớp: ")
        point = int(input("Nhập điểm: "))
        file = open("dataBase.txt", "a", encoding="utf-8")
        data = classStudent(fullName, sex, className, point)
        file.writelines(data.__str__() + "\n")
        file.close()
        print("Đã lưu dữ liệu của bạn!")
    except:
        print("Xin lỗi. Có một số lỗi!")


def removeStudent():
    fullName = input("Nhập tên đầy đủ của sinh viên muốn xóa: ")
    if not isExist(fullName):
        print(fullName + " không tồn tại")
        return
    data = []
    try:
        file = open("dataBase.txt", "r", encoding="utf-8")
        data = map(lambda item: item.split(";"), file)
        #file.close()
    except:
        print("Lỗi khi đọc tệp")
        return
    newData = list(filter(lambda item: item[0] != fullName, data))
    file = open("dataBase.txt", "w", encoding="utf-8")
    for row in newData:
        file.writelines(";".join(row))
    file.close()
    print("Sinh viên bị xóa có tên là " + fullName)


def updateStudent():
    fullName = input("Nhập tên đầy đủ của sinh viên muốn cập nhật: ")
    if not isExist(fullName):
        print(fullName + " không tồn tại")
        return
    print("Vui lòng nhập thông tin để cập nhật (Nhập '.' bỏ qua)")
    while True:
        sex = input("Giới tính (Nam/Nữ): ")
        if sex in ["Nam", "Nữ", "."]:
            break
        else:
            print("Chúng tôi chỉ chấp nhận Nam hoặc Nữ hoặc .")
    className = input("Tên lớp: ")
    point = input("Điểm: ")
    data = []
    try:
        file = open("dataBase.txt", "r", encoding="utf-8")
        data = list(map(lambda item: item.split(";"), file))
        # file.close()
    except:
        print("Lỗi khi đọc tệp")
        return
    for i in range(len(data)):
        if data[i][0] == fullName:
            data[i][1] = sex if sex != "." else data[i][1]
            data[i][2] = className if className != "." else data[i][2]
            data[i][3] = point + "\n" if point != "." else data[i][3]
    file = open("dataBase.txt", "w", encoding="utf-8")
    for row in data:
        file.writelines(";".join(row))
    file.close()
    print("Cập nhật sinh viên có tên là " + fullName)


def viewStudent():
    try:
        file = open("dataBase.txt", "r", encoding="utf-8")
        print("| {} | {} | {} | {} |".format("Tên đầy đủ".center(20), "Giới tính".center(6), "Tên lớp".center(10),
                                             "Điểm".center(4)))
        print("".center(53, "-"))
        for row in file:
            data = row.split(";")
            data[3] = int(data[3])
            sv = classStudent(*data)
            sv.showInfo()
        file.close()
    except:
        print("Lỗi khi đọc dữ liệu")


def viewAfterSort():
    try:
        file = open("dataBase.txt", "r", encoding="utf-8")
        print("| {} | {} | {} | {} |".format("Tên đầy đủ".center(20), "Giới tính".center(6), "Tên lớp".center(10),
                                             "Điểm".center(4)))
        print("".center(53, "-"))
        listData = list(file)
        listData.sort(key=lambda item: int(item.split(";")[3]))
        for row in listData:
            data = row.split(";")
            data[3] = int(data[3])
            sv = classStudent(*data)
            sv.showInfo()
        file.close()
    except:
        print("Lỗi khi đọc dữ liệu")