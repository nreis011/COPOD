# KITTI DATASET folder

### Folder Structure:

Parent Folder:
    - Scripts and Notebooks
    - Folder: kitti
        - training
            - calib
            - label_2
            - velodyne
    - Folder: output

The kitti folder is where to place all the kitti dataset files. Using only the training data, it should look as outlined above.
Outputs stores the output from running a notebook, these folders are created automatically.

Run the notebooks in the following order:
extract.ipynb
collectgrtuth.ipynb
copod_x.ipynb
analyze_x.ipynb

visualize.ipynb serves to visualize individual bounding boxes both individually and in the context of the wider point cloud.

The overall structure and function is the same as in the Olivia dataset but with adaptations for KITTI's structure.