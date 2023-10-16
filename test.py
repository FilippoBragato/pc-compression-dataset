from SELMA_utils import *
import seaborn as sns
import open3d as o3d

def visualize(pc, gt):
    colors = np.zeros((pc.shape[0], 3))
    palette = sns.color_palette("hsv", n_colors=25)
    get_color = lambda tag:palette[tag%25]
    colors = np.array(np.vectorize(get_color)(gt[:,1])).T

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(pc)
    pcd.colors = o3d.utility.Vector3dVector(colors)
    o3d.visualization.draw_geometries([pcd])


if __name__ == "__main__":
    path = "low/data.hdf5"
    pc, gt = open_measurement_sample_TLC(path, 200)
    # visualize(pc, gt)

    write_to_ply(pc, gt, "00001.ply")
    pcd1 = o3d.io.read_point_cloud("00000.ply")
    pcd2 = o3d.io.read_point_cloud("00001.ply")
    # print(pcd)
    # o3d.visualization.draw_geometries([pcd])
    a = pcd1.compute_point_cloud_distance( pcd2)
    a = np.sum(np.asarray(a))

    b = pcd2.compute_point_cloud_distance( pcd1)
    b = np.sum(np.asarray(b))

    chamfer_distance = a + b
    print(chamfer_distance)
