# 🧬 YOLO Models for Electrophoresis

![Gel Example](gel.png)

This repository provides **YOLOv5 to YOLOv12** models trained for automatic detection of electrophoresis gel features — including DNA bands, wells, and molecular markers.

> 🔬 Models trained as part of the study:  
> **"Electrophoresis Gels Detection and Analysis Using YOLO"**  
> Clenivaldo Pires da Silva et al., 2025.

---

## 📦 Available Models

| Model      | Filename      | mAP (%) | Size (MB) | Download |
|------------|----------------|---------|-----------|----------|
| YOLOv5     | `yolov5.pt`     | 92.2    | 168.9     | [📥 Download](https://drive.google.com/file/d/1nnCRpD7Mfh7vTBkdd7XjODLjFbib8ZTU/view?usp=sharing) |
| YOLOv6     | `yolov6.pt`     | 94.6    | 466.8     | [📥 Download](https://drive.google.com/file/d/1yOUuWX4ywO1VXzLe2h-jYhY84vTY5Yod/view?usp=sharing) |
| YOLOv7     | `yolov7.pt`     | 94.3    | 138.7     | [📥 Download](https://drive.google.com/file/d/1h--OfAziFfuYRK48MGwKYlE-Dq0FnZQo/view?usp=sharing) |
| YOLOv8     | `yolov8.pt`     | 94.8    | 133.5     | [📥 Download](https://drive.google.com/file/d/1A0nhh3HtB5iJb33k8N1XrrM6TI8WPQAP/view?usp=sharing) |
| YOLOv9     | `yolov9.pt`     | 94.6    | 199.8     | [📥 Download](https://drive.google.com/file/d/13qCQOQSTyJrc8OhVsYHz0ushGtTW5kGf/view?usp=sharing) |
| YOLOv10    | `yolov10.pt`    | 93.8    | 62.7      | [📥 Download](https://drive.google.com/file/d/1A0nhh3HtB5iJb33k8N1XrrM6TI8WPQAP/view?usp=sharing) |
| YOLOv11 ✅ | `yolov11.pt`    | **95.0**| 111.7     | [📥 Download](https://drive.google.com/file/d/1xt5hUh9XOOnI0pw3IXlZcJnW689hK5pD/view?usp=sharing) |
| YOLOv12    | `yolov12.pt`    | 90.9    | 113.6     | [📥 Download](https://drive.google.com/file/d/116fXm0VluzffuEbw1OuY8w_B1MFWfh-R/view?usp=sharing) |

> ✅ **YOLOv11 is the recommended model**, with the highest accuracy in our experiments.

---

## 🧾 Dataset & Annotations

- **Image count**: 1,230 images (augmented from 246 real gel electrophoresis images)
- **Annotation tool**: [Roboflow](https://roboflow.com)
- **Classes**:
  - `B` – Band
  - `L` – Marker region
  - `M` – Individual marker
  - `P` – Well region
  - `Pc` – Individual well

📂 Public dataset and annotations:  
👉 [Access the dataset on Roboflow Universe](https://app.roboflow.com/lbiomic-laboratorio-de-biotecnologia-microbiana)

---

## ⚙️ Training Configuration

- Framework: [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- Transfer learning from: MS COCO
- Image size: 416x416
- Epochs: 2000
- Hardware: NVIDIA RTX 2060 (12GB)

---

## 📜 Citation

If you use these models, please cite:

> Clenivaldo Pires da Silva, Mateus F. T. Carvalho, Yandre M. G. Costa,  
> Franklin C. Flores, Julio C. Polonio, and Claudete A. Mangolim.  
> **"Electrophoresis Gels Detection and Analysis Using YOLO"**, 2025.

---

## 📄 License

These models are available for **academic and research use only**.  
For commercial use, please contact the authors.

