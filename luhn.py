def verify_cardnum(card_num):
     sum_odd_digits = 0
     cardnum_reversed = card_num[::-1]
     odd_digits = cardnum_reversed[::2]
     
     for digit in odd_digits:
          sum_odd_digits += int(digit)
          
     sum_even_digits = 0
     even_digits = cardnum_reversed[1::2]
     for digit in even_digits:
          number = int(digit) * 2
          if number >= 10:
               number = (number // 10) + (number % 10)
          sum_even_digits += number
     total = sum_odd_digits + sum_even_digits
     return total % 10 == 0

def main():
     card_num = '4091-9019-0111-111'
     card_translation = str.maketrans({'-': '', ' ': ''})
     translated_cardnum = card_num.translate(card_translation)
     
     if verify_cardnum(translated_cardnum):
          print('VALID')
     else:
          print('Mmm...INVALID')
          
main()
