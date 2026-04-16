def get_rect_area(w, h):
    return w * h

def main():
    width = int(input("너비 입력: "))
    height = int(input("높이 입력: "))

    area = get_rect_area(width, height)
    print("사각형의 면적:", area)

main()