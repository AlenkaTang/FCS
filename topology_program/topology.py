topoFile = open('/Users/tangalenka/CS/topology_program/topofile.txt', 'r')
file = topoFile.read()
lines = file.splitlines()
changeFile = open('/Users/tangalenka/CS/topology_program/changefile.txt','r')
c_file = changeFile.read()
c_lines = c_file.splitlines()

node1 = {}
node2 = {}
node3 = {}
node4 = {}
new_node1 = {}
new_node2 = {}
new_node3 = {}
new_node4 = {}
for line in lines:
    temp = line.split()
    if(temp[0] == '1'):
        node1[temp[1]] = temp[2]
        new_node1[temp[1]] = temp[2]
    elif(temp[0] == '2'):
        node2[temp[1]] = temp[2]
        new_node2[temp[1]] = temp[2]
    elif(temp[0] == '3'):
        node3[temp[1]] = temp[2]
        new_node3[temp[1]] = temp[2]
    elif(temp[0] == '4'):
        node4[temp[1]] = temp[2]
        new_node4[temp[1]] = temp[2]
outputFile = open('/Users/tangalenka/CS/topology_program/output.txt','w')
outputFile.write('After Initialization \n')
outputFile.write('Node 1\n')
for key in node1:
    s = '1 '
    s += key
    s += ' '
    s += node1[key]
    outputFile.write(s)
    outputFile.write('\n')
outputFile.write('\n')
outputFile.write('Node 2\n')
for key in node2:
    s = '2 '
    s += key
    s += ' '
    s += node2[key]
    outputFile.write(s)
    outputFile.write('\n')
outputFile.write('\n')
outputFile.write('Node 3\n')
for key in node3:
    s = '3 '
    s += key
    s += ' '
    s += node3[key]
    outputFile.write(s)
    outputFile.write('\n')
outputFile.write('\n')
outputFile.write('Node 4\n')
for key in node4:
    s = '4 '
    s += key
    s += ' '
    s += node4[key]
    outputFile.write(s)
    outputFile.write('\n')
outputFile.write('\n')
outputFile.write('\n')


#first round

for index in range(4):
    for key in node1:
        if(int(node1[key]) != 0):
            text = "1 "
            text += key
            text += " : the cost for this path is "
            text += node1[key]
            outputFile.write(text)
            outputFile.write('\n')
    for key in node2:
        if(int(node2[key]) != 0):
            text = "2 "
            text += key
            text += " : the cost for this path is "
            text += node2[key]
            outputFile.write(text)
            outputFile.write('\n')
    for key in node3:
        if(int(node3[key]) != 0):
            text = "3 "
            text += key
            text += " : the cost for this path is "
            text += node3[key]
            outputFile.write(text)
            outputFile.write('\n')
    for key in node4:
        if(int(node4[key]) != 0):
            text = "4 "
            text += key
            text += " : the cost for this path is "
            text += node4[key]
            outputFile.write(text)
            outputFile.write('\n')
    outputFile.write('\n')
    outputFile.write('change applied')
    outputFile.write('\n')
    outputFile.write('\n')

    c_line = c_lines[index]
    c_arr = c_line.split()
    if(c_arr[0] == '1'):
        node1.update({c_arr[1]:c_arr[2]})
    if(c_arr[0] == '2'):
        node2.update({c_arr[1]:c_arr[2]})
    if(c_arr[0] == '3'):
        node3.update({c_arr[1]:c_arr[2]})
    if(c_arr[0] == '4'):
        node4.update({c_arr[1]:c_arr[2]})
    
    

#node1
    pathCost_through_2 = int(node1['2'])
    path_through_3 = int(node1['3']) 
    path_through_4 = int(node1['4'])

    if(pathCost_through_2 != -999):#through node2

        current_to_3 = int(node1['3'])
        if(int(node2['3']) != -999):
            throughNode2 = pathCost_through_2 + int(node2['3'])
            if(current_to_3 == -999 or current_to_3 > throughNode2):
                new_node1.update({'3':str(throughNode2)})
            else:
                new_node1.update({'3':str(current_to_3)})
    
        current_to_4 = int(node1['4'])
        if(int(node2['4']) != -999):
            throughNode2 = pathCost_through_2 + int(node2['4'])
            if(current_to_4 > throughNode2):
                new_node1.update({'4':str(throughNode2)})
            else:
                new_node1.update({'4':str(current_to_4)})


