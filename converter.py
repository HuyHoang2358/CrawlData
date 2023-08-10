import aspose.threed as a3d

# input_path = "data/591e6eff89deb4147c31d2ed.obj
# output_path = "output.glb"

def convertFile(input_path, output_path):
    scene = a3d.Scene.from_file(input_path)
    scene.save(output_path)