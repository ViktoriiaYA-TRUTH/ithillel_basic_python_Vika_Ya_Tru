def group_by_surname(list_of_enrollees): # returns 4 ints
    a_i, j_p, q_t, u_z = 0, 0, 0, 0
    for name in list_of_enrollees:
        last_name = name.split()[-1]
        upper_letter = last_name[0].upper()
        if 'A' >= upper_letter < 'J':
            a_i += 1
        elif 'J' >= upper_letter < 'Q':
            j_p += 1
        elif 'Q' >= upper_letter < 'U':
            q_t += 1
        elif upper_letter >= 'U':
            u_z += 1
    return a_i, j_p, q_t, u_z


def main():
    list_of_enrollees = ['Jay z', 'Will smith', 'Brad Pitt', 'Josh Bush', 'Amy Lee']
    print(group_by_surname(list_of_enrollees))


if __name__ == '__main__':
    main()
