# interaction with user
# check and clean up duplicates
# output message

def list_filter_1(seq):
      """
      Func delete duplicates via set() variant 1
      :param seq: list of strings
      :return: list of strings w/o duplicates
      """
      check_set = set(seq)
      sorted_list = []
      for item in seq:
            if item in check_set and item not in sorted_list:
                  sorted_list.append(item)
      return sorted_list

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



# app delete duplicates in list provided by user
print('Application delete duplicates in list provided by user via console \n'
      'All values should be separated by comas ')

user_input = input('Please enter a list of values: ')

user_list = user_input.split(',')
norm_list = [x.strip(' ') for x in user_list]

sorted_list = list_filter_2(norm_list)
print(sorted_list)