#through node 3
    if(path_through_3 != -999):

        current_to_2 = int(node1['2'])
        if(int(node3['2']) != -999):
            through_node_3 = path_through_3 + int(node3['2'])
            if(current_to_2 == -999 or current_to_2 > through_node_3):
                new_node1.update({'2':str(through_node_3)})
            else:
                new_node1.update({'2':str(current_to_2)})

        current_to_4 = int(node1['4'])
        if(int(node3['4']) != -999):
            through_node3 = path_through_3 + int(node3['4'])
            if(current_to_4 == -999 or current_to_4 > through_node3):
                new_node1.update({'4':str(through_node3)})
            else:
                new_node1.update({'4':str(current_to_4)})

#through node 4
    if(path_through_4 != -999):

        current_to_2 = int(node1['2'])
        if(int(node4['2']) != -999):
            through_node_4 = path_through_4 + int(node4['2'])
            if(current_to_2 == -999 or current_to_2 > through_node_4):
                new_node1.update({'2':str(through_node_4)})
            else:
                new_node1.update({'2':str(current_to_2)})
    
        current_to_3 = int(node1['3'])
        if(int(node4['3']) != -999):
            through_node4 = path_through_4 + int(node4['3'])
            if(current_to_3 == -999 or current_to_3 > through_node4):
                new_node1.update({'3':str(through_node4)})
            else:
                new_node1.update({'3':str(current_to_3)})


#node 2

    pathCost_through_1 = int(node2['1'])
    path_through_3 = int(node2['3']) 
    path_through_4 = int(node2['4'])

    if(pathCost_through_1 != -999):#through node1

        current_to_3 = int(node2['3'])
        if(int(node1['3']) != -999):
            throughNode1 = pathCost_through_1 + int(node1['3'])
            if(current_to_3 == -999 or current_to_3 > throughNode1):
                new_node2.update({'3':str(throughNode1)})
            else:
                new_node2.update({'3':str(current_to_3)})
    
        current_to_4 = int(node2['4'])
        if(int(node1['4']) != -999):
            throughNode1 = pathCost_through_1 + int(node1['4'])
            if(current_to_4 > throughNode1):
                new_node2.update({'4':str(throughNode1)})
            else:
                new_node2.update({'4':str(current_to_4)})


#through node 3
    if(path_through_3 != -999):

        current_to_1 = int(node2['1'])
        if(int(node3['1']) != -999):
            through_node_3 = path_through_3 + int(node3['1'])
            if(current_to_1 == -999 or current_to_1 > through_node_3):
                new_node2.update({'1':str(through_node_3)})
            else:
                new_node2.update({'1':str(current_to_1)})

        current_to_4 = int(node2['4'])
        if(int(node3['4']) != -999):
            through_node3 = path_through_3 + int(node3['4'])
            if(current_to_4 == -999 or current_to_4 > through_node3):
                new_node2.update({'4':str(through_node3)})
            else:
                new_node2.update({'4':str(current_to_4)})

#through node 4
    if(path_through_4 != -999):

        current_to_1 = int(node2['1'])
        if(int(node4['1']) != -999):
            through_node_4 = path_through_4 + int(node4['1'])
            if(current_to_1 == -999 or current_to_1 > through_node_4):
                new_node2.update({'1':str(through_node_4)})
            else:
                new_node2.update({'1':str(current_to_1)})
    
        current_to_3 = int(node2['3'])
        if(int(node4['3']) != -999):
            through_node4 = path_through_4 + int(node4['3'])
            if(current_to_3 == -999 or current_to_3 > through_node4):
                new_node2.update({'3':str(through_node4)})
            else:
                new_node2.update({'3':str(current_to_3)})
    
#node 3
    pathCost_through_1 = int(node3['1'])
    path_through_2 = int(node3['2']) 
    path_through_4 = int(node3['4'])

    if(pathCost_through_1 != -999):#through node1

        current_to_2 = int(node3['2'])
        if(int(node1['2']) != -999):
            throughNode1 = pathCost_through_1 + int(node1['2'])
            if(current_to_2 == -999 or current_to_2 > throughNode1):
                new_node3.update({'2':str(throughNode1)})
            else:
                new_node3.update({'2':str(current_to_2)})
    
        current_to_4 = int(node3['4'])
        if(int(node1['4']) != -999):
            throughNode1 = pathCost_through_1 + int(node1['4'])
            if(current_to_4 == -999 or current_to_4 > throughNode1):
                new_node3.update({'4':str(throughNode1)})
            else:
                new_node3.update({'4':str(current_to_4)})


