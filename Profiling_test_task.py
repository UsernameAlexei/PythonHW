# TEST TASK
import unittest

from Profiling_task import football_1, football_2, list_transformation_1, list_transformation_2, \
    list_transformation_3, bubble_sort, selection_sort, unpacking_1, unpacking_2

# parameters for the test
result_profiling_1 = {0: 'United Arab Emirates', 1: 'Kuwait', 2: 'Dominican Republic', 3: 'Guatemala',
                      4: 'Dominican Republic',
                      5: 'Iraq', 6: 'Panama', 7: 'United States', 8: 'Jordan', 9: 'Jordan', 10: 'Jordan',
                      11: 'Guatemala',
                      12: 'Kenya', 13: 'Kenya', 14: 'Ethiopia', 15: 'Oman', 16: 'Belarus', 17: 'Jordan', 18: 'Kosovo',
                      19: 'Qatar', 20: 'Suriname', 21: 'Guatemala', 22: 'Dominican Republic', 23: 'Portugal',
                      24: 'Serbia',
                      25: 'France', 26: 'Finland', 27: 'Belgium', 28: 'Estonia', 29: 'Turkey', 30: 'Gibraltar',
                      31: 'Latvia',
                      32: 'Malta', 33: 'Slovenia', 34: 'Cyprus', 35: 'Chad', 36: 'Guinea', 37: 'South Sudan',
                      38: 'Uganda',
                      39: 'Rwanda', 40: 'Ethiopia', 41: 'Bahrain', 42: 'India', 43: 'Japan', 44: 'Saudi Arabia',
                      45: 'United States', 46: 'El Salvador', 47: 'Canada', 48: 'Panama', 49: 'Haiti', 50: 'Spain',
                      51: 'Sweden', 52: 'Bulgaria', 53: 'Italy', 54: 'Israel', 55: 'Scotland', 56: 'Moldova',
                      57: 'England',
                      58: 'Andorra', 59: 'Hungary', 60: 'Germany', 61: 'Liechtenstein', 62: 'Romania',
                      63: 'South Africa',
                      64: 'Gambia', 65: 'Gabon', 66: 'Comoros', 67: 'Kenya', 68: 'Botswana', 69: 'Zambia',
                      70: 'Equatorial Guinea', 71: 'Libya', 72: 'Chile', 73: 'Burundi', 74: 'Mauritania',
                      75: 'Cape Verde',
                      76: 'Eswatini', 77: 'Congo', 78: 'Bosnia and Herzegovina', 79: 'Nepal', 80: 'Qatar', 81: 'Wales',
                      82: 'U.S. Virgin Islands', 83: 'Aruba', 84: 'Anguilla', 85: 'Bahamas', 86: 'Republic of Ireland',
                      87: 'Serbia', 88: 'Belarus', 89: 'Czech Republic', 90: 'Montenegro', 91: 'Netherlands',
                      92: 'Norway',
                      93: 'Russia', 94: 'Croatia', 95: 'Slovakia', 96: 'Lesotho', 97: 'Benin', 98: 'Greece',
                      99: 'Northern Ireland', 100: 'Dominica', 101: 'Georgia', 102: 'Kosovo', 103: 'Switzerland',
                      104: 'Bulgaria', 105: 'Kazakhstan', 106: 'Ukraine', 107: 'Denmark', 108: 'Austria', 109: 'Israel',
                      110: 'Albania', 111: 'Poland', 112: 'San Marino', 113: 'Armenia', 114: 'North Macedonia',
                      115: 'Romania',
                      116: 'Namibia', 117: 'Mali', 118: 'Sudan', 119: 'Tanzania', 120: 'Ecuador', 121: 'India',
                      122: 'Kuwait',
                      123: 'Nepal', 124: 'Uzbekistan', 125: 'Cayman Islands', 126: 'Burkina Faso', 127: 'Malawi',
                      128: 'Angola', 129: 'DR Congo', 130: 'Egypt', 131: 'Algeria', 132: 'Zimbabwe', 133: 'Bahrain',
                      134: 'Costa Rica', 135: 'Iran', 136: 'Republic of Ireland', 137: 'Grenada', 138: 'Bermuda',
                      139: 'Barbados', 140: 'Guyana', 141: 'Azerbaijan', 142: 'Luxembourg', 143: 'Wales',
                      144: 'Belgium',
                      145: 'Gibraltar', 146: 'Montenegro', 147: 'Turkey', 148: 'Cyprus', 149: 'Croatia',
                      150: 'Slovakia',
                      151: 'Saudi Arabia', 152: 'Japan', 153: 'Tajikistan', 154: 'Central African Republic',
                      155: 'Morocco',
                      156: 'Cameroon', 157: 'Mozambique', 158: 'Guinea-Bissau', 159: 'Ivory Coast', 160: 'Madagascar',
                      161: 'Nigeria', 162: 'Sweden', 163: 'Switzerland', 164: 'Spain', 165: 'Greece',
                      166: 'Northern Ireland',
                      167: 'Lithuania', 168: 'Bosnia and Herzegovina', 169: 'Ukraine', 170: 'Scotland', 171: 'Austria',
                      172: 'Moldova', 173: 'England', 174: 'Andorra', 175: 'San Marino', 176: 'Armenia', 177: 'Germany',
                      178: 'Liechtenstein', 179: 'Ukraine', 180: 'Iraq', 181: 'United Arab Emirates', 182: 'Indonesia',
                      183: 'Oman', 184: 'Turkey', 185: 'Bahrain', 186: 'Italy'}

