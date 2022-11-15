from solution import Solution


def main():
    s = Solution()
    blocks = "WBWBBBW"
    k = 2
    res = s.minimumRecolors(blocks, k)
    print(res)


if __name__ == '__main__':
    main()