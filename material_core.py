# -*- coding: utf-8 -*-

import json
import os

import maya.cmds as cmds


def write_json(json_path, write_dict):
    """
    write json
    : param str json_path : "D:/json/dir.json"
    : param dict json_path : The value you want to write to
    """

    with open(json_path, "w") as fp:
        end = json.dumps(write_dict, indent=4, encoding="utf-8")
        fp.write(end)


def read_json(json_path):
    """
    read json
    : param str json_path : "D:/json/dir.json"
    """
    if os.path.isfile(json_path):
        with open(json_path) as fp:
            return json.loads(fp.read())


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
    try:
        sg_nodes.remove('initialShadingGroup')
    except ValueError:
        pass

    return sg_nodes


def get_sg_connect_obj():
    """
    Get shadingEngine connection transform object
    :return: shadingEngine map transform object
    :rtype: dict or None
    """
    sg_obj_sets = {}
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
            sg_obj_sets[sg_node] = object_nodes_temp
    else:
        return

    return sg_obj_sets


def reference_material_file(ma_path):
    """
    import materials and return namespace
    :param ma_path: materials path
    :return: namespace
    :rtype: str
    """
    all_reference = cmds.file(q=True, reference=True)
    if ma_path in all_reference:
        cmds.file(ma_path, removeReference=True)

    file_name = os.path.splitext(os.path.basename(ma_path))[0]
    cmds.file(ma_path, reference=True, ignoreVersion=True,
              groupLocator=True, mergeNamespacesOnClash=False,
              options="v=0;", namespace=file_name)
    namespace = cmds.referenceQuery(ma_path, namespace=True)

    return namespace.split(':')[-1]


def export_material(ma_path, json_path=None):
    """
    Export material file and SG-associated object collection information
    :param ma_path: export material file path
    :param json_path: Store connection information between sg nodes and objects
    """
    sg_obj_sets = get_sg_connect_obj()

    if sg_obj_sets:
        cmds.select(sg_obj_sets.keys(), r=True, ne=True)
        cmds.file(ma_path, op='v=0;', typ='mayaAscii', pr=1, es=1)
        if not json_path:
            json_path = ma_path.replace('.ma', '.json')
        write_json(json_path, sg_obj_sets)
        return True
    else:
        return False


def give_material(ma_path, json_path=None, obj_namespace=None):
    """
    Give the selected object material
    :param ma_path: material path
    :param json_path: sg json path
    :param obj_namespace: mesh object namespace
    """
    material_namespace = reference_material_file(ma_path)
    if not json_path:
            json_path = ma_path.replace('.ma', '.json')
    sg_obj_sets = read_json(json_path)

    for sg_name, mesh_objects in sg_obj_sets.items():
        mesh_list_new = []
        for mesh_object in mesh_objects:
            if obj_namespace:
                mesh_object = '{0}:{1}'.format(obj_namespace, mesh_object)
            if not cmds.objExists(mesh_object):
                continue
            mesh_list_new.append(mesh_object)

        cmds.sets(mesh_list_new, fe='{0}:{1}'.format(material_namespace, sg_name), e=True)
