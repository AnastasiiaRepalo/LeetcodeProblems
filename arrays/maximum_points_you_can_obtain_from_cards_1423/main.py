from solution import Solution

def main():
    s = Solution()
    cardPoints = [1,2,3,4,5,6,1]
    k = 3

    res = s.maxScore(cardPoints, k)
    print(res)


if __name__ == '__main__':
    main()