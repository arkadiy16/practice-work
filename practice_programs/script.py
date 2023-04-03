with open('Lightpack.txt', 'r') as orig, open('Lightpack_back.txt', 'w') as edit:
    orig = orig.readlines()
    edit.writelines(orig[:44])
    pos_x = 0 + 12
    pos_y = 1080 - 121
    x = 67
    y = 121
    for i in range(28):
        pos_ind = i * 8 + 44

        edit.writelines(orig[pos_ind:pos_ind + 2])
        edit.write(f'Position=@Point({pos_x} {pos_y})\n')
        edit.writelines(orig[pos_ind + 3: pos_ind + 8])
        pos_x += x

    pos_y = 1080 - 40
    pos_x = 1920 - y
    for i in range(28, 44):
        pos_ind = i * 8 + 44

        edit.writelines(orig[pos_ind:pos_ind + 2])
        edit.write(f'Position=@Point({pos_x} {pos_y})\n')
        edit.writelines(orig[pos_ind + 3: pos_ind + 8])
        pos_y -= x

    pos_y = 0
    pos_x = 1920 - 12 - x
    for i in range(44, 72):
        pos_ind = i * 8 + 44

        edit.writelines(orig[pos_ind:pos_ind + 2])
        edit.write(f'Position=@Point({pos_x} {pos_y})\n')
        edit.writelines(orig[pos_ind + 3: pos_ind + 8])
        pos_x -= x

    pos_y = 8
    pos_x = 0
    for i in range(72,89):
        pos_ind = i * 8 + 44

        edit.writelines(orig[pos_ind:pos_ind + 2])
        edit.write(f'Position=@Point({pos_x} {pos_y})\n')
        edit.writelines(orig[pos_ind + 3: pos_ind + 8])
        pos_y += 66





    pass
