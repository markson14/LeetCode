import numpy as np


# bbox input (x1,y1,x2,y2)


def iou(bbox_target, bbox_list):
    iou_list = []
    for bbox in bbox_list:
        x1, y1, x2, y2 = bbox
        x1_t, y1_t, x2_t, y2_t = bbox_target[:, 0], bbox_target[:,
                                                                1], bbox_target[:, 2], bbox_target[:, 3]
        target_area = abs(x2-x1)*abs(y2-y1)
        bbox_area = abs(x2_t-x1_t)*abs(y2_t-y1_t)
        intersection_x1 = np.max(x1, x1_t)
        intersection_y1 = np.max(y1, y1_t)
        intersection_x2 = np.min(x2, x2_t)
        intersection_y2 = np.min(y2, y2_t)

        intersection_area = max(
            0, (intersection_y2-intersection_y1)*(intersection_x2-intersection_x1))

        iou_current = intersection_area / \
            (bbox_area + target_area - intersection_area + 1e-6)
        iou_list.append(iou_current)
    return iou_list


def nms(bbox_list, iou_theshold):
    """
    normal nms
    Args:
        bbox_list: input bbox list, [[x1,y1,x2,y2,score],[]...]
    """
    # 获取bbox坐标信息
    boxes = bbox_list[:, :4]
    # 获取bbox分数信息
    scores = bbox_list[:, 4]
    # 获取score倒序排列的index列表
    order = scores.argsort()[::-1]
    keep = []
    # 当order列表存在值，继续递归
    while order.size:
        # 获取分数最大的index
        i = order[0]
        # 将其添加在keep
        keep.append(i)
        # 计算分数最大的bbox与剩余bbox的IOU
        ovr = iou(boxes[i], boxes[order])
        # 获取小于threshold的index并保留
        inds = np.where(ovr <= iou_theshold)[0]
        order = order[inds]
    # 返回保留bbox的index
    return keep


def soft_nms(bbox_list, iou_theshold, score_threshold):
    # 获取bbox坐标信息
    boxes = bbox_list[:, :4]
    # 获取bbox分数信息
    scores = bbox_list[:, 4]
    keep = []
    # 当order列表存在值，继续递归
    while boxes.size:
        # 获取分数最大的index
        i = scores.argmax()
        # 将其添加在keep
        keep.append(i)
        # 计算分数最大的bbox与剩余bbox的IOU
        ovr = iou(boxes[i], boxes[order])
        '''
        1. 获取小于threshold的index并保留
        2. 大于iou阈值的bbox分数：score = score * (1 - iou)
        3. 若分数大于分数阈值，则保留inds
        '''
        inds = np.where(ovr > iou_theshold)[0]
        scores[inds] -= scores[inds]*(1-ovr[inds])
        inds = np.where(scores > score_threshold)[0]
        # 更新需要保留的index
        boxes = boxes[inds]
    # 返回保留bbox的index
    return keep


def fast_nms(bbox_list, score_list, iou_theshold):
    scores_index = np.argmax(score_list)
    best_score_box = bbox_list[scores_index[0]]
    best_scores_list = score_list[scores_index[0]]
    iou_list = iou(best_score_box, best_score_box)
    iou_list = np.triu(iou_list, k=1)
    keep = iou_list.max(1) < iou_theshold
    return best_score_box[keep], best_scores_list[keep]


if __name__ == '__main__':
    bbox = np.random.random((100, 4))*100
    bbox[:, 0], bbox[:, 1], bbox[:, 2], bbox[:, 3] = bbox[:, 0]-bbox[:, 2] / \
        2, bbox[:, 1]-bbox[:, 3]/2, bbox[:, 0] + \
        bbox[:, 2]/2, bbox[:, 1]+bbox[:, 3]/2

    bbox[bbox < 0] = 0
    scores = np.random.random((100))
    print(nms(bbox, scores, 80))