City = ['Athens', 'Paris', 'St Louis', 'London', 'Stockholm', 'Antwerp', 'Amsterdam',
        'Los Angeles', 'Berlin', 'Helsinki', 'Melbourne / Stockholm', 'Rome', 'Tokyo',
        'Mexico', 'Munich', 'Montreal', 'Moscow', 'Seoul', 'Barcelona', 'Atlanta',
        'Sydney', 'Beijing']

result_profiling_2 = ['ATHENS', 'PARIS', 'ST LOUIS', 'LONDON', 'STOCKHOLM', 'ANTWERP', 'AMSTERDAM', 'LOS ANGELES',
                      'BERLIN', 'HELSINKI', 'MELBOURNE / STOCKHOLM', 'ROME', 'TOKYO', 'MEXICO', 'MUNICH', 'MONTREAL',
                      'MOSCOW', 'SEOUL', 'BARCELONA', 'ATLANTA', 'SYDNEY', 'BEIJING']

arr = [5, 2, 1, 8, 4, 3, 6, 7, 9]
result_profiling_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

unpacking_list = [['E', 'L', 'O', 'N'], ['M', 'U', 'S', 'K']]
result_profiling_4 = 'E L O N M U S K'


# START TEST
class Test_profiling(unittest.TestCase):

    # Profiling_1 test
    def test_output_football_pandas(self):
        result = football_1('home_team')
        self.assertEqual(result, result_profiling_1)

    def test_output_footbal_csv(self):
        result = football_2('home_team')
        self.assertEqual(result, result_profiling_1)

    # Profiling_2 test
    def test_upper_list_tr_1(self):
        result = list_transformation_1(City)
        self.assertEqual(result, result_profiling_2)

    def test_upper_list_tr_2(self):
        result = list_transformation_2(City)
        self.assertEqual(result, result_profiling_2)

    def test_upper_list_tr_3(self):
        result = list_transformation_3(City)
        self.assertEqual(result, result_profiling_2)

    # Profiling_3 test
    def test_bubble_sort_output(self):
        result = bubble_sort(arr)
        self.assertEqual(result, result_profiling_3)

    def test_selection_sort_output(self):
        result = selection_sort(arr)
        self.assertEqual(result, result_profiling_3)

    # Profiling_4 test
    def test_unpacking_1(self):
        result = unpacking_1(unpacking_list)
        self.assertEqual(result, result_profiling_4)

    def test_unpacking_2(self):
        result = unpacking_2(unpacking_list)
        self.assertEqual(result, result_profiling_4)


if __name__ == '__main__':
    unittest.main()
