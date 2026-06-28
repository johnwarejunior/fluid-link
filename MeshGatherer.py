import maya.cmds as cmds
import csv

selection = cmds.ls(sl = True)

col = ['', 'id', 'tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']

with open("C:\MeshGatherer\data.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(col)

    for idx, obj in enumerate(selection):
        data = []
        data.append(idx)
        data.append(idx)

        data.append(cmds.getAttr(obj + '.translateX'))
        data.append(cmds.getAttr(obj + '.translateY'))
        data.append(cmds.getAttr(obj + '.translateZ'))

        data.append(cmds.getAttr(obj + '.rotateX'))
        data.append(cmds.getAttr(obj + '.rotateY'))
        data.append(cmds.getAttr(obj + '.rotateZ'))

        data.append(cmds.getAttr(obj + '.scaleX'))
        data.append(cmds.getAttr(obj + '.scaleY'))
        data.append(cmds.getAttr(obj + '.scaleZ'))

        writer.writerow(data)
        del data