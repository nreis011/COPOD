import numpy as np
import os
import utils
from calibration import Calibration

n=0
for j in range (0, 7480):
    if (j < 10):
        idx = '00000' + str(j)
    elif (j >= 10 and j < 100 ):
        idx = '0000' + str(j)
    elif (j >= 100 and j < 1000 ):
        idx = '000' + str(j)
    elif (j >= 1000 and j < 10000 ):
        idx = '00' + str(j)
    points_path = 'kitti/training/velodyne/' + idx + '.bin'
    label_path = 'kitti/training/label_2/' + idx + '.txt'
    calib_path = 'kitti/training/calib/' + idx + '.txt'

    calib = Calibration(calib_path)
    points = utils.load_point_clouds(points_path)
    bboxes = utils.load_3d_boxes(label_path, 'pedestrian')
    if len(bboxes != 0):
        if (os.path.exists('output/pedestrian/') == False):
            os.makedirs('output/pedestrian/points/')
            os.makedirs('output/pedestrian/boxes/')

        bboxes = calib.bbox_rect_to_lidar(bboxes)

        corners3d = utils.boxes_to_corners_3d(bboxes)
        points_flag = utils.is_within_3d_box(points, corners3d)

        points_is_within_3d_box = []
        for i in range(len(points_flag)):
            p = points[points_flag[i]]
            if len(p)>0:
                points_is_within_3d_box.append(p)
                box = bboxes[i]
                points_canonical, box_canonical = utils.points_to_canonical(p, box)
                points_canonical, box_canonical = utils.lidar_to_shapenet(points_canonical, box_canonical)
                pts_name = 'output/{}/points/{}_point_{}'.format('pedestrian', n, idx)
                box_name = 'output/{}/boxes/{}_bbox_{}'.format('pedestrian', n, idx)
                #pts_name = 'output/{}_{}_point_{}'.format(args.idx, args.category, i)
                #box_name = 'output/{}_{}_bbox_{}'.format(args.idx, args.category, i)
                utils.write_points(points_canonical, pts_name)
                utils.write_bboxes(box_canonical, box_name)
                n+=1

#points_is_within_3d_box = np.concatenate(points_is_within_3d_box, axis=0)
#points = points_is_within_3d_box

#utils.write_points(points, 'output/points')
#utils.write_bboxes(bboxes, 'output/bboxes')