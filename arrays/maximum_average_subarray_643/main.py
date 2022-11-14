from solution import Solution

def main():
    s = Solution()
    arr = [1,12,-5,-6,50,3]
    k = 4
    res = s.findMaxAverage(arr, k)
    print(res)


if __name__ == '__main__':
    main()