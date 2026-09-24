from string import digits


is_non_negative_num = lambda num: num.replace('.', '', 1).isdigit()
