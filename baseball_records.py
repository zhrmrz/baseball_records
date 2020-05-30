class Sol:
    def baseball_records(self,arr):
        list_of_pints_each_level=[]
        for x in arr:
            if x=='C':
                list_of_pints_each_level.pop()
            elif x=='D':
                list_of_pints_each_level.append(2*int(list_of_pints_each_level[-1]))
            elif x=='+':
                list_of_pints_each_level.append(int(list_of_pints_each_level[-1])+int(list_of_pints_each_level[-2]))
            else:
                list_of_pints_each_level.append(int(x))

        return sum(list_of_pints_each_level)


if __name__ == '__main__':
    p=Sol()
    print(p.baseball_records(["5","-2","4","C","D","9","+","+"]))
