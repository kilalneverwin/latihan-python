def main():
    print("dear seseorang maukah kau menjadi kekasihku.")
    print("1. mau")
    print("2. tidak")
    print("3. aku gak suka pacaran")

    choice = input("masukkan pilihan==> ")

    if choice == "mau" or choice == "1":
        print("Alhamdulilah")
    elif choice == "tidak" or choice == "2":
        print("yah kirain mau")
    elif choice == "aku gak suka pacaran" or choice == "3":
        print("Bacot lu ngentot")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
    