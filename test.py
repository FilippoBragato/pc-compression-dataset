from SELMA_utils import *
import seaborn as sns


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
    path = "high/data.hdf5"
    pc, gt = open_measurement_sample_TLC(path, 200)
    visualize(pc, gt)

    write_to_ply(pc, gt, "test.ply")