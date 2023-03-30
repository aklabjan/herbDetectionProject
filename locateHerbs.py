import skimage.io
from skimage import measure
import os
from matplotlib import plt

def get_properties(img_path):
    # Load image
    img = skimage.io.imread(img_path)
    # Convert to binary image
    bwimg = img > skimage.filters.threshold_otsu(img)
    # Compute region properties
    stats = measure.regionprops(bwimg)

    return stats

def annotate_center(img_path, stats, out_path):
    fig, ax = plt.subplots()
    ax.imshow(img_path)
    for obj in stats:
        y, x = obj.centroid
        ax.plot(x, y, 'ro')
    plt.save_fig(out_path)

if __name__ == '__main__':
    directory = "images/segmentationImages"
    for photo_file in os.listdir(directory):
        if photo_file.startswith("img"):
            img_path = os.path.join(directory,photo_file,"noWordsOuput.png")
            stats = get_properties(img_path)
            out_path = os.path.join(directory,photo_file,"annotateCenterOuput.png")
            annotate_center(img_path,stats,out_path)
