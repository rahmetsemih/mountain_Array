def validMountainArray(arr):
    if (len(arr) < 3):
        return False

    # Arrayin yükselen kısmının bittiği noktayı bulalım..
    i = 1
    while (i < len(arr) and arr[i] > arr[i - 1]):
        i += 1

    #  Dizinin sonuna geldiysek sadece yükselme işlemi var alçalan kısım yok False döndür..
    if (i == 1 or i == len(arr)):
        return False

    # Arrayin azalan kismina bakalım nereye kadar azalma olacak
    while (i < len(arr) and arr[i] < arr[i - 1]):
        i += 1

    # Eğer alçalan kısmın bitişi dizinin sonu ise bu bir Mountain Array'dir..
    # Aksi takdirde tekrar bir yükselme veya eşitlik olacaktır ki Mountain Array tanımına
    # uymaz...
    if (i == len(arr)):
        return True
    else:
        return False


lst = [0, 4, 2, 1]
print(validMountainArray(lst))   