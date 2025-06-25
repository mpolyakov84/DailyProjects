import timeit

test_list = ['1','wer','34','qw','one', 'tre', ' sfe', ' zwef', '23', 'qw', 'test', 'pet', 'cat', 'cat', 'reay', '2',
             '2','wer','34','qw','one', 'tre', ' sfe', ' zwef', '23', 'qw', 'test', 'pet', 'cat', 'cat', 'reay', '2',
             '2', 'fart', 'cap', ' rat', 'rat', 'test', 'pet', 'cat', 'cat', 'reay', '2']

setup1 = '''
def list_filter_1(seq):
      check_set = set(seq)
      sorted_list = []
      for item in seq:
            if item in check_set and item not in sorted_list:
                  sorted_list.append(item)
      return sorted_list

'''
stmt1 =f'list_filter_1({test_list})'

setup2 = '''
def list_filter_2(seq):
      """
      Func delete duplicates via loop variant 2
      :param seq: list of strings
      :return: list of strings w/o duplicates
      """
      iter = 0
      while True:

          item = iter+1

          while True:
                if seq[iter] == seq[item]:
                        seq.pop(item)
                item += 1
                if item >= len(seq):
                      break


          iter += 1
          if iter >= len(seq)-1:
                break
      return seq

'''
stmt2 =f'list_filter_2({test_list})'

setup3 = '''
def list_filter_3(seq):
      """
      Func delete duplicates via loop variant 3
      :param seq: list of strings
      :return: list of strings w/o duplicates
      """
      result_list = []
      for item in seq:
            if item not in result_list:
                  result_list.append(item)

      return result_list
'''
stmt3 =f'list_filter_3({test_list})'

print('Timing func1 : ', timeit.timeit(stmt1, setup=setup1, number=100000))
print('Timing func2 : ', timeit.timeit(stmt2, setup=setup2, number=100000))
print('Timing func3 : ', timeit.timeit(stmt3, setup=setup3, number=100000))