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
        
        """Spliting the first half of the array"""
        first = numbers[:split]
        """Spliting it further more recursively and sorting until the array will be equal to 1"""
        sort(first)        
        
        """Spliting the second half of the array"""
        second = numbers[split:]
        """Spliting the it further more recursively and sorting until the array will be equal to 1"""
        sort(second)
       
        "These are the points to keep track of the merging process"
        x = y = z = 0
       
        "Here the loop will merge the halves back ito numbers array"
        while x < len(first) and y < len(second):
            if first[x] < second[y]:
                numbers[z] = first[x]
                x = x+1
            else: 
                numbers[z] = second[y]
                y=y+1
            z= z+1
        "This loop will add the left over numebrs from the first half"    
        while x < len(first):
            numbers[z] =  first[x]
            x = x+1
            z = z+1
        "This loop will add the left over numebrs from the second half"      
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