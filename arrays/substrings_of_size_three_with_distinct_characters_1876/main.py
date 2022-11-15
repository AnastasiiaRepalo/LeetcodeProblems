from solution import Solution


def main():
    s = Solution()
    string = "aababcabc"
    res = s.countGoodSubstrings(string)
    print(res)


if __name__ == '__main__':
    main()