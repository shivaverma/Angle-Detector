## Angle-Detector

**version** - `1.0.0`

This Software read the angle of tilted images. Images are rotated between -30 to 30 degree.

### Requirements

- **`python`** - `3.7`
- **`keras`** -  `2.4.3`
- **`tensorflow`** -  `2.3.0`

---

### Project Content

| File      | Description |
| :-----------: | :-----------: |
| **main.ipynb**   | jupyter notebook for running and testing the model |
| **model.py**   | neural network implementation     |
| **scripts**      | scripts for generating and loading data     |
| **saved_model** | trained model |

---
### Performance

Network was able to read the angle close to 2.5 degree(average). Following is a snippet showing network reading the angle. 

<img src=results/sample.png width="300">

---

### References

- Download the [**dataset**](https://www.kaggle.com/shivajbd/imagerotation) for this project.
- Read the [**blog**](https://shiva-verma.medium.com/image-angle-detection-using-neural-networks-77f38524951c) for this project.
