import sys
sys.path.insert(0, '../src')
from test_the import test_the
from test_num import test_num
from test_sym import test_sym
from test_bignum import test_bignum
from test_data import test_data
from test_stats import test_stats
from test_csv import test_csv
def main():
    result = 0
    result += test_the()
    result += test_num()
    result += test_sym()
    result += test_bignum()
    result += test_data()
    result += test_stats()
    result += test_csv()
    print(result, " tests failed")
    print(7 - result, " tests passed")
    return result

if __name__ == '__main__':
    main()