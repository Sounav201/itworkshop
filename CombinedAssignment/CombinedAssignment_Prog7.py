def Calculate_Bill(StoreList,Customer_List):
    total = 0
    for item in Customer_List:
        if item in StoreList:
            cost = StoreList[item] * Customer_List[item]
            total += cost
        else:
            return -1
    return total

Products = { "PlayStation 5": 40000, "Xbox Series X": 45000, "Sony WBHX900": 14000, "Raspberry Pi 4": 6000, "San-Disk 32GB USB Drive": 700 }
CustomerProducts = { "Raspberry Pi 4": 3, "Xbox Series X": 1, "San-Disk 32GB USB Drive": 5 }


print("Yor total bill : Rs " , Calculate_Bill(Products,CustomerProducts))
