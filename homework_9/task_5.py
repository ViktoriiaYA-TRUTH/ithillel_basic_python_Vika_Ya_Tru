def group_by_surname(list_of_enrollees): # returns 4 ints
    for name in list_of_enrollees:
        last_name = name.split()[-1]
        print(last_name[0])
        a_i, j_p, q_t, u_z = 0, 0, 0, 0
        if 'A' >= last_name[0] < 'J':
            a_i += 1
        elif 'J' >= last_name[0] < 'Q':
            j_p += 1
        elif 'Q' >= last_name[0] < 'U':
            q_t += 1
        elif last_name[0] >= 'U':
            u_z += 1
    return a_i, j_p, q_t, u_z


def main():
    list_of_enrollees = ['Jay Z', 'Will Smith', 'Brad Pitt', 'Josh Bush', 'Amy Lee']
    print(group_by_surname(list_of_enrollees))


if __name__ == '__main__':
    main()
