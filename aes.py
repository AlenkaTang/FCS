
s_box = [
    [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
    [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
    [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
    [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
    [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
    [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
    [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
    [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
    [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
    [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
    [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
    [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
    [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
    [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
    [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
    [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16],
]
c_matrix = [[0x02, 0x03, 0x01, 0x01],
            [0x01, 0x02, 0x03, 0x01],
            [0x01, 0x01, 0x02, 0x03],
            [0x03, 0x01, 0x01, 0x02]]

def toStringMatrix(str):
    s= []
    for i in range(0, len(str),2):
        s.append(str[i:i+2])
    result = []
    for i in range(0, len(s),4):
        temp = []
        temp.append(s[i])
        temp.append(s[i+1])
        temp.append(s[i+2])
        temp.append(s[i+3])
        result.append(temp)
    
    return result

def toIntMatrix(string_matrix):
    result = []
    for i in range(4):
        row = []
        for j in range(4):
            box = int(string_matrix[i][j],16)
            row.append(box)
        result.append(row)
    return result


def shift_rows(matrix):
    temp1 = matrix[1][0]
    temp2 = matrix[2][0]
    temp3 = matrix[3][0]
    for i in range(1, len(matrix[1])):
        matrix[1][i-1] = matrix[1][i]
        matrix[2][i-1] = matrix[2][i]
        matrix[3][i-1] = matrix[3][i]
        
    matrix[1][3] = temp1
    matrix[2][3] = temp2
    matrix[3][3] = temp3
    return matrix

def shift_single_row(arr):
    temp = arr[0]
    for i in range(1,4):
        arr[i-1]=arr[i]
    arr[3] = temp
    return arr

   

def s_sub(matrix):
    for row in matrix:
        for index in range(len(row)):
            i_temp = row[index][0]
            j_temp = row[index][1]
            i = int(i_temp,16)
            j = int(j_temp,16)
            row[index] = s_box[i][j]
    return matrix #int matrix
def single_row_s_sub(arr):
    result = []
    for index in range(4):
        i_temp = arr[index][0]
        j_temp = arr[index][1]
        i = int(i_temp,16)
        j = int(j_temp,16)
        result.append(s_box[i][j])
    return result


def addRoundKey(state_matrix, key_matrix):
    result = []
    for a in range(len(state_matrix)):
        temp_row = []
        for b in range(len(state_matrix[a])):
            temp_box = state_matrix[a][b]^key_matrix[a][b]
            temp_row.append(temp_box)
        result.append(temp_row)
    return result #int matrix

def mixColumn(state_matrix):
    column0_temp = []
    column1_temp = []
    column2_temp = []
    column3_temp = []
    for r in range(len(state_matrix)):
        column0_temp.append(state_matrix[r][0])
        column1_temp.append(state_matrix[r][1])
        column2_temp.append(state_matrix[r][2])
        column3_temp.append(state_matrix[r][3])
    column0 = []
    column1 = []
    column2 = []
    column3 = []

    for i in range(4):
        temp0 = 0
        temp1 = 0
        temp2 = 0
        temp3 = 0
        for j in range(4):
            temp0 = temp0 ^ column0_temp[j]* state_matrix[i][j]
            temp1 = temp1 ^ column1_temp[j]* state_matrix[i][j]
            temp2 = temp2 ^ column2_temp[j]* state_matrix[i][j]
            temp3 = temp3 ^ column3_temp[j]* state_matrix[i][j]
        column0.append(temp0)
        column1.append(temp1)
        column2.append(temp2)
        column3.append(temp3)

    row0 = []
    row0.append(column0[0])
    row0.append(column1[0])
    row0.append(column2[0])
    row0.append(column3[0])
    row1 = []
    row1.append(column0[1])
    row1.append(column1[1])
    row1.append(column2[1])
    row1.append(column3[1])
    row2 = []
    row2.append(column0[2])
    row2.append(column1[2])
    row2.append(column2[2])
    row2.append(column3[2])
    row3 = []
    row3.append(column0[3])
    row3.append(column1[3])
    row3.append(column2[3])
    row3.append(column3[3])
    result_matrix = []
    result_matrix.append(row0)
    result_matrix.append(row1)
    result_matrix.append(row2)
    result_matrix.append(row3)
    return result_matrix


def keyExpansion(key_str):
    key_matrix = []
    keySize = len(key_str)*8
    s = []
    for i in range(0, len(key_str),2):
        s.append(key_str[i:i+2])
    key_arr = [] 
    for i in range(0, len(s),4):
        temp = []
        temp.append(int(s[i],16))
        temp.append(int(s[i+1],16))
        temp.append(int(s[i+2],16))
        temp.append(int(s[i+3],16))
        key_arr.append(temp) #default 128-key
        total_round = 10
        num = 3
        round_count = 1
    if(keySize == 128):
        total_round = 10
        num =3
    elif(keySize == 192):
        total_round = 12
        num = 5
    elif(keySize == 256):
        total_round = 14
        num = 7
    while(round_count <= total_round):
        last_index = len(key_arr)-1
        t = []
        for i in range(4):
            t.append(str(key_arr[last_index][i]))
        t = shift_single_row(t)
        t = single_row_s_sub(t) 
        temp_arr = []
        temp_num0 = t[0]^key_arr[last_index-num][0]
        temp_arr.append(temp_num0)
        temp_num1 = t[1]^key_arr[last_index-num][1]
        temp_arr.append(temp_num1)
        temp_num2 = t[0]^key_arr[last_index-num][2]
        temp_arr.append(temp_num2)
        temp_num3 = t[0]^key_arr[last_index-num][3]
        temp_arr.append(temp_num3)
        key_arr.append(temp_arr)
        for count in range(num):
            temp_a = []
            temp_n0 = key_arr[last_index][0] ^ key_arr[last_index - num][0]
            temp_a.append(temp_n0)
            temp_n1 = key_arr[last_index][0] ^ key_arr[last_index - num][0]
            temp_a.append(temp_n1)
            temp_n2 = key_arr[last_index][0] ^ key_arr[last_index - num][0]
            temp_a.append(temp_n2)
            temp_n3 = key_arr[last_index][0] ^ key_arr[last_index - num][0]
            temp_a.append(temp_n3)
            key_arr.append(temp_a)
        round_count = round_count + 1
    result_matrix = []
    for i in range(0,len(key_arr),4):
        roundKey = []
        roundKey.append(key_arr[i])
        roundKey.append(key_arr[i+1])
        roundKey.append(key_arr[i+2])
        roundKey.append(key_arr[i+3])
        result_matrix.append(roundKey)
    return result_matrix #int matrix
    

def round0(state_matrix, key_matrix):
    result_matrix = []
    for i in range(4):
        row = []
        for j in range(4):
            box = state_matrix[i][j] ^ key_matrix[i][j]
            row.append(box)
        result_matrix.append(row)
    return result_matrix
def intToStringMatrix(int_matrix):
    result = []
    for row in int_matrix:
        row_temp = []
        for i in range(len(row)):
            temp = hex(row[i])
            temp = temp[2:]
            if(len(temp)<2):
                temp = '0' + temp
            row_temp.append(temp)
        result.append(row_temp)
    return result


def normalRound(state_matrix, key_matrix):
    state0_temp = intToStringMatrix(state_matrix)
    state0 = s_sub(state0_temp)
    state1 = shift_rows(state0)
    state2 = mixColumn(state1)
    output_state = addRoundKey(state2, key_matrix)
    return output_state

def aes_encryption(str, key0,keySize):
    key_arr = keyExpansion(key0)
    state_matrix0 = toStringMatrix(str)
    state0 = toIntMatrix(state_matrix0)
    round_0 = round0(state0,key_arr[0]) #int_matrix
    current = round0(state0,key_arr[0])
    count = 0
    result = []
    result.append(round_0)
    if(keySize == 128):
        count = 10
    elif(keySize == 192):
        count = 12
    elif(keySize == 256):
        count = 14
    for i in range(count):
        new_current = normalRound(current, key_arr[i])
        result.append(new_current)
        current = []
        for e in new_current:
            current.append(new_current)
    return key_arr

print('question 1')
q1_text = '00112233445566778899aabbccddeeff'
q1_key = '000102030405060708090a0b0c0d0e0f1011121314151617'
print(aes_encryption(q1_text,q1_key,192))
print('question 2')
q2_key = '000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f'
print(keyExpansion(q2_key))

    










        
   
        
    



    








        
    
