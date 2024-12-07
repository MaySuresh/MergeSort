def sortAndFindMedian(numbers):
    sort(numbers)
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else: 
        return numbers[n // 2]

def sort (numbers):
    if len(numbers) >1:
        split = len(numbers) // 2
        
        first = numbers[:split]
        sort(first)        
        
        second = numbers[split:]
        sort(second)
       
        x = y = z = 0
       
        while x < len(first) and y < len(second):
            if first[x] < second[y]:
                numbers[z] = first[x]
                x = x+1
            else: 
                numbers[z] = second[y]
                y=y+1
            z= z+1
        while x < len(first):
            numbers[z] =  first[x]
            x = x+1
            z = z+1
            
        while y < len(second):
            numbers[z] = second[y]
            y = y+1
            z = z+1


def main():
    numbers = [38, 27, 43, 3, 9, 82,10]
  
    median = sortAndFindMedian(numbers)

    print("Median:", median)


if __name__ == '__main__':
    main()