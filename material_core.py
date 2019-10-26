# -*- coding: utf-8 -*-
# ================================
# @Time    : 2019/10/26 23:00
# @Author  : KaiJun Fan
# @Email   : qq826530928@163.com
# ================================
import maya.cmds as cmds


def get_select_object_sg():
    """
    Get the shadingEngine node of the selected object
    :return: shadingEngine node list
    :rtype: list
    """
    sg_nodes = []
    cmds.select(hi=True)
    sel_obj_shape_list = cmds.ls(sl=True, type='surfaceShape')

    for obj_shape in sel_obj_shape_list:
        sg_nodes.extend(cmds.listConnections(obj_shape, d=True, t='shadingEngine'))

    sg_nodes = list(set(sg_nodes))

    # remove maya default ShadingGroup
    sg_nodes.remove('initialShadingGroup')

    return sg_nodes


def get_sg_connect_obj():
    """
    Get shadingEngine connection transform object
    :return: shadingEngine map transform object
    :rtype: dict or None
    """
    sg_map_obj = {}
    sg_nodes = get_select_object_sg()

    if sg_nodes:
        for sg_node in sg_nodes:
            object_nodes = cmds.sets(sg_node, q=True)
            object_nodes_temp = []
            for object_node in object_nodes:
                if '.f' in object_node:
                    object_nodes_temp.append(object_node)
                else:
                    object_nodes_temp.append(cmds.listRelatives(object_node, p=True, pa=True)[0])
            sg_map_obj[sg_node] = object_nodes_temp
    else:
        return

    return sg_map_obj


