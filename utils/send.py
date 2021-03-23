from networktables import NetworkTables
NetworkTables.initialize(server = '10.30.21.2')

vision_table = NetworkTables.getTable("vision")

def table(send_str : str):
    smallest_distance_index = -1
    smallest_distance = -1
    idx = 0
    for box in send_str.split('\n')[:-1]:
        #print(box)
        coors = box.split(' ')
        bx = float(coors[1])
        by = float(coors[2])
        bh = float(coors[4])

        distance_from_bottom_center = ((by+(bh/2)-1)**2+(bx-.5)**2)**0.5
        if smallest_distance_index != -1:
            if distance_from_bottom_center < smallest_distance:
                smallest_distance_index = idx
                smallest_distance = distance_from_bottom_center
        else:
            smallest_distance_index = idx
            smallest_distance = distance_from_bottom_center
        idx += 1

    if smallest_distance_index != -1:
        selected_bbox = send_str.split('\n')[smallest_distance_index]
        selected_coors = selected_bbox.split(' ')
        c = float(selected_coors[0])
        x = float(selected_coors[1])
        y = float(selected_coors[2])
        w = float(selected_coors[3])
        h = float(selected_coors[4])

        vision_table.putBoolean('bv',True)
        vision_table.putNumber('bc', c)
        vision_table.putNumber('bx', x)
        vision_table.putNumber('by', y)
        vision_table.putNumber('bw', w)
        vision_table.putNumber('bh', h)
        #print('sent '+ selected_bbox)

def zero():
    vision_table.putBoolean('bv',False)
    vision_table.putNumber('bc', 0.)
    vision_table.putNumber('bx', 0.)
    vision_table.putNumber('by', 0.)
    vision_table.putNumber('bw', 0.)
    vision_table.putNumber('bh', 0.)







    

