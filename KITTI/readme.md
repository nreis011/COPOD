# KITTI DATASET folder

### Folder Structure:
```
Parent Folder:
    - Scripts and Notebooks
    - kitti
        - training
            - calib
            - label_2
            - velodyne
    - output
```

Place all files belonging to the KITTI dataset within the "kitti" folder. Use onlytraining data.\
Outputs are stored within the "output" folder which is created automatically.

Run the notebooks in the following order:
extract.ipynb\
collectgrtuth.ipynb\
copod_x.ipynb\
analyze.ipynb\

visualize.ipynb serves to visualize individual bounding boxes.

The overall structure and function is the same as the Olivia dataset's but with adaptations for KITTI's folder structure.
