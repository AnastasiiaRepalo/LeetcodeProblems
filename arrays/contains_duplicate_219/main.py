from solution import Solution


def main():
    s = Solution()
    arr = [1,2,3,1,2,3]
    k = 2
    res = s.containsNearbyDuplicate(arr, k)
    print(res)


if __name__ == '__main__':
    main()