def bubble_sort(arr, pos = 3) -> list:
    n = len(arr) - 1 
    for i in range(n):
        
        for j in range(0, n-i):
        
            if arr[j][pos] > arr[j+1][pos] :
                arr[j], arr[j+1] = arr[j+1], arr[j]    
    return arr

def read_data(file_name: str) -> list:
    data = []
    with open(file_name + ".txt") as data_file: 
        for line in data_file:
            line = line.replace("\n","") 
            newline = line.rstrip(",").split(",") 
            data.append(newline) 
    return data

if __name__ == '__main__':
    import pandas as pd 
    data = read_data("datos")
    print("|-----------------------------Unordered list----------------------------|")
    printable = pd.DataFrame(data, columns=["Paternal surname","Mother's last name","Name","CURP"])
    print(printable.to_string(index=False))
    data = bubble_sort(data)
    printable = pd.DataFrame(data, columns=["Paternal surname","Mother's last name","Name","CURP"])
    print("\n|------------------------------Ordered list------------------------------|")
    print(printable.to_string(index=False))