#through node 2
    if(path_through_2 != -999):

        current_to_1 = int(node3['1'])
        if(int(node2['1']) != -999):
            through_node_2 = path_through_3 + int(node2['1'])
            if(current_to_1 == -999 or current_to_1 > through_node_2):
                new_node3.update({'1':str(through_node_2)})
            else:
                new_node3.update({'1':str(current_to_1)})

        current_to_4 = int(node3['4'])
        if(int(node2['4']) != -999):
            through_node_2 = path_through_2 + int(node2['4'])
            if(current_to_4 == -999 or current_to_4 > through_node_2):
                new_node3.update({'4':str(through_node_2)})
            else:
                new_node3.update({'4':str(current_to_4)})

#through node 4
    if(path_through_4 != -999):

        current_to_1 = int(node3['1'])
        if(int(node4['1']) != -999):
            through_node_4 = path_through_4 + int(node4['1'])
            if(current_to_1 == -999 or current_to_1 > through_node_4):
                new_node3.update({'1':str(through_node_4)})
            else:
                new_node3.update({'1':str(current_to_1)})
    
        current_to_2 = int(node3['2'])
        if(int(node4['2']) != -999):
            through_node4 = path_through_4 + int(node4['2'])
            if(current_to_2 == -999 or current_to_2 > through_node4):
                new_node3.update({'2':str(through_node4)})
            else:
                new_node3.update({'2':str(current_to_2)})

#node 4

    pathCost_through_1 = int(node4['1'])
    path_through_2 = int(node4['2']) 
    path_through_3 = int(node4['3'])

    if(pathCost_through_1 != -999):#through node1

        current_to_2 = int(node4['2'])
        if(int(node1['2']) != -999):
            throughNode1 = pathCost_through_1 + int(node1['2'])
            if(current_to_2 == -999 or current_to_2 > throughNode1):
                new_node4.update({'2':str(throughNode1)})
            else:
                new_node4.update({'2':str(current_to_2)})
    
        current_to_3 = int(node4['3'])
        if(int(node1['3']) != -999):
            throughNode1 = pathCost_through_1 + int(node1['3'])
            if(current_to_3 == -999 or current_to_3 > throughNode1):
                new_node4.update({'3':str(throughNode1)})
            else:
                new_node4.update({'3':str(current_to_4)})


#through node 2
    if(path_through_2 != -999):

        current_to_1 = int(node4['1'])
        if(int(node2['1']) != -999):
            through_node_2 = path_through_2 + int(node2['1'])
            if(current_to_1 == -999 or current_to_1 > through_node_2):
                new_node4.update({'1':str(through_node_2)})
            else:
                new_node4.update({'1':str(current_to_1)})

        current_to_3 = int(node4['3'])
        if(int(node2['3']) != -999):
            through_node_2 = path_through_2 + int(node2['3'])
            if(current_to_3 == -999 or current_to_3 > through_node_2):
                new_node4.update({'3':str(through_node_2)})
            else:
                new_node4.update({'3':str(current_to_4)})

#through node 3
    if(path_through_3 != -999):

        current_to_1 = int(node4['1'])
        if(int(node3['1']) != -999):
            through_node_3 = path_through_3 + int(node3['1'])
            if(current_to_1 == -999 or current_to_1 > through_node_3):
                new_node4.update({'1':str(through_node_3)})
            else:
                new_node4.update({'1':str(current_to_1)})
    
        current_to_2 = int(node4['2'])
        if(int(node3['2']) != -999):
            through_node3 = path_through_3 + int(node3['2'])
            if(current_to_2 == -999 or current_to_2 > through_node3):
                new_node4.update({'2':str(through_node3)})
            else:
                new_node4.update({'2':str(current_to_3)})

    outputFile.write('Updated Node 1\n')
    for key in new_node1:
        node1.update({key:new_node1[key]})
        s = '1 '
        s += key
        s += ' '
        s += node1[key]
        outputFile.write(s)
        outputFile.write('\n')

    outputFile.write('Updated Node 2\n')
    for key in new_node2:
        node2.update({key:new_node2[key]})
        s = '2 '
        s += key
        s += ' '
        s += node2[key]
        outputFile.write(s)
        outputFile.write('\n')

    outputFile.write('Updated Node 3\n')    
    for key in new_node3:
        node3.update({key:new_node3[key]})
        s = '3 '
        s += key
        s += ' '
        s += node3[key]
        outputFile.write(s)
        outputFile.write('\n')

    outputFile.write('Updated Node 4\n')    
    for key in new_node4:
        node4.update({key:new_node4[key]})
        s = '4 '
        s += key
        s += ' '
        s += node4[key]
        outputFile.write(s)
        outputFile.write('\n')
    outputFile.write('\n')
    outputFile.write('\n')
    outputFile.write('\n')

    








    








