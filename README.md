# Convert-Polygon-Annotation-to-BoundingBox-Annotation

# Polygon to YOLO Bounding Box Converter

## 📝 Description
This Python tool converts polygon annotations to YOLO format bounding boxes and provides visualization capabilities. It's specifically designed for computer vision and machine learning projects that require format conversion between polygon coordinates and YOLO-style bounding boxes.

## 🔑 Key Features
- Convert polygon coordinates to YOLO format bounding boxes
- Visualize bounding boxes on original images
- Save annotations in YOLO format
- Professional logging system
- Error handling and validation
- Object-oriented design
- Type hints for better code maintenance

## 🛠️ Requirements
```bash
numpy>=1.19.2
opencv-python>=4.5.1
matplotlib>=3.3.4
```

## 📦 Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/polygon-to-yolo-converter.git
cd polygon-to-yolo-converter
```

2. Install required packages
```bash
pip install -r requirements.txt
```

## 💻 Usage
### Basic Usage
```python
from polygon_processor import PolygonProcessor

# Initialize processor with image and label paths
processor = PolygonProcessor(
    image_path='path/to/your/image.jpg',
    label_path='path/to/your/labels.txt'
)

# Process and display results
processor.load_data()
processor.save_yolo_format('output.txt')
processor.draw_bbox()
processor.display_image()
```

### Command Line Usage
```bash
python main.py --image_path /path/to/image --label_path /path/to/label --output_path output.txt
```

## 📁 Project Structure
```
polygon-to-yolo-converter/
│
├── src/
│   ├── __init__.py
│   ├── polygon_processor.py
│   ├── yolo_formatter.py
│   └── bounding_box.py
│
├── tests/
│   ├── __init__.py
│   └── test_polygon_processor.py
│
├── examples/
│   ├── example_image.jpg
│   └── example_label.txt
│
├── requirements.txt
├── README.md
└── main.py
```

## 📝 Class Structure

### BoundingBox
```python
@dataclass
class BoundingBox:
    x_min: float
    y_min: float
    x_max: float
    y_max: float
    class_id: int = 0
```

### YOLOFormatter
```python
class YOLOFormatter:
    @staticmethod
    def to_yolo_format(bbox: BoundingBox, img_width: int, img_height: int) -> str
```

### PolygonProcessor
```python
class PolygonProcessor:
    def load_data(self) -> None
    def save_yolo_format(self, output_path: str) -> None
    def draw_bbox(self) -> None
    def display_image(self) -> None
```

## 🎯 Input Format
The input label file should contain polygon coordinates in the following format:
```
class_id x1 y1 x2 y2 x3 y3 ...
```

## 📤 Output Format
The output will be in YOLO format:
```
class_id x_center y_center width height
```

## 📊 Example
```python
# Example input
0 0.1 0.1 0.2 0.1 0.2 0.2 0.1 0.2

# Example output
0 0.15 0.15 0.1 0.1
```

## 🚀 Advanced Usage
### Custom Visualization
```python
processor = PolygonProcessor(image_path, label_path)
processor.load_data()

# Custom visualization settings
processor.draw_bbox(color=(0, 255, 0), thickness=2)
processor.display_image(figsize=(15, 15))
```

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## 📧 Contact
Your Name - [@yourusername](https://twitter.com/yourusername)
Project Link: [https://github.com/yourusername/polygon-to-yolo-converter](https://github.com/yourusername/polygon-to-yolo-converter)

## 🙏 Acknowledgments
* OpenCV team for their amazing computer vision library
* YOLO project for their contribution to object detection
* All contributors who have helped with this project

---
Made with ❤️ by [Your Name]

Bu README.md dosyası:
1. Projenin amacını açıklar
2. Kurulum adımlarını detaylandırır
3. Kullanım örnekleri sunar
4. Proje yapısını gösterir
5. Katkıda bulunma kılavuzları içerir
6. İletişim bilgileri ve lisans bilgisi sağlar

Emojiler ve düzenli başlıklar sayesinde okunabilirliği artırılmıştır. Projenizi GitHub'a yüklerken bu README.md dosyasını kullanabilirsiniz.
