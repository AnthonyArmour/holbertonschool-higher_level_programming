#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    t = 0
    tot = 0
    lst = list()
    while t < list_length:
        try:
            tot = my_list_1[t] / my_list_2[t]
        except ZeroDivisionError:
            print("{}".format("division by 0"))
            lst.append(0)
        except TypeError:
            print("{}".format("wrong type"))
            lst.append(0)
        except IndexError:
            print("{}".format("out of range"))
            lst.append(0)
        except Exception:
            lst.append(0)
        else:
            lst.append(tot)
        finally:
            t = t + 1
    return lst